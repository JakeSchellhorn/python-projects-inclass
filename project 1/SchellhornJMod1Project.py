"""
*Class: 44-141 Computer Programming I
*Author: Jake Schellhorn
*Description: Module 1 Project Interactive Super Store Program
*Due: January 26 2022
*I pledge that I have completed the programming assignment independently.
*I have not copied the code from a student or any source.
*I have not given my code to any other student and will not share this code
*with anyone under any circumstances.
"""

"""This interactive program let's the user choose an item, the number of items
as well as name a price per unit of the item then prompt for shipping information.
It will then give a bill of information about the purchase.
"""
# Constant Variables
SALES_TAX = 0.042
LIMIT = 100

#Display information and prompt inputs saved as variable
print("***********************************")
print("* Welcome to OnlineSuperStore.com *")
print("***********************************")

item = input("Enter the name of the item you would like to purchase:")
itemPrice = float(input("Enter price of requested item:"))
quantity = int(input("Enter number of requested item:"))
contactName = input("Name of customer:")
address = input("Customer shipping address:")

#Total Price with round function
totalPrice = float(round((itemPrice * quantity) * (1 + SALES_TAX),2))


#Displaying billing information using variables 
print("\n Billing Information\n*********************\n")
print("Contact Name:",contactName)
print("Shipping Address:",address)
print("Item:",item)
print("Quantity:",quantity)

#used format() method and precision specification field to get decimal expressed to hundredths(ch.4)
print("The total bill for your purchase today is ${:.2f}".format(totalPrice,)) 

#Boolean function using relational operators to determine Super Shopper
print("Were you a super shopper today?" , totalPrice >= LIMIT) 

#Ending display
print("\n*************************\n Thank You For Shopping")
