# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 15:59:08 2020

This module contains the classes for the Player and Asset specifications. 

"""
from Functions import *

# class for specification of a player
class Player:
    __helptip = "A player has certain features aka instances: country of origin."

    def __init__(self, name, country): 
        self.__name = name  
        self.__country = country
    """
    
    This class prescribes and stores the player features: 
        1. Name 
        2. Country of origin 
    Country objects are stored in Dictionaries.py.

    """ 
     
    @classmethod     
    def helptp(cls): 
        return cls.__helptip
       
    def setName(self, name): 
        self.__name = name 
    def getName(self):
        return self.__name
    
    def setCountry(self, country):
        while country not in self.__country: 
            printSlow("The game currently does not serve this country. Sorry!\n")
            country = input(printSlow("Let's try again. What is your nationality?\n"))
        else: 
            x = self.__country[country]
            printSlow(x + " bureaucratic procedures will apply.\n") 
            
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
   
# class for asset specification 
class Assets: 
    __helptip = "Each player has 100 units of money, time and connection. \n Assets can be spent and earned throughout the game.\n"
    
    def __init__(self, money, time, connection): 
        self.__money = money
        self.__time = time
        self.__connection = connection
    
    def assetStatus(self): 
        printSlow("You have " + str(self.__money) + " money, " + str(self.__time) + " time, " + "and " + str(self.__connection) + " connection units left.\n")
        
    def assetChange(self, money, time, connection): 
        self.__money -= money
        self.__time -= time 
        self.__connection -= connection 
        printSlow("You have " + str(self.__money) + " money, " + str(self.__time) + " time, " + "and " + str(self.__connection) + " connection units left.\n")

# data for class specification 
assets = Assets(100, 100, 100)