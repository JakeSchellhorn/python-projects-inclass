"""
Class: 44-141 Computer Programming I
Author: Jake Schellhorn
Description: Program for project that uses functions to search for info in a .txt file and
returns info in main program
Due: April 6, 2022
I pledge that I have completed the programming assignment independently.
I have not copied the code from a student or any source.
I have not given my code to any other student and will not share this code with anyone under
any circumstances.
"""
#define functions
def fileReader(lastName, fileInput):
    #read lines in file
    for line in fileInput:
        lower=line.lower()
        name1=lower.find(lastName)
        if(name1!=-1):
            break
    if(name1==-1):
        return name1
    else:
        #.split() to return list that will be used later to access each piece of info
        studentInfo=line.split()
        return studentInfo
#functions to return each bit of student information        
def firstName (studentInfo):
    return studentInfo[0]

def lastName(studentInfo):
    return studentInfo[1]
    
def gpa(studentInfo):
    return studentInfo[2]
    
def creditHours(studentInfo):
    return studentInfo[3]
    
def mealPlan(studentInfo):
    return studentInfo[4]

def advisor(studentInfo):
    return studentInfo[5]
#function with if statment to return a string according to the information provided in the .txt file
def enrollmentSubmit(studentInfo):
    enrollment= studentInfo[6]
    if(enrollment=="True"):
        return studentInfo[0] + " has enrolled"
    if(enrollment=="False"):
        return studentInfo[0] + " has not enrolled"


#Main Program

print("Welcome to the Enrollment Center!\nPlease enter a last name or enter 0 to stop ", end="")
name=input("program: ").lower()
print()
#sentinel value while loop
while(name!="0"):
    #open file in while loop so file reading resets each time
    inputFile = open("studentinfo.txt","r")
    info=fileReader(name,inputFile)
    if(info!=-1):
        #use concatenation and the above functiosn to piece together information
        print(str(firstName(info)) +" " + str(lastName(info)) + " has a " + str(gpa(info)) + " gpa")
        print("Credit Hours: " + str(creditHours(info)))
        print("Meal Plan: " + str(mealPlan(info)))
        print(str(firstName(info)) + "'s advisor is " + str(advisor(info)))
        print(str(enrollmentSubmit(info)))
    else:
        print("Student not found")
    #gather user input again to update variable
    name=input("\nPlease enter a last name or enter 0 to stop program: ").lower()
