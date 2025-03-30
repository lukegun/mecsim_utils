"""
    These are a bunch of functions for auto identifying function involved with 
    auto identifying things involved with processing the ftacv signal

"""


import numpy as np
import mecsim_utils.utils.utils as Cutils
from scipy.fft import rfft, rfftfreq

# these are all required such that frequency and scanrate couple and analytical is to difficult. multiple DNNs
# Will be reuired for higher faster DC regions
# TODO MAKE THESE FUNCTIONS A BUNCH SMARTER
def bandwidthallocator(freq):

    # sets up an array which can be called from 
    bandwidth = bandwidthchanger(6)

    if freq <= 12:
        bandwidth = bandwidth[0]
    elif freq > 12 and freq <= 24:
        bandwidth = bandwidth[1]
    elif freq > 24 and freq <= 34:
        bandwidth = bandwidth[2]
    elif freq > 34 and freq <= 45:
        bandwidth = bandwidth[3]
    elif freq > 45 and freq <= 75:
        bandwidth = bandwidth[4]
    elif freq >= 75:
        bandwidth = bandwidth[5]
    else:
        print("incorrect parameters")
        print(freq)

    return bandwidth


# required to change the broadening of peaks due to scanrate
def bandwidthchanger(bandwidth):

    bandwidth2 = [bandwidth]
    bandwidth2.append(bandwidth*1.5) #12
    bandwidth2.append(bandwidth*2)  #18
    bandwidth2.append(bandwidth*3)  #18
    bandwidth2.append(bandwidth * 3)   #60
    bandwidth2.append(bandwidth * 3)   #72

    return bandwidth2

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

    fft_res = rfft(Curr)

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