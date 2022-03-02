# ---------------------------------------------------------------------------- #
# Title: Assignment 07
# Description: Scripts to demonstrate how structured error handling works (example 1)
# ChangeLog (Who,When,What):
# SKang,3.1.2022,Created code to complete assignment 07
# ---------------------------------------------------------------------------- #

#Structured error handling (Try-Except)
#Using the Exception class; (source) https://www.kite.com/python/examples/3538/exceptions-catch-an-%60indexerror%60

listData = [5, 10, 15]
try:
    print(listData[4])
except Exception as e:
    print("There was an error!")
    print("Built-In Pythons error info: ")
    print(e)
    print(type(e))
    print(e.__doc__)
    print(e.__str__())