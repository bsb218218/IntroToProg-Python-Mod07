# ---------------------------------------------------------------------------- #
# Title: Assignment 07
# Description: Scripts to demonstrate how Pickling works (examples)
# ChangeLog (Who,When,What):
# SKang,3.1.2022,Created code to complete assignment 07
# ---------------------------------------------------------------------------- #

#Pickling
import pickle  # This imports code from another code file!

strTask = str(input("Task:  "))
strTime = str(input("Time:  "))
lstSchedule = [strTask, strTime]
print("New task added:   ", lstSchedule)

# storing the data with the pickle.dump method
objFile = open("ScheduleData.dat", "ab")
pickle.dump(lstSchedule, objFile)
objFile.close()

#reading the data back with the pickle.load method
objFile = open("ScheduleData.dat", "rb")
objFileData = pickle.load(objFile) #load() only loads one row of data.
objFile.close()
print("The first task in the list:  ", objFileData)

#loading all rows of data #(source) https://stackoverflow.com/questions/49261006/load-all-pickled-objects
obj = []
with open("ScheduleData.dat", "rb") as fileOpener:
    while True:
        try:
            obj.append(pickle.load(fileOpener))
        except EOFError:
            break
print("All tasks in the list:   ", obj)
