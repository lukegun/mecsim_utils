"""
    This is a list of functions to convert back and forth for the specific row into our custom function
"""

import mecsim_utils.utils.utils as Cutils

# this stores the functions to convert into the datastructure
def inp_to_datastructure():

    # get some generalised stucural mapping for RL
    funcmapping = get_structure_type()

    # series of pointers to convert from list of ints to datastructure
    # is there a better way to do this
    struc = {}
    for var in funcmapping["parameter"]["float"]:
        struc.update({var:float})

    for var in funcmapping["parameter"]["int"]:
        struc.update({var:int})

    repeatdic = {"AC": ac_inp2struct, # start of the frequency data
                 "conc": sol_inp2struct, # storing the sol stuff start
                 "kinetic": kinetic_inp2struct} 
    for var in funcmapping["parameter"]["repeat"]:
        repeatdic.update({var:repeat_inp2struct})

    return {"function":struc, "repeat":repeatdic}


######################################################################
############# THESE FUNCTIONS convert list to structure  #############
######################################################################

# this stores the functions to convert to the row from the datastructure
def repeat_inp2struct(vallist):

    output = []
    for vals in vallist:
        output.append(float(vals))

    return output

def sol_inp2struct(vallist):

    output = []
    for vals in vallist:
        s = vals.split(",")
        output.append({"c":float(s[0]), "d":float(s[1]),"s":int(s[2])})

    return output

def ac_inp2struct(vallist):
    output = []
    for vals in vallist:
        s = vals.split(",")
        output.append({"a":float(s[0]), "f":float(s[1])})

    return output

def kinetic_inp2struct(vallist):
    output = []
    for vals in vallist:
        s = vals.split(",")

        kinetic = []
        for l in s[1:len(s)-5]:
            kinetic.append(int(l))

        output.append({"type":float(s[0]), "react":kinetic,"kf":float(s[-5]),
                       "kb":float(s[-4]),"E0":float(s[-3]),
                       "ksreal":float(s[-2]),"alpha":float(s[-1])})

    return output


######################################################################
############# THESE FUNCTIONS convert structure to list  #############
######################################################################


# this stores the functions to convert into the datastructure
def data_structure2inp():

    # get some generalised stucural mapping for RL
    funcmapping = get_structure_type()

    # series of pointers to convert from list of ints to datastructure
    # is there a better way to do this
    struc = {}
    for var in funcmapping["parameter"]["float"]:
        struc.update({var:Cutils.format_e}) # formate

    for var in funcmapping["parameter"]["int"]:
        struc.update({var:str})

    for var in funcmapping["parameter"]["repeat"]:
        struc.update({var:repeat_struct2inp})


    repeatdic = {"AC": ac_struct2inp, # start of the frequency data
                 "conc": sol_struct2inp, # storing the sol stuff start
                 "kinetic": kinetic_struct2inp} 
    for var in funcmapping["parameter"]["repeat"]:
        repeatdic.update({var:repeat_struct2inp})


    return {"function":struc, "repeat":repeatdic}

# this stores the functions to convert to the row from the datastructure
def repeat_struct2inp(vallist):
    output = []
    for vals in vallist:
        output.append(Cutils.format_e(vals)) # needs to be formate 
    return output

def sol_struct2inp(vallist):

    output = []
    for vals in vallist:
        s1 = Cutils.format_e(vals["c"])
        s2 = Cutils.format_e(vals["d"])
        s3 = int(vals["s"])

        output.append(f'{ s1 }, { s2 }, { s3 }')

    return output

def ac_struct2inp(vallist):
    output = []
    for vals in vallist:
        s = "{:.4f}, {:.4f}".format(vals["a"],vals["f"]) # thisis enough of a 
        output.append(s)

    return output

def kinetic_struct2inp(vallist):
    output = []
    for vals in vallist:

        r = [str(x) for x in vals["react"]]
        skin = ', '.join(r)
        
        s1 = int(vals["type"])
        s2 = Cutils.format_e(vals["kf"])
        s3 = Cutils.format_e(vals["kb"])
        s4 = Cutils.format_e(vals["E0"])
        s5 = Cutils.format_e(vals["ksreal"])
        s6 = Cutils.format_e(vals["alpha"])

        output.append(f'{ s1 }, { skin }, { s2 }, { s3 }, { s4 }, { s5 }, { s6 }')

    return output


#### Instead of putting them in config files I'm just putting this info to be embedded into the stuff
def get_inp_comments():
    
    # set up to work with the datastructure keys
    comments_dic = {"temp": "! Temperature (K)",
            "ru": "! uncompensated resistance (ohms)",
            "estart": "! E_start (V)",
            "eend": "! E_rev (V)",
            "Ncyc": "! number of cycles",
            "v": "! scan speed (V/s)",
            "np": "! 2^N points in time across n cycles (int)",
            "digifft": "! correct vscan and freq for DigiPot/FFT (1 = yes, 0 for no)",
            "digi": "! output type: 0=E,i,t; 1=DigiPot compatible",
            "et_mech": "! EC type: 0 = Butler-Volmer, 1 = Marcus theory",
            "pre_eq": "! Pre-equilibrium switch: 0=stay with user entered, 1 = apply Pre-eqm operation",
            "s_tm": "! fix number of timesteps (1 = yes; 0 = no)",
            "n_fixed": "! Use a fixed number of timesteps rather than 2^N",
            "beta": "! beta",
            "dstar": "! Dstar_min",
            "v_st": "! max voltage step",
            "t_res": "! time resolution experimentally to correct vscan/f (us)",
            "debug": "! show debug output files as well as MECSimOutput.txt (1=yes; 0=no)",
            "adv_v": "! use advanced voltage ramp (0 = E_start=E_end, 1 = use advanced ramp below, 2=From file 'EInput.txt')",
            "nerev": "! number of E_rev lines for advanced ramp (if enter 0 then first E_rev value is the final time)",
            "adv_estr": "! E_start (V)",
            "adv_eend": "! E_end (V)",
            "erev": "! E_rev - REPEAT for more complicated ramps",
            "geotype": "! Geometry type (1=planar, 2=spherical, 3=cylinder, 4=RDE)",
            "area": "! Planar: surface area of electrode (cm^2)",
            "nsph": "! Number of spheres (can be fractional)",
            "radsph": "! Radius of single sphere (cm)",
            "ncycl": "! Number of cylinders (can be fractional)",
            "radcyl": "! Radius of single cylinder (cm)",
            "radlen": "! Length of single cylinder (cm)",
            "spares": "! Spacial Resolution (>20)",
            "rder": "! RDE radius (cm)",
            "rders": "! RDE rotation speed (rad/s)",
            "rdekv": "! RDE kinematic viscosity (cm^2/s)",
            "nac": "! number of AC sources to add (keep 1 with zero amplitude if want DC only)",
            "AC": "! AC sin wave: amp (mV), freq(Hz) (REPEAT)",
            "nsol": "! number of species (need n lines below)",
            "conc": "! REPEAT: initial concentration of i (mol/cm3 or mol/cm2 if SC), Diffusion coeff for i, D_i [cm2/s], surface confined (=1 for yes, else in solution)",
            "ncap": "! maximum a^n term for a capacitance given by C = a_0 + a_1 V + a_2 V^2 + ... + a_n V^n, where V = Eapp - iR - Epzc. Make sure there are enough lines below to go to a^n",
            "Epzc": "! Epzc (Volts)",
            "cap": ["! a_0 term (F/cm^2)", "! a_1 term (F/cm^2)", "! a_2 term (F/cm^2)", "! a_3 term (F/cm^2)", "! a_4 term (F/cm^2)"],
            "kinetic": "! type, reactions (nsp times): kf,kb, E0 (V),ksreal (cm/s), alpha for BV or lambda* for MH (1eV) (REPEAT FOR EACH REACTION)"
                }

    return comments_dic

# this defines general strucutal type and how we want the tranformation to work
def get_structure_type():

    structtype = {"parameter": {
                        # these are floats types
                        "float": ["temp", "ru", "estart", "eend", "Ncyc", "v",
                                  "beta", "dstar", "v_st", "t_res", "adv_estr",
                                  "adv_eend", "area", "radsph", "ncycl", "radcyl",
                                  "radlen", "spares", "rder", "nsph", "rders", "rdekv",
                                  "Epzc"],
                        # these are inp types
                        "int": ["np", "digifft", "digi", "et_mech", "pre_eq", "s_tm", 
                                "n_fixed", "debug", "adv_v", "nerev", "geotype", "nac",
                                "nsol", "ncap" ],
                        # values that are repeated over multiple rows
                        "repeat": ["erev", "cap"],
                        # these are custom rows
                        "custom": {"AC": "ac_struct",
                                   "conc": "sol_struct",
                                   "kinetic": "kinetic_struct"}
                            }
                    }



    return structtype


# TODO set up a pydantic class for testing