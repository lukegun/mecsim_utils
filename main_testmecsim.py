"""
This is a main function for the analysis of errors in
MECSim file. It is designed for analysis of MECSim.exe
as well as the MECSim_F2PY

LG 20/6/2023
"""

import mecsim_utils.processing.utils as mecUtils
import matplotlib.pyplot as plt
from mecsim_utils.transformations.inp.datamodel import INP_DataModel
import mecsim_utils.processing.auto_ftacv as ftcount
# import test_utils.Script_generator as scriptgen


def MECSim_test(comp_files):
    # generate the simulation space from the parameterfile.txt USE COMBINATIONAL OR OTHER

    # save outputs to dic
    """# Calculate the F2Py function"""
    # f2py
    f2py_currentdic = {}
    # print(comp_file)
    files = comp_files[0]

    """# Calculate the F2Py function"""
    # Load the data file
    # read master file
    filename = comp_files[0]

    # read in the inp file
    with open(filename) as f:
        data = f.readlines()
    print("fucker")

    # identify key splits in the mecsim input file
    # {'rotation': 34, 'solution': 38, 'reac': 47, 'Num_solutions': 2, 'Number_freq': 1}
    # spaces_dic = utilsmec.data_finderV2(datanum)
    Mec_parser = INP_DataModel(filename, to_struct=True)
    MECsimstruct = Mec_parser.transform()
    print(MECsimstruct.temp)
    # exit(1)
    print("EHHH")
    Mec_parser2 = INP_DataModel(MECsimstruct, to_struct=False)
    MECsiminp = Mec_parser2.transform()
    print("fuck")

    """I SHOULD PUT SOMETHING HERE TO MORE CLEANLY WRAP THE mecsim instance and the transformation"""
    Currenttot = mecUtils.mecsim_current(MECsimstruct)

    # get autobandwidth
    bandwidth = ftcount.bandwidthallocator(MECsimstruct.AC[0]["f"])

    np = len(Currenttot)
    deltatime = 1 / np
    nsimdeci = ftcount.Simerharmtunc(
        len(Currenttot), deltatime, bandwidth, MECsimstruct.AC[0]["f"], HarmMax=12
    )

    # calculate a rough N estimate
    Nprim = ftcount.harmoniccounter(Currenttot, nsimdeci, PSdiff=1.0)

    bandwidtharray = []
    for i in range(Nprim):
        bandwidtharray.append(bandwidth)

    # this function takes the current and
    harmonics = mecUtils.primaryharmoniccalc(
        Currenttot, MECsimstruct.AC[0]["f"], bandwidtharray
    )

    plt.plot(Currenttot)
    plt.savefig("test.png")

    print(Currenttot)

    print("Compiled MECSim")

    f2py_currentdic.update({files: Currenttot})

    # multplies one of the currents by negitive one

    # identify the name for output "compfile1-comp_process-date_V1.txt"

    # print output to mean err to textfile

    # print all to output

    return "work"


if __name__ == "__main__":
    # need to input AC = {True, False}
    # python3 main.py compfile1.inp compfile2.inp comp_process AC

    comp_files = ["tests/testingconfig/Master.inp"]
    # comp_varibles = False#args[3] # left out as it would take to long to implement correctly

    y = MECSim_test(comp_files)

    print("validation worked")
