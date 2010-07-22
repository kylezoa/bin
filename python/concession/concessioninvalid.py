#Created by Kyle Cheung- July 8, 2010. Licensed under the MIT/X11 license: http://www.opensource.org/licenses/mit-license.php

#Meh, the outrageous prices of movie concessions

#importing sleep so people can read on the bottom of the prompt that their selection was invalid
from time import sleep

print("\nHi, how many I help you rip you off on expensive beverages and popcorn?\n")

#because I can't for the life of me find out how to do multi-line print statements

def inputSelection():
    return int(input("Please enter the number of your selection: "))

def printInvalidSelection():
    print('You have entered an invalid number, please enter a correct number.')
    sleep(0.8)
    
##FIRST MENU-- POPCORN SIZE
#This is the first choice menu for the size of popcorn. It will declare the variable popcornPrice to use for total price.
askPopcornSize = '''What size popcorn do you want?
        Press 1 for Small
        Press 2 for Medium
        Press 3 for Large
        Press 4 for Artery-clogging X-Large
        '''
print(askPopcornSize)

#The user inputs their number, gets changed into an integer and matches up with appropriate variable number. If no proper variable is used it goes back up to the while loop. The popcornPrice variable will be used later to determine final price.

while True:
    popcornSize = inputSelection()
    
    if popcornSize == 1:
        popcornPrice = 4.75
        print('You have chosen the small sized popcorn.')
        break
    if popcornSize == 2:
        popcornPrice = 5.75
        print('You have chosen the medium sized popcorn.')
        break
    if popcornSize == 3:
        popcornPrice = 6.75
        print('You have chosen the large sized popcorn.')
        break
    if popcornSize == 4:
        popcornPrice = 10.75
        print('You have chosen the artery-clogging, x-large sized popcorn. Menial insurance protection is included with this purchase.')
        break
    printInvalidSelection()
        
#SECOND MENU -- GENERAL BEVERAGE -> SIZE

askGeneralBeverage = '''\nWhat beverage would you like?
                Press 1 for Coke (no diet for you woosies)
                Press 2 for 7-Up
                Press 3 for 7-11 GULP Slurpy ($4.00)
                Press 4 for bottled water which is worse than tap water.. Aquafina ($8.00)\n'''
        
print(askGeneralBeverage)

#User inputs number, goes to more indepth menus to get proper beverage size.

while True:

    beverageGeneral = inputSelection()

    #coke mania
    if beverageGeneral == 1:
        askBeverageSizeCoke = '''\nWhich size would you like for that Coke?
                        Press 1 for the small size ($3.25)
                        Press 2 for the medium size ($3.75)
                        Press 3 for the large size ($4.25)
                        Press 4 for the x-large size ($4.75)\n'''

        print(askBeverageSizeCoke)

        while beverageSize == inputSelection():

            if beverageSize == 1:
                beveragePrice = 3.25
                print('You have selected the small size Coke.')
                break
            if beverageSize == 2:
                beveragePrice = 3.75
                print('You have selected the medium size Coke.')
                break
            if beverageSize == 3:
                beveragePrice = 4.25
                print('You have selected the large size Coke.')
                break
            if beverageSize == 4:
                beveragePrice = 4.75
                print('You have selected the x-large size Coke. Please burp responsibly.')
                break
           
            printInvalidSelection()

    #7-up mania
    while beverageGeneral == 2:
        askBeverageSize7up = '''\nWhich size would you like for that 7-up?
                        Press 1 for the small size ($3.00)
                        Press 2 for the medium size ($3.25)
                        Press 3 for the large size ($3.75)
                        Press 4 for the x-large size ($4.05)\n'''
        print(askBeverageSize7up)

        beverageSize = inputSelection()

        if beverageSize == 1:
            beveragePrice = 3
            print('You have chosen the small size 7-up.')
            break
        if beverageSize == 2:
            beveragePrice = 3.25
            print('You have chosen the medium size 7-up.')
            break
        if beverageSize == 3:
            beveragePrice = 3.75
            print('You have chosen the large size 7-up.')
            break
        if beverageSize == 4:
            beveragePrice = 4.05
            print('You have chosen the x-large size 7-up.')
            break
        else:
            printInvalidSelection()
            continue

    #slurpy
    if beverageGeneral == 3:
        beveragePrice = 4
        print('You have chosen the slurpy. Slurp steathily.')
        break

    #aquafina
    if beverageGeneral == 4:
        beveragePrice = 8
        print('You have chosen Aquafina. Very bad choice. You know how much plastic goes into these bottles?')
        break
        
    printInvalidSelection()

#sneaky prices
tax = (popcornPrice + beveragePrice) * 0.0925
surcharge = 2

print('\nThe popcorn cost $', popcornPrice, 'and your beverage cost $', beveragePrice, 'with a tax of $', tax, '. Your final total including a $2.00 surcharge is, $', (popcornPrice + beveragePrice + tax + surcharge),'. Thanks for purchasing your grub here!')

#and that's your average concession stand ladies and gentlemen!