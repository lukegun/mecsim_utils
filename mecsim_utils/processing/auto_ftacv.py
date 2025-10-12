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
    hW = (W-1)//2 # Half window size
    return scipy.ndimage.maximum_filter1d(a.real,size=W)[hW:-hW]

# these are all required such that frequency and scanrate couple and analytical is to difficult. multiple DNNs
# Will be reuired for higher faster DC regions
# TODO MAKE THESE FUNCTIONS A BUNCH SMARTER
def bandwidthallocator(frequency_current, frequency_space, MECsimstruct, label, maxharm=12):

    # get the ac signals
    AC_signals = [x["f"] for x in MECsimstruct.AC]
    
    # constant values
    constant= False
    if constant:
        pass
    # automatic detection
    else:
        print(AC_signals)
        # this will need to be a standa alone function
        ln_current = np.log(frequency_current)

        # Smooth the max of the background and fit
        n = int(frequency_space.shape[0]/2)
        fit = max_filter1d_valid(ln_current[:n],60)
        
        # account for windowing function
        n2 = fit.shape[0]
        diff = int((n - n2)/2)

        # could add an additional process here to remove the known harmonic info
        p=np.polyfit(frequency_space[diff:n-diff],fit, 7)
        func = np.poly1d(p)
        fit = func(frequency_space[:n])
      
        plt.figure()
        plt.plot(frequency_space[:n],ln_current[:n])
        plt.plot(frequency_space[:n],fit)
        plt.savefig(f"{label}.png")

        # need to figure out rough possible



        # count AC signals (make multiAC possible) secondarary
        threshold = 2.30

        #  generate a bandwidth

    return 


def frequency_transform(Currenttot, tot_time):

    n = Currenttot.shape[0]
    dt = tot_time/n

    frequency_space = fftfreq(n, d=dt)
    frequency_curr = fft(Currenttot)

    return frequency_curr, frequency_space

def single_AC(AC_signals,nmax=12):

    possible_harmonics = {}
    for i in range(1,nmax+1):
        freq = i*AC_signals[0]
        datastruct = datastruct_func(freq,{f"{AC_signals[0]}":i},1,i)
        possible_harmonics.update({f"{freq}":datastruct})

    return possible_harmonics

def calc_secondrary(AC_signals,nmax=12):

    possible_harmonics = {}

    AC_signals.sort().reverse()

    # only need to do this for the larger of the two  (ie little one splitting of major)
    for i in range(1,nmax+1):
        for j in range(1,nmax+1):
            k = abs(i)+ abs(j)

            #for z in range(3): # loop over the pos and negitive cases
            freq_pos_pos = i*AC_signals[0] + j*AC_signals[1]
            freq_pos_neg = i*AC_signals[0] - j*AC_signals[1]
            freq_neg_pos = -i*AC_signals[0] + j*AC_signals[1]
            if freq_pos_pos not in possible_harmonics.keys(): # to avoid duplicates
                datastruct = datastruct_func(freq_pos_pos,
                                                {f"{AC_signals[0]}":i,
                                                f"{AC_signals[1]}": j},
                                                2, k)
                possible_harmonics.update({f"{freq_pos_pos}":datastruct})

            if freq_pos_neg > 0 and freq_pos_neg not in possible_harmonics.keys(): # to avoid duplicates
                datastruct = datastruct_func(freq_pos_neg,
                                                {f"{AC_signals[0]}":i,
                                                f"{AC_signals[1]}":-j},
                                            2, k)
                possible_harmonics.update({f"{freq_pos_neg}":datastruct})

            if freq_neg_pos > 0 and freq_neg_pos not in possible_harmonics.keys(): # to avoid duplicates
                datastruct = datastruct_func(freq_neg_pos,
                                                {f"{AC_signals[0]}":-i,
                                                f"{AC_signals[1]}":j},
                                            2, k)
                possible_harmonics.update({f"{req_neg_pos}":datastruct})

    return possible_harmonics

def calc_tertiary(AC_signals,nmax=12):

    possible_harmonics = {}

    AC_signals.sort().reverse()

    
    for i in range(nmax):
        for j in range(nmax):
            for k in range(nmax):
                freq_pos_pos = i*AC_signals[0] + j*AC_signals[1] + k*AC_signals[2]
                freq_pos_neg = i*AC_signals[0] + j*AC_signals[1] - k*AC_signals[2]
                freq_neg_pos = i*AC_signals[0] - j*AC_signals[1] + k*AC_signals[2]
                freq_neg_neg = i*AC_signals[0] - j*AC_signals[1] + k*AC_signals[2]
            

    return possible_harmonics

def dual_AC(AC_signals, nmax=12):

    possible_harmonics = {}
    # identify the primrary harmonics
    primary_harms = single_AC([AC_signals[0]],nmax=nmax)
    possible_harmonics.update(primary_harms)

    primary_harms = single_AC([AC_signals[1]],nmax=nmax)
    possible_harmonics = append_and_check(primary_harms, possible_harmonics)

    # calculate the secondary harmonics
    secondary_harms =  calc_secondrary(AC_signals,nmax=nmax)
    possible_harmonics = append_and_check(secondary_harms, possible_harmonics)

    return


def triplicate_AC(AC_signals, nmax=12):


    possible_harmonics = {}
    # calculate the primrary harmonics
    for z in range(3):
        primary_harms = single_AC([AC_signals[z]],nmax=nmax)
        possible_harmonics = append_and_check(primary_harms, possible_harmonics)

    # calculate the secondary harmonics
    for z in range(3):
        secondary_harms =  calc_secondrary([AC_signals[z],AC_signals[(z+1)%2]],nmax=nmax)
        possible_harmonics = append_and_check(secondary_harms, possible_harmonics)

    # calculate the tertiary frequencies


    return

# clean function for defining the FTACV_harmonic goes args to kwargs
def datastruct_func(freq,combination,allocation,harmonic_num):
    datastruct = FTACV_harmonic(freq=freq,
                                combination = combination , # dict of AC harmonic combination 
                                allocation=allocation ,# 0 for dc, 1 for primrary, 2 for secondary so on
                                harmonic_num=harmonic_num,
                                    )
    return datastruct

def append_and_check(incoming_dic, landing_dic):

    for keys, items in incoming_dic.items():
        if keys not in landing_dic.keys():
            landing_dic.update({keys:items})
    
    return landing_dic

# this is the parent class for the FTACV experiment ( this stores and links all the harmonic data structures)
class FTACV_experiment():



    def __init__(self, MECsimstruct, Nmax = 12):

         # get the ac signals
        self._AC_signals = [x["f"] for x in MECsimstruct.AC]
        self._AC_signals.sort().reverse()
        self._Nac = len(self._AC_signals)
        self._Nmax = Nmax

        assert self._Nac != 0, "ERROR: no AC signal found for experiment"
        
        # confirm that the AC allocation function is right for number of AC_signals
        if self._Nac == 1:
            self.harmonic_alloc = single_AC
        elif self._Nac == 2:
            self.harmonic_alloc = dual_AC
        elif self._Nac == 3:
            self.harmonic_alloc = triplicate_AC
        else:
            raise ValueError("Number of AC signals are not currently supported")



        return

    # this identifies all the possible harmonics and 
    def __call__(self):
        print(self._Nac)

        # identify all stable possible AC harmonics
        possible_harmonics = self.harmonic_alloc(self._AC_signals,nmax=self._Nmax)

        # check the threshold and tune


        # generate the harmonics

        return  possible_harmonics



# this is a specific harmonic information
@dataclass
class FTACV_harmonic:

    freq: float
    combination: dict # list of AC harmonic combination 
    allocation: int # 0 for dc, 1 for primrary, 2 for secondary so on
    #harmonic: Optional[np.array] # this stores the harmonic but that information comes later
    harmonic_num: int # abs sum of the combination
    bandwith: float = 4 # defaults to 4 Hz

    def __repr__(self):
        # put something here so people know whats in the dataclass
        return f"""Harmonic information for {self.freq} Hz, as the {self.harmonic_num} harmonic of {self.allocation}."""
