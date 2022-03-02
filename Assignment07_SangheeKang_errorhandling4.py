# ---------------------------------------------------------------------------- #
# Title: Assignment 07
# Description: Scripts to demonstrate how structured error handling works (example 4)
# ChangeLog (Who,When,What):
# SKang,3.1.2022,Created code to complete assignment 07
# ---------------------------------------------------------------------------- #

#Creating Custom Exception classes # (source) https://www.programiz.com/python-programming/user-defined-exception
class Error(Exception):
    """  Base class for other errors  """
    def __str__(self):
        return 'Some error message'
#
class NameTooShortError(Exception):
    """The name entered must be longer than four characters!  """
    def __str__(self):
        return 'Name Too Short'

try:
    name = str(input("Tell me a name:   "))
    number = len(name)
    if number < 5:
        raise NameTooShortError('Give me a longer name!')
    else:
        raise Error()
except Exception as e:
    print("There was a non-specific error!")
    print("Built-In Python error info: ")
    print(e, e.__doc__, type(e), sep='\n')
