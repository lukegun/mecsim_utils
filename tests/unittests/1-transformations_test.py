"""
These tests validate that the MEC data structures all work well
"""

import numpy as np

from mecsim_utils.transformations.inp.datamodel import INP_DataModel
import mecsim_utils.processing.utils as mecUtils

# load in the sample testing stuff
from tests.unittests.fixture_ftacv import inp_factory  # fixtures


def inp_split(string):
    return string.split("!")[0].strip("\t\n, ")


def example_input(testingfiles):
    # read in the inp file
    with open(testingfiles) as f:
        dummy_inp_E = f.readlines()

    return dummy_inp_E


def check_inp_line(input_INP, transformed_lines, comment, ni, n):
    for i in range(n):
        x = inp_split(input_INP[ni + i])
        y = inp_split(transformed_lines[ni + i])
        s = f" input {input_INP[ni + i]} and output {transformed_lines[ni + i]}"
        x, y = x.split(","), y.split(",")
        for j in range(max(len(x), len(y))):
            assert float(x[j]) == float(y[j]), comment + s


# check if the inp to data transformation works
def test_INP_2_data(inp_factory):
    # removed as test examples are list[str]
    input_INP = inp_factory.inp_file

    Mec_parser = INP_DataModel(input_INP, to_struct=True)
    MECsimstruct = Mec_parser.transform()

    Mec_parser2 = INP_DataModel(MECsimstruct, to_struct=False)
    MECsiminp = Mec_parser2.transform()

    # test the geniric header content
    transformed_lines = MECsiminp.split("\n")
    comment = (
        """ERROR: forward and backwards INP transformation generic form, error line"""
    )
    check_inp_line(input_INP, transformed_lines, comment, 0, len(input_INP))

    assert len(input_INP) == len(
        transformed_lines
    ), "ERROR: number of lines don't match"


# this checks if MECSIM works right
def test_INP_2_mecsim(inp_factory):
    Mec_parser = INP_DataModel(inp_factory.inp_file, to_struct=True)
    MECsimstruct = Mec_parser.transform()

    """I SHOULD PUT SOMETHING HERE TO MORE CLEANLY WRAP THE mecsim
        instance and the transformation"""
    Currenttot = mecUtils.mecsim_current(MECsimstruct)

    # just some basic checks for structure
    s = np.log2(Currenttot.shape[0])
    assert int(s) == s, "ERROR: mecsim current output not divisable by 2"

    message = "ERROR: mexim current has large proportion of 0"
    assert np.sum(Currenttot == 0) < 0.001 * Currenttot.shape[0], message

    assert not np.isnan(Currenttot).any(), "ERROR: current output countains a nan"

    return


# validate that the data structors converted match a specific data class PYDANTIC???
