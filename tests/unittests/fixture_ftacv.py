"""
These functions set the sample input features to be used in the testsing
"""

import pytest

# load in the sample testing stuff
import tests.unittests.mecsim_examples as mec_examples  # fixtures
from mecsim_utils.transformations.inp.datamodel import INP_DataModel
import mecsim_utils.processing.utils as mecUtils


# this parameterises over all the experimental input files
@pytest.fixture(
    params=[
        mec_examples.example_ftacvE_red,
        mec_examples.example_ftacvE_ox,
    ],
    # TODO add some way to save the information that can be validated
    ids=["E_ox", "E_red"],
    scope="module",
)
def inp_factory(request):

    # unpack the parameters here
    mecsim_data = request.param()

    return mecsim_data


# this parameterises over the mecsim simulations
@pytest.fixture(scope="module")
def current_factory(inp_factory):

    # generate the current and split it with validation data
    Mec_parser = INP_DataModel(inp_factory.inp_file, to_struct=True)
    MECsimstruct = (
        Mec_parser.transform()
    )  # I can modify this to shift between DC and FTACV

    """I SHOULD PUT SOMETHING HERE TO MORE CLEANLY WRAP THE
    mecsim instance and the transformation"""
    Currenttot = mecUtils.mecsim_current(
        MECsimstruct,
    )

    return Currenttot, MECsimstruct, inp_factory
