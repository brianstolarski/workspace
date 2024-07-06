schoolSubjects = ["math", "python", "english"] # list of 3 subject
subjectGrades = [91, 81, 71] # 3 grades for the subject

subjectInput = input("Enter the name of the subject: ")
gradeInput = input("Enter the grade of that subject: ")

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
    schoolSubjects.append(subjectInput)
    subjectGrades.append(gradeInput)

schoolSubjects.extend(subjectGrades) # extending school subjects with subjectGrades 
print(schoolSubjects)