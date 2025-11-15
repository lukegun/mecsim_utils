# this builds all the mecsim examples into a usefull callable systems

# this are all the standard FTACV examples we are loading in
from .hetrogeneous import (
    example_ftacvE_red,
    example_ftacvE_ox,
    example_ftacvEE_red,
    example_ftacvEE_ox,
    example_ftacvEC1_red,
    example_ftacvEC1_ox,
    example_ftacvEC2_red,
    example_ftacvEC2_ox,
)

# from .homogeneous import example_ftacvESurf_red, example_ftacvESurf_ox

# IS THERE A CLEANER WAY TO ORGANISE THIS ????


########## These functions collect the functions and group them
# This could be done by marks but I am aiming to have this non pydantic based
def get_AC_cases():
    AC_examples = [
        example_ftacvE_red,
        example_ftacvE_ox,
        example_ftacvEE_red,
        example_ftacvEE_ox,
        example_ftacvEC1_red,
        example_ftacvEC1_ox,
        example_ftacvEC2_red,
        example_ftacvEC2_ox,
    ]
    return AC_examples
