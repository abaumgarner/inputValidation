#!/usr/bin/env python3

""" Author: Aaron Baumgarner
    Created: 12/9/20
    Updated: 12/9/20
    Notes: Script created to look at user input and check based on various functions. Looks if a username 
        exists in a plain text file (bad practice but practicing python) and will check a phone number entered
        to see if it is formated correctly based on a regex."""
import checkInput
import fileIO

fileName = "users.txt"

""" Displays a menu to the user """
def displayMenu():
    print("1) Enter Username")
    print("2) Enter Phone Number")
    print("3) Add Username")
    print("4) Check File")
    print("0) Quit")

""" Prompts the user for a menu option and verifies it is a valid option """
def promptOption():
    checkOption = False

    while checkOption != True:
        option = input("Option: ")
        checkOption = checkInput.checkOption(option)

        if checkOption == False:
            print("Option " + option + " is not in the menu. Please try again.\n")
            displayMenu()
    return option

""" Prompts the user to enter a username """
def promptUsername():
    userCheck = False

    while userCheck != True:
        username = input("Enter username: ")
        userCheck = checkInput.checkUsername(username)

        if userCheck == False:
            print("Username " + username + " does not exist. Please try again or create a new account.")
        else:
            return "User " + username + " is allowed to login."

""" Prompts the user for a phone number """
def promptPhoneNumber():
    phoneCheck = False

    while phoneCheck != True:
        phoneNumber = input("Enter Phone Number: ")
        phoneCheck = checkInput.checkPhoneNumber(phoneNumber)
        
        if phoneCheck == False:
            print("Phone number entered is not in the standard US phone format. Please try again.")
        else:
            return "Phone Number: " + phoneNumber

""" Prompts for a new user and will check to see if user exists in the file already """
def promptNewUser():
    newUserCheck = True

    while newUserCheck:
        newUser = input("Enter new Username: ")
        newUserCheck = checkInput.checkUsername(newUser)

        if newUserCheck:
            print(newUser + " already exists. Please enter a new username.")

    fileIO.saveNewLine(newUser, fileName)
    return newUser + " has been entered"

""" Prompts the user for a file name """
def promptFileName():
    exist = False
    while exist != True:
        fileName = input("File Name: ")
        exist = fileIO.checkFileExists(fileName)
        if exist == False:
            print("File " + fileName + " wasn't found. Please try again.\n")
    checkInput.checkFile(fileName)

""" Executes the menu option after it has been varified """
def executeOption(option):
    if option == 1:
        username = promptUsername() 
        print(username)
    elif option == 2:
        phoneNumber = promptPhoneNumber()
        print(phoneNumber)
    elif option == 3:
        newUser = promptNewUser()
        print(newUser)
    elif option == 4:
        promptFileName()
    elif option == 0:
        exit()
    else:
        print("Not sure how you got here..... o.O")

""" Main section of the code """
displayMenu()
option = int(promptOption())
executeOption(option)

exit()