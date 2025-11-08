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


import polars as pl


class dummy_exp_ftacv:


    def __init__(self):

        self.AC = [{"f":2.700835e+01}]  
        self.time_tot =      2.684352e+01 

        return

# dummy AC case
def main():

    test_case = 0
    exp_inp = (
        "test_au.txt",
    )

    df = pl.read_csv(source=exp_inp[test_case], skip_rows=19,
                      separator='\t',new_columns=["v","i","t"], has_header=False)
    Currenttot =  df['i'].to_numpy()

    frequency_curr, frequency_space = ftcount.frequency_transform(
        Currenttot, df['t'][-1]
    )
    MECsimstruct = dummy_exp_ftacv()

    # TODO RENAME
    Ftacv_Class = ftcount.FTACV_experiment(MECsimstruct, threshold=1.15)
    harmonics = Ftacv_Class(Currenttot)

    # TO DO SET UP A FUNCTION TO DO WINDOWING AND HARMONIC EXTRACTION
    # TODO add a function to write this function
    #harmonics_BU = deepcopy(harmonics)
    #func = ft_wind.harmonics_generate(window_func="guassian", envelope=False)
    #harmonics = func(Currenttot, MECsimstruct, harmonics)
    t1 = time.time()
    func = ft_wind.harmonics_generate(
        window_func="guassian", envelope=True, flatten_percent=0.01
    )
    harmonics2 = func(Currenttot, MECsimstruct, harmonics)
    print(time.time()-t1)
    time.sleep(10)
    t = np.linspace(
        0, MECsimstruct.time_tot, num=int(harmonics[0]["0"].harmonic.shape[0])
    )

    for keys_p, harms2 in harmonics2.items():
        for keys_c, harms in harms2.items():
            npp =  max(harms.harmonic)
            print(f"{keys_p}_{keys_c}",npp)
            plt.figure()
            plt.plot(t, harms.harmonic)
            plt.savefig(f"pics/{keys_p}_{keys_c}_harm.png")
            plt.close()

            if np.isnan(npp):
                print(harms)


if __name__ == "__main__":
    main()
