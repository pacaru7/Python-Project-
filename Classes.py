# -*- coding: utf-8 -*-
"""

This module contains the classes for the Player and Asset specifications. 
Below each class, there are the game-specific objects of the class. 

"""
from Functions import *

# class for specification of a player
class Player:
    __helptip = "A player has certain features aka instances: country of origin."

    def __init__(self, name, country): 
        self.__name = name  
        self.__country = country
        
    @classmethod     
    def helptp(cls): 
        return cls.__helptip
       
    def setName(self):
        name = str(input(printSlow("Please tell us your name.\n")))
        name = name.strip()
        if(name==""):
            self.setName()
        else:
            self.__name = name         
    def getName(self):
        return self.__name
    def getCountry(self):
        return self.__country
    
    def setCountry(self, country):
        Country = country.strip().lower()
        if Country not in self.__country: 
            printSlow("The game currently does not serve this country. Sorry!\n")
            country = self.setCountry(input(str(printSlow("Let's try again. What is your nationality?\n"))))
        else: 
            self.__country = self.__country[Country]
            printSlow(self.__country + " bureaucratic procedures will apply.\n") 
            
# data for Player class
stats = Player("Name",
                   {"austria":               "EU", 
                   "usa":                    "USA", 
                   "colombia":               "Colombia", 
                   "india":                  "India",
                   "belgium":                "EU", 
                   "bulgaria":               "EU", 
                   "croatia":                "EU", 
                   "republic of cyprus":     "EU", 
                   "czech republic":         "EU", 
                   "denmark":                "EU",
                   "estonia":                "EU", 
                   "finland":                "EU", 
                   "france":                 "EU", 
                   "germany":                "EU", 
                   "greece":                 "EU", 
                   "hungary":                "EU", 
                   "ireland":                "EU", 
                   "italy":                  "EU", 
                   "latvia":                 "EU", 
                   "lithuania":              "EU", 
                   "luxembourg":             "EU", 
                   "malta":                  "EU", 
                   "netherlands":            "EU", 
                   "poland":                 "EU", 
                   "portugal":               "EU", 
                   "romania":                "EU", 
                   "slovakia":               "EU", 
                   "slovenia":               "EU", 
                   "spain":                  "EU",
                   "sweden":                 "EU"})
   
# class for asset specification 
class Assets: 
    __helptip = "Each player has 100 units of money, time and connection. \n Assets can be spent and earned throughout the game.\n"
    
    def __init__(self, money, time, connection): 
        self.__money = money
        self.__time = time
        self.__connection = connection
    
    def assetStatus(self): 
        printSlow("You have " + str(self.__money) + " money, " + str(self.__time) + " time, " + str(self.__connection) + " connection units left.\n")
        
    def assetChange(self, money, time, connection): 
        tempMoney = self.__money - money
        tempTime = self.__time - time
        tempConnection = self.__connection - connection
        if(tempMoney < 0):
            ## no more money. gg (good game).
            self.__money = 0
        else:
            self.__money -= money
            
        if(tempTime < 0):
            self.__time = 0
        else:
            self.__time -= time
        
        if(tempConnection < 0):
            self.__connection = 0
        else:
            self.__connection -= connection
        self.assetStatus()
        self.check()
        
    def check(self):
        x = 0
        if(self.__money <= 0):
            printSlow("Sorry. You don't have enough money to continue.\n")
            x = 1
        if(self.__time <= 0):
            printSlow("Sorry. You don't have enough time to continue.\n")
            x = 1
        if(self.__connection <= 0):
            printSlow("Sorry. You don't have enough connection to continue.\n")
            x = 1
        if(x!=0):
            printSlow("Game over.")
        
# data for class specification 
assets = Assets(1000, 1000, 1000)