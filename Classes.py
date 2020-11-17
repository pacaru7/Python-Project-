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
       
    def setName(self, name): 
        self.__name = name 
    """
    
    Parameters
    ----------
    name : STRING
           String to set name.

    Returns
    -------
    str
        The input is the output.

    """
      
    def getName(self):
        return self.__name
    """
    
    Returns
    -------
    str
        Returns the name as specified in setName().

    """
    
    
    
    def setCountry(self, country):    
        Country = country.lower()
        while Country not in self.__country: 
            printSlow("The game currently does not serve this country. Sorry!\n")
            country = input(printSlow("Let's try again. What is your nationality?\n"))
        else: 
            x = self.__country[Country]
            printSlow(x + " bureaucratic procedures will apply.\n") 
        """
    
        Parameters
        ----------
        country : STRING
              Name of the country, regardless of letter case.
              

        Returns
        -------
        str
            While the string input does not correspond to any 
            objects as specified in the dictionary, the function
            will return a default string. 
        
            If the string input does correspond to any objects 
            as specified in the dictionary, the function is going 
            to set the country and return a default string to 
            confirm the registration of the country.
    
        """
            
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
        printSlow("You have " + str(self.__money) + " money, " + str(self.__time) + " time, " + "and " + str(self.__connection) + " connection units left.\n")
        """
    
        Returns
        -------
        str
            Default string specifying current distribution of 
            assets. 

        """
        
    def assetChange(self, money, time, connection):
        self.__money -= money
        self.__time -= time 
        self.__connection -= connection 
        printSlow("You have " + str(self.__money) + " money, " + str(self.__time) + " time, " + "and " + str(self.__connection) + " connection units left.\n")
        """
    
        Parameters
        ----------
        money       : INT
        time        : INT
        connection  : INT
        

        Returns
        -------
        str
            Default string returning the distribution of assets
            after specified deduction.
            
        """

# data for class specification 
assets = Assets(100, 100, 100)