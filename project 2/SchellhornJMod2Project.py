'''
Class: 44-141 Computer Programming I
Author: Jake Schellhorn
Description: Created below is a program to calculate a hospitals burn rate when given user input
Due: February 17, 2022
I pledge that I have completed the programming assignment independently.
I have not copied the code from a student or any source.
I have not given my code to any other student and will not share this code with anyone under any circumstances.
'''
QUANITY_PER_BOX = 200

#Gather Input from user
ppe = str(input("Enter the type of PPE:"))
print("Enter the number that corresponds to the day of the week that you would\nlike to enter PPE for or 0 to quit")
print("1-Mon 2-Tues 3-Wed 4-Thurs 5-Fri:")
day = int(input())

#Sentinal while loop in order to gather input from user 
while (day!=0):
    print("Please enter the number of full boxes of", ppe, "for day",day,":",end="")
    boxes = int(input())
    print("Enter the number that corresponds to the day of the week that you would\nlike to enter PPE for or 0 to quit")
    print("1-Mon 2-Tues 3-Wed 4-Thurs 5-Fri:")
       
#selection structure to store boxes for each day
    if (day==1):
        boxes1 = boxes
    elif (day==2):
        boxes2 = boxes
    elif (day==3):
        boxes3 = boxes
    elif (day==4):
        boxes4 = boxes
    elif (day==5):
        boxes5 = boxes
    day = int(input())    
        
#calculations for final print
average = round((((boxes1-boxes2)+(boxes2-boxes3)+(boxes3-boxes4)+(boxes4-boxes5))/4),2)
ppeLeft = boxes5*QUANITY_PER_BOX
daysLeft = int(boxes5//average)

#print each calculation
print("Average boxes of",ppe, "used per day is:", average)
print("Total number of",ppe, "left:", ppeLeft)
print("Number of days left of",ppe,":", daysLeft)