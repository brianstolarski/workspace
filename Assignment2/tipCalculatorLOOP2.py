#This program will allow the user to choose between 3 different tip options until the user decides
#that they do not want to tip (user input = no) then the program will end.

print("Welcome to the tip calculator!")

tipPercent1 = 15 #15% tip
tipPercent2 = 20 #20% tip
tipPercent3 = 25 #25% tip

leaveTip = "yes"
tipAgain = "yes"

while tipAgain.lower() == "yes":
    mealCost = float(input("\nEnter the cost of the meal: "))
    print("\nCost of meal:", mealCost)

    tip1 = mealCost * (tipPercent1 / 100)
    tip2 = mealCost * (tipPercent2 / 100)
    tip3 = mealCost * (tipPercent3 / 100)
    totalAmount1 = tip1 + mealCost
    totalAmount2 = tip2 + mealCost
    totalAmount3 = tip3 + mealCost

    leaveTip = input("\nWould you like to leave a tip? (Yes/No): ")

    if leaveTip.lower() == "yes":
        print("\nPlease select a tip option: ")
        print("1. 15%")
        print("2. 20%")
        print("3. 25%")
        tipOption = input("\nEnter option here: ")

        if tipOption == "1":
            print("\nYou chose15%")
            print(f"Tip amount: {tip1:.2f}")
            print(f"Total amount: {totalAmount1:.2f}")

        elif tipOption == "2":
            print("\nYou chose 20%")
            print(f"Tip amount: {tip2:.2f}")
            print(f"Total amount: {totalAmount2:.2f}")

        elif tipOption == "3":
            print("\nYou chose 25%")
            print(f"Tip amount: {tip3:.2f}")
            print(f"Total amount: {totalAmount3:.2f}")
    else:
        print("\nYour total without tip is:", mealCost)

    tipAgain = input("\nWould you like to calculate another tip? (Yes/No): ")
        
print("\nThank you for using the tip calculator!")

