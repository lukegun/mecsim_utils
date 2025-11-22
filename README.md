# mecsim_utils
This is a repo to make module that has been made for a range of mecsim FTAC voltammetry AI  systems


# UNIT TESTS
python -m pytest --cov --config-file=.coveragerc

# TODO TOMMOROW
- refactor harmonics (Map out the process)
- why is the 3AC not passing AC validation
    (ISSUE is so many combination it overloads the possible harmonics this needs a fix)
- see if theres a way to remove the currently two FFT's that are done
- validate accuracy
- add unit tests
- optimise the flow

# draft up the SQL stuff (set up databases and rough structure)
SQL
auto capacitance fitting
SOME smart way to lo9ad in files

# TO MAJOR BUGS IN multi harmonic
- max_filter1d on Line221 in auto_ftacv needs to be a varible based on length of frequency domain star DONE
- There is a bug where an harmonic will be labeled 0:-6:4 instead of like 1:-1:0 due to the processs that the id get checked and filtered. obviously the oppisite would be prefered in this case (This has been fixed and bug was also found in the triplicate secondary case harmonics)
- issue one fix's a lot of the issues but there is still an issue with random noise at VERY high frequency harmonics this could be a random simulation noise but I need some way to be like there is no way a stable harmonic could be id'd from this info
- NEED TO RESET THE FUCKING experimental examples (DO THIS BY LOADING IN THE SAVED dataclasses)

# TODO

- Finish up the unit tests for this component 
    TODO FIX THE AUTO HARM CASE FOR VERY HIGH FREQUENCY INFORMATION
    3. MULTI AC cases
    4. DC cases including Capacitance linear and non-linear
    5. Comlplex hetrogeneous (mediated catalyse (three steps of catalyse))
    6. Marcus-hush 
    7. double check the testing use

- MOVE HARM CALC INTO A SINGLE CLASS

- set up the auto capacitance fitting
- experimental loaders dynamic
- upload to SQL database transforms


# todo before break
GET MECWRITTERV3 working and set up
- get clusteringV2 set up
- get DNN clustering set up
- prototype RL learning

## AIM for weekend do the SQL API

# Do the SQL uploading procedure
