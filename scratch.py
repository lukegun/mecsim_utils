import numpy as np

from mecsim_utils.processing.auto_ftacv import FTACV_experiment

from mecsim_utils.transformations.inp.datamodel import INP_DataModel
import mecsim_utils.processing.utils as mecUtils

# this imports the FTACV stuff
import mecsim_utils.processing.auto_ftacv as ftcount
import matplotlib.pyplot as plt


# dummy AC case
def main():

    test_case = 1
    exp_inp = (
        "tests/testingconfig/MasterE_2AC.inp",
        "tests/testingconfig/MasterE_3AC.inp",
    )

    Mec_parser = INP_DataModel(exp_inp[test_case], to_struct=True)
    MECsimstruct = (
        Mec_parser.transform()
    )  # I can modify this to shift between DC and FTACV

    """I SHOULD PUT SOMETHING HERE TO MORE CLEANLY WRAP THE mecsim instance and the transformation"""
    Currenttot = mecUtils.mecsim_current(MECsimstruct)

    frequency_curr, frequency_space = ftcount.frequency_transform(
        Currenttot, MECsimstruct.time_tot
    )

    ln_current = np.log(frequency_curr)

    # TODO RENAME
    Ftacv_Class = ftcount.FTACV_experiment(MECsimstruct)
    harmonics = Ftacv_Class(Currenttot)

    # TO DO SET UP A FUNCTION TO DO WINDOWING AND HARMONIC EXTRACTION


if __name__ == "__main__":
    main()
