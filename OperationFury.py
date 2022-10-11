
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

#Weather
#Developer:Andrew Krusniak
#version 1.0

"""
Create a function for our current weather using the 
random.choice function to determine what the weather is 
picking from a list-using a If,elif & E;se statements 
to check the condition and print a specific print line
"""


#Weather condition list using the random.choic library
#to randomly choos a condition and storing it in its brain

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


