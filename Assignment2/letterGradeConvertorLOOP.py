print("Letter Grade Convertor")

runAgain = "y"

while runAgain.lower() == "y":
    score = int(input("Enter your numerical grade: "))
    grade = score

    if score >= 88:
        print("Your grade is A")
        grade = "A"
    elif score >= 80:
        print("Your grade is B")
        grade = "B"
    elif score >= 67:
        print("Your grade is C")
        grade = "C"
    elif score >= 60:
        print("Your grade is D")
        grade = "D"
    else:
        print("Your grade is F")
        grade = "F"
        
    runAgain = input(("Continue? (y/n): "))


print("Thank you for using the letter grade converter.")




