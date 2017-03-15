#!/usr/bin/python
# -*- coding: utf-8 -*-

# NOTE: Import technique #1: all functions (e.g., from 'set_ops.py')
import set_ops

# NOTE: Import technique #2: some functions (e.g., function 'greeting_for_hour' from 'greeting.py')
from greeting import greeting_for_hour
from name import Name

# Function declarations

def demo(name, sex_list=['M'], is_married_list=[True], hour_list=None):
    """ Prints a set of demographically-driven greetings to a particular person.
        
    Args:
        name (Name): An instance of a 'Name'.
        sex_list ([str]): A list of of sex types.
        is_married_list ([bool]): A list of marrital status types.
        hour_list ([bool]): A list of hours of the day.
        
    Returns:
        N/A.
    """
    
    for sex in sex_list:
        for is_married in is_married_list:
            for hour in hour_list:
                name_str = name.formal_from_demographics(sex=sex, is_married=is_married)
                greeting_str = greeting_for_hour(name_str, hour=hour)
                status = 'married' if is_married else 'single'
                print("sex: {},\tis_married: {},\tstatus: {}, \thour: {},\tgreeting: {}".format(sex, is_married, status, hour, greeting_str))

# Demo

# NOTE: For unit testing purposes, execute as self-test only if being run as a top-level script.
if __name__ == "__main__":
    
    # Set variables.
    
    name = Name('Pat', 'Patterson') # Instantiated custom object 'Name'
    sex_list = ['M', 'f', 'NA']     # List of string
    is_married_list = [True, False] # List of booleans
    
    # NOTES:
    # 1. Built-in constant 'None' represents the absent of a value.
    # 2. Built-in function 'range()' generates a list of integers by some step amount
    #    (e.g., start at 0, stop before 36, step by 6).
    #
    hour_list = sorted(list(set_ops.union([None], range(0, 36, 6))))

    demo(name, sex_list=sex_list, is_married_list=is_married_list, hour_list=hour_list)
