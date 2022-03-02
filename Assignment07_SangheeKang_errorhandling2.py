# ---------------------------------------------------------------------------- #
# Title: Assignment 07
# Description: Scripts to demonstrate how structured error handling works (example 2)
# ChangeLog (Who,When,What):
# SKang,3.1.2022,Created code to complete assignment 07
# ---------------------------------------------------------------------------- #

#Catching Specific Exceptions
listData = [5, 10, 15]
try:
    print(listData[4])
except IndexError as e:
    print("Please select an index in the range!")
    print("Built-In Python error info: ")
    print(e, e.__doc__, type(e), sep='\n')
except Exception as e:
    print("There was a non-specific error!")
    print("Built-In Python error info: ")
    print(e, e.__doc__, type(e), sep='\n')