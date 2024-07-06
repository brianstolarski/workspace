print("Tip Calculator", end="\n\n")

mealCost = float(input("Enter the cost of your meal: "))
tip = float(input("Please enter your tip amount. 15%, 20% or 25%: "))
print("Cost of meal:", mealCost)

tipAmount =  mealCost * (tip / 100)
totalAmount = mealCost + tipAmount

if tip == 15:
    print("Tip Amount:", round(tipAmount, 2))
    print("Total Amount: ", round(totalAmount, 2))
elif tip == 20:
    print("Tip Amount:", round(tipAmount, 2))
    print("Total Amount: ", round(totalAmount, 2))
elif tip == 25:
    print("Tip Amount:", round(tipAmount, 2))
    print("Total Amount: ", round(totalAmount, 2))
else:
    print("Please select one of the 3 options.")
    