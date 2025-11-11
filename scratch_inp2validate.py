# This is a generic script 
# that loads in an INP and generates
#  a .txt woth the information required to generate a 
# data struction used to generate a inp file


import numpy as np
import time

from mecsim_utils.transformations.inp.datamodel import INP_DataModel
import mecsim_utils.processing.utils as mecUtils

# this imports the FTACV stuff
import mecsim_utils.processing.auto_ftacv as ftcount
import mecsim_utils.processing.window_func as ft_wind

import matplotlib.pyplot as plt

exp_inp = (
        "tests/testingconfig/MasterE.inp",
        "tests/testingconfig/Master.inp",
        "tests/testingconfig/POM_Example.inp",
        "tests/testingconfig/Master_EE_OX.inp",
        "tests/testingconfig/MasterE_2AC.inp",
        "tests/testingconfig/MasterE_3AC.inp",
    )

# dummy AC case
def main(test_case = 0):


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
    t1 = time.time()
    func = ft_wind.harmonics_generate(
        window_func="guassian", envelope=True, flatten_percent=0.025
    )
    harmonics2 = func(Currenttot, MECsimstruct, harmonics)
    print(time.time() - t1)
    #time.sleep(10)
    t = np.linspace(
        0, MECsimstruct.time_tot, num=int(harmonics[0]["0"].harmonic.shape[0])
    )

    harm_dic = {    }
    i = 0 
    for keys_p, harms2 in harmonics2.items():
        print(keys_p, type(keys_p))
        harm_dic.update({keys_p:{}})
        for keys_c, harms in harms2.items():
            i += 1
            print(keys_c, type(keys_c))
            npp = max(harms.harmonic)
            itemindex = np.argwhere(harms.harmonic == npp)

            val = (float(npp), int(itemindex[0][0]))
            harm_dic[keys_p].update({keys_c:val})
            

    print(harm_dic)
    # generate an amount of validation features
    print("Nharm: ", i)
    print("shape current: ",Currenttot.shape[0])
    print("mean current: ",np.average(Currenttot))


    print(Mec_parser.datanum)

    # print a information into a txtfile that somarises the value in datastruct format 


if __name__ == "__main__":
    main(test_case=1)
