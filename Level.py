# -*- coding: utf-8 -*-
"""
This module contains all the level structures. 


"""
from Functions import *
from Classes import * 
from Dictionaries import *

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
    stats.setName()
    printSlow("Welcome to the game, " + stats.getName() + "!\n")
    stats.setCountry(str(input(printSlow("Your nationality will "\
    "determine your gameplay. What is the country of your nationality?\n")))) 
        
def level0():
    """
    

    Returns
    -------
    This function checks whether the country of origin was Colombia or India
    and returns a character string related to the acquisition of German Visa, 
    and contains the transition strings from the game setup to the game itself.

    """
    
    countryName = stats.getCountry()
    countryVisas = [ 'Colombia','India']
    if(countryName in countryVisas):
        printSlow("You've somehow managed to get German Visa.\n")
        printSlow(input("Press enter to continue.\n"))
    printSlow("How will you proceed to the airport for your flight to Berlin?\n"\
    "Let's see if the luck is in your hands.\n")
    diceRollPrompt()
    
def level1(): 
    """
    Returns
    -------
    This function returns the plot structure for the first level, 
    transportation from the player's current destination to the airport.
    """
    
    # Level 1: transportation from residence to airport 
    m = diceRoll()
    ##m=
    printSlow("You rolled a " + str(m) + ".\n")
    if m == 1: 
        ##for x in range(len(L1_1)): 
        ## just one question
            y = question(L1_1[0])
            if y == L1_1[0]["results"][0]: 
                printSlow(input("You went home. Gameover. Press ENTER to end the game"))
            elif y == L1_1[0]["results"][1]: 
                assets.assetChange(20, 0, 0)
    elif (m == 2 or m == 3 or m == 4 or m == 5):  
        # for not necessary. just one question...
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
                if actioncard()% 2 == 0:  
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
                if actioncard()%2 == 0: 
                    printSlow(L1_25[0]["actioncard_p"][0])
                    assets.assetChange(0, 20, 0)
                else: 
                    printSlow(L1_25[0]["actioncard_p"][1])
                    assets.assetChange(30, 0, 0)
                printSlow(Lvlup[0]["lvl1"])
        ## if it is 6 continue here
    elif m == 6: 
        printSlow(Lvlup[0]["lvl1"])
    printSlow("\n. . .\n", 0.5)
    printSlow("Yay, you arrived in Berlin. But how do you get to your accommodation?")
    diceRollPrompt()
    
def level2():
    """
    Returns
    -------
    This function returns the plot structure for the second level, 
    transportation from the airport to the player's accommodation in Germany.
    """
    
    m = diceRoll()
    printSlow("You rolled a " + str(m) + ".\n")
    if m == 1: 
        printSlow("For some reason, you felt like walking, so you walked all "\
                  "the way from the airport to your accommodation.\n") 
        assets.assetChange(0, 60, 0)
        printSlow(Lvlup[0]["lvl2"][1])
    elif (m == 2 or m == 3 or m == 4 or m == 5):  
        # for not necessary. just one question...
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
                printSlow(Lvlup[0]["lvl2"][1])
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
                printSlow(Lvlup[0]["lvl2"][1])
    elif m == 6: 
        printSlow(Lvlup[0]["lvl2"][0])
    printSlow("You've settled in for a couple days. But for you to stay and "\
              "become a permanent non-tourist resident, you need the residence "\
              "permit and appropriate passport photos for it.\n")
    diceRollPrompt()
    
def level3(): 
    """
    Returns
    -------
    This function returns the plot structure for the third level, 
    acquisition of appropriate photos for the bureaucratic procedures to 
    follow.
    """
    
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
    if (m == 5 or m == 6): 
        printSlow(L3_16[0]["x56"])
        assets.assetChange(20, 0, 0)
    printSlow(Lvlup[0]["lvl3"])
    # Paths are yet to be finished !!
    
def level4(): 
    """
    Returns
    -------
    This function returns the plot structure for the fourth level. It
    asks the player to decide between the Anmeldung or residence permit 
    process. Either option will be followed by the other one. Essentially, 
    plot structures are activated.
    """
    
    u = input(printSlow("Which one do you want to do first: " \
                        "Anmeldung or residence permit?\n"))
    if u.lower() == "residence permit": 
        Residencepermit() 
        diceRollPrompt()
        Anmeldung()
        printSlow(input("You won, press ENTER to end the game"))
    elif u.lower() == "anmeldung": 
        Anmeldung()
        diceRollPrompt()
        Residencepermit()
        printSlow(input("You won, press ENTER to end the game"))
    else:
        printSlow(u + " is not a valid answer.")
        level4()
    
   
    
def Anmeldung():
    """
    Returns
    -------
    This function returns the plot structure for the fourth level, 
    registration at local Bürgeramt, also called Anmeldung.
    """
    
    printSlow("Time to get your Anmeldung!\n")
    m = diceRoll()
    printSlow("You rolled a " + str(m) + ".\n")
    if (m == 1 or m == 2): 
        printSlow(L4_1[0]["x12"]) 
        assets.assetChange(50, 50, 50)
        if actioncard() > 5: 
            printSlow(L4_1[0]["actioncard_12"])
            assets.assetChange(0, 0, -20)
    elif (m == 3 or m == 4):  
        printSlow(L4_1[0]["x34"])
        assets.assetChange(50, 50, 50)
         ## 25 % should be 100-25
        if actioncard() > 75: 
            printSlow(L4_1[0]["actioncard_34"][0])
            assets.assetChange(0, 100, 0)
        elif actioncard() > 70: 
            printSlow(L4_1[0]["actioncard_34"][1])
            assets.assetChange(0, 50, 0)
    elif (m == 5 or m == 6): 
            printSlow(L4_1[0]["x56"])
            assets.assetChange(50, 50, 50)
    printSlow("Anmeldung finished.")
    
# not completed! 

def Residencepermit():   
    """
    Returns
    -------
    This function returns the plot structure for the fourth level, 
    acquisition residence permit.
    """
    
    printSlow("Time to get your residence permit!\n")      
    m = diceRoll()
    printSlow("You rolled a " + str(m) + ".\n")
    if (m == 1):         
        printSlow(L4_2[0]["x1"]) 
        #assets.assetChange(50, 50, 50)
    elif (m == 2):          
        printSlow(L4_2[0]["x2"])
        #assets.assetChange(50, 50, 50)
    elif (m == 3): 
        printSlow(L4_2[0]["x3"])
        #assets.assetChange(50, 50, 50)
    elif (m == 4 or m == 5 or m == 6): 
        printSlow(L4_2[0]["x4_6"])
    printSlow("Residence permit obtained.")
    
    
    
    