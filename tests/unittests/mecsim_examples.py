# This stores a bunch of Example of mecsim data with some validated example cases


from dataclasses import dataclass, field

#############################################################################################
####################################### DC INP SAMPLES ###################################
#############################################################################################


# E, EC, EE / ox & red


#############################################################################################
####################################### FTACV INP SAMPLES ###################################
#############################################################################################


# this sets up the post_init_ to return the validation set up.
class validation_setup:

    # This is here in case we need to figure out any later information
    def __post_init__(self):

        return

    # this prints the explanation of what this use case is testing for
    def __repr__(self):
        f = "AC" if self.AC_case else "DC"
        return f"{f} case pytest ID {self.ID}: using reason {self.testing_use}"


# These following data structures stores key information used in the
# validation of the MECSIM validation
@dataclass
class example_ftacvE_red(validation_setup):

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
    ID: str = "E_red"
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
class example_ftacvE_ox(validation_setup):

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
    ID: str = "E_red"
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


# note done below


# validation of the MECSIM validation
@dataclass
class example_ftacvEE_ox(validation_setup):

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
    ID: str = "E_red"
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
class example_ftacvEE_red(validation_setup):

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
    ID: str = "E_red"
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
class example_ftacvEC_ox(validation_setup):

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
    ID: str = "E_red"
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
class example_ftacvEC_red(validation_setup):

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
    ID: str = "E_red"
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
class example_ftacvESurf_ox(validation_setup):

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
    ID: str = "E_red"
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
class example_ftacvEESurf_ox(validation_setup):

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
    ID: str = "E_red"
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
class example_ftacvECSurf_ox(validation_setup):

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
    ID: str = "E_red"
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
class example_ftacvESurf_red(validation_setup):

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
    ID: str = "E_red"
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
class example_ftacvEESurf_red(validation_setup):

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
    ID: str = "E_red"
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
class example_ftacvECSurf_red(validation_setup):

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
    ID: str = "E_red"
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
class example_ftacvECE_ox(validation_setup):

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
    ID: str = "E_red"
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
class example_ftacvECE_red(validation_setup):

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
    ID: str = "E_red"
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
class example_ftacvE_2AC_red(validation_setup):

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
    ID: str = "E_red"
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
class example_ftacvE_3AC_red(validation_setup):

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
    ID: str = "E_red"
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
