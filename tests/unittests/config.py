"""
    These functions set the sample input features to be used in the testsing
"""
import pytest

@pytest.fixture(params=["tests/testingconfig/Master.inp",
                        "tests/testingconfig/MasterE.inp",
                        "tests/testingconfig/Master_EE_OX.inp"],
                 ids=["E_ox", "E_red", "EE_ox"])
def inp_factory(request):
    return request.param