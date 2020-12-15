#!/usr/bin/env python3

""" Author: Aaron Baumgarner
    Created: 12/9/20
    Updated: 12/9/20
    Notes: Opens a file and reads each line into a list. Able to save a new line to the file. Made as
            generic as possible to be used for other projects. 
"""
import os.path

""" Opens and reads in all lines from the users text file. Returns as a list """
def getLines(fileName):
    lines = open(fileName, 'r')
    allLines = []
    while True:
        line = lines.readline()
        allLines.append(line.rstrip('\n'))

        if not line:
            lines.close()
            break
    return allLines

""" Saves a new user to the users text file """
def saveNewLine(user, fileName):
    fout = open(fileName, "a")
    fout.write(user +"\n")
    fout.close()

""" Checks if file given eists """
def checkFileExists(fileName):
    return os.path.isfile(fileName)