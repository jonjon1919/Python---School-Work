""" Tests for banking.py"""
import datetime as dt
from banking import Account, Transaction


def test_deposit_are_appeneded_to_transactions_list():
    """
    Test to assert deposits append to transactions list
    """
    test = Account()
    print(test.deposit(50))
    print(test.transactions)
    assert test.transactions == [50]


def test_deposit_is_positve():
    """
    Test for positve amount on deposits
    """
    test = Account()
    test.deposit(100)
    assert test.get_balance() == 100


def test_withdraw_is_negative():
    """
    Test for negative amount on withdraws
    """
    test = Account()
    test.withdraw(50)
    assert test.get_balance() == -50


def test_for_zero_balance():
    """
    Test for Zero balance of an account
    """
    test = Account()
    assert test.get_balance() == 0


def test_transaction_without_date():
    """
    Testing Transaction Class
    """
    print(Transaction(100))


def test_trans_with_date():
    """
    Testing transaction with a date
    """
    print(Transaction(125, dt.date(2019, 10, 31)))
