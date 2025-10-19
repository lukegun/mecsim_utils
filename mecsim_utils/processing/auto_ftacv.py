"""
These are a bunch of functions for auto identifying function involved with
auto identifying things involved with processing the ftacv signal

"""

import scipy
import numpy as np
import mecsim_utils.utils.utils as Cutils
from scipy.fft import ifft, fft, fftfreq
from typing import Optional

from dataclasses import dataclass

# plotting functions
import matplotlib.pyplot as plt

"""
    I think I need to sit down and figure out the best way to organise the flow of these systems at some point
"""


# move this to a utils function or just in the bandwidth processing
def max_filter1d_valid(a, W):
    hW = (W - 1) // 2  # Half window size
    return scipy.ndimage.maximum_filter1d(a.real, size=W)[hW:-hW]


# these are all required such that frequency and scanrate couple and analytical is to difficult. multiple DNNs
# Will be reuired for higher faster DC regions
# TODO MAKE THESE FUNCTIONS A BUNCH SMARTER
def bandwidthallocator(
    frequency_current, frequency_space, MECsimstruct, label, maxharm=12
):

    # get the ac signals
    AC_signals = [x["f"] for x in MECsimstruct.AC]
    # constant values
    constant = False
    if constant:
        pass
    # automatic detection
    else:
        print(AC_signals)
        # this will need to be a standa alone function
        ln_current = np.log(frequency_current)

        # Smooth the max of the background and fit
        n = int(frequency_space.shape[0] / 2)
        fit = max_filter1d_valid(ln_current[:n], 60)

        # account for windowing function
        n2 = fit.shape[0]
        diff = int((n - n2) / 2)

        # could add an additional process here to remove the known harmonic info
        p = np.polyfit(frequency_space[diff : n - diff], fit, 7)
        func = np.poly1d(p)
        fit = func(frequency_space[:n])

        plt.figure()
        plt.plot(frequency_space[:n], ln_current[:n])
        plt.plot(frequency_space[:n], fit)
        plt.savefig(f"{label}.png")

        # need to figure out rough possible

        # count AC signals (make multiAC possible) secondarary
        threshold = 2.30

        #  generate a bandwidth

    return


def AC_threshold_check(
    frequency_current, frequency_space, harmonics, ongoing_freq, threshold=2.30, nmax=12
):

    # get the frequency increment
    df = frequency_space[1]

    # this will need to be a standa alone function
    ln_current = np.log(np.abs(frequency_current))

    # Smooth the max of the background and fit
    n = int(frequency_space.shape[0] / 2)
    fit = max_filter1d_valid(ln_current[:n], 60)

    # account for windowing function
    n2 = fit.shape[0]
    diff = int((n - n2) / 2)

    # could add an additional process here to remove the known harmonic info
    p = np.polyfit(frequency_space[diff : n - diff], fit, 7)
    func = np.poly1d(p)
    fit = func(frequency_space[:n])

    # compare ln_current to the fit over the harmonics
    lndiff = ln_current[:n] - fit

    harmonics = calibrate_harms(harmonics, ongoing_freq, lndiff, df, threshold)

    return harmonics


# this probably isn't required but easiest to do for time being
def calibrate_harms(harmonics, ongoing_freq, lndiff, df, threshold):

    # check how many allocations are in the system
    harms = list(harmonics.keys())
    harms.sort()

    # check the primrary harmonics
    for j in range(1, len(harms) + 1):
        for i in range(1, len(list(harmonics[j].keys())) + 1):
            # get band of interest
            exist, temp_harms = check_harm_band(
                harmonics[j][str(i)], ongoing_freq, lndiff, df, threshold
            )

            if exist:
                harmonics[1][i] = temp_harms
            else:
                # TODO drop all other related harmonics
                term_harm = str(i)
                break
            # RECURSIVE
            # check threshold add to drop and continue

        # delete the primrary harmonics
        for h in harms[j:]:
            keys = list(harmonics[h].keys())
            for hi in keys:
                if term_harm == hi.split("-")[j - 1]:
                    del harmonics[h][hi]

    return harmonics


def check_harm_band(harms, ongoing_freq, lndiff, df, threshold):

    AC_freq = harms.freq

    int_harmband_1 = int((AC_freq - 0.5) / df)
    int_harmband_2 = int((AC_freq + 0.5) / df)

    #
    lndiff = np.where(lndiff < 0, 0, lndiff)

    # check if the freq is above a threshold
    adjustedband = False
    test_freq = 0.25
    # get the max value in the diff
    peak_current = np.max(lndiff[int_harmband_1:int_harmband_2])
    if peak_current > threshold:
        exist = True
        # adjust the bandwidth
        n = 24
        for i in range(1, n):
            i1 = int((AC_freq - i * test_freq) / df)
            i2 = int((AC_freq + i * test_freq) / df)
            # detect if the bandwidth is appropriate minimum
            if np.average(lndiff[i1:i2]) < peak_current * 0.2:
                minband = 2 * i * test_freq
                adjustedband = True
                break

        if not adjustedband:
            minband = 2 * (n - 1) * test_freq

        # calculate the maximum bandwidth
        # TODO make rounding safe
        ind = ongoing_freq.index(
            int(AC_freq)
        )  # we use int as its a quick truncation to a labelled harm
        if ind == 0:
            bandidthrange = (AC_freq, ongoing_freq[ind + 1] - AC_freq)
        else:
            bandidthrange = (
                AC_freq - ongoing_freq[ind - 1],
                ongoing_freq[ind + 1] - AC_freq,
            )

        # TODO add something to prevent edge case of negitive here
        max_range = (
            min(bandidthrange) - minband
        )  # this takes the average between largest and smallest

        # some arbitrary rule to attempt to estimate the
        # Edge cases (massive AC harmonics)
        # to harmonic overlaps (KILL harmonics)
        bandwidth = min(max_range, 40, 2 * 6 * minband)
        print(
            ind,
            AC_freq,
            ongoing_freq[ind],
            bandidthrange,
            max_range,
            bandwidth,
            minband,
        )

        # TODO use some basic set of rules to take the average of the two abovve or some failsafe rules for the edge cases
        # harms.bandwith
        # NOTE BANDWIDTH IS RANGE OF WINDOW
        if exist:
            if minband not in [0.5, 1.0] and ind == 8:
                plt.plot(lndiff[i1:i2])
                plt.savefig("test2.png")
                plt.close()
                exit(1)
        print(
            "ohno", harms, harms.bandwith, adjustedband, np.max(lndiff[i1:i2]), i1, i2
        )
    else:
        exist = False

    return exist, harms


def frequency_transform(Currenttot, tot_time):

    n = Currenttot.shape[0]
    dt = tot_time / n

    frequency_space = fftfreq(n, d=dt)
    frequency_curr = fft(Currenttot)

    return frequency_curr, frequency_space


def calc_primrary(AC_signal, ongoing_freq=set(), nmax=12):

    temp_harmonics = {}
    for i in range(1, nmax + 1):
        freq = i * AC_signal
        if int(freq) not in ongoing_freq:
            ongoing_freq.add(int(freq))
            s = f"{i}"
            datastruct = datastruct_func(freq, {AC_signal: i}, 1, i)
            temp_harmonics.update({s: datastruct})

    return temp_harmonics, ongoing_freq


def calc_secondrary(AC_signals, ongoing_freq=set(), nmax=12):

    possible_combinations = [(1, 1), (1, -1), (-1, 1)]

    AC_signals.sort()
    AC_signals.reverse()

    possible_harmonics = {}

    # only need to do this for the larger of the two  (ie little one splitting of major)
    for i in range(1, nmax + 1):
        for j in range(1, nmax + 1):
            p = i + j
            for z1, z2 in possible_combinations:  # loop over the pos and negitive cases
                freq = z1 * i * AC_signals[0] + z2 * j * AC_signals[1]
                if freq > 0 and int(freq) not in ongoing_freq:  # to avoid duplicates
                    ongoing_freq.add(int(freq))
                    s = f"{z1*i}:{z2*j}"
                    datastruct = datastruct_func(
                        freq, {AC_signals[0]: z1 * i, AC_signals[1]: z2 * j}, 2, p
                    )
                    possible_harmonics.update({s: datastruct})

    return possible_harmonics, ongoing_freq


def calc_tertiary(AC_signals, ongoing_freq=set(), nmax=12):

    AC_signals.sort()
    AC_signals.reverse()

    possible_harmonics = {}

    # this are combination of harmonics we are using
    possible_combinations = [
        (1, 1, 1),
        (1, 1, -1),
        (1, -1, 1),
        (-1, 1, 1),
        (1, -1, -1),
        (-1, 1, -1),
        (-1, -1, 1),
    ]

    for i in range(nmax):
        for j in range(nmax):
            for k in range(nmax):
                p = i + j + k
                for (
                    z1,
                    z2,
                    z3,
                ) in possible_combinations:  # loop over the pos and negitive cases
                    freq = (
                        z1 * i * AC_signals[0]
                        + z2 * j * AC_signals[1]
                        + z3 * k * AC_signals[2]
                    )
                    if (
                        freq > 0 and int(freq) not in ongoing_freq
                    ):  # to avoid duplicates
                        ongoing_freq.add(int(freq))
                        s = f"{z1*i}:{z2*j}:{z3*k}"
                        datastruct = datastruct_func(
                            freq,
                            {
                                AC_signals[0]: z1 * i,
                                AC_signals[1]: z2 * j,
                                AC_signals[2]: z3 * k,
                            },
                            3,
                            p,
                        )
                        possible_harmonics.update({s: datastruct})

    return possible_harmonics, ongoing_freq


def single_AC(AC_signals, possible_harmonics={}, ongoing_freq=set(), nmax=12):

    possible_harmonics = {1: {}}
    ongoing_freq = set()
    temp, ongoing_freq = calc_primrary(
        AC_signals[0], ongoing_freq=ongoing_freq, nmax=nmax
    )
    possible_harmonics[1].update(temp)

    return possible_harmonics, ongoing_freq


def dual_AC(AC_signals, nmax=12):

    possible_harmonics = {1: {}, 2: {}}
    ongoing_freq = set()

    # identify the primrary harmonics
    for z in range(2):
        temp, ongoing_freq = calc_primrary(AC_signals[z], ongoing_freq, nmax=nmax)
        possible_harmonics[1].update(temp)

    # calculate the secondary harmonics
    temp, ongoing_freq = calc_secondrary(AC_signals, ongoing_freq, nmax=nmax)
    possible_harmonics[2].update(temp)

    return possible_harmonics, ongoing_freq


def triplicate_AC(AC_signals, nmax=12):

    possible_harmonics = {1: {}, 2: {}, 3: {}}
    ongoing_freq = set()
    # calculate the primrary harmonics
    for z in range(3):
        temp, ongoing_freq = calc_primrary(AC_signals[z], ongoing_freq, nmax=nmax)
        possible_harmonics[1].update(temp)

    # calculate the secondary harmonics
    for z in range(3):
        temp, ongoing_freq = calc_secondrary(
            [AC_signals[z], AC_signals[(z + 1) % 2]], ongoing_freq, nmax=nmax
        )
        possible_harmonics[2].update(temp)

    # calculate the tertiary frequencies
    temp, ongoing_freq = calc_tertiary(AC_signals, ongoing_freq, nmax=nmax)
    possible_harmonics[3].update(temp)

    return possible_harmonics, ongoing_freq


# clean function for defining the FTACV_harmonic goes args to kwargs
def datastruct_func(freq, combination, allocation, harmonic_num):
    datastruct = FTACV_harmonic(
        freq=freq,
        combination=combination,  # dict of AC harmonic combination
        allocation=allocation,  # 0 for dc, 1 for primrary, 2 for secondary so on
        harmonic_num=harmonic_num,
    )

    return datastruct


# this is the parent class for the FTACV experiment ( this stores and links all the harmonic data structures)
# TODO MAKE THIS MORE LIKE A CLASS WHERE SELF CONTAINED
class FTACV_experiment:

    def __init__(self, MECsimstruct, Nmax=12):

        # get the ac signals
        self.MECsimstruct = MECsimstruct
        self._AC_signals = [x["f"] for x in self.MECsimstruct.AC]
        self._AC_signals.sort()
        self._AC_signals.reverse()
        self._Nac = len(self._AC_signals)
        self._Nmax = Nmax

        assert self._Nac != 0, "ERROR: no AC signal found for experiment"
        print("hello", self._AC_signals, self._Nac)
        # confirm that the AC allocation function is right for number of AC_signals
        if self._Nac == 1:
            self.harmonic_alloc = single_AC
        elif self._Nac == 2:
            self.harmonic_alloc = dual_AC
        elif self._Nac == 3:
            self.harmonic_alloc = triplicate_AC
        else:
            raise ValueError(
                "Number of AC signals greater then 3 are not currently supported"
            )

        return

    # this identifies all the possible harmonics and
    def __call__(self, Currenttot):
        print(self._Nac)

        # identify all stable possible AC harmonics
        # TODO: split up the primrary, secondary and tert harmonics an label in possible harmonic
        # another issue is we use hertz labeling and not a nomeculture name
        possible_harmonics, ongoing_freq = self.harmonic_alloc(
            self._AC_signals, nmax=self._Nmax
        )

        # convert ongoing freqency to sorted listy
        ongoing_freq = list(ongoing_freq)
        ongoing_freq.sort()

        # add in the DC component

        # check the threshold and tune
        frequency_current, frequency_space = frequency_transform(
            Currenttot, self.MECsimstruct.time_tot
        )

        print("FUCK", frequency_space[0], frequency_space[1])

        # adjust bandwidths
        AC_threshold_check(
            frequency_current,
            frequency_space,
            possible_harmonics,
            ongoing_freq,
            threshold=2.3,
            nmax=self._Nmax,
        )

        # remove overlapping bandwidths

        # generate the harmonics

        return possible_harmonics


# this is a specific harmonic information
@dataclass
class FTACV_harmonic:

    freq: float
    combination: dict  # list of AC harmonic combination {Hz: scalar multi}
    allocation: int  # 0 for dc, 1 for primrary, 2 for secondary so on
    # harmonic: Optional[np.array] # this stores the harmonic but that information comes later
    harmonic_num: int  # abs sum of the combination
    bandwith: float = 4  # defaults to 4 Hz

    def __repr__(self):

        hertz = []
        for keys in self.combination.keys():
            hertz.append(keys)

        hertz.sort()
        hertz.reverse()

        s = f"{self.combination[hertz[0]]}"
        if len(hertz) > 1:
            for keys in hertz[1:]:
                s += f",{self.combination[keys]}"

        # put something here so people know whats in the dataclass
        return f"""Harmonic information for {s} at {self.freq} Hz, as the {self.harmonic_num} harmonic of {self.allocation}."""
