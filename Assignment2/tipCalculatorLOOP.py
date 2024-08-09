print("Welcome to the tip calculator!")

goAgain = "Y"
count = 0

while goAgain.upper() == "Y": #runs N number of times until user enters no
    mealCost = float(input("\nEnter the cost of the meal: "))
    tipPercent = float(input("Enter the amount you want to tip: "))
    tipTotal = mealCost * (tipPercent / 100)
    totalCost = mealCost + tipTotal
    print(f"\nTip amount: {tipTotal:.2f}")
    print(f"Total Amount: {totalCost:.2f}")
    goAgain = input("\nWould you like to calculate another tip? (y/n): ")
    print("--------------------------------------------------------")
    count = count + 1

print("Thanks for using the tip calculator!")
print(f"You calctulated a total of {count} tip(s)!")
