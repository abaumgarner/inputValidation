#!/usr/bin/env python3

""" Author: Aaron Baumgarner
    Created: 12/9/20
    Updated: 12/9/20
    Notes: Various checks on a user's input form
"""
import re
import fileIO

fileName = "users.txt"
""" List of acceptable usernames based on file"""
users = fileIO.getLines(fileName)

""" Checks to see if entered username is in the users list """
def checkUsername(username):
    found = False
    for user in users:
        if user == username:
           found = True
    return found

""" Checks if entered phone number is a phone number """
def checkPhoneNumber(phoneNumber):
    found = False
    phoneNumRegex = re.compile(r'((\d{3}|\(\d{3}\))?(\s|-|\.)?\d{3}(\s|-|\.)\d{4}(\s*(ext|x|ext.)\s*\d{2,5})?)')
    if re.match(phoneNumRegex, phoneNumber):
        found = True
    return found

""" Checks menu option entered is in the menu """
def checkOption(option):
    found = False
    optionRegex = re.compile('[0-4]')
    if re.match(optionRegex, option):
        found = True
    return found

def checkFile(fileName):
    red = "\033[1;31;40m"
    default = "\033[m"
    fin = fileIO.getLines(fileName)
    fileRegex = re.compile("[^\x00-\x21,\x23-\x26,\x28-\x7F]")

    for line in fin:
        if(fileRegex.search(line)):
            loc = str(fin.index(line)+1)

            print(red + "Line " + loc + ": " + default + line + " "+ "\n")
