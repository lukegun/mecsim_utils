"""
    These functions set the sample input features to be used in the testsing
"""
import pytest

from mecsim_utils.transformations.inp.datamodel import INP_DataModel
import mecsim_utils.processing.utils as mecUtils

# this parameterises over all the experimental input files
@pytest.fixture(params=["tests/testingconfig/Master.inp",
                        "tests/testingconfig/MasterE.inp",
                        "tests/testingconfig/Master_EE_OX.inp"],
                 ids=["E_ox", "E_red", "EE_ox"])
def inp_factory(request):
    return request.param


# this parameterises over the mecsim simulations
@pytest.fixture
def current_factory(inp_factory):

    Mec_parser = INP_DataModel(inp_factory, to_struct=True)
    MECsimstruct = Mec_parser.transform()

    """I SHOULD PUT SOMETHING HERE TO MORE CLEANLY WRAP THE mecsim instance and the transformation"""
    Currenttot = mecUtils.mecsim_current(MECsimstruct)

    return Currenttot, MECsimstruct