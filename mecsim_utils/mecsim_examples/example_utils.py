# this is the base class for all FTACV examples
class FTACV_base_setup:

    # This is here in case we need to figure out any later information
    def __post_init__(self):

        # put some validation here

        return

    # this prints the explanation of what this use case is testing for
    def __repr__(self):
        f = "AC" if self.AC_case else "DC"
        return f"{f} case pytest ID {self.ids}: using reason {self.testing_use}"
