#!/usr/bin/python
# -*- coding: utf-8 -*-

# Function declarations

# INSPIRATION: http://www.saltycrane.com/blog/2008/01/how-to-find-intersection-and-union-of/

""" NOTES:
      - requires Python 2.4 or greater
      - elements of the lists must be hashable
      - order of the original lists is not preserved
"""

def unique(a):
    """ Return the list with duplicate elements removed.
        
    Args:
        a (list): A list.
        
    Returns (list):
        The list with duplicate elements removed.
    """
    
    # NOTES:
    # 1. Built-in function 'set()' can convert a list (ordered) into a set (unordered).
    # 2. Built-in function 'list()' can convert a set (unordered) into a list (ordered).
    return list(set(a))

def intersect(a, b):
    """ Return the intersection of two lists.
        
    Args:
        a (list): A list.
        b (list): Another list.
        
    Returns (list):
        The intersection of the two lists.
    """
    
    # NOTE: Binary operator '&' is built in and returns the intersection of 2 sets.
    return list(set(a) & set(b))

def union(a, b):
    """ Return the union of two lists.
        
    Args:
        a (list): A list.
        b (list): Another list.
        
    Returns (list):
        The union of the two lists.
    """
    
    # NOTE: Binary operator '|' is built in and returns the union of 2 sets.
    return list(set(a) | set(b))

# NOTE: For unit testing purposes, execute as self-test only if being run as a top-level script.
if __name__ == "__main__":

    # Set variables.

    a = [0,1,2,0,1,2,3,4,5,6,7,8,9] # List of integers
    b = [5,6,7,8,9,10,11,12,13,14]  # List of integers
    
    # NOTES:
    # 1. In Python 2.x.x, reserved word 'print' is a statement, so it doesn't use paretheses.
    # 1. In Python 3.x.x, reserved word 'print' is a function, so it does use paretheses.
    print(unique(a))
    print(intersect(a, b))
    print(union(a, b))
