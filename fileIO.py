#!/usr/bin/env python3

""" Opens and reads in all lines from the users text file. Returns as a list """
def getUsers():
    users = open("users.txt", 'r')
    allUsers = []
    while True:
        user = users.readline()
        allUsers.append(user.rstrip('\n'))

        if not user:
            users.close()
            break
    return allUsers