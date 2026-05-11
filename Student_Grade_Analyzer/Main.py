# ask user to input student name and subjects with marks 

student_name=input("Enter your student name:")
print("____________________________________________________________________________________________________ ")


#need user to enter amount of subjects they are doing
num_subjects=int(input("Enter the number of subjects enrolled in:"))

#we should use a dictionary so that every value entered in the loop can be stored
storage={}

#use loops to repeat the question and allow users to enter their subject names and marks
for a in range(num_subjects):
    subjects=input("Enter subject name:")
    mark=float(input("Test1:"))
    mark1=float(input("Test2:"))
    assignment=float(input("Assignment:"))

    storage[subjects]={
        "test 1":mark ,
        "test 2":mark1 ,
        "Assignment":assignment
    }
    print(" ")

#call out the analyzer file so it can recieve data
import Analyzer

#specify which data will be imported to the analyzer file
Analyzer.reciever(student_name, storage)