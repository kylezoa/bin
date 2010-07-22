#Created by Kyle Cheung with help from "CaZe" Licensed under the MIT/X11 license: http://www.opensource.org/licenses/mit-license.php

#Meh, the outrageous prices of movie concessions

from time import sleep
from Decimal import 

#price and size list
sizes = ['small', 'medium', 'large', 'x-large']
pricePopcorn = [4.75, 5.75, 6.75, 10.75]
priceCoke = [3.25, 3.75, 4.25, 4.75]
price7up = [3, 3.25, 3.75, 4]

#standard function list
def inputSelection():
    return int(input("Please enter the number of your selection: "))

def printInvalidSelection():
    print('\nYou have entered an invalid number, please enter a correct number.\n')
    sleep(0.8)
    
#standardized ask size
def askSize(product, priceList):
    print('What size would you like with that ' + product +'?\n')
    
    #Press <#> for the <size> <product>
    for i in range(len(sizes)):
        print('Press ' + str(i + 1) + ' for the ' + sizes[i] + ' size ($' + str(priceList[i]) + ')')
    
    selection = inputSelection()
    
    #if number > the number of size selection or < 1 it returns 0 that goes to a while statement for each selection
    if (selection > len(priceList)) or (selection < 1):
        return 0
    else:
        print('You have selected the ' + sizes[selection -  1] + ' size ' + product + '.')
        return priceList[selection - 1]

print("\nHi, how many I help you rip you off on expensive beverages and popcorn?\n")

#defining beverage specific functions
def coke():
    selection = askSize('Coke', priceCoke)
    while selection == 0:
        printInvalidSelection()
        askSize('Coke', priceCoke)
    return selection
    
def sevenup():
    selection = askSize('7-up', price7up)
    while selection == 0:
        printInvalidSelection()
        selection = askSize('Coke', priceCoke)
    return selection
    
    
#first popcorn menu asking size
popcornPrice = askSize('popcorn', pricePopcorn)
while popcornPrice == 0:
    sleep(0.8)
    printInvalidSelection()
    popcornPrice = askSize('popcorn', pricePopcorn)
    
#ask general beverage
askBeverageGeneral = '''\nWhat beverage would you like?
                    Press 1 for Coke (no diet for you woosies)
                    Press 2 for 7-Up
                    Press 3 for 7-11 GULP Slurpy ($4.00)
                    Press 4 for bottled water which is worse than tap water.. Aquafina ($8.00)\n'''
    
while True:
    print(askBeverageGeneral)
    beverageGeneral = inputSelection()
    
    if beverageGeneral == 1:
        beveragePrice = coke()
        break
    if beverageGeneral == 2:
        beveragePrice = sevenup()
        break
    if beverageGeneral == 3:
        beveragePrice = 4
        break
    if beverageGeneral == 4:
        beveragePrice = 8
        break
    printInvalidSelection()

#sneaky prices
tax = (popcornPrice + beveragePrice) * 0.0925
surcharge = 2.00

print('\nThe popcorn cost $' + str(popcornPrice) + ' and your beverage cost $' + str(beveragePrice) + ' with a tax of $' + str(tax) + '. Your final total including a $2.00 surcharge is, $' + str(popcornPrice + beveragePrice + tax + surcharge) + '. Thanks for purchasing your grub here!')    

#and that's your average concession stand ladies and gentlemen!