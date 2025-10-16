from mecsim_utils.processing.auto_ftacv import FTACV_experiment

from dataclasses import dataclass


# dummy AC case
@dataclass
class Dummy_MECSTRUCT:
    AC: list[dict]  # = [{"f":9}]


MECsimstruct = Dummy_MECSTRUCT(AC=[{"f": 9}, {"f": 117}, {"f": 550}])


ftacv_func = FTACV_experiment(MECsimstruct, Nmax=4)

harmonics = ftacv_func()

print(harmonics)

exit(0)
