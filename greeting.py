#!/usr/bin/python
# -*- coding: utf-8 -*-

# Function declarations

def greeting(greeting, name):
    # NOTES:
    # 1. String technique #3: %-interpolation
    # 2. Built-in function 'title()' capitalizes only the first letter of a string.
    return "%s, %s!" % (greeting.title(), name)

def greeting_for_hour(name, hour=None):
    greeting_str = 'hello'

    if hour != None:
        # NOTE: Binary operator '%' computes the remainder (i.e., modular arithmetic).
        new_hour = hour%24

        if new_hour >= 0 and new_hour < 12:
            greeting_str = 'good morning'
        elif new_hour >= 12 and new_hour < 16:
            greeting_str = 'good afternoon'
        elif new_hour >= 16 and new_hour < 21:
            greeting_str = 'good evening'
        elif new_hour >= 21:
            greeting_str = 'good night'

    return greeting(greeting_str, name)
