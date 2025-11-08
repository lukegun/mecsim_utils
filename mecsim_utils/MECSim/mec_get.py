"""
THIS IS A FUNCTION FOR GETTING A MECSIM cextention that is made
by the numpy F2PY which is COMPADIBLE
BASED on python version and archetecture
"""

import sys
import platform


# this is so that these utils aren't version specific
def mecs_get():
    python_version = f"{sys.version_info[0]}.{sys.version_info[1]}"
    cpu_arch = platform.processor()

    # to lazy to make this a switch or a hashmap
    try:
        if python_version == "3.12" and cpu_arch == "x86_64":
            from .python_312.mecsim import mecsim_main  # load in python_312
        else:
            message = (
                f"ERROR: compiled MECSim's not compadable with "
                f"python version {python_version} "
                f"and cpu arch {cpu_arch}."
            )
            raise ValueError(message)

    except ValueError as e:
        print("ERROR: ", e)
        exit(1)

    return mecsim_main
