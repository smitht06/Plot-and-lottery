"""
Anthony Smith
SDEV300
LAB 2
Lottery Generator
"""
#import random library
import random

#method to generate 3 and 4 digit lottery number using for/ in range
def threeDigitLottery():
    for num in range(3):
        print(random.randrange(1,    10), end=' ')
def fourDigitLottery():
    for num in range(4):
        print(random.randrange(1,    10), end=' ')

#set default choice to 0
choice = 0
#while statement to make program repeat until user enters 3
while(choice != 3):
    #print the menu to the user and prompt for input
    print("Please selct one of the following options: ")
    print( "\t 1. Generate 3-digit Lottery Number")
    print( "\t 2. Generate 4-digit Lottery Number")
    print( "\t 3. Exit application")
    #saves user's input in variable
    choice = int(input())
    #use if staements to use methods to generate 3 or four number lottery numbers
    if choice == 3:
        exit(0)
    elif choice == 1:
        threeDigitLottery()
        print("")
    elif choice == 2:
        fourDigitLottery()
        print("")
    


    