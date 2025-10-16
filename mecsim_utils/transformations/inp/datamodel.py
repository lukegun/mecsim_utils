"""
This is a class for trasnforming the input function into dic and viceversa
MAY NEED TO ADD SOMETHIGN ELSE IN TO TRANSFORM A
"""

from . import stuctural_func as inp_struct

# required to load in the dataclasss
from ..datastruct import Base_MEC
import dataclasses


# TODO SET THIS ALL UP TO HANDLE OTHER DATA THAT WOULD BE PASSED TO IT
class INP_DataModel:
    def __init__(self, input, to_struct=True):
        # this are needed for the backward pregression but less so other way
        self.input = input

        self.to_struct = to_struct

        # identifies if  we are converting to
        if isinstance(self.input, str):  # check to see
            self.loadinp = True  # might need to be moved out but fine enough
        elif isinstance(self.input, list):  # check to see
            self.loadinp = False
        elif dataclasses.is_dataclass(self.input) and not self.to_struct:
            self.to_struct = False
        else:
            raise Exception(
                "Error: incorrect file passed to inp <-> structer convertor"
            )

        return

    # this if the main runtime class
    def transform(self):
        if self.to_struct:
            output = self.mec_inp2dic()
        else:
            output = self.mec_dic2inp()

        return output

    # convert the dictionary structure to inp file
    def mec_inp2dic(self):
        # load in the inp file and and convert to our two lists
        if self.loadinp:
            self.load_inp(self.input)  # this assumes comments are removed
        else:
            self.datanum = self.input

        # get the initial key dataspaces
        self.data_finder_inp(self.datanum)

        # set up the datastructure used for the system
        self.listmapping()

        # set up the conversion from list to dic
        output = self.data2structure(self.datanum)

        return output

    # convert the dictionary structure to inp file
    def mec_dic2inp(self):
        # convert datastructures as
        self.input = dataclasses.asdict(self.input)

        # get the initial key dataspaces
        self.data_finder_struct(self.input)

        # set up the datastructure used for the system
        self.listmapping()

        # set up the conversion from list to dic
        output = self.structure2inp(self.input)

        return output

    # calculates a bunch of indices
    # this is here because of the spaces dic
    def listmapping(self):
        # set up as an aliasing yaml
        self.mapping_forward = {
            "temp": 0,  # Temperature (K)
            "ru": 1,  # uncompensated resistance (ohms)
            "estart": 2,  # E_start (V)
            "eend": 3,  # E_rev (V)
            "Ncyc": 4,  # number of cycles
            "v": 5,  # scan speed (V/s)
            "np": 6,  # 2^N points in time across n cycles (int)
            "digifft": 7,  # correct vscan and freq for DigiPot/FFT (1 = yes, 0 for no)
            "digi": 8,  # output type: 0=E,i,t; 1=DigiPot compatible
            "et_mech": 9,  # EC type: 0 = Butler-Volmer, 1 = Marcus theory
            "pre_eq": 10,  # Pre-equilibrium switch: 0=stay with user entered, 1 = apply Pre-eqm operation
            "s_tm": 11,  # fix number of timesteps (1 = yes; 0 = no)
            "n_fixed": 12,  # Use a fixed number of timesteps rather than 2^N
            "beta": 13,  # beta
            "dstar": 14,  # dtar_min
            "v_st": 15,  # max voltage step
            "t_res": 16,  # time resolution experimentally to correct vscan/f (us)
            "debug": 17,  # show debug output files as well as MECSimOutput.txt (1=yes; 0=no)
            "adv_v": 18,  # use advanced voltage ramp (0 = E_start=E_end, 1 = use advanced ramp below, 2=From file 'EInput.txt')
            "nerev": 19,  # number of E_rev lines for advanced ramp (if enter 0 then first E_rev value is the final time)
            "adv_estr": 20,  # E_start (V)
            "adv_eend": 21,  # E_end (V)
            "erev": 22,  # start of Erev list
            "geotype": 22
            + self.spaces_dic[
                "erev"
            ],  # Geometry type (1=planar, 2=spherical, 3=cylinder, 4=RDE)
            "area": 23
            + self.spaces_dic["erev"],  # Planar: surface area of electrode (cm^2)
            "nsph": 24
            + self.spaces_dic["erev"],  # Number of spheres (can be fractional)
            "radsph": 25 + self.spaces_dic["erev"],  # Radius of single sphere (cm)
            "ncycl": 26
            + self.spaces_dic["erev"],  # Number of cylinders (can be fractional)
            "radcyl": 27 + self.spaces_dic["erev"],  # Radius of single cylinder (cm)
            "radlen": 28 + self.spaces_dic["erev"],  # Length of single cylinder (cm)
            "spares": 29 + self.spaces_dic["erev"],  # Spacial Resolution (>20)
            "rder": 30 + self.spaces_dic["erev"],  # RDE radius (cm)
            "rders": 31 + self.spaces_dic["erev"],  # RDE rotation speed (rad/s)
            "rdekv": 32 + self.spaces_dic["erev"],  # RDE kinematic viscosity (cm^2/s)
            "nac": 1
            + self.spaces_dic[
                "ind_rotation"
            ],  # number of AC sources to add (keep 1 with zero amplitude if want DC only)
            "AC": 2 + self.spaces_dic["ind_rotation"],  # start of the frequency data
            "nsol": self.spaces_dic[
                "ind_solution"
            ],  # number of species (need n lines below)
            "conc": 1 + self.spaces_dic["ind_solution"],  # storing the sol stuff start
            "ncap": 1
            + self.spaces_dic["ind_solution"]
            + self.spaces_dic[
                "conc"
            ],  # maximum a^n term for a capacitance given by C = a_0 + a_1 V + a_2 V^2 + ... + a_n V^n,
            "Epzc": 2
            + self.spaces_dic["ind_solution"]
            + self.spaces_dic["conc"],  # Epzc (Volts)
            "cap": 3
            + self.spaces_dic["ind_solution"]
            + self.spaces_dic["conc"],  # a_0 term (F/cm^2)
            "kinetic": self.spaces_dic["ind_reac"],
        }

        # set up the inverse dictionary
        self.mapping_backward = {v: k for k, v in self.mapping_forward.items()}

        return

    def data2structure(self, datanum):
        """WILL NEED SOMETHING TO DO THE LINE MAPPING TO DICT VALUES"""  # this could be inverted to do the oppisite

        # collect a bunch of pointer structures
        functionpointers = inp_struct.inp_to_datastructure()
        self.datastruct = {}  # TODO CANGE TO CLASS

        # parameterspecific
        for keys, funcs in functionpointers["function"].items():
            s = self.mapping_forward[keys]
            self.datastruct.update({keys: funcs(datanum[s])})

        # DO THE REPEAT PROCESS
        for keys, funcs in functionpointers["repeat"].items():
            s = self.mapping_forward[keys]
            listin = datanum[s : s + self.spaces_dic[keys]]
            self.datastruct.update({keys: funcs(listin)})

        # calculate an approximate total runtime
        tottime = self.runtime_guesser()
        self.datastruct.update({"time_tot": tottime})

        # self.datastruct.update({"MISC":1})
        # load in the data structures
        # DataStruct = Base_MEC("INP")
        self.datastruct = Base_MEC(**self.datastruct)

        return self.datastruct

    # This is a function to convert the structure back to an inp Just returns a giant string that can be printer to file
    def structure2inp(self, structure):
        #
        functionpointers = inp_struct.data_structure2inp()

        # convert the functions into something to use

        # create an empty thing
        output = ["" for i in range(self.spaces_dic["Ntot"])]

        # insert the values into the output

        # add in the comments
        self.comment_dic = inp_struct.get_inp_comments()

        # parameterspecific
        for keys, funcs in functionpointers["function"].items():
            s = self.mapping_forward[keys]
            s1 = funcs(structure[keys])
            comment = self.comment_dic[keys]  # get the comments
            output[s] = f"{s1}\t\t{comment}"

        # DO THE REPEAT PROCESS
        for keys, funcs in functionpointers["repeat"].items():
            s = self.mapping_forward[keys]
            comment = self.comment_dic[keys]  # get the comments
            cal = funcs(structure[keys])  # these functions return a row
            for i, v in enumerate(cal):
                if isinstance(comment, str):
                    output[s + i] = f"{v}\t\t{comment}"
                else:
                    output[s + i] = f"{v}\t\t{comment[i]}"
        # check for empties Failsafe
        if not all(output):
            raise Exception("Error, empty inp row")

        # join all the comments together
        output = " \n".join(output)

        return output

    # load the print(Nrec) inp file and convert the .inp into a list
    def load_inp(self, filename):
        # read in the inp file
        with open(filename) as f:
            data = f.readlines()

        self.datanum = []
        for rows in data:
            s = rows.split("!")
            # clean whitespaces and such
            for i, val in enumerate(s):
                val = val.strip()
                s[i] = val
            self.datanum.append(s[0])
            # how are we going to put these back in
            # self.comments.append("! " + s[1]) # add "! "  # This should be saved as a config

        return

    # this reads MECSim settings and tells the copmuter what line everything is on
    def data_finder_inp(self, data):
        i = 22  # dataframe index always same

        # get the number of custom reverses
        nrev = int(data[i - 3])
        Crot = i + 10 + nrev  # add values to next varible rotation speed
        Nac = int(data[Crot + 1])  # Number of AC inputs
        Nsol = int(data[Crot + 2 + Nac])  # number of sols pres
        Csol = Crot + 2 + Nac  # Line solution propities start n
        Ncap = int(data[Csol + Nsol + 1]) + 1

        # find indices row occurs in
        Ckin = Csol + Nsol + Ncap + 3
        Nrec = len(data) - (Ckin)  # number of reaactions
        Nrows = len(data)

        # save all the allocations
        self.spaces_dic = {
            "ind_rotation": Crot,
            "ind_solution": Csol,
            "ind_reac": Ckin,
            "conc": Nsol,
            "AC": Nac,
            "erev": nrev,
            "kinetic": Nrec,
            "cap": Ncap,
            "Ntot": Nrows,
        }  # seconds number of repeats

        return

    # will need a backwards process for teh structure
    def data_finder_struct(self, data):
        i = 22  # dataframe index always same

        # these can all be extracted directly from the structure
        nrev = data["nerev"]
        Nsol = data["nsol"]
        Nac = data["nac"]
        Nrec = len(data["kinetic"])  # just uses the number of kinetic rows
        Ncap = data["ncap"] + 1  # need to include the c_0 value count here

        # these will need to be calculated for indices
        Crot = i + 10 + nrev
        Csol = Crot + 2 + Nac
        Ckin = Csol + Nsol + Ncap + 3

        # get the total number
        Nrows = Ckin + Nrec

        # save all the allocations
        self.spaces_dic = {
            "ind_rotation": Crot,
            "ind_solution": Csol,
            "ind_reac": Ckin,
            "conc": Nsol,
            "AC": Nac,
            "erev": nrev,
            "kinetic": Nrec,
            "cap": Ncap,
            "Ntot": Nrows,
        }  # seconds number of repeats

        return

    # because it works best for downstream process's if we have an approximate
    # runtime as this allows us to not have to guess it elsewhere
    def runtime_guesser(self):
        # check if using advanced voltage ramp
        if self.datastruct["adv_v"] == 0:  # generic use case cyclic voltage
            tot_time = self.datastruct["Ncyc"] * (
                2
                * abs(self.datastruct["estart"] - self.datastruct["eend"])
                / self.datastruct["v"]
            )
        elif self.datastruct["adv_v"] == 1:  # complex voltage ramp use case
            s = self.datastruct["adv_estr"]  # E_start (V)
            e_len = 0
            for e in self.datastruct["erev"]:
                e_len += abs(s - e)
                s = e
            e_len += abs(s - self.datastruct["adv_eend"])

            # allow for multiple cycles
            e_len *= self.datastruct["Ncyc"]

            tot_time = e_len / self.datastruct["v"]

        elif self.datastruct["adv_v"] == 2:
            raise ValueError(
                "ERROR: method of passing EInput.txt isn't currently supported, try advanced ramp case instead."
            )

        return tot_time
