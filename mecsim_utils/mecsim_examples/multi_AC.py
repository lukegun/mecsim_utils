# this stores a bunch of


# This stores a bunch of random

from dataclasses import dataclass, field
from .example_utils import FTACV_base_setup


# validation of the MECSIM validation
@dataclass
class example_ftacvE_2AC_red(FTACV_base_setup):

    # TODO figure out how to make this dynamic mainly so we can duplicate this over the MECSIM unit tests
    inp_file: list[str] = field(
        default_factory=lambda: [
            "294.75",
            "50",
            "-0.8",
            "0.0",
            "1",
            ".1e0",
            "17",
            "0",
            "1",
            "0",
            "0",
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
            "1.0e-6, 5.820569e-06, 0",
            "0.0e0, 5.820569e-06, 0",
            "4",
            "0.0e0",
            "4.0E-05",
            "0",
            "0",
            "0",
            "0",
            "0,1,-1, 0, 0, -0.4,8.201159e-01, 5.0e-01",
        ]
    )
    testing_use: str = "This covers a generic E reduction case with minor resistance"
    AC_case: bool = True
    id: str = "E_red"
    ft_threshold: float = 1.15
    flattern_percentage: float = 0.025

    # how to fix this
    harmdic: dict = field(
        default_factory=lambda: {
            0: {"0": (1.2688240416313286e-05, 1214)},
            1: {
                "1": (7.981697581166737e-05, 3073),
                "2": (2.398803376691606e-05, 3212),
                "3": (1.4083977067572565e-05, 3073),
                "4": (5.252455041944776e-06, 3160),
                "5": (2.551691294378777e-06, 1026),
                "6": (9.137862381124487e-07, 1091),
            },
        }
    )
    N_harms: int = 7
    shape: int = 131072
    average: float = 1.8966123268198947e-06


# validation of the MECSIM validation
@dataclass
class example_ftacvE_3AC_red(FTACV_base_setup):

    # TODO figure out how to make this dynamic mainly so we can duplicate this over the MECSIM unit tests
    inp_file: list[str] = field(
        default_factory=lambda: [
            "294.75",
            "50",
            "-0.8",
            "0.0",
            "1",
            ".1e0",
            "17",
            "0",
            "1",
            "0",
            "0",
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
            "1.0e-6, 5.820569e-06, 0",
            "0.0e0, 5.820569e-06, 0",
            "4",
            "0.0e0",
            "4.0E-05",
            "0",
            "0",
            "0",
            "0",
            "0,1,-1, 0, 0, -0.4,8.201159e-01, 5.0e-01",
        ]
    )
    testing_use: str = "This covers a generic E reduction case with minor resistance"
    AC_case: bool = True
    id: str = "E_red"
    ft_threshold: float = 1.15
    flattern_percentage: float = 0.025

    # how to fix this
    harmdic: dict = field(
        default_factory=lambda: {
            0: {"0": (1.2688240416313286e-05, 1214)},
            1: {
                "1": (7.981697581166737e-05, 3073),
                "2": (2.398803376691606e-05, 3212),
                "3": (1.4083977067572565e-05, 3073),
                "4": (5.252455041944776e-06, 3160),
                "5": (2.551691294378777e-06, 1026),
                "6": (9.137862381124487e-07, 1091),
            },
        }
    )
    N_harms: int = 7
    shape: int = 131072
    average: float = 1.8966123268198947e-06
