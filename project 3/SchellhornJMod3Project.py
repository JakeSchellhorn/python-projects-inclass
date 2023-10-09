"""
Class: 44-141 Computer Programming I
Author: Jake Schellhorn
Description:Gather input from user of a job title and use a randomly generated salary to calculate either the min max or average
depending on what the user wants.
Due: March 2, 2022

I pledge that I have completed the programming assignment independently.
I have not copied the code from a student or any source.
I have not given my code to any other student and will not share this code with anyone under any circumstances.
"""
import random

#declare variables for calculations
total=0
average=0
count=0

#gather input for which calculation to print
print("Determine the minimum, maximum, or average of the minimum salry of different tech salaries.\nWhat would you like to calculate?")
calculation=int(input("Enter 1 for min, 2 for max, 3 for average, or 0 to quit:"))

#sentinel value while loop so 0 exits loop
while(calculation!=0):
    #gather input and generate random salary for input
    jobTitle=input("Enter the job title name or quit to exit:")
    salary=random.randint(10000, 199999)
    
    #baseline min and max values
    minimum = salary
    maximum = salary
    
    #nested sentinel value while loop so quit exits and calculate min and max
    while(jobTitle!="quit"):
        print("The salary is:", salary)
        if (salary<minimum):
            minimum = salary
        if (salary>maximum):
            maximum = salary
        #update variables for calculations
        total+=salary
        count+=1
        
        #update variables
        jobTitle=input("Enter the job title name or quit to exit:")
        salary=random.randint(10000, 199999)
        
    if (count!=0):
            average = round((total/count),2)
    
    #if/elif statement so the right print will output
    if (calculation==1):
        print("The minimum wage of the jobs entered is:",minimum)
    elif(calculation==2):
        print("The maximum wage of the jobs entered is:", maximum)
    elif(calculation==3):
        print("The average of the jobs entered is:", average)
    #update priming read for original loop if the user wants to continue or quit
    print("Determine the minimum, maximum, or average of the minimum salry of different tech salaries.\nWhat would you like to calculate?") 
    calculation=int(input("Enter 1 for min, 2 for max, 3 for average, or 0 to quit:"))
print("Thank You")