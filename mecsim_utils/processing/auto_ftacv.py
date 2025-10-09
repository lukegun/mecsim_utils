"""
    These are a bunch of functions for auto identifying function involved with 
    auto identifying things involved with processing the ftacv signal

"""

import scipy
import numpy as np
import mecsim_utils.utils.utils as Cutils
from scipy.fft import ifft, fft, fftfreq


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
def bandwidthallocator(frequency_current, frequency_space, MECsimstruct, label):

    # get the ac signals
    AC_signals = [x["f"] for x in MECsimstruct.AC]
    
    # constant values
    constant= False
    if constant:
        pass
    # automatic detection
    else:
        print(AC_signals)
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
      
        #plt.figure()
        #plt.plot(frequency_space[:n],ln_current[:n])
        #plt.plot(frequency_space[:n],fit)
        #plt.savefig(f"{label}.png")

        # count AC signals (make multiAC possible) secondarary


        #  generate a bandwidth

        
    
    return 


def frequency_transform(Currenttot, tot_time):

    n = Currenttot.shape[0]
    dt = tot_time/n

    frequency_space = fftfreq(n, d=dt)
    frequency_curr = fft(Currenttot)

    return frequency_curr, frequency_space


#extracts windows for log10 auto counter
def Simerharmtunc(Nsimlength, exptime, bandwidth, AC_freq, HarmMax=12):
    # this checky fix migt cause some issues
    Nex = [0]
    truntime = [0, HarmMax*AC_freq+2*AC_freq]
    frequens = rfftfreq(Nsimlength, d=exptime)

    N = HarmMax #len(bandwidth[0])
    nsimdeci = []

    # DC section
    if bandwidth[0][0] != 0:
        if truntime[0] < bandwidth[0][0]:
            Nhigh = -Nex[0] + Cutils.find_nearest(frequens, bandwidth[0][0])
            nsimdeci.append([0,Nhigh])

    j = 0
    while j != 1:
        i = 0
        while i != N:
            if (i+1)*AC_freq[j] + bandwidth[j + 1][i]/2 > truntime[1] or (i+1)*AC_freq[j] + bandwidth[j + 1][i]/2 >max(frequens):
                if (i + 1) * AC_freq[j] - bandwidth[j + 1][i]/2 < truntime[1]:
                    Nwindlow = -Nex[0] + Cutils.find_nearest(frequens, (i + 1) * AC_freq[j] - bandwidth[j + 1][i]/2)
                    Nwindhigh = Nsimlength  # this will probs be some arbitary number/freq
                    #freqx.append(frequens[Nwindlow:Nwindhigh])
                    nsimdeci.append([Nwindlow, Nwindhigh])
                i = N
            else:
                Nwindlow = -Nex[0] + Cutils.find_nearest(frequens, (i+1)*AC_freq[j] - bandwidth[j + 1][i]/2)
                Nwindhigh = -Nex[0] + Cutils.find_nearest(frequens, (i+1)*AC_freq[j] + bandwidth[j + 1][i]/2)
                #freqx.append(frequens[Nwindlow:Nwindhigh])
                nsimdeci.append([Nwindlow,Nwindhigh])
                i += 1
        j += 1

    return nsimdeci


def PSbackextract(powerspec, nsimdeci):

    PSBG = np.empty([0])  # Scurr[Nsimdeci[0][0]:Nsimdeci[0][1]]
    PSBGlist = []
    i = 0
    for X in nsimdeci[0:-1]:
        PSBG = np.concatenate((PSBG, powerspec[X[1]:nsimdeci[i + 1][0]]))
        PSBGlist.append(powerspec[X[1]:nsimdeci[i + 1][0]])
        i += 1

    return PSBG, PSBGlist


def PSsigextract(powerspec, nsimdeci):

    PSsignal = np.empty([0])  # Scurr[Nsimdeci[0][0]:Nsimdeci[0][1]]
    PSsiglist = []
    for X in nsimdeci:
        PSsignal = np.concatenate((PSsignal, powerspec[X[0]:X[1]]))
        PSsiglist.append(powerspec[X[0]:X[1]])

    return PSsignal, PSsiglist

def harmoniccounter(Curr, nsimdeci, PSdiff=1.0):

    fft_res = fft(Curr)

    # this can be done seperatly So lok into it
    #freq = rfftfreq(len(fft_res),d = exptime) try yo pass through DELTAexptime
    powerspec = np.log10(np.abs(fft_res) / len(fft_res))
    """Will need the code to extract harmonics and background"""

    PSBG, PSBGlist = PSbackextract(powerspec, nsimdeci)             #extracted background
    _, PBsiglist = PSsigextract(powerspec, nsimdeci)          #extracted signals

    #checks first harmonic to Harmax
    for i in range(1,len(PSBGlist) - 1):

        # Calculates the average max of the background
        backaverage = (np.max(PSBGlist[i])+np.max(PSBGlist[i+1]))/2
    
        sigmax = np.max(PBsiglist[i])
        if sigmax < backaverage + PSdiff:
            break

    Nharm = i -1

    return Nharm