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

    test_case = 2
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
    Ftacv_Class = ftcount.FTACV_experiment(MECsimstruct, threshold=1.15)
    harmonics = Ftacv_Class(Currenttot)

    # TO DO SET UP A FUNCTION TO DO WINDOWING AND HARMONIC EXTRACTION
    # TODO add a function to write this function
    harmonics_BU = deepcopy(harmonics)
    func = ft_wind.harmonics_generate(window_func="guassian", envelope=False)
    harmonics = func(Currenttot, MECsimstruct, harmonics)
    t1 = time.time()
    func = ft_wind.harmonics_generate(
        window_func="guassian", envelope=True, flatten_percent=0.01
    )
    harmonics2 = func(Currenttot, MECsimstruct, harmonics_BU)

    t = np.linspace(
        0, MECsimstruct.time_tot, num=int(harmonics[0]["0"].harmonic.shape[0])
    )

    for keys_p, harms2 in harmonics2.items():
        for keys_c, harms in harms2.items():
            print(f"{keys_p}_{keys_c}", max(harms.harmonic))
            plt.figure()
            plt.plot(t, harms.harmonic)
            plt.savefig(f"pics/{keys_p}_{keys_c}_harm.png")
            plt.close()


if __name__ == "__main__":
    main()
