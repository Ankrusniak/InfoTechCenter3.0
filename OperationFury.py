#Welcome Screen
#Developer: Mr.Lange
#Version: 1.0

"""
Our Welcome Screen will start our program letting
drivers know that the InfoTechCenter OS is Loading 
"""

#Import Libraries Here

from time import sleep #We imported the sleep function from the Time library


print('\n\033[1;31;0"m Welcome to Operation Fury InfoTech Center')
sleep(2)
print('\n \033[1;28;0"mOperation fury System is Booting Up\033[0m')

for i in range(2):
    print("\033{1;36m os Booting up")
    sleep(5)
    print("Os Booting up")
