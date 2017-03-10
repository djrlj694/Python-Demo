#!/usr/bin/python
# -*- coding: utf-8 -*-

# Function declarations

# NOTES:
# 1. In Python 2.x.x, the 'object' argument is optional and used for "new-style" class declarations
#    (in constrast to "old-style" class declarations that don't pass 'object'
# 2. In Python 3.x.x, all class declarations are "new-style", so passing 'object' is unnecessary.
class Name(object):

    def __init__(self, first, last):
        self.first = first
        self.last = last

    def full(self):
        # NOTE: String technique #1: concatentation
        return self.first + ' ' + self.last
        
    def formal(self, prefix=''):
        if len(prefix):
            # NOTE: String technique #2: templating
            return '{} {}'.format(prefix, self.full())
        else:
            return self.full()

    def formal_from_demographics(self, sex='M', is_married=True):
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

