# This stores a bunch of Example of mecsim data with some validated example cases
from dataclasses import dataclass, field
from .example_utils import FTACV_base_setup


# validation of the MECSIM validation
@dataclass
class example_ftacvEsurf_red(FTACV_base_setup):

    # TODO figure out how to make this dynamic mainly so we can duplicate this over the MECSIM unit tests
    inp_file: list[str] = field(
        default_factory=lambda: [
            "294.75",
            "50",
            "0.6",
            "-0.6",
            "1",
            "0.1e0",
            "15",
            "0",
            "1",
            "1",
            "1",
            "0",
            "4000",
            "0.10",
            "10.0",
            "0.005e0",
            "25.6e0",
            "0",
            "0",
            "2",
            "0.0",
            "0.0",
            "0.50",
            "-0.50",
            "1",
            "0.07854",
            "1.0e0",
            "1.0e-4",
            "0.50e0",
            "0.001e0",
            "0.10e0",
            "100.0",
            "1.0e-1",
            "1.0e2",
            "1.0e-5",
            "1",
            "80.0e0, 27.5e0",
            "2",
            "1.0e-11, 5.8e-06, 1",
            "0.0e0, 5.8e-06, 1",
            "4",
            "0",
            "0.0e0",
            "0.0e0",
            "0.0e0",
            "0.0e0",
            "0.0e0",
            "0,-1,1,0, 0, 0, 10000, 5.0e-01",
        ]
    )
    testing_use: str = "This covers a generic E reduction case with no resistance"
    AC_case: bool = True
    id: str = "red__Esurf."
    ft_threshold: float = 1.15
    flattern_percentage: float = 0.025

    # how to fix this
    harmdic: dict = field(
        default_factory=lambda: {
            0: {"0": (4.81441653084991e-08, 12129)},
            1: {
                "1": (6.756981432170081e-06, 12295),
                "2": (3.501171513905732e-06, 11913),
                "3": (2.599879348443764e-06, 12274),
                "4": (1.2391530712642165e-06, 12517),
                "5": (7.206222108635483e-07, 4099),
                "6": (3.301678739726468e-07, 12119),
            },
        }
    )
    N_harms: int = 7
    shape: int = 32768
    average: float = -4.2822574011180496e-11


# validation of the MECSIM validation
@dataclass
class example_ftacvEsurf_ox(FTACV_base_setup):

    # TODO figure out how to make this dynamic mainly so we can duplicate this over the MECSIM unit tests
    inp_file: list[str] = field(
        default_factory=lambda: [
            "294.75",
            "500",
            "-0.6",
            "0.6",
            "1",
            "0.1e0",
            "16",
            "0",
            "1",
            "1",
            "1",
            "0",
            "4000",
            "0.10",
            "10.0",
            "0.005e0",
            "25.6e0",
            "0",
            "0",
            "2",
            "0.0",
            "0.0",
            "0.50",
            "-0.50",
            "1",
            "0.07854",
            "1.0e0",
            "1.0e-4",
            "0.50e0",
            "0.001e0",
            "0.10e0",
            "100.0",
            "1.0e-1",
            "1.0e2",
            "1.0e-5",
            "1",
            "80.0e0, 9.0e0",
            "2",
            "6.35e-12, 0, 1",
            "0.0e0, 0, 1",
            "4",
            "0",
            "1.0e-6",
            "0.0e0",
            "0.0e0",
            "0.0e0",
            "0.0e0",
            "0,1,-1, 0, 0, 0.0, 5.1, 5.0e-01",
        ]
    )
    testing_use: str = (
        "This covers a generic E reduction with a quasi-reversible C case"
        " with minimal resistance"
    )
    AC_case: bool = True
    id: str = "ox__Esurf."
    ft_threshold: float = 1.15
    flattern_percentage: float = 0.025

    # how to fix this
    harmdic: dict = field(
        default_factory=lambda: {
            0: {"0": (4.897768883350734e-08, 2078)},
            1: {
                "1": (6.403063123220705e-07, 6165),
                "2": (5.3030456610823694e-08, 2279),
                "3": (3.4952955776590806e-08, 6163),
                "4": (4.72710466506189e-09, 2264),
                "5": (1.1333243997485817e-09, 6166),
            },
        }
    )
    N_harms: int = 6
    shape: int = 65536
    average: float = -1.1634316921515934e-15


# validation of the MECSIM validation
@dataclass
class example_ftacvEEsurf_red(FTACV_base_setup):

    # TODO figure out how to make this dynamic mainly so we can duplicate this over the MECSIM unit tests
    inp_file: list[str] = field(
        default_factory=lambda: [
            "294.75",
            "50",
            "0.6",
            "-0.6",
            "1",
            "0.1e0",
            "18",
            "0",
            "1",
            "1",
            "1",
            "0",
            "4000",
            "0.10",
            "10.0",
            "0.005e0",
            "25.6e0",
            "0",
            "0",
            "2",
            "0.0",
            "0.0",
            "0.50",
            "-0.50",
            "1",
            "0.07854",
            "1.0e0",
            "1.0e-4",
            "0.50e0",
            "0.001e0",
            "0.10e0",
            "100.0",
            "1.0e-1",
            "1.0e2",
            "1.0e-5",
            "1",
            "80.0e0, 9.0e0",
            "3",
            "1.145e-14, 0, 1",
            "0.0e0, 0, 1",
            "0.0e0, 0, 1",
            "4",
            "0",
            "0.0e0",
            "0.0e0",
            "0.0e0",
            "0.0e0",
            "0.0e0",
            "0,-1, 1, 0, 0, 0, 0.08, 10000, 5.0e-01",
            "0, 0,-1, 1, 0, 0,-0.08, 10000, 5.0e-01",
        ]
    )
    testing_use: str = "This covers a generic E oxidation case with no resistance"
    AC_case: bool = True
    id: str = "red__Esurf_Esurf."
    ft_threshold: float = 1.15
    flattern_percentage: float = 0.025

    # how to fix this
    harmdic: dict = field(
        default_factory=lambda: {
            0: {"0": (6.360628878509033e-11, 6144)},
            1: {
                "1": (2.6204603045990307e-09, 2297),
                "2": (1.3060966943357625e-09, 6602),
                "3": (9.186925565216192e-10, 6423),
                "4": (5.342203168691838e-10, 5992),
                "5": (2.816577284973439e-10, 6416),
                "6": (1.224782028923181e-10, 6499),
                "7": (6.492598732825306e-11, 2321),
            },
        }
    )
    N_harms: int = 8
    shape: int = 262144
    average: float = 7.770695697323994e-16


# validation of the MECSIM validation
@dataclass
class example_ftacvEEsurf_ox(FTACV_base_setup):

    # TODO figure out how to make this dynamic mainly so we can duplicate this over the MECSIM unit tests
    inp_file: list[str] = field(
        default_factory=lambda: [
            "294.75",
            "500",
            "-0.6",
            "0.6",
            "1",
            "0.1e0",
            "16",
            "0",
            "1",
            "1",
            "1",
            "0",
            "4000",
            "0.10",
            "10.0",
            "0.005e0",
            "25.6e0",
            "0",
            "0",
            "2",
            "0.0",
            "0.0",
            "0.50",
            "-0.50",
            "1",
            "0.07854",
            "1.0e0",
            "1.0e-4",
            "0.50e0",
            "0.001e0",
            "0.10e0",
            "100.0",
            "1.0e-1",
            "1.0e2",
            "1.0e-5",
            "1",
            "80.0e0, 9.0e0",
            "3",
            "6.35e-12, 0, 1",
            "0.0e0, 0, 1",
            "0.0e0, 0, 1",
            "4",
            "0",
            "1.0e-6",
            "0.0e0",
            "0.0e0",
            "0.0e0",
            "0.0e0",
            "0, 1,-1, 0, 0, 0,-0.2, 5.1, 5.0e-01",
            "0, 0, 1,-1, 0, 0, 0.2, 5.1, 5.0e-01",
        ]
    )
    testing_use: str = "This covers a generic E oxidation case with no resistance"
    AC_case: bool = True
    id: str = "ox__Esurf_Esurf."
    ft_threshold: float = 1.15
    flattern_percentage: float = 0.025

    # how to fix this
    harmdic: dict = field(
        default_factory=lambda: {
            0: {"0": (4.899183806055666e-08, 1395)},
            1: {
                "1": (6.403024431934329e-07, 5483),
                "2": (5.3054602866698736e-08, 5692),
                "3": (3.495559792180389e-08, 1384),
                "4": (4.727503639134046e-09, 2946),
                "5": (1.1379405288468542e-09, 1384),
            },
        }
    )
    N_harms: int = 6
    shape: int = 65536
    average: float = -2.5449073965024033e-13


# Currently not supported (i think)
# # validation of the MECSIM validation
# @dataclass
# class example_ftacvEsurfC_ox(FTACV_base_setup):

#     # TODO figure out how to make this dynamic mainly so we can duplicate this over the MECSIM unit tests
#     inp_file: list[str] = field(
#         default_factory=lambda: []
#     )
#     testing_use: str = "This covers a generic E oxidation case with no resistance"
#     AC_case: bool = True
#     id: str = "ox__Esurf_C."
#     ft_threshold: float = 1.15
#     flattern_percentage: float = 0.025

#     # how to fix this
#     harmdic: dict = field(
#         default_factory=lambda: {}
#     )
#     N_harms: int = 7
#     shape: int = 131072
#     average: float = -3.7886402665599184e-05


# # validation of the MECSIM validation
# @dataclass
# class example_ftacvEsurfC_red(FTACV_base_setup):

#     # TODO figure out how to make this dynamic mainly so we can duplicate this over the MECSIM unit tests
#     inp_file: list[str] = field(
#         default_factory=lambda: []
#     )
#     testing_use: str = "This covers a generic E oxidation case with no resistance"
#     AC_case: bool = True
#     id: str = "ox__Esurf_C."
#     ft_threshold: float = 1.15
#     flattern_percentage: float = 0.025

#     # how to fix this
#     harmdic: dict = field(
#         default_factory=lambda: {}
#     )
#     N_harms: int = 7
#     shape: int = 131072
#     average: float = -3.7886402665599184e-05
