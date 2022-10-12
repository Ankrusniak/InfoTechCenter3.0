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
def listOFGasStations():
       gasStation = ["Shell","Circle K","Marathon","Speedway","Meijer"]
       gasStationNearby = random.choice(gasStation)
       return gasStationNearby
def gasLevelAlert():
    milesToGasStation = round(random.uniform(1, 25), 2) milesToGasStation(1,25)
    MilesToGasStationQuarterTank=round(random.uniform(1, 25), 2)
    if gasLevelIndicator == "Empty":
        print("***WARING YOU ARE ON EMPTY***\nCalling Emergency Contact")
    elif gasLevelIndicator == "Low":
        print("***WARNING***")
        print("Your gas tank is extremely low, checking Google Maps for the closest gas station")
        print("The closest gas station is",listOFGasStations(),"which is", milesToGasStation ,"miles away.")
gasLevelAlert()
