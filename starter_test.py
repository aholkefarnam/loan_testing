# test_friend.py

# assert expression
## if true nothing happens
## if false raises AssertionError

# create virtual environment and activate
# pip install pytest
# pip install pytest-cov

# run tests with python -m pytest -s
# compare -s and -v when running the tests
# run coverage tests with python -m pytest --cov

import pytest
from datetime import date
from friend import *


### unit tests ###
def test_calculate_current_age():
    """
    GIVEN a user enters the year they were born
    WHEN that year is passed to this function
    THEN the user's age is accurately calculated
    """
    print("\r")  # carriage return
    print(" -- calculate_current_age unit test")
    assert (
        calculate_current_age(2000) == 23
    )  # STATIC: will change as the years progress


def test_calculate_current_age():
    """
    GIVEN a user enters the year they were born
    WHEN that year is passed to this function
    THEN the user's age is accurately calculated
    """
    birth_year = 1995
    today = date.today()
    expected_age = today.year - birth_year
    assert (
        calculate_current_age(birth_year) == expected_age
    )  # DYNAMIC: calculates the current year
