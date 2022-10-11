#Gasolin
#Programer:Andrew Krusniak
#Version 1.0

"""
Define a fundtion to check our gas gauge and determine based how far
we have until we need gasoline based on an if,elif,else
condition
"""

#import library here
import random
#Gas level function
def gasLevelGauge() :
    gasLevelList =["Empty","Low","Quarter tank","Half tank","Three Quarter Tank","Full Tank"]
    currentGasLevel = random.choice(gasLevelList)
    return currentGasLevel

# Variable calling the gasLevelGauge Function to store value once
gasLevelIndicator = gasLevelGauge()

def gasLevelAlert():
    if gasLevelIndicator == "Empty":
        print("***WARING YOU ARE ON EMPTY***\nCalling Emergency Contact")

gasLevelAlert()