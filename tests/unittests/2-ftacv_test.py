"""
These tests validate that the ftacv processing all work
"""

import pytest
import numpy as np

import mecsim_utils.processing.auto_ftacv as ftcount
import mecsim_utils.processing.window_func as ft_wind

# load in the sample testing stuff
from tests.unittests.fixture_ftacv import inp_factory, current_factory  # fixtures


# this function takes a number and rounds it based on scientific notation
# TODO move this elsewhere if its required
def quick_scientific_round(num, accuracy):
    return np.round(num, int(np.ceil(abs(np.log10(np.abs(num))))+accuracy))


def test_frequency_transform(current_factory):
    Currenttot, MECsimstruct, _ = current_factory

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

# NEED TO ADD A DC testing case (Could just add to below)

# NEED TO PARAMETERISE OVER WINDOWING AND window/totalcurrent
@pytest.mark.parametrize("window_func", ["guassian","square"])
@pytest.mark.parametrize("envelope", [True,False])
def test_auto_harmcount(current_factory, window_func, envelope):
    Currenttot, MECsimstruct, validation_data = current_factory

    # generate possible harmonics
    Ftacv_Class = ftcount.FTACV_experiment(MECsimstruct, threshold=validation_data.ft_threshold)
    harmonics = Ftacv_Class(Currenttot)
    
    # calculate the harmonics
    func = ft_wind.harmonics_generate(
        window_func=window_func, envelope=envelope, 
        flatten_percent=validation_data.flattern_percentage
    )
    harmonics = func(Currenttot, MECsimstruct, harmonics)

    # validate max harmonic and number of harmonics # also validate that the harmonics haven't corrupted
    round_acc = 0 # this is the rounding error that will be accepted # TODO HOW DO WE MAKE THIS ACCEPTABLE
    s = "ERROR: max value index not found at same point"
    i = 0
    for keys_p, harms2 in harmonics.items():
        for keys_c, harms in harms2.items():
            i += 1 # count the harmonics present
            expected_val =  validation_data.harmdic[keys_p][keys_c][0]
                #quick_scientific_round(
               # validation_data.harmdic[keys_p][keys_c][0], round_acc)
            
            npp_ind = np.argmax(harmonics[keys_p][keys_c].harmonic)
            npp = harmonics[keys_p][keys_c].harmonic[npp_ind]
            
            found_val = npp # quick_scientific_round(npp, round_acc)
            
            # assert that the value was found at expected value and point
            s = f"ERROR: max harmonic value varies to what is expected for {keys_p} / {keys_c}"
            assert np.abs(expected_val - found_val)/expected_val < 0.05, s
            #assert abs(npp_ind - validation_data.harmdic[keys_p][keys_c][1]) < 80, s # TODO FIX to work over parameterisation

    # validate the possible overall information are right COULD ADD DC HERE
    message = "ERROR, number of harmonics calculated don't match the precalculated amount expected"
    assert validation_data.N_harms == i, message
    message = "ERROR, Number in time series matches the expected size"
    assert validation_data.shape == Currenttot.shape[0], message
    message = "ERROR, average "
    assert (
        quick_scientific_round(validation_data.average, round_acc) == 
        quick_scientific_round(np.average(Currenttot), round_acc)), message

    return

