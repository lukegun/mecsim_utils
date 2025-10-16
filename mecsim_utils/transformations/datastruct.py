"""
This is a custom data structure
to store information and ease transformation
between MECSim related tools.
"""

from dataclasses import dataclass


# TODO FIGURE OUT THE INHERATANCE PROBLEM
@dataclass
class Base_MEC:
    """Class for keeping track of MECSim related information,
    Plus additional metadata."""

    # key features important to MECSim
    temp: float  # temperature of solution
    ru: float  # this is the
    estart: float  # starting potential
    eend: float  # end potential for the voltammmogram
    Ncyc: int  # number of cycles of voltammogram
    v: float  # scanrate
    area: float  # electrode surface area
    time_tot: float  # overall runtime for the simulation

    # Misc other items
    # MISC: dict

    # multivalue things TODO MAKE this validated
    conc: list  # stores the dics of conc {c: concentration, d: diffusion }
    kinetic: list  # stores the dics of reaction stuff
    # {type: int , react: list, kf: float, kb: float, E0, ksreal, alpha}
    AC: list  # [{a: mV, f: hertz}]
    cap: list  # store double layer cap F/cm^2
    erev: list  # store complex steps

    # complex mecsim settings
    adv_estr: float
    adv_eend: float
    n_fixed: int  # fixed number of timestep
    nsph: float  # number of spheres
    radsph: float
    ncycl: float  # number of cylinders
    radcyl: float  # radius of cylinderBase_MEC(
    radlen: float  # length of cylinder

    # rotating disk electrode stuff
    rder: float  # rde radius (cm)
    rders: float  # rotating disk electrode speed (rad/s)
    rdekv: float  # kinematic viscosity

    # nondefault stuff
    # mechanism specific
    et_mech: bool = False  # butlervolmer or marcus hushpre_eq": 10,  # Pre-equilibrium switch: 0=stay with use
    pre_eq: bool = False  # if or not to apply pre-equilbrum
    nerev: int = 1  # number of Erev lines
    adv_v: int = 0  # use advanced voltage ramp (0 = E_start=E_end, 1 = use advanced ramp below, 2=From file 'EInput.txt')
    nac: int = 0  # number of AC sources
    nsol: int = 2  # number of analyts in solution
    ncap: int = 1  # number of capitance
    np: int = 17  # number of points in current # TODO fix multiples of two

    # MECSIMSETTING
    Epzc: float = 0.0  # potentail offset
    geotype: int = 1  # Geometry type (1=planar, 2=spherical, 3=cylinder, 4=RDE)

    # TODO FIGURE OUT HOW TO FIX THIS
    # mecsim parameters (set to some standard value)
    # add to generated function optional
    beta: float = 0.1  # simulation beta
    dstar: float = 10.0  # dstar min
    v_st: float = 0.005  # max voltage step
    t_res: float = 25.6  # time resolution
    s_tm: bool = False  # fixed number of timesteps
    spares: float = 100.0  # Spacial Resolution (>20)
    debug: int = 0  # print debug output
    digifft: bool = False  # correct vscan and freq for digipot
    digi: bool = False  # output voltage compadable

    # def __init__(self, source):
    #    self.source = source
