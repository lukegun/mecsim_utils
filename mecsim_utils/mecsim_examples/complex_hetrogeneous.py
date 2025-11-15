# This stores a bunch of random non-standard examples of FTACV reaction mechanisms

from dataclasses import dataclass, field
from .example_utils import FTACV_base_setup


# validation of the MECSIM validation
@dataclass
class example_ftacvECE_ox(FTACV_base_setup):

    # TODO figure out how to make this dynamic mainly so we can duplicate this over the MECSIM unit tests
    inp_file: list[str] = field(
        default_factory=lambda: [
            "298.2",
            "0.0e0",
            "0.50",
            "-0.50",
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
            "1.0e0",
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
            "1.0e-6, 1.0e-5, 0",
            "0.0e0, 1.0e-5, 0",
            "4",
            "0.0e0",
            "0.0e0",
            "0.0e0",
            "0.0e0",
            "0.0e0",
            "0.0e0",
            "0, -1, 1, 1.0e0, 1.0e0, 0.150e0, 1.0e4, 0.50e0",
        ]
    )
    testing_use: str = "This covers a generic E oxidation case with no resistance"
    AC_case: bool = True
    id: str = "E_red"
    ft_threshold: float = 1.15
    flattern_percentage: float = 0.025

    # how to fix this
    harmdic: dict = field(
        default_factory=lambda: {
            0: {"0": (0.00015899128901162587, 7072)},
            1: {
                "1": (0.0011777003301974701, 1434),
                "2": (0.00041642389754321414, 6531),
                "3": (0.00024505514221551355, 1434),
                "4": (0.00010381545941930582, 1296),
                "5": (5.499996607924297e-05, 1434),
                "6": (2.2164214744488786e-05, 1334),
            },
        }
    )
    N_harms: int = 7
    shape: int = 131072
    average: float = -3.7886402665599184e-05


# validation of the MECSIM validation
@dataclass
class example_ftacvECE_red(FTACV_base_setup):

    # TODO figure out how to make this dynamic mainly so we can duplicate this over the MECSIM unit tests
    inp_file: list[str] = field(
        default_factory=lambda: [
            "298.2",
            "0.0e0",
            "0.50",
            "-0.50",
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
            "1.0e0",
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
            "1.0e-6, 1.0e-5, 0",
            "0.0e0, 1.0e-5, 0",
            "4",
            "0.0e0",
            "0.0e0",
            "0.0e0",
            "0.0e0",
            "0.0e0",
            "0.0e0",
            "0, -1, 1, 1.0e0, 1.0e0, 0.150e0, 1.0e4, 0.50e0",
        ]
    )
    testing_use: str = "This covers a generic E oxidation case with no resistance"
    AC_case: bool = True
    id: str = "E_red"
    ft_threshold: float = 1.15
    flattern_percentage: float = 0.025

    # how to fix this
    harmdic: dict = field(
        default_factory=lambda: {
            0: {"0": (0.00015899128901162587, 7072)},
            1: {
                "1": (0.0011777003301974701, 1434),
                "2": (0.00041642389754321414, 6531),
                "3": (0.00024505514221551355, 1434),
                "4": (0.00010381545941930582, 1296),
                "5": (5.499996607924297e-05, 1434),
                "6": (2.2164214744488786e-05, 1334),
            },
        }
    )
    N_harms: int = 7
    shape: int = 131072
    average: float = -3.7886402665599184e-05
