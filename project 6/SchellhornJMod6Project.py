"""
Class: 44-141 Computer Programming I
Author: Jake Schellhorn
Description: Program written to take a file of passwords and encrypt them
as well as take an encrypted file of passwords and decrypt them
Due: April 21, 2022
I pledge that I have completed the programming assignment independently.
I have not copied the code from a student or any source.
I have not given my code to any other student and will not share this code with anyone under any circumstances.
"""
#define functions
def encrypt():
    
    #user input for file to open
    userInputFile = input("Enter file to encrypt: ")
    userOutputFile = input("Enter output file: ")
    
    #open the files
    inputFile= open(userInputFile,"r")
    outputFile = open(userOutputFile,"w")
    
    #create blank list to add to
    dataList=[]
    for line in inputFile:
        
        #use join as a way to then split each password into it's own seperate list
        line='*'.join(line)
        line=line.split('*')
        dataList.append(line)
        
    #create empty string to add to
    dataString=""
    for data in dataList:
        
        #used count and while loop to split each password and start the index over
        count=0
        while (count!=7):
            element= data[count]
            encrypted=ord(element)-count
            dataString+=str(encrypted) +"."
            count+=1
            
    #write to files and close them
    outputFile.write (dataString)
    outputFile.close
    inputFile.close
    print("Encrypted passwords wrote to", userOutputFile)

def decrypt():
    
    #user input for file to open
    userInputFile = input("Enter file to encrypt: ")
    userOutputFile = input("Enter output file: ")
    
    #open files
    inputFile= open(userInputFile,"r")
    outputFile = open(userOutputFile,"w")
    for line in inputFile:
        
        #split string at the '.' so list is created
        line=line.split(".")
        
        #pop the last item in list which is a blank string
        line.pop()
        
    #reversing the encryption
    count=0
    for element in line:
        element=chr(int(element)+count)
        if (count!=6):
            count+=1
        else:
            count=0
        outputFile.write(element)
    outputFile.close
    inputFile.close
    print("Decrypted passwords wrote to", userOutputFile)
    
#main program
    
#print menu and ask for initial user input
print("Welcome to the password encryption program!\nOptions:\n< e for encryption >")
print("< d for decryption >\n< q to exit>")
option = input("Select and option: ")

#sentinel value while loop for functions to run in depending on input option
while (option!="q"):
    if (option=="e"):
        encrypt()
    if (option=="d"):
        decrypt()
        
    #reprompt the menu and input
    print("Options:\n< e for encryption >\n< d for decryption >\n< q to exit>")
    option = input("Select and option: ")
print("Thank you for using our program!")