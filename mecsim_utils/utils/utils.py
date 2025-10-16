"""
This holds generic utils files
"""

import numpy as np


# function to get around python printing numbers truncated and worng0
def format_e(n):
    a = "%E" % n
    return a.split("E")[0].rstrip("0").rstrip(".") + "E" + a.split("E")[1]


# function for finding the nearest value in a series of array
def find_nearest(array, value):
    """Find nearest value is an array"""
    idx = (np.abs(array - value)).argmin()
    return idx
