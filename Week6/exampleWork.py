#Ask the user to enter first name, lastname and a student ID all in one input statement.
#Create and empty list, then append the entered information into the list using append() one at a time.
#Last, print the list

studentInfo = input("Please enter your first name, last name, and student ID with spaced in between: ")
print("Your information: ", studentInfo)

studentInfoSplit = studentInfo.split() #Takes all 3 inputs and seperates them, default is spaces between the strings

studentInfoList = [] #Creates am empty list

for studentInfo in studentInfoSplit: 
    studentInfoList.append(studentInfo)

print("Information split: ", studentInfoList)

####################################################################################
#Ask the user to enter 4 sales amounts as float values, all in one input statement seperated with (,)
#Append them into a list
#Find the minimum, maximum, and the sum of the list of the sales
#Sort the list then reverse it
#Last, count the number of times an amount occurs in a list
#Print out all outputs in the above questions

salesAmount = input("Enter 4 sales amounts as floats and seperate each value with a comma: ")
salesAmountList = [float(salesAmount) for salesAmount in salesAmount.split(',')]
print("Initial list: ", salesAmountList)

minSales = min(salesAmountList)
maxSales = max(salesAmountList)
sumSales = sum(salesAmountList)

sortedSales = sorted(salesAmountList)
reversedSales = sortedSales[::-1]
countedList = sortedSales.count(44.4)


print("Sale list: ", salesAmountList)
print("Min sales: ", minSales)
print("Max sales: ", maxSales)
print("Sum of sales: ", sumSales)
print("Sorted sales: ", sortedSales)
print("Reverse sales: ", reversedSales)
print("44.4 appears this many time in the list: ", countedList)

####################################################################################
# Create a list of 3 subjects you take in your school
# Create another list of the 3 grades of the subjects
# Extend the first list to include the second one
# Check for a specific subject if it is in the list, if so, remove it with its grade.
# If the subject is not in the list, append it with its grade into the list so it still looks consistent - the subjects followed by the grades.
# Calculate the average of the grades. In a new list, append or extend it to include the subject and average value.
# Get the average value from the list and check for it to print the corresponding grading letter. (e.g., A, B, C, etc) - follow the example 
# in last weeks lesson.

schoolSubjects = ["math", "python", "english"] # list of 3 subject
subjectGrades = [91, 81, 71] # 3 grades for the subject

subjectInput = input("Enter the name of the subject: ")

if subjectInput == "math": 
    schoolSubjects.remove("math") 
    subjectGrades.remove(91)
elif subjectInput == "python":
    schoolSubjects.remove("python")
    subjectGrades.remove(81)
elif subjectInput == "english":
    schoolSubjects.remove("english")
    subjectGrades.remove(71)
else:
    gradeInput = input("Enter the grade of that subject: ")
    schoolSubjects.append(subjectInput)
    subjectGrades.append(gradeInput)

schoolSubjects.extend(subjectGrades) # extending school subjects with subjectGrades 
print(schoolSubjects)


####################################################################################
# Create a list of three lists of 2 float numbers in each
# Access the second list
# Compare the two values of that list
# If they are equal, append 'neutral' to the list, if the first value is smaller than the second, append 'safe'; otherwise, append 'risky'
# Access the appended value in the previous step and print out to the screen

# floatList = [[10.0, 20.0], #index 0 
#              [29.0, 28.0], #index 1
#              [50.0, 60.0]] #index 2

# compareList2 = floatList[1]

# if compareList2[0] == compareList2[1]:
#     compareList2.append("neutral")
# elif compareList2[0] < compareList2[1]:
#     compareList2.append("safe")
# else:
#     compareList2.append("risky")
    
# print(compareList2)
    



