print("Welcome to the Travel Time Calculator")

calculateAgain = "yes"


while calculateAgain.lower() == "yes": #runs N number of times until user enters no
    miles = int(input("\nEnter miles: "))
    milesPH = int(input("Enter miles per hour: "))

    hours = miles // milesPH # integer division so there are no decimal points
    minutes = int((miles / milesPH - hours) * 60)

    print("\nEstimated travel time: ")  
    print("Hours:", hours)
    print("Minutes:", minutes)

    calculateAgain = input("Would you like to calculate again? (yes/no): ")

print("\nThanks for using the Travel Time Calculator!")

