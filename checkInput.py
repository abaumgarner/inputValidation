#!/usr/bin/env python3
import re
import fileIO

""" List of acceptable usernames based on file"""
users = fileIO.getUsers()

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