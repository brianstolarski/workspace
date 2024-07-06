print("Tip Calculator")
costofmeal = float(input("Enter the cost of the meal: "))
tippercent = float(input("Enter the amount you want to tip: "))
print() #adding a space

print("Cost of the meal: ", costofmeal)
print("Tip percent:", tippercent, end="\n\n")

tip = costofmeal * (tippercent / 100)
totalamount = tip + costofmeal

print("Tip Amount:", round(tip, 2))
print("Total amount:", round(totalamount, 2))