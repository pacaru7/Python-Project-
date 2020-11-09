# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 12:52:58 2020

@author: ba-li
"""

# Level up messages 

Lvlup = [{
    "lvl1": "Congratulations. You made it to your flight on time, and "\
          "will be arriving in Berlin shortly.\n", 
    "lvl2": ["You got an international SIM card and can access Google "\
             "maps to get to your accomodation.\n" \
              "Yay, you've made it to your accomodation!\n", 
              "Yay, you've made it to your accomodation!\n"], 
    "lvl3": "Your passport photos fit the criteria and you are ready to "\
              "proceed to your appointments.\n"
    
    }]

# Level 1 (transportation) for dice roll of 1
L1_1 = [{
    "question": "Will you go home or pay 20 units of money "\
                "for a new flight?\n",
    "answers" : ["Go home", "Pay"],
    "results" : ["You chose to go home.\n", "You chose to pay 20 units "\
                "of money for a new flight.\n"]      
    }]
    
    
# Level 1 (transportation) for dice roll of 2 to 5
L1_25 = [{ 
     "question": "Will you take an Uber or Public transportation?\n",
     "answers" : ["Uber","Public"],
     "results" : ["You chose Uber.\n","You chose public transportation.\n"], 
     "actioncard_u": ["You temporarily got stuck in a traffic jam and lost "\
                    "some valuable time.\n", "The uber driver connects you "\
                    "to a friend of his in Berlin who will happily help " \
                    "you out.\n"],
    "actioncard_p": ["You got lost and lost valuable "\
                    "time.\n", "You forgot to validate your "\
                    "ticket and had to pay a penalty.\n"]
    }]

# Level 2 (transportation in Berlin) 
L2_25 = [{
     "question": "Will you take an Uber or Public transportation?\n",
     "answers" : ["Uber","Public"],
     "results" : ["You chose Uber.\n","You chose public transportation.\n"], 
     "actioncard_u": ["You temporarily got stuck in a traffic jam and lost "\
                      "some valuable time.\n", "The uber driver has a nephew "\
                      "in Berlin who will help you out in need.\n"], 
     "actioncard_p": ["You got lost and lost valuable time.\n", 
                      "You forgot to validate your "\
                      "ticket and had to pay a penalty.\n"]
    }]

# Level 3 (photo for residence permit/Anmeldung) 
L3_16 = [{
    "x1": "Oops, you've tried to use old photos. They got rejected "\
        "and you wasted time in that attempt.\n",
    "x2": "You went to a photo box but there was a rat that bit you. "\
        "You needed to go the hospital, and lost time and money.\n", 
    "x34": "You used a photo box at some random S-Bahn station close "\
        "to your home and it worked out just fine.""You used a photo "\
        "box at some random S-Bahn station close to your home and it "\
        "worked out just fine.\n",
    "x56": "You went to a professional photo shop."
    
    }]