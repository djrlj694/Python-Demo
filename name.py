#!/usr/bin/python
# -*- coding: utf-8 -*-

# Function declarations

# NOTES:
# 1. In Python 2.x.x, the 'object' argument is optional and used for "new-style" class declarations
#    (in constrast to "old-style" class declarations that don't pass 'object'
# 2. In Python 3.x.x, all class declarations are "new-style", so passing 'object' is unnecessary.
class Name(object):

    def __init__(self, first, last):
        """ Constructor for the class 'Name'.
        
        Args:
            first (str): A person's first name.
            last (str): A person's last name.
        
        Returns (Name):
            An instance of 'Name'.
        """
            
        self.first = first
        self.last = last

    def full(self):
        """ Returns the full name of a person.
            
        Args:
            N/A
            
        Returns (str):
            A person's full name.
        """
        # NOTE: String technique #1: concatentation
        return self.first + ' ' + self.last
        
    def formal(self, prefix=''):
        """ Returns a person's formal name.
            
        Args:
            N/A
            
        Returns (str):
            A person's formal name.
        """
        
        if len(prefix):
            # NOTE: String technique #2: templating
            return '{} {}'.format(prefix, self.full())
        else:
            return self.full()

    def formal_from_demographics(self, sex='M', is_married=True):
        """ Returns the formal name of a person, based on his/her demographics.
            
        Args:
            N/A
            
        Returns:
            A person's formal name.
        """
        
        prefix = ''

        # NOTE: Built-in function 'upper()' uppercases all of a string's letters.
        if sex.upper() == 'M':
            prefix = 'Mr.'
        elif sex.upper() == 'F' and is_married == True:
            prefix = 'Mrs.'
        elif sex.upper() == 'F' and is_married == False:
            prefix = 'Miss'
        else:
            print("ERROR: Illegal value for one of the arguments: sex={}, is_married={}".format(sex, is_married))

        return self.formal(prefix)

# NOTE: For unit testing purposes, execute as self-test only if being run as a top-level script.
if __name__ == "__main__":
    pass
