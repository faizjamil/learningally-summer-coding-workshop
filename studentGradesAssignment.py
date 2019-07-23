#!/usr/bin/python3

studentName = []
assignments = ["Assignment1", "Assignment2", "Assignment3", "Assignment4", "Assignment5"]
grade = []

def addStudent():
  """For this method you need to add all new students to the studentName list. I took care of the line to read the input."""
  newStudent = input("Enter students name: ")
  studentName.append(newStudent)

def computeGrade():
  """For this method I want you to calculate the grade of the students for each assignment and add the final grade to the grade list. I took care of the input."""
  assignmentGrade = 0
  for i in assignments:
    assignmentGrade += input("Enter the grade for " + i)
  grade.append(assignmentGrade)


def printGrades():
  """In this method I want you to print each students name and their final grade on the same line."""
  if (grade[0] == 0):
    print("No grades have been computed yet!")
classSize = 2
numOfStudents = 0
while numOfStudents < classSize:
  addStudent()
  computeGrade()
  numOfStudents+=1

printGrades()
