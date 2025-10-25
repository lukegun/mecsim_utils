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
    inv_std = s/std

    z = (
        c
        * std
        * (
            sci.special.erf((-x[:] + mean + band * 0.5) *  inv_std)
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


# this sets up all the filters for the
def rg_guassconv_filters(Ndata, bandwidth, dt, AC_freq, std):
    filter_hold = []
    fft_freq = rfftfreq(Ndata, d=dt)
    Convguass = rg_guassconv_fund(
        fft_freq, bandwidth[0][0], std * bandwidth[0][0]
    )
    filter_hold.append(Convguass)

    for NNNN in range(1, len(bandwidth[1]) + 1):
        # analytical solution to guass rec convultion
        Convguass = rg_guassconv(
            fft_freq,
            bandwidth[1][NNNN - 1],
            NNNN * AC_freq[0],
            std * bandwidth[1][NNNN - 1],
        )
        filter_hold.append(Convguass)

    return filter_hold


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
    conv = rg_guassconv(frequency_space, harmonic.bandwith,
                    harmonic.freq, harmonic.std * harmonic.bandwith)  
    return conv


# wrappers to unpack the harmonic info and pass to the convolution case
def square_window_wrapper(frequency_space, harmonic):
    conv = square_window(frequency_space, harmonic.bandwith,
                        harmonic.freq)  
    return conv

import matplotlib.pyplot as plt

def harmonics_generate(Currenttot,MECsimstruct,harmonics, window_func="guassian", envolope=True):

    frequency_curr, frequency_space = ftcount.frequency_transform(
        Currenttot, MECsimstruct.time_tot
    )

    # POSSIBLY DECIMATE THE HARMONICS FOR OPTIMISATION

    # THIS CAN BE REMOVED AS we should be able to abstract it away with the 
    # below function
    parent_harms = list(harmonics.keys())
    if 0 in parent_harms:
        parent_harms.remove(0)

    # set something up split to optional function for windowing and output harmonic vs harmonic current
    match window_func:
        case "guassian":
            windowing = rg_guassconv_wrapper
        case "square":
            windowing = square_window_wrapper
        case _:
            raise ValueError(f'ERROR: unreconised window func "{window_func}", please use guassian or square.')

    n = int((frequency_curr.shape[0])/2)
    N = frequency_curr.shape[0]
    # TODO fix this
    # loop the harmonics
    for p_h in parent_harms:
        # loop over the harmonics 
        for keys, harms in harmonics[p_h].items():

            # generate the harmonics
            # TODO make this optional
            Convguass = windowing(frequency_space, harms)

            # this deals with the imaginary component
            f = Convguass[:n]
            Convguass[n:] = f[::-1]

            # TODO PUT THE total current vs envolope harmonic
            if envolope:
                ## FLIP IT OR SET IMAGINARY TO O
                #frequency_curr[n:] = 0
                print("FUCK")
                h = np.zeros(N, dtype= frequency_curr.dtype)
                if N % 2 == 0:
                    h[0] = h[N // 2] = 1
                    h[1:N // 2] = 2
                else:
                    h[0] = 1
                    h[1:(N + 1) // 2] = 2


                frequency_curr = frequency_curr*h
                #frequency_curr[n:] = 0



            # convert to harmonic TODO FIGURE OUT WHERE TO PUT THIS
            harmonic = ifft(Convguass * frequency_curr)

            # put the harmonic back in the structure
            # TODO truncate this somewhere ????
            # FIX THERES A BUG HERE WHERE SIGNALS DO NOT MATCH
            if envolope:
                harmonics[p_h][keys].harmonic = np.abs(harmonic)
            else:
                harmonics[p_h][keys].harmonic = harmonic.real #np.absolute(harmonic)
    # flattern noise ???



    return harmonics


# TODO REMOVE OR MAKE A UTILITY FUNCTION
def find_nearest(array1, value):
    array1 = np.asarray(array1)
    idx = (np.abs(array1 - value)).argmin()
    return int(idx)
