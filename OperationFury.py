
#**********************************************************************************
#Import Libraries Here

from time import sleep #We imported the sleep function from the Time library
import random
 #*********************************************************************************
#Welcome Screen                                     
#Developer: Andrew Krusniak                         
#Version: 1.0                                       
# print("\033[1;33m This text is Dark Blue \n")
                                                    
"""                                                 
Our Welcome Screen will start our program letting   
drivers know that the InfoTechCenter OS is Loading  
"""                                                 
print("\n\nWelcome to Operation Fury InfoTech Center")
sleep(2)

for i in range(2):
    print("\nOperation Fury's Operation system is Booting Up")
    print("\nOs Booting up")
    sleep(2)
    print("\033{1;36m os Booting up")
    sleep(2)

#Gasolin
#Programer:Andrew Krusniak
#Version 1.0

"""
Define a fundtion to check our gas gauge and determine based how far
we have until we need gasoline based on an if,elif,else
condition
"""

#import library here

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
    milesToGasStation = round(random.uniform(1,25),2)
    milesToGasStationQuarterTank = round(random.uniform(26,50),2)
    if gasLevelIndicator == "Empty":
        print("***WARING YOU ARE ON EMPTY***\nCalling Emergency Contact")
    elif gasLevelIndicator == "Low":
        print("***WARNING***")
        print("Your gas tank is extremely low, checking Google Maps for the closest gas station")
        print("The closest gas station is",listOFGasStations(),"which is", milesToGasStation ,"miles away.")
    elif gasLevelIndicator == "Quarter tank":
        print("***WARNING***")
        print("Your gas tank is extremely QuarterTank, checking Google Maps for the closest gas station")
        print("The closest gas station is",listOFGasStations(),"which is", milesToGasStationQuarterTank ,"miles away.")
    elif gasLevelIndicator == "half tank":
        print("your gas tank is a half full,you have plenty of gas to get where you are going")
    elif gasLevelIndicator == "Three Quarter Tank":
        print("your gas tank is a Three Quarter Tank,you have plenty of gas to get where you are going")
    else:
        print("Your gas tank is full,you have plenty of gas to get where you are going")


gasLevelAlert()


#Weather
#Developer:Andrew Krusniak
#version 1.0

"""
Create a function for our current weather using the 
random.choice function to determine what the weather is 
picking from a list-using a If,elif & E;se statements 
to check the condition and print a specific print line
"""


#Weather condition list using the random.choice library
#to randomly choose a condition and storing it in its brain

def weather():
    weather_forcast = ["Rain","Snow","Sunny","Cloudy","Foggy","Storming","Icy"]
    weatherCondition = random.choice(weather_forcast)
    return weatherCondition
weatherAlert = weather()
def vrs():
    if weatherAlert == "Icy":
        print("\nvrs has changed your alarm 30 minutes earlier based on the NWS forcast of ",weatherAlert)
        print("VRS will only allow your car to go 30MPH")
    elif weatherAlert == "Snow":
        print("\nvrs has changed your alarm 30 minutes earlier based on the NWS forcast of ",weatherAlert)
        print("VRS will only allow your car to go 50MPH")
    elif weatherAlert == "Rain":
        print("\nvrs has changed your alarm 30 minutes earlier based on the NWS forcast of " ,weatherAlert)
        print("VRS will only allow your car to go 60MPH")
    elif weatherAlert == "Foggy":
        print("\nvrs has changed your alarm 30 minutes earlier based on the NWS forcast of " ,weatherAlert)
        print("VRS will only allow your car to go 60MPH")
    elif weatherAlert == "Rain":
        print("\nvrs has changed your alarm 30 minutes earlier based on the NWS forcast of "  ,weatherAlert)
        print("VRS will only allow your car to go 60MPH")
    elif weatherAlert == "Storming":
        print("\nvrs has changed your alarm 30 minutes earlier based on the NWS forcast of " ,weatherAlert)
        print("VRS will only allow your car to go 50MPH")
    else:
        print("\nThe weather today is,"+weatherAlert, "let's goooo!")

vrs()


