# This file contains tests that they are addressing the reliability and robustness of the program aiming to break it
# with unexpected input checking if the outcome is the one expected.
from unittest import TestCase


class TestUtilities(TestCase):
    # Tests if a wrong input not in the choices will return an error message.
    def wrongInputLeadsToErrorMessage(self):
        pass

    # Tests what is going to happen with 2 flags passed. This should be tested in multiple ways as currently
    # one flag is using the __contains__ function.
    def reactionWithTwoFlagsPassedAsQueries(self):
        pass

    # I know that is unusual to pass a name of an individual or a company including a dash, but this can happen in a
    # domain name.  Need to prove the way we parse.
    def reactionWithParsingWithQueryHavingDash(self):
        pass

    # The way that this function is operating is by using the contains flag, the reason is that people name and location
    # may well include more that 2 words.
    def reactionWithPiplFlagIncludingLocation(self):
        pass
