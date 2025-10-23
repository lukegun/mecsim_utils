"""
These tests validate that the ftacv processing all work
"""

import mecsim_utils.processing.auto_ftacv as ftcount

# load in the sample testing stuff
from tests.unittests.fixture_ftacv import inp_factory, current_factory  # fixtures


def test_frequency_transform(current_factory):
    Currenttot, MECsimstruct = current_factory

    frequency_curr, frequency_space = ftcount.frequency_transform(
        Currenttot, MECsimstruct.time_tot
    )

    assert (
        Currenttot.shape == frequency_curr.shape
    ), "ERROR: returned current in f space has the wrong shape"
    assert (
        Currenttot.shape == frequency_space.shape
    ), "ERROR: frequency space returned something wrong"

    return


#
def test_auto_harmcount(current_factory):
    Currenttot, MECsimstruct = current_factory

    print(Currenttot.shape)
    # calculate a rough N estimate
    Ftacv_Class = ftcount.FTACV_experiment(MECsimstruct)
    harmonics = Ftacv_Class(Currenttot)
    # Nprim = ftcount.harmoniccounter(current_factory, nsimdeci, PSdiff=1.)

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
