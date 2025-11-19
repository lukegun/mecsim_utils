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
