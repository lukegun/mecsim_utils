"""
These functions set the sample input features to be used in the testsing
"""

import pytest

# load in the sample testing stuff
import mecsim_utils.mecsim_examples as mec_examples  # fixtures
from mecsim_utils.transformations.inp.datamodel import INP_DataModel
import mecsim_utils.processing.utils as mecUtils


# this packs a list of pointers to that we can load it in
def generate_mecsamples(data_cls_list):

    pytest_list = []
    for data_cls in data_cls_list:
        data = data_cls
        pytest_list.append(pytest.param(data, id=data.id))

    return pytest_list


## TODO make this so that we can query subsets of the examples (WRapper fixtures???)


# this parameterises over all the experimental input files
@pytest.fixture(
    # TODO MOVE TO FIXTURE AS RETURNED CALL FUNCTION
    params=generate_mecsamples(mec_examples.get_AC_cases()),
    scope="module",
    autouse=True,
)
def inp_factory(request):

    # unpack the parameters here
    mecsim_data = request.param()

    yield mecsim_data


# this parameterises over the mecsim simulations
@pytest.fixture(scope="module", autouse=True)
def current_factory(inp_factory):

    # generate the current and split it with validation data
    Mec_parser = INP_DataModel(inp_factory.inp_file, to_struct=True)
    MECsimstruct = (
        Mec_parser.transform()
    )  # I can modify this to shift between DC and FTACV

    # Run a single mecsim instance
    Currenttot = mecUtils.mecsim_current(
        MECsimstruct,
    )

    yield Currenttot, MECsimstruct, inp_factory
