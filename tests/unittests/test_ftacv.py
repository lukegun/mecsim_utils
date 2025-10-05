"""
    These tests validate that the ftacv processing all work
"""
import pytest
import numpy as np

import mecsim_utils.processing.utils as mecUtils
import mecsim_utils.processing.auto_ftacv as ftcount

# load in the sample testing stuff
from tests.unittests.config import inp_factory, current_factory
import mecsim_utils.processing.auto_ftacv as ftcount


def test_frequency_transform(current_factory):

    Currenttot, MECsimstruct = current_factory

    frequency_curr, frequency_space = ftcount.frequency_transform(Currenttot, MECsimstruct)

    

    return

# test bandwidth allicator
def test_bandwidth_ally(current_factory):

    Currenttot, MECsimstruct = current_factory

    # get autobandwidth
    bandwidth = ftcount.bandwidthallocator(Currenttot, MECsimstruct.AC[0]["f"])

    return

# test the nsimdeci
def test_Sim_deci():

    np = len(Currenttot)
    deltatime = 14/np
    nsimdeci = ftcount.Simerharmtunc(len(Currenttot), deltatime, bandwidth, MECsimstruct.AC[0]["f"], HarmMax=12)

    return

# 
def test_auto_harmcount(current_factory):

    Currenttot, MECsimstruct = current_factory

    print(Currenttot.shape)
    # calculate a rough N estimate
    Nprim = ftcount.harmoniccounter(current_factory, nsimdeci, PSdiff=1.)

    return

#
def test_bandwidthsetup():

    return

#
def test_square_windowing():

    return

#
def test_guassian_windowing():

    return


# test harmonic extraction
def test_primrary_harmonic_extraction():

    return

# test harmonic extraction
def test_secondary_harmonic_extraction():

    return