#Created by Kyle Cheung- July 8, 2010. Licensed under the MIT/X11 license: http://www.opensource.org/licenses/mit-license.php

#Meh, the outrageous prices of movie concessions

print("\nHi, how many I help you rip you off on expensive beverages and popcorn?\n")

#because I can't for the life of me find out how to do multi-line print statements

##FIRST MENU-- POPCORN SIZE
#This is the first choice menu for the size of popcorn. It will declare the variable popcornPrice to use for total price.
askPopcornSize = '''What size popcorn do you want?
        Press 1 for Small
        Press 2 for Medium
        Press 3 for Large
        Press 4 for Artery-clogging X-Large
        '''
print(askPopcornSize)

#The user inputs their number, gets changed into an integer and matches up with appropriate variable number. The popcornPrice variable will be used later to determine final price.
popcornSize = int(input("Please select your number: "))
if popcornSize == 1:
    popcornPrice = 4.75
    print('You have chosen the small sized popcorn.')
if popcornSize == 2:
    popcornPrice = 5.75
    print('You have chosen the medium sized popcorn.')
if popcornSize == 3:
    popcornPrice = 6.75
    print('You have chosen the large sized popcorn.')
if popcornSize == 4:
    popcornPrice = 10.75
    print('You have chosen the artery-clogging, x-large sized popcorn. Menial insurance protection is included with this purchase.')    
        
#SECOND MENU-- BEVERAGES
#This is the second choice menu for beverages. In this instance they don't contain second depth menus... yet.

askBeverage = '''\nWhich beverage would you like?
            Press 1 for a Small Coke (no diet for you woosies)
            Press 2 for a Medium Coke
            Press 3 for a Large Coke
            Press 4 for an X-Large Coke
            Press 5 for a Small 7-Up
            Press 6 for a Medium 7-Up
            Press 7 for a Large 7-Up
            Press 8 for a X-Large 7-Up
            Press 9 for your 7-11 GULP Slurpy
            Press 10 for bottled water which is worse than tap water.. Aquafina'''
print(askBeverage)

#User inputs number, blahblahblah, you get the picture from the first prompt.
beverage = int(input("Please select your number: "))
#coke mania
if beverage == 1:
    beveragePrice = 3.25
    print('You have chosen the small coke.')
if beverage == 2:
    beveragePrice = 3.75
    print('You have chosen the medium coke.')
if beverage == 3:
    beveragePrice = 4.25
    print('You have chosen the large coke.')
if beverage == 4:
    beveragePrice = 4.75
    print("You have chosen the x-large coke. Please don't burp a lot while watching in the movie. Thanks.")
#7-up mania
if beverage == 5:
    beveragePrice = 3
    print('You have chosen the small 7-up.')
if beverage == 6:
    beveragePrice = 3.25
    print('You have chosen the medium 7-up.')
if beverage == 7:
    beveragePrice = 3.75
    print('You have chosen the large 7-up.')
if beverage == 8:
    beveragePrice = 4.00
    print('You have chosen the x-large 7-up.')
#and the other beverages
if beverage == 9:
    beveragePrice = 4
    print('You have chosen the slurpy. Slurp steathily.')
if beverage == 10:
    beveragePrice = 8
    print('You have chosen Aquafina. Very bad choice.')

#sneaky prices
tax = (popcornSize + beveragePrice) * 0.0925
surcharge = 2

print('\nThe popcorn cost $', popcornSize, 'and your beverage cost $', beveragePrice, 'with a tax of $', tax, '. Your final total including a $2.00 surcharge is, $', (popcornSize + beveragePrice + tax + surcharge),'. Thanks for purchasing your grub here!')

#and that's your average concession stand ladies and gentlemen!