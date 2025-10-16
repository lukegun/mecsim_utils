"""
These are generic functions for running mecsim
"""

from mecsim_utils.MECSim.mec_get import mecs_get
from ..transformations.mecsim.datamodel import MECSIM_DataModel

# this gets mecsim fortran function
mecsim_fortran = mecs_get()


# this is a generic function for converting the datamodel struct into mecsim compadable stuff and running
def mecsim_current(structmodel):
    # convert data into a dictionary from dataframe
    mecsimclass = MECSIM_DataModel(structmodel)
    (
        MECSettings,
        Numberin,
        Reacpara,
        reacMech,
        Capaci,
        Diffvalues,
        ACSignal,
        EModown,
        Currenttot,
        Ecustom,
        Tcustom,
        Error_Code,
    ) = mecsimclass.transform()

    # Run the MECSIM function
    mecsim_fortran(
        MECSettings,
        Numberin,
        Reacpara,
        reacMech,
        Capaci,
        Diffvalues,
        ACSignal,
        EModown,
        Ecustom,
        Tcustom,
        Currenttot,
        Error_Code,
    )
    Currenttot = Currenttot[
        0 : int(Numberin[0]),
    ]  # truncates the static varibles of Fortran77

    return Currenttot


# generic function for calculating harmonics
# how will this work for secondary harmonics and weights WHAT FUNCTIONALITY DO WE NEED
def primaryharmoniccalc(
    Currenttot, ACfreq, bandwidtharray, std=0.1, windowfunc=True, HilbertTran=True
):
    """
    IF STD SET TO 0 just no guassian?
    """

    # calculate the windowing function
    if windowfunc:
        pass
    else:  # calculate the window guassian function
        pass

    # do fft

    # do hilbert transform hack

    # apply window functions to n number harmonics

    # apply inverse fft n times

    return


"""JUST SET UP A SECONDARY FUNCTION FOR SECONDARY HARMONICS"""


# TODO
def secondaryharmoniccalc(
    Currenttot, bandwidtharray, std=0.1, windowfunc=True, HilbertTran=True
):
    """
    IF STD SET TO 0 just no guassian?
    """

    # calculate the windowing function
    if windowfunc:
        pass
    else:  # calculate the window guassian function
        pass

    # do fft

    # do hilbert transform hack

    # apply window functions to n number harmonics

    # apply inverse fft n times

    return
