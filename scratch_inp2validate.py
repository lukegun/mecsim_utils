# This is a generic script
# that loads in an INP and generates
#  a .txt woth the information required to generate a
# data struction used to generate a inp file


import numpy as np

from mecsim_utils.transformations.inp.datamodel import INP_DataModel
import mecsim_utils.processing.utils as mecUtils

# this imports the FTACV stuff
import mecsim_utils.processing.auto_ftacv as ftcount
import mecsim_utils.processing.window_func as ft_wind

import matplotlib.pyplot as plt

test_case = 2
inp_loc = "tests/testingconfig"
exp_inp = (
    f"{inp_loc}/done/Master_EE_OX.inp",
    f"{inp_loc}/MasterE_2AC.inp",
    f"{inp_loc}/MasterE_3AC.inp",
)


# dummy AC case
def main(test_case=0):
    print(f"RUNNING: {exp_inp[test_case]}")
    Mec_parser = INP_DataModel(exp_inp[test_case], to_struct=True)
    MECsimstruct = (
        Mec_parser.transform()
    )  # I can modify this to shift between DC and FTACV

    """I SHOULD PUT SOMETHING HERE TO MORE CLEANLY WRAP THE mecsim instance and the transformation"""
    Currenttot = mecUtils.mecsim_current(MECsimstruct)

    # TODO RENAME
    Ftacv_Class = ftcount.FTACV_experiment(MECsimstruct, threshold=1.15)
    harmonics = Ftacv_Class(Currenttot)

    # TO DO SET UP A FUNCTION TO DO WINDOWING AND HARMONIC EXTRACTION
    # TODO add a function to write this function
    # harmonics_BU = deepcopy(harmonics)
    # func = ft_wind.harmonics_generate(window_func="guassian", envelope=False)
    # harmonics = func(Currenttot, MECsimstruct, harmonics)
    func = ft_wind.harmonics_generate(
        window_func="guassian", envelope=True, flatten_percent=0.025
    )
    harmonics2 = func(Currenttot, MECsimstruct, harmonics)
    # time.sleep(10)
    t = np.linspace(
        0, MECsimstruct.time_tot, num=int(harmonics[0]["0"].harmonic.shape[0])
    )

    harm_dic = {}
    i = 0
    for keys_p, harms2 in harmonics2.items():
        harm_dic.update({keys_p: {}})
        for keys_c, harms in harms2.items():
            i += 1
            npp = max(harms.harmonic)
            itemindex = np.argwhere(harms.harmonic == npp)

            val = (float(npp), int(itemindex[0][0]))
            harm_dic[keys_p].update({keys_c: val})
            plt.figure()
            plt.plot(t, harms.harmonic)
            plt.title(f"{harms.freq}")
            plt.savefig(f"pics/{keys_p}_{keys_c}_harm.png")
            plt.close()

    print(harm_dic)
    # generate an amount of validation features
    print("Nharm: ", i)
    print("shape current: ", Currenttot.shape[0])
    print("mean current: ", np.average(Currenttot))

    print(Mec_parser.datanum)

    # print a information into a txtfile that somarises the value in datastruct format


if __name__ == "__main__":
    main(test_case=test_case)
