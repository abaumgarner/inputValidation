#!/usr/bin/env python3

""" Author: Aaron Baumgarner
    Created: 12/9/20
    Updarted: 12/9/20
    Notes: Script created to look at user input and check based on various functions. Looks if a username 
        exists in a plain text file (bad practice but practicing python) and will check a phone number entered
        to see if it is formated correctly based on a regex."""
import checkInput

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

""" Main section of the code """
username = promptUsername() 
print(username)
""" phoneNumber = promptPhoneNumber()
print(phoneNumber) """
