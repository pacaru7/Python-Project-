# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 14:28:59 2020

This module contains system (?) functions.

"""

# function for printing strings a bit more slowly
import sys, time
def printSlow(sth, x = 0.01):
    for letter in sth:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(x)
    return ""
 
# function for the dice roll
import random
def diceRoll():
  return random.choice([1,2,3,4,5,6])

# function for actioncard 
def actioncard(): 
    return random.randrange(101)