# ---------------------------------------------------------------------------- #
# Title: Assignment 07
# Description: Scripts to demonstrate how structured error handling works (example 3)
# ChangeLog (Who,When,What):
# SKang,3.1.2022,Created code to complete assignment 07
# ---------------------------------------------------------------------------- #

#Raising Custom Errors
#You need to give me a name longer than 3 characters

try:
    name = str(input("Tell me a name:   "))
    number = len(name)
    if number < 4:
        raise Exception('Give me a longer name!')
except Exception as e:
    print("There was a non-specific error!")
    print("Built-In Python error info: ")
    print(e, e.__doc__, type(e), sep='\n')