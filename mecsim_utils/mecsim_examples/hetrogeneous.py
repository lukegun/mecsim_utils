# This stores a bunch of Example of mecsim data with some validated example cases


from dataclasses import dataclass, field
from .example_utils import FTACV_base_setup


#############################################################################################
####################################### DC INP SAMPLES ###################################
#############################################################################################


# E, EC, EE / ox & red


# will also need to test non-linear capacitance and resistance effects


#############################################################################################
####################################### FTACV INP SAMPLES ###################################
#############################################################################################


# These following data structures stores key information used in the
# validation of the MECSIM validation
@dataclass
class example_ftacvE_ox(FTACV_base_setup):

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
    testing_use: str = "This covers a generic E oxidation case with minor resistance"
    AC_case: bool = True
    id: str = "ox__E."
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
class example_ftacvE_red(FTACV_base_setup):

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
    testing_use: str = "This covers a generic E reduction case with no resistance"
    AC_case: bool = True
    id: str = "red__E."
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
class example_ftacvEE_ox(FTACV_base_setup):

    # TODO figure out how to make this dynamic mainly so we can duplicate this over the MECSIM unit tests
    inp_file: list[str] = field(
        default_factory=lambda: [
            "294.75",
            "500",
            "-1.2",
            "1.2",
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
            "80.0e0, 27.5e0",
            "3",
            "1.0e-6, 5.8e-06, 0",
            "0.0e0, 5.8e-06, 0",
            "0.0e0, 5.8e-06, 0",
            "4",
            "0",
            "0.0e0",
            "0.0e0",
            "0.0e0",
            "0.0e0",
            "0.0e0",
            "0,1,-1, 0,0, 0, -0.4, 0.01, 5.0e-01",
            "0,0,1, -1,0, 0, 0.4, 0.01, 5.0e-01",
        ]
    )
    testing_use: str = (
        "This covers a generic EE oxidation case with somewhat high resistance and a quasireversible electrode kinetics"
    )
    AC_case: bool = True
    id: str = "ox__E-E."
    ft_threshold: float = 1.15
    flattern_percentage: float = 0.025

    # how to fix this
    harmdic: dict = field(
        default_factory=lambda: {
            0: {"0": (1.7042347498468427e-05, 11282)},
            1: {
                "1": (5.214691615952667e-05, 5535),
                "2": (7.716096952996453e-06, 5010),
                "3": (1.1198515151328813e-06, 10897),
                "4": (2.9768960277541515e-07, 4952),
                "5": (7.854250422158492e-08, 4746),
            },
        }
    )
    N_harms: int = 6
    shape: int = 262144
    average: float = 2.214786841623382e-06


# validation of the MECSIM validation
@dataclass
class example_ftacvEE_red(FTACV_base_setup):

    # TODO figure out how to make this dynamic mainly so we can duplicate this over the MECSIM unit tests
    inp_file: list[str] = field(
        default_factory=lambda: [
            "294.75",
            "50",
            "1.2",
            "-1.2",
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
            "80.0e0, 27.5e0",
            "3",
            "1.0e-6, 5.8e-06, 0",
            "0.0e0, 5.8e-06, 0",
            "0.0e0, 5.8e-06, 0",
            "4",
            "0",
            "0.0e0",
            "0.0e0",
            "0.0e0",
            "0.0e0",
            "0.0e0",
            "0,-1,1, 0,0, 0, 0.4, 0.01, 7.0e-01",
            "0,0,-1, 1,0, 0, -0.4, 0.01, 7.0e-01",
        ]
    )
    testing_use: str = (
        "This covers a generic EE reduction case with minimal resistance, quasireversible and mild asymetry of electrod kinetics"
    )
    AC_case: bool = True
    id: str = "red__E-E."
    ft_threshold: float = 1.15
    flattern_percentage: float = 0.025

    # how to fix this
    harmdic: dict = field(
        default_factory=lambda: {
            0: {"0": (1.2669945344821087e-05, 27663)},
            1: {
                "1": (7.059248958627867e-05, 10962),
                "2": (1.3168849554644293e-05, 10559),
                "3": (4.119084366382263e-06, 10955),
                "4": (8.38054608206708e-07, 5178),
                "5": (2.385874236938491e-07, 5489),
                "6": (5.205952386445564e-08, 11225),
            },
        }
    )
    N_harms: int = 7
    shape: int = 262144
    average: float = -2.214148116605755e-06


# validation of the MECSIM validation
@dataclass
class example_ftacvEC1_ox(FTACV_base_setup):

    # TODO figure out how to make this dynamic mainly so we can duplicate this over the MECSIM unit tests
    inp_file: list[str] = field(
        default_factory=lambda: [
            "294.75",
            "50",
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
            "1.0e-6, 5.8e-06, 0",
            "0.0e0, 5.8e-06, 0",
            "0.0e0, 5.8e-06, 0",
            "4",
            "0",
            "0.0e0",
            "0.0e0",
            "0.0e0",
            "0.0e0",
            "0.0e0",
            "0,1,-1, 0,0, 0, 0, 0.001, 5.0e-01",
            "1,0,-1, 1, 0.6, 0, 0.4, 0.01, 5.0e-01",
        ]
    )
    testing_use: str = (
        "This covers a generic EC 1st order oxidation case,"
        " with minimal resistance, c reaction is completely irrevesible"
    )
    AC_case: bool = True
    id: str = "ox__E-C1."
    ft_threshold: float = 1.15
    flattern_percentage: float = 0.025

    # how to fix this
    harmdic: dict = field(
        default_factory=lambda: {
            0: {"0": (1.1976260911828836e-05, 2363)},
            1: {
                "1": (1.5048392573264529e-05, 2217),
                "2": (2.428896151274058e-06, 2150),
                "3": (5.995598871411927e-07, 2094),
                "4": (1.265019769221734e-07, 2337),
                "5": (1.9088344864207386e-08, 2207),
                "6": (3.77414616288976e-09, 2493),
            },
        },
    )
    N_harms: int = 7
    shape: int = 65536
    average: float = 2.764084200340602e-06


# validation of the MECSIM validation
@dataclass
class example_ftacvEC1_red(FTACV_base_setup):

    # TODO figure out how to make this dynamic mainly so we can duplicate this over the MECSIM unit tests
    inp_file: list[str] = field(
        default_factory=lambda: [
            "294.75",
            "50",
            "0.6",
            "-0.6",
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
            "80.0e0, 27.5e0",
            "3",
            "1.0e-6, 3.8e-06, 0",
            "0.0e0, 3.8e-06, 0",
            "0.0e0, 3.8e-06, 0",
            "4",
            "0",
            "0.0e0",
            "0.0e0",
            "0.0e0",
            "0.0e0",
            "0.0e0",
            "0,-1,1, 0,0, 0, 0.0, 100, 7.0e-01",
            "1,0,-1, 1,100, 10, 0.0, 0.01, 5.0e-01",
        ]
    )
    testing_use: str = (
        "This covers a generic E reduction with a quasi-reversible "
        "1st order C case with minimal resistance"
    )
    AC_case: bool = True
    id: str = "red__E-C1."
    ft_threshold: float = 1.15
    flattern_percentage: float = 0.025

    # how to fix this
    harmdic: dict = field(
        default_factory=lambda: {
            0: {"0": (5.229788092183023e-06, 13294)},
            1: {
                "1": (3.670193610452491e-05, 3779),
                "2": (1.8952890260054967e-05, 3615),
                "3": (6.335448064859937e-06, 4049),
                "4": (3.2926002907544023e-06, 3815),
                "5": (1.283048009940734e-06, 4083),
                "6": (5.679330346064959e-07, 3917),
            },
        }
    )
    N_harms: int = 7
    shape: int = 65536
    average: float = -1.6993358213567514e-06


#### TODO ADD EC2 CASE
# validation of the MECSIM validation
@dataclass
class example_ftacvEC2_ox(FTACV_base_setup):

    # TODO figure out how to make this dynamic mainly so we can duplicate this over the MECSIM unit tests
    inp_file: list[str] = field(
        default_factory=lambda: [
            "294.75",
            "50",
            "-0.6",
            "0.6",
            "1",
            "0.1e0",
            "17",
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
            "4",
            "1.0e-6, 5.8e-06, 0",
            "0.0e0, 5.8e-06, 0",
            "1.0e-3, 5.8e-06, 0",
            "0.0e0, 5.8e-06, 0",
            "4",
            "0",
            "0.0e0",
            "0.0e0",
            "0.0e0",
            "0.0e0",
            "0.0e0",
            "0,1,-1,0, 0,    0, 0, 0, 0.001, 5.0e-01",
            "2,0,-1,-1, 1, 1000, 1, 0.4, 0.01, 5.0e-01",
        ]
    )
    testing_use: str = (
        "This covers a generic EC 2st order oxidation case,"
        " with minimal resistance, 2nd order c reaction is quasi-revesible"
    )
    AC_case: bool = True
    id: str = "ox__E-C2."
    ft_threshold: float = 1.15
    flattern_percentage: float = 0.025

    # how to fix this
    harmdic: dict = field(
        default_factory=lambda: {
            0: {"0": (1.1961726550481314e-05, 2362)},
            1: {
                "1": (1.4935867232373266e-05, 2218),
                "2": (2.444795272148071e-06, 2150),
                "3": (5.935643595653127e-07, 2093),
                "4": (1.243856242524644e-07, 2336),
                "5": (1.9261841185169743e-08, 2217),
            },
        }
    )
    N_harms: int = 6
    shape: int = 131072
    average: float = 1.83458709108408e-06


# validation of the MECSIM validation
@dataclass
class example_ftacvEC2_red(FTACV_base_setup):

    # TODO figure out how to make this dynamic mainly so we can duplicate this over the MECSIM unit tests
    inp_file: list[str] = field(
        default_factory=lambda: [
            "294.75",
            "50",
            "0.6",
            "-0.6",
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
            "80.0e0, 27.5e0",
            "4",
            "1.0e-6, 5.8e-06, 0",
            "0.0e0, 5.8e-06, 0",
            "1.0e-3, 5.8e-06, 0",
            "0.0e0, 5.8e-06, 0",
            "4",
            "0",
            "0.0e0",
            "0.0e0",
            "0.0e0",
            "0.0e0",
            "0.0e0",
            "0,-1,1, 0,0, 0, 0.0, 100, 7.0e-01",
            "2,0,-1,-1, 1, 1000, 0, 0.4, 0.01, 5.0e-01",
        ]
    )
    testing_use: str = (
        "This covers a generic E reduction with a irreversible C 2nd order case"
        " with minimal resistance"
    )
    AC_case: bool = True
    id: str = "red__E-C2."
    ft_threshold: float = 1.15
    flattern_percentage: float = 0.025

    # how to fix this
    harmdic: dict = field(
        default_factory=lambda: {
            0: {"0": (2.5848444407217573e-07, 13066)},
            1: {
                "1": (0.00010661004167230727, 4036),
                "2": (3.9076671598651884e-05, 3733),
                "3": (2.0853860917473834e-05, 4095),
                "4": (8.008526634069053e-06, 3840),
                "5": (3.567058563632931e-06, 4093),
                "6": (1.3901140870495398e-06, 3896),
            },
        }
    )
    N_harms: int = 7
    shape: int = 65536
    average: float = -2.9302171746935723e-06
