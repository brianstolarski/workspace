score = int(input("Enter your score: "))
grade = score
if score >= 90:
    print("Your grade is A")
    grade = "A"
elif score >= 80:
    print("Your grade is B")
    grade = "B"
elif score >= 70:
    print("Your grade is C")
    grade = "C"
elif score >= 60:
    print("Your grade is D")
    grade = "D"
else:
    print("Your grade is F")
    grade = "F"

if grade == "A":
    print("Excellent job!")
elif grade == "B":
    print("Great work!")
elif grade == "C":
    print("Good work!")
elif grade == "D":
    print("Okay job!")
else:
    print("Work harder next time!") #F Grade