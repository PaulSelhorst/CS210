"""
CS 210 Lab 1 Lab 1 Exercises
Author: Pk Selhorst
Credits: N/A
Lab exercises demonstrating how
IDLE Editor and Shell interact
"""
def is_even(n):
    '''
    (int) -> Boolean
    Returns True if n
    is an even number
    >>> is_even(100)
    True
    >>> is_even(101)
    False
    >>> is_even(0)
    True
    '''
    return (n % 2) == 0
print(help(is_even))