import numpy as np

from mecsim_utils.processing.auto_ftacv import FTACV_experiment, FTACV_harmonic

from dataclasses import dataclass

# dummy AC case
@dataclass
class Dummy_MECSTRUCT:

    AC : list[dict] #= [{"f":9}]

MECsimstruct = Dummy_MECSTRUCT(AC= [{"f":9}])


ftacv_func = FTACV_experiment(MECsimstruct)

harmonics = ftacv_func()

print(harmonics)

exit(0)


MECsimstruct = Dummy_MECSTRUCT

nmax = 3

p1 = [(i+1)*f1 for i in range(nmax)]
p2 = [(i+1)*f2 for i in range(nmax)]
p3 = [(i+1)*f3 for i in range(nmax)]

# now I need a way to save the metadata for

matrix = np.zeros((2*nmax,2*nmax)) # likily going to need more
freq = []
for i in range(nmax):

    freq.append(p1[i])
    freq.append(p2[i])

    for j in range(nmax):
        freq.append(p2[i] - p1[j])
        freq.append(p2[i] + p1[j])
        freq.append(- p2[i] + p1[j])

# conditional filters
freq = np.array(freq)
freq = np.where(freq>0, freq, 0) # remove impossible frequencies
print(freq)


freq = []            
for i in range(nmax):


    freq.append(p1[i])
    freq.append(p2[i])
    freq.append(p3[i])

    for j in range(nmax):

        freq.append(p2[i] - p1[j])
        freq.append(p2[i] + p1[j])
        freq.append(- p2[i] + p1[j])

        freq.append(p3[i] - p1[j])
        freq.append(p3[i] + p1[j])
        freq.append(- p3[i] + p1[j])

        freq.append(p3[i] - p2[j])
        freq.append(p3[i] + p2[j])
        freq.append(- p3[i] + p2[j])

        for k in range(nmax):
            freq.append(p3[k] + p2[i] + p1[j])

            freq.append(p3[k] + p2[i] - p1[j])
            freq.append(p3[k] - p2[i] + p1[j])
            freq.append(-p3[k] + p2[i] + p1[j])

            freq.append(p3[k] - p2[i] - p1[j])
            freq.append(-p3[k] + p2[i] - p1[j])
            freq.append(-p3[k] - p2[i] + p1[j])

# conditional filters
freq = np.array(freq)
freq = np.where(freq>0, freq, 0) # remove impossible frequencies
print(set(freq))