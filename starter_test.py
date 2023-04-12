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

from datetime import date   
import pytest
from oop_loan_pmt import Loan, collectLoanDetails, main


# Unit tests for Loan class
def test_discount_factor_calculation():
    loan = Loan(100000, 30, 0.06)
    loan.calculateDiscountFactor()
    print("\r")  # carriage return
    print(" -- discount_factor_calculation unit test")
    assert loan.getDiscountFactor() == pytest.approx(166.7916, rel=1e-2)

def test_loan_payment_calculation():
    loan = Loan(100000, 30, 0.06)
    loan.calculateLoanPmt()
    print("\r")  # carriage return
    print(" -- loan_payment_calculation unit test")
    assert loan.getLoanPmt() == pytest.approx(599.55, rel=1e-2)

# Functional tests for collectLoanDetails() function
def test_collect_loan_details_input(monkeypatch):
    user_input = ['100000', '30', '0.06']
    monkeypatch.setattr('builtins.input', lambda x: user_input.pop(0))
    loan = collectLoanDetails()
    print("\r")  # carriage return
    print(" -- collect_loan_details functional test")
    assert loan.loanAmount == 100000
    assert loan.numberOfPmts == 30 * 12
    assert loan.annualRate == 0.06

def test_collect_loan_details_invalid_input(monkeypatch):
    user_input = ['abc', '30', '0.06']
    monkeypatch.setattr('builtins.input', lambda x: user_input.pop(0))
    print("\r")
    print(" -- invalid_loan_details functional test")
    with pytest.raises(ValueError):
        collectLoanDetails()

# Functional test for main() function
def test_main_output(capsys):
    # Capture the stdout to check the output
    loan = Loan(100000, 30, 0.06) # Set up a Loan object with known values
    loan.calculateLoanPmt()
   
    print("\r")
    print(" -- main functional tesr")
    expected_output = "Your monthly payment is: $599.55"
    assert main() == expected_output