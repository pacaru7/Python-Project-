#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module contains the code for the internal game structure.
It starts off with the setting of game parameters, the player features 
as specified in Classes.py, and continues with the specific game level
structures.

"""
from Classes import *
from Dictionaries import *
from Functions import *
   
       
def game_setting(): 
    """
    

    Returns
    -------
    This function sets the player parameters, using the methods setName()
    and setCountry() from the class Player() in the Classes.py file. It does 
    not return any value but is designed to take as input the name and the 
    country of the player. 
    
    The name of the player can be any type of string or even number 
    constellation. The country of the player ignores letter case and can 
    only take the country name (e.g. Germany) as opposed to the nationality
    (German) as input.
    
    The objects of the class are specified in Classes.py file.

    """
    printSlow("Welcome to the game!\n")
    stats.setName(str(input(printSlow("Please tell us your name.\n"))))
    printSlow("Welcome to the game, " + stats.getName() + "!\n")
    stats.setCountry(str(input(printSlow("Your nationality will "\
    "determine your gameplay. What is the country of your nationality?\n"))))         

# function for gameplay
def game(): 
    """
    

    Returns
    -------
    This function contains aside from the setting of the game parameters 
    all the existing game pathways.

    """
    game_setting()
    printSlow("You've somehow managed to get German Visa.\n"\
    "How will you proceed to the airport for your flight to Berlin?\n"\
    "Let's see if the luck is in your hands.\n")
    printSlow(input("Press enter to continue."))

# Level 1: transportation from residence to airport 
    m = diceRoll()
    printSlow("You rolled a " + str(m) + ".\n")
    if m == 1: 
        for x in range(len(L1_1)): 
            y = question(L1_1[x])
            if y == L1_1[0]["results"][0]: 
                printSlow("You went home. Gameover.")
            elif y == L1_1[0]["results"][1]: 
                assets.assetChange(20, 0, 0)
                printSlow(Lvlup[0]["lvl1"])
    elif (m == 2 or m == 3 or m == 4 or m == 5):  
        for x in range(len(L1_25)):
            y = question(L1_25[x])
            # Uber
            if y == L1_25[0]["results"][0]: 
                if m == 2: 
                    assets.assetChange(45, 50, -30)
                elif m == 3: 
                    assets.assetChange(40, 30, -20) 
                elif m == 4: 
                    assets.assetChange(35, 20, -10)
                else: 
                    assets.assetChange(30, 10, -5)
                if actioncard() > 50: 
                    printSlow(L1_25[0]["actioncard_u"][0])
                    assets.assetChange(0, 30, 0)
                else: 
                    printSlow(L1_25[0]["actioncard_u"][1])
                    assets.assetChange(0, 0, -20)
                printSlow(Lvlup[0]["lvl1"])
            # Public transportation
            elif y == L1_25[0]["results"][1]:
                if m == 2: 
                    assets.assetChange(5, 20, 0)
                elif m == 3: 
                    assets.assetChange(5, 15, 0)
                elif m == 4: 
                    assets.assetChange(5, 10, 0)
                else: 
                    assets.assetChange(5, 5, 0)
                if actioncard() > 50: 
                    printSlow(L1_25[0]["actioncard_p"][0])
                    assets.assetChange(0, 20, 0)
                else: 
                    printSlow(L1_25[0]["actioncard_p"][1])
                    assets.assetChange(30, 0, 0)
                printSlow(Lvlup[0]["lvl1"])
    elif m == 6: 
        printSlow(Lvlup[0]["lvl1"])
    printSlow("\n. . .\n", 0.5)
    printSlow("Yay, you arrived in Berlin. But how do you get to your accommodation?")
    printSlow(input("Press enter to continue."))

# Level 2: transportation from airport to accommodation 
    m = diceRoll()
    printSlow("You rolled a " + str(m) + ".\n")
    if m == 1: 
        printSlow("For some reason, you felt like walking, so you walked all "\
                  "the way from the airport to your accommodation.\n") 
        assets.assetChange(0, 60, 0)
        printSlow(Lvlup[0]["lvl2"])
    elif (m == 2 or m == 3 or m == 4 or m == 5):  
        for x in range(len(L2_25)):
            y = question(L2_25[x])
            if y == L2_25[0]["results"][0]:
                if m == 2: 
                    assets.assetChange(45, 40, -30)
                elif m == 3: 
                    assets.assetChange(40, 30, -20) 
                elif m == 4: 
                    assets.assetChange(35, 20, -10)
                else: 
                    assets.assetChange(30, 10, -5)
                if actioncard() > 50: 
                    printSlow(L2_25[0]["actioncard_u"][0])
                    assets.assetChange(0, 30, 0)
                else: 
                    printSlow(L2_25[0]["actioncard_u"][1])
                    assets.assetChange(0, 0, -20)
                printSlow(Lvlup[0]["lvl2"])
            elif y == L2_25[0]["results"][1]:
                if m == 2: 
                    assets.assetChange(5, 20, 0)
                elif m == 3: 
                    assets.assetChange(15, 15, 0)
                elif m == 4: 
                    assets.assetChange(10, 10, 0)
                else: 
                    assets.assetChange(5, 5, 0)
                if actioncard() > 50: 
                    printSlow(L2_25[0]["actioncard_p"][0])
                    assets.assetChange(0, 20, 0)
                else: 
                    printSlow(L2_25[0]["actioncard_p"][1])
                    assets.assetChange(30, 0, 0)
                printSlow(Lvlup[0]["lvl2"])
    elif m == 6: 
        printSlow(Lvlup[0]["lvl2"])
# Possibility of adding bank account, health insurance as extra levels 
# Level 3: Photos for residence permit/Anmeldung 
    printSlow("You've settled in for a couple days. But for you to stay and "\
              "become a permanent non-tourist resident, you need the residence "\
              "permit and appropriate passport photos for it.\n")
    printSlow(input("Press enter to continue."))
    m = diceRoll()
    printSlow("You rolled a " + str(m) + ".\n")
    if m == 1: 
        printSlow(L3_16[0]["x1"])
        assets.assetChange(0, 40, 0)
    if m == 2: 
        printSlow(L3_16[0]["x2"])
        assets.assetChange(10, 30, 0)
    if (m == 3 or m == 4): 
        printSlow(L3_16[0]["x34"])
        assets.assetChange(5, 0, 0)
        printSlow(Lvlup[0]["lvl3"])
    if (m == 5 or m == 6): 
        printSlow(L3_16[0]["x56"])
        assets.assetChange(20, 0, 0)
    printSlow(Lvlup[0]["lvl3"])
# Paths are yet to be finished !!
# Level 4: Anmeldung or Residence Permit 
    x = printSlow(input("Which one do you want to do first: " \
                        "Anmeldung or residence permit?\n"))
    if x.lower() == "anmeldung": 
        pass
    elif x.lower() == "residence permit": 
        pass 
    

game()


    
    
    
    