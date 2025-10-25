import numpy as np
from copy import deepcopy
import time

from mecsim_utils.processing.auto_ftacv import FTACV_experiment

from mecsim_utils.transformations.inp.datamodel import INP_DataModel
import mecsim_utils.processing.utils as mecUtils

# this imports the FTACV stuff
import mecsim_utils.processing.auto_ftacv as ftcount
import mecsim_utils.processing.window_func as ft_wind

import matplotlib.pyplot as plt


# dummy AC case
def main():

    test_case = 0
    exp_inp = (
        "tests/testingconfig/Master.inp",
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

    plt.figure()
    plt.plot(frequency_space)
    plt.savefig("frequencyspace.png")
    plt.close()

    # TODO RENAME
    Ftacv_Class = ftcount.FTACV_experiment(MECsimstruct)
    harmonics = Ftacv_Class(Currenttot)

    # TO DO SET UP A FUNCTION TO DO WINDOWING AND HARMONIC EXTRACTION
    # TODO add a function to write this function
    harmonics_BU = deepcopy(harmonics)
    func = ft_wind.harmonics_generate(
         window_func="guassian", envelope=False
    )
    harmonics = func(Currenttot, MECsimstruct, harmonics)
    t1 = time.time()
    func = ft_wind.harmonics_generate(
         window_func="guassian", envelope=True
    )
    harmonics2 = func(Currenttot, MECsimstruct, harmonics_BU)
    t = np.linspace(0, MECsimstruct.time_tot, num=int(harmonics[1]["1"].harmonic.shape[0]))

    for i, (harms1, harms2) in enumerate(zip(harmonics[1].values(),harmonics2[1].values())):
        print(i, max(harms2.harmonic))
        plt.figure()
        plt.plot(t, harms1.harmonic)
        plt.plot(t, harms2.harmonic)
        plt.savefig(f"{i + 1}_harm.png")
        plt.close()


if __name__ == "__main__":
    main()
