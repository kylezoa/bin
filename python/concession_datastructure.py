#Created by Kyle Cheung with help from "CaZe" Licensed under the MIT/X11 license: http://www.opensource.org/licenses/mit-license.php

#Meh, the outrageous prices of movie concessions

#price and size list
sizes = ['small', 'medium', 'large', 'x-large']
pricePopcorn = [4.75, 5.75, 6.75, 10.75]
priceCoke = [3.25, 3.75, 4.25, 4.75]
price7up = [3, 3.25, 3.75, 4]

#standard function list
def inputSelection():
    return int(input("Please enter the number of your selection: "))

def printInvalidSelection():
    print('You have entered an invalid number, please enter a correct number.')
    
#standardized ask size
def askSize(product, priceList):
    print('What size would you like with that,' + product +,'?\n')
    
    #Press <#> for the <size> <product>
    for i in range(len(sizes))
        print('Press' + str(i + 1) + 'for the' + sizes[i] + 'size ($' + str(priceList[i]) + ')')
    
    selection = inputSelection()
    
    #if number > the number of size selection or < 1 it returns 0 that goes to a while statement for each selection
    if (selection > len(sizes)) or (selection < 1):
        return 0
    else:
        print('You have selected the ' + sizes[input -  1] + product + '.')
        return pricelist[input - 1]

print("\nHi, how many I help you rip you off on expensive beverages and popcorn?\n")

popcornPrice = size('popcorn', pricePopcorn)


