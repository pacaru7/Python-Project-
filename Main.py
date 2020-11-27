#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module contains the code for the internal game structure.
It starts off with the setting of game parameters, the player features 
as specified in Classes.py, and continues with the specific game level
structures.
Things we still have to figure out: 
    - Default option when you don't have any units left to expend. 
"""

from Functions import *
from Level import *   
       
# function for gameplay
def game(): 
    """
    Returns
    -------
    This function contains aside from the setting of the game parameters 
    all the existing game pathways.

    """
    game_setting()
    level0()
    level1() 
    level2()
# Possibility of adding bank account, health insurance as extra levels 
    level3()
    level4() 

    
game()


    
    
    
    