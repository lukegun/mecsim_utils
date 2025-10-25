import numpy as np
import scipy as sci
from scipy.fftpack import ifft, fftfreq


# this imports the FTACV stuff
import mecsim_utils.processing.auto_ftacv as ftcount


def square_window_fund(ftt_freq, band):
    # funcdimental is full input
    nhigh = find_nearest(ftt_freq, band)

    x = np.zeros(len(ftt_freq))

    x[0:nhigh] = 1

    return x


def square_window(ftt_freq, band, mu):
    nlow = find_nearest(ftt_freq, mu - band / 2)
    nhigh = find_nearest(ftt_freq, mu + band / 2)

    x = np.zeros(len(ftt_freq))

    x[nlow:nhigh] = 1

    return x


# below works but isnt relavant at moment
def blackman_win(x, band, mu):
    a_0 = 7938 / 18608
    a_1 = 9240 / 18608
    a_2 = 1430 / 18608

    z = (
        a_0
        - a_1 * np.cos((2 * np.pi * (x[:] - mu - band) / (2 * band)))
        + a_2 * np.cos((4 * np.pi * (x[:] - mu - band) / (2 * band)))
    )

    int_s = find_nearest(x, mu - band)
    int_e = find_nearest(x, mu + band)

    x = np.zeros(len(x))

    x[int_s:int_e] = z[int_s:int_e]

    return x


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
    z = z / np.max(z)

    return z


def rg_guassconv_fund(x, band, std):
    s = np.sqrt(2) / 2  # np.sqrt(2)/2
    c = np.sqrt(np.pi / 2)  # np.sqrt(np.pi/2)

    z = (
        c
        * std
        * (
            sci.special.erf((-x[:] + band) * s / std)
            - sci.special.erf((-x[:] - band) * s / std)
        )
    )

    # normalization for ease of computation
    z = z / np.max(z)

    return z


# flaterns the noise of DC and fundimental then replaces it of averge cut for capacitance
def Average_noiseflattern(harmonic, trunvec, avgnum):
    int_s = trunvec[0]  # first truncation point
    int_e = trunvec[1]  # second truncation point

    # adjustment for DC
    harmonic[:int_s] = np.average(harmonic[int_s + 1 : int_s + avgnum])
    harmonic[int_e:] = np.average(harmonic[int_e - avgnum : int_e])

    return harmonic


#
def noiseflattern(hil_store, time, trun):
    Ndc = 2  # here to exclude DC and fundimenal

    # finds indexes
    int_s = trunvec[0]  # first truncation point
    int_e = trunvec[1]  # second truncation point

    # truncates to zero
    hil_store[Ndc:, :int_s] = 0
    hil_store[Ndc:, int_e:] = 0

    return hil_store


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


# wrappers to unpack the harmonic info and pass to the convolution case
def square_window_wrapper(frequency_space, harmonic):
    conv = square_window(frequency_space, harmonic.bandwith, harmonic.freq)
    return conv

# this function takes the filter and ftt_current and outputs a harmonic envelope
def harmonic_envelope(Convguass, frequency_curr):

    N = frequency_curr.shape[0] # int(np.floor(frequency_curr.shape[0]/2))

    ## FLIP IT OR SET IMAGINARY TO O
    h = np.zeros(N, dtype=frequency_curr.dtype)
    if N % 2 == 0:
        h[0] = h[N // 2] = 1
        h[1 : N // 2] = 2
    else:
        h[0] = 1
        h[1 : (N + 1) // 2] = 2

    frequency_curr = frequency_curr * h
    #frequency_curr[n:] = 0

    # convert to harmonic TODO FIGURE OUT WHERE TO PUT THIS
    harmonic = ifft(Convguass * frequency_curr)

    # np abs converts the imaginary output to a real number
    return np.abs(harmonic) # np.imag(harmonic)#

# this function takes the filter and ftt_current and outputs a harmonic envelope
def total_current_harmonic(Convguass, frequency_curr):

    # convert to harmonic TODO FIGURE OUT WHERE TO PUT THIS
    harmonic = ifft(Convguass * frequency_curr)

    return harmonic.real

# make a class
class harmonics_generate():  

    def __init__(self,window_func="guassian",  envelope=True, flatten=False):
        
        self.flatten = flatten

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

            
        return

    # this function ID's if theres any unneeded harmonic information in the high frequency and
    # does a decismation in the frequency domain to speed up the ifft
    def frequency_decimation(self, frequency_curr, frequency_space,harmonics):

        # add something to calculate max frequency in harmonics
        max_harm_freq = 0
        for _, harm_group in harmonics.items():
            for _, harm in harm_group.items():
                if harm.freq > max_harm_freq:
                    max_harm_freq = harm.freq

        # based on above lightly decimate the frequency
        max_freq = frequency_space[int(frequency_space.shape[0]/2)-1]
        if max_freq > 4 * max_harm_freq:
            df = frequency_space[1]
            d_int = int(4 * max_harm_freq/df)
            y_deci = np.ceil(np.log2(d_int))
            y_full = np.floor(np.log2(frequency_space.shape[0]))
            d_ratio = 1/(2**(y_full - y_deci))

            if y_full > y_deci and d_ratio < 1: # just a saftey check
                # POSSIBLY DECIMATE THE HARMONICS FOR OPTIMISATION
                #print("CUNT",np.max(frequency_space),np.log2(frequency_space.shape)) # try deci 4
                d = int(frequency_curr.shape[0]*d_ratio/2)
                frequency_curr = np.concatenate((frequency_curr[:d], frequency_curr[-d:]))*d_ratio
                frequency_space = np.concatenate((frequency_space[:d], frequency_space[-d:]))


        return frequency_curr, frequency_space
    

    def __call__(self, Currenttot, MECsimstruct, harmonics):


        frequency_curr, frequency_space = ftcount.frequency_transform(
            Currenttot, MECsimstruct.time_tot
        )

        # check if we can decimate the harmonic information (only do if 2**N)
        y = np.log2(frequency_space.shape[0])
        if int(y) == y:
            frequency_curr, frequency_space = self.frequency_decimation(frequency_curr, frequency_space, harmonics)


        parent_harms = list(harmonics.keys())
        n = int((frequency_curr.shape[0]) / 2)
        for p_h in parent_harms:
            # loop over the harmonics
            for keys, harms in harmonics[p_h].items():

                # generate the harmonics
                # TODO make this optional
                Convguass = self.windowing(frequency_space, harms)

                # this deals with the imaginary component
                # TODO MOVE THIS INTO THE FUNCTION
                f = Convguass[:n]
                Convguass[n:] = f[::-1]

                harmonics[p_h][keys].harmonic = self.generation(Convguass, frequency_curr)

                # add something in here to opptionally flattern the noise
                if self.flatten:
                    # NOW THE ISSUE WITH THE FLATTEN IS WE NEED TO FIGURE OUT IF set to zero or average
                    pass

        return harmonics


# TODO REMOVE OR MAKE A UTILITY FUNCTION
def find_nearest(array1, value):
    array1 = np.asarray(array1)
    idx = (np.abs(array1 - value)).argmin()
    return int(idx)
