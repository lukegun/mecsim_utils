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

        # count AC signals (make multiAC possible) secondarary


        #  generate a bandwidth

        
    
    return 


def frequency_transform(Currenttot, tot_time):

    n = Currenttot.shape[0]
    dt = tot_time/n

    frequency_space = fftfreq(n, d=dt)
    frequency_curr = fft(Currenttot)

    return frequency_curr, frequency_space
