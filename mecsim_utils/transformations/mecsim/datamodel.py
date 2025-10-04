"""
    This is the data model to convert to something to pass to mecsim function
"""

import numpy as np
from dataclasses import asdict


class MECSIM_DataModel:

    def __init__(self,input):

        # this are needed for the backward pregression but less so other way
        self.input = asdict(input) # this is the data structure

        # Key values used to deal with fortran being static varibles

        # this will need to be made consistent to the FORTRAN function
        # TODO WRITE DOWN WHAT THESE ARE
        self.nrmax = 30
        self.nsigmax = 30
        self.nrmaxtot = 100
        self.nmaxErev = 10000
        self.nsp = 30 
        self.nmaxcapcoeff = 4 # Max number of cap values
        self.nstoremax = 10000000 # max current value

        return
    
    def transform(self):

        # generic Error code
        Error_Code = 0

        # extracts some key values to pass
        MECSettings, Numberin = self.input_sep()

        # turns values and the more complex stuff into varibles for mecsim
        Reacpara, reacMech, Capaci, Diffvalues, ACSignal, \
            EModown, Currenttot = self.general_transform()

        # set up some placeholder customm values
        # Empty BUT ADJUST TO FIT THE NUMBER OF CUSTOM values
        MECSettings[18] = 0 # sets the output type to take the below values in  2 for custom #TODO this just turns it off

        Ecustom, Tcustom, MECSettings = self.custom_pottime(MECSettings, Numberin)

        # I RECKON THIS NEEDS TO BE CHANGED TO A KWARGS THAT WE CAN WRAP THE MECSIM FUNCTION IN
        return MECSettings,Numberin, Reacpara,reacMech,Capaci, \
            Diffvalues, ACSignal, EModown, Currenttot, Ecustom, Tcustom, Error_Code
    
    # this packages up a bunch of generic info for mecsim
    def input_sep(self):

        Numberin = [0, 0, 0, 0, 0, 0]

        # Numberin
        Numberin[0] = 2 ** self.input["np"]  # Ndatapoint
        Numberin[1] = self.input["nerev"]  # Nev
        Numberin[2] = self.input["nac"]  # NAC
        Numberin[3] = self.input["nsol"]  # Nspecies
        Numberin[4] = self.input["ncap"] + 1  # Ncap+1
        Numberin[5] = len(self.input["kinetic"])  # Nmech

        MECSettings = [self.input["temp"],self.input["ru"], self.input["estart"], self.input["eend"],
                       self.input["Ncyc"], self.input["v"], self.input["np"], self.input["digifft"],
                       self.input["digi"], self.input["et_mech"], self.input["pre_eq"], 
                       self.input["s_tm"], self.input["n_fixed"], self.input["beta"], self.input["dstar"],
                       self.input["v_st"], self.input["t_res"], self.input["debug"], self.input["adv_v"],
                       self.input["nerev"],self.input["geotype"], self.input["area"], self.input["nsph"],
                       self.input["radsph"], self.input["ncycl"], self.input["radcyl"], self.input["radlen"],
                       self.input["spares"], self.input["rder"], self.input["rders"], 
                       self.input["rdekv"],self.input["Epzc"]]
        
        # Extract Data into MECSettings
        """MECSettings = [Temp,Resistance, E_start, E_rev, Ncyc, scanrate, datapoints, 
               Digipotcompad, outputtype, ECtype, pre_equalswitch, fixtimestep,
               Nfixedsteps, beta, Dstar_min, maxvoltstep, timeres, debugout, 
               Advolt, NEVramp,Geotype, planararea, Nsphere, sphererad, Ncyilinders,
               rad_cylinder, cylLen, spacialres, RDErad, RDErots, RDEkinvis, Epzc]"""


        return MECSettings, Numberin
    
    # this does the general structure transformation
    def general_transform(self):

        # static varible for fortran
        Currenttot = np.zeros(self.nstoremax)  # the plus ones are due to fortran starting at zero
        EModown = np.zeros(self.nmaxErev + 1)
        ACSignal = np.zeros((self.nsigmax + 1, 2))
        Diffvalues = np.zeros((self.nrmax + 1, 3))
        reacMech = np.zeros((self.nsp + 1, self.nrmax + 1))
        Reacpara = np.zeros((self.nsp + 1, 4 + 1))
        Capaci = np.zeros(self.nmaxcapcoeff + 2)

        # MIGHT NEED TO CHECK IF VALUES DON"T GO OVER FOR SAFTEY

        """POPULATE THE STATIC VARIBLE WITH VALUES FROM THE RL"""

        """example  output
        reacMech1 = [[0,-1,1,0],[2,0,-1,1]]
        Reacpara1 = [[2,10 ,0,1000,0.5],[2,2 ,0.1,2000,0.5]]
        Capacipre = [NCap, cap0, cap1, cap2, cap3, cap4]
        Diffvaluespre = [[Conc1,Diff1,surf1],[Conc2,Diff2,surf2],[Conc3,Diff3,surf3]]
        ACSignalpre = [[A1, freq1],[A2, freq2]]
        EModownpre = [AdEst, AdEend, E_rev1, E_rev2]
        """

        # EModown        
        EModown[0] = self.input["adv_estr"]
        EModown[1] = self.input["adv_eend"]
        for i, val in enumerate(self.input["erev"]):
            EModown[2+i] = val

        # Capaci
        Capaci[0] = self.input["ncap"]
        cap = self.input["cap"]
        for i in range(len(cap)):
            Capaci[1+i] = cap[i]

        # ACSignal
        for i, vals in enumerate(self.input["AC"]):
            ACSignal[i, 0] = vals["a"]
            ACSignal[i, 1] = vals["f"]

        # Diffvalues
        for i, vals in enumerate(self.input["conc"]):
            Diffvalues[i, 0] = vals["c"]
            Diffvalues[i, 1] = vals["d"]
            Diffvalues[i, 2] = vals["s"]

        # this figures out thereaction mechanisms
        for i, vals in enumerate(self.input["kinetic"]):
            Reacpara[i,0] = vals["kf"]
            Reacpara[i,1] = vals["kb"]
            Reacpara[i,2] = vals["E0"]
            Reacpara[i,3] = vals["ksreal"]
            Reacpara[i,4] = vals["alpha"]

            reacMech[i,0] = vals["type"]
            rm = vals["react"]
            for j in range(len(rm)):
                reacMech[i,1+j] = rm[j]

        return Reacpara, reacMech, Capaci, Diffvalues, ACSignal, EModown, Currenttot
    

    # TODO THIS WILL NEED TO BE MODIFIED IN FUTURE FOR THE GENERAL STRUCTURE
    # preallocate the functions
    def custom_pottime(self,MECSettings,Numberin):
        
        # I'm skipping this but in future this will need to be set up with the 
        MECSettings[18] = 0

        Ecustom = np.zeros(self.nstoremax)
        Tcustom = np.zeros(self.nstoremax)
        # example values placeholder
        if MECSettings[18] == 2: # load in custom values
            # This crashes if all zeros for Ecustom and Tcustom and using
            Numberin[0] = 16000  # changes the number of datapoints to N

            # allocate the rest of it
            # These will need to be loaded in from the structure
            Ecustom[:Numberin[0]] = np.linspace(0.01,0.8,num=Numberin[0]) # Custom voltage
            Tcustom[:Numberin[0]] = np.linspace(0.0,14,num=Numberin[0])  # Custom time


        return Ecustom, Tcustom, MECSettings
