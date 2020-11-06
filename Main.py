#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 18:07:48 2020

@author: coco
"""
from Classes import Player, printSlow, diceRoll, Assets, actioncard

# data for Player class
stats = Player("Name",
                   {"Austria":               "EU", 
                   "USA":                    "USA", 
                   "Colombia":               "Colombia", 
                   "India":                  "India",
                   "Belgium":                "EU", 
                   "Bulgaria":               "EU", 
                   "Croatia":                "EU", 
                   "Republic of Cyprus":     "EU", 
                   "Czech Republic":         "EU", 
                   "Denmark":                "EU",
                   "Estonia":                "EU", 
                   "Finland":                "EU", 
                   "France":                 "EU", 
                   "Germany":                "EU", 
                   "Greece":                 "EU", 
                   "Hungary":                "EU", 
                   "Ireland":                "EU", 
                   "Italy":                  "EU", 
                   "Latvia":                 "EU", 
                   "Lithuania":              "EU", 
                   "Luxembourg":             "EU", 
                   "Malta":                  "EU", 
                   "Netherlands":            "EU", 
                   "Poland":                 "EU", 
                   "Portugal":               "EU", 
                   "Romania":                "EU", 
                   "Slovakia":               "EU", 
                   "Slovenia":               "EU", 
                   "Spain":                  "EU",
                   "Sweden":                 "EU"})
 
# function for dict junctions
def question(aDictionary):
    userInput = None
    printSlow(aDictionary["question"])
    
    while userInput not in aDictionary["answers"]:   
        printSlow("Write " + aDictionary["answers"][0] + " or " 
                  + aDictionary["answers"][1]+ ".\n")
        userInput = input() 
        
        if userInput == aDictionary["answers"][0]:
            printSlow(aDictionary["results"][0])
            return aDictionary["results"][0]
            
            
        elif userInput == aDictionary["answers"][1]:
            printSlow(aDictionary["results"][1])
            return aDictionary["results"][1]
            
            
        else:
            printSlow(userInput + " is not a Valid Answer.\n")
        
# function for successful level 1
def lvl1up(): 
    printSlow("Congratulations. You made it to your flight on time, and "\
          "will be arriving in Berlin shortly.")
        
       
# function for initial game setting, including name, country & assets 
def game_setting(): 
    printSlow("Welcome to the game!\n")
    stats.setName(str(input(printSlow("Please tell us your name.\n"))))
    printSlow("Welcome to the game, " + stats.getName() + "!\n")
    stats.setCountry(str(input(printSlow("Your nationality will "\
    "determine your gameplay. What is your nationality?\n"))))         

from Dictionaries import L1_1, L1_25, L2_25

# function for gameplay
def game(): 
    game_setting()
    printSlow("You've somehow managed to get German Visa.\n"\
    "How will you proceed to the airport for your flight to Berlin?\n"\
    "Let's see if the luck is in your hands.\n")
    printSlow(input("Press enter to continue."))
    m = diceRoll()
    printSlow("You rolled a " + str(m) + ".\n")
    if m == 1: 
        for x in range(len(L1_1)): 
            y = question(L1_1[x])
            if y == L1_1[0]["results"][0]: 
                printSlow("You went home. Gameover.")
            elif y == L1_1[0]["results"][1]: 
                assets.assetChange(20, 0, 0)
                lvl1up()
    elif (m == 2 or m == 3 or m == 4 or m == 5):  
        for x in range(len(L1_25)):
            y = question(L1_25[x])
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
                    printSlow("You temporarily got stuck in "\
                          "a traffic jam and lost some "\
                        "valuable time.\n")
                    assets.assetChange(0, 30, 0)
                else: 
                    printSlow("The uber driver connects you "\
                             "to a friend of his in Berlin "\
                             "who will happily help you out.\n")
                    assets.assetChange(0, 0, -20)
                lvl1up()
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
                    printSlow("You got lost and lost valuable "\
                                      "time.\n")
                    assets.assetChange(0, 20, 0)
                else: 
                    printSlow("You forgot to validate your "\
                                      "ticket and had to pay a penalty.\n")
                    assets.assetChange(30, 0, 0)
                lvl1up()
    elif m == 6: 
        lvl1up()
    printSlow(". . .", 0.5)
    printSlow("Yay, you arrived in Berlin. But how do you get to your accommodation?")
    
        
    
# data for class specification 
assets = Assets(100, 100, 100)

game()


    
    
    
    