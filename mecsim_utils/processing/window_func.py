import numpy as np
import scipy as sci
from scipy.fftpack import ifft


# this imports the FTACV stuff
import mecsim_utils.processing.auto_ftacv as ftcount


def square_window(x, band, mu):

    # calculate the int point from df/di
    df = x[1]
    nlow = int((mu - band * 0.5) / df)
    nhigh = int((mu + band * 0.5) / df)

    # this allows the abstraction over the Fundimental harmonics
    if nlow < 0:
        nlow = 0

    z = np.zeros(len(x))
    z[nlow:nhigh] = 1
    # this adds it in for the windowing function

    if mu == 0:  # correction for fundimental case
        z[-nhigh:] = 1
    else:
        z[-nhigh:-nlow] = 1

    return z


# wrappers to unpack the harmonic info and pass to the convolution case
def square_window_wrapper(frequency_space, harmonic):
    conv = square_window(frequency_space, harmonic.bandwith, harmonic.freq)
    return conv


# std = band*std0
def rg_guassconv(x, band, mean, std):
    s = np.sqrt(2) / 2  # np.sqrt(2)/2
    c = np.sqrt(np.pi / 2)  # np.sqrt(np.pi/2)
    inv_std = s / std

    z = (
        c
        * std
        * (
            sci.special.erf((-x[:] + mean + band * 0.5) * inv_std)
            - sci.special.erf((-x[:] + mean - band * 0.5) * inv_std)
        )
    )

    # normalization for ease of computation
    z_max = np.max(z)
    z = z / z_max

    # this deals with the imaginary component (added as moved it to fft)
    n = int((x.shape[0]) / 2)
    f = z[:n]
    z[n:] = f[::-1]

    return z


# wrappers to unpack the harmonic info and pass to the convolution case
def rg_guassconv_wrapper(frequency_space, harmonic):
    conv = rg_guassconv(
        frequency_space,
        harmonic.bandwith,
        harmonic.freq,
        # TODO consider moving this
        harmonic.std * harmonic.bandwith,
    )
    return conv


def auto_flatten(harm, percentage):

    # finds indexes
    int_s = int(percentage * harm.shape[0])  # first truncation point
    int_e = int((1 - percentage) * harm.shape[0])  # second truncation point

    # value
    val_s = np.average(harm[int_s : 2 * int_s])
    val_e = np.average(harm[int_e - int_s : int_e])

    # set the new value
    harm[:int_s] = val_s
    harm[int_e:] = val_e

    return harm


# this function takes the filter and ftt_current and
# outputs a harmonic envelope
def harmonic_envelope(Convguass, frequency_curr, fundimental):

    N = frequency_curr.shape[0]  # int(np.floor(frequency_curr.shape[0]/2))

    # FLIP IT OR SET IMAGINARY TO O
    h = np.zeros(N, dtype=frequency_curr.dtype)
    if N % 2 == 0:
        h[0] = h[N // 2] = 1
        h[1 : N // 2] = 2
    else:
        h[0] = 1
        h[1 : (N + 1) // 2] = 2

    frequency_curr = frequency_curr * h
    # frequency_curr[n:] = 0

    # convert to harmonic TODO FIGURE OUT WHERE TO PUT THIS
    harmonic = ifft(Convguass * frequency_curr)

    # this enables extraction of FTACV and fundimental harmonics
    if fundimental:
        harmonic = np.abs(harmonic)
    else:
        harmonic = harmonic.real

    # np abs converts the imaginary output to a real number
    return harmonic  # np.imag(harmonic)#


# this function takes the filter and ftt_current and outputs a harmonic envelope
def total_current_harmonic(Convguass, frequency_curr, fundimental):

    # convert to harmonic TODO FIGURE OUT WHERE TO PUT THIS
    harmonic = ifft(Convguass * frequency_curr)

    return harmonic.real


# make a class
class harmonics_generate:

    def __init__(self, window_func="guassian", envelope=True, flatten_percent=0.0):

        # set something up split to optional function for windowing and output harmonic vs harmonic current
        match window_func:
            case "guassian":
                self.windowing = rg_guassconv_wrapper
            case "square":
                self.windowing = square_window_wrapper
            case _:
                raise ValueError(
                    f'ERROR: unreconised window func "{window_func}", please use guassian or square.'
                )

        # put something here to split the function to convert harmonic output type
        if envelope:
            self.generation = harmonic_envelope
        else:
            self.generation = total_current_harmonic

        # flattern is only supported for envolope method
        # TODO consider make the percentage only varible
        if envelope and flatten_percent:
            self.flatten_percent = flatten_percent
        else:
            self.flatten_percent = 0.0

        return

    # this function ID's if theres any unneeded harmonic information in the high frequency and
    # does a decismation in the frequency domain to speed up the ifft
    def frequency_decimation(self, frequency_curr, frequency_space, harmonics):

        # add something to calculate max frequency in harmonics
        max_harm_freq = 0
        for _, harm_group in harmonics.items():
            for _, harm in harm_group.items():
                if harm.freq > max_harm_freq:
                    max_harm_freq = harm.freq

        # based on above lightly decimate the frequency
        max_freq = frequency_space[int(frequency_space.shape[0] / 2) - 1]
        freq_tol = 4  # this is the amount of frequency we want to filter
        if max_freq > freq_tol * max_harm_freq:
            df = frequency_space[1]
            d_int = int(freq_tol * max_harm_freq / df)
            y_deci = np.ceil(np.log2(d_int))
            y_full = np.floor(np.log2(frequency_space.shape[0]))
            d_ratio = 1 / (2 ** (y_full - y_deci))

            if y_full > y_deci and d_ratio < 1:  # just a saftey check
                # try deci 4
                d = int(frequency_curr.shape[0] * d_ratio / 2)
                frequency_curr = (
                    np.concatenate((frequency_curr[:d], frequency_curr[-d:])) * d_ratio
                )
                frequency_space = np.concatenate(
                    (frequency_space[:d], frequency_space[-d:])
                )

        return frequency_curr, frequency_space

    def __call__(self, Currenttot, MECsimstruct, harmonics):

        frequency_curr, frequency_space = ftcount.frequency_transform(
            Currenttot, MECsimstruct.time_tot
        )

        # check if we can decimate the harmonic information (only do if 2**N)
        y = np.log2(frequency_space.shape[0])
        if int(y) == y:
            frequency_curr, frequency_space = self.frequency_decimation(
                frequency_curr, frequency_space, harmonics
            )

        parent_harms = list(harmonics.keys())
        for p_h in parent_harms:
            # loop over the harmonics
            for keys, harms in harmonics[p_h].items():

                # generate the harmonics
                Convguass = self.windowing(frequency_space, harms)

                harm = self.generation(Convguass, frequency_curr, harms.freq)

                # add something in here to opptionally flattern the spectral filtering
                if self.flatten_percent:
                    harm = auto_flatten(harm, self.flatten_percent)

                harmonics[p_h][keys].harmonic = harm

        return harmonics
