"""
Palindrome Tests
"""
from palindrome import is_palindrome


def test_for_error():
    """
    Test to assert an ValueError returns
    """
    astring = is_palindrome(123)
    assert astring == ValueError


def test_for_a():
    """
    Test to assert 'a' returns True
    """
    still_equal = is_palindrome('a')
    assert still_equal is True


def test_for_bb():
    """
    Test to assert 'bb' returns True
    """
    still_equal = is_palindrome('bb')
    assert still_equal is True


def test_for_abc():
    """
    Test to assert 'abc' returns True
    """
    still_equal = is_palindrome('abc')
    assert still_equal is False


def test_for_laval():
    """
    Test to assert 'laval' returns True
    """
    still_equal = is_palindrome('laval')
    assert still_equal is True


def test_for_toronto():
    """
    Test to assert 'toronto' returns True
    """
    still_equal = is_palindrome('toronto')
    assert still_equal is False


def test_for_able():
    """
    Test to assert 'Able was I ere I saw Elba' returns True
    """
    still_equal = is_palindrome('Able was I ere I saw Elba')
    assert still_equal is True
