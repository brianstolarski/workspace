schoolSubjects = ["math", "python", "english"] # list of 3 subject
subjectGrades = [81, 76, 63] # 3 grades for the subject

subjectInput = input("Enter the name of the subject: ")

if subjectInput == "math": 
    schoolSubjects.remove("math") 
    subjectGrades.remove(81)
elif subjectInput == "python":
    schoolSubjects.remove("python")
    subjectGrades.remove(76)
elif subjectInput == "english":
    schoolSubjects.remove("english")
    subjectGrades.remove(63)
else:
    gradeInput = int(input("Enter the grade of that subject: "))
    schoolSubjects.append(subjectInput)
    subjectGrades.append(gradeInput)

averageGrade = sum(subjectGrades) / len(subjectGrades) #divides it by the length of the list after items are appended

schoolSubjects.extend(subjectGrades) # extending school subjects with subjectGrades 
print(schoolSubjects)

letterGrade = averageGrade
if averageGrade <= 100:
    print("Your grade is A")
    letterGrade = "A"
elif averageGrade <= 80:
    print("Your grade is B")
    letterGrade = "B"
elif averageGrade <= 70:
    print("Your grade is C")
    letterGrade = "C"
elif averageGrade <= 60:
    print("Your grade is D")
    letterGrade = "D"
else:
    print("Your average grade was an F")
    letterGrade = "F"

print("The Average grade is:", f"{averageGrade:.2f}", letterGrade)