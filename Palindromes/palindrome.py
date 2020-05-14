"""
Palindrome checker.
"""
from collections import deque


def is_palindrome(astring):
    """
    Palindrome checker using Deque
    """
    if isinstance(astring, (float, int)):
        return ValueError
    string_deque = deque(astring)
    if not string_deque:
        still_equal = False
        return still_equal
    while len(string_deque) == 1:
        still_equal = True
        return still_equal
    while len(string_deque) > 1:
        first = string_deque.popleft()
        last = string_deque.pop()
    if first != last:
        still_equal = False
    else:
        still_equal = True
    return still_equal
