# COST OF ITEMS SHIPPING COST
# ============= ==============
# < 30.00          5.95
# 30.00-49.99      7.95
# 50.00-74.99      9.95
# >= 75.00         FREE


print("Welcome to the shipping cost calculator!")

costofItem = float(input("Please enter the cost of your item: "))

if costofItem <= 0:
    print("Invalid input. Please enter a cost greater than 0.")
    exit()

if costofItem < 30.00:
    print("Your shipping cost will be $5.95")
    ship = 5.95
elif costofItem <= 49.99:
    print("Your shipping cost will be $7.95")
    ship = 7.95
elif costofItem <= 74.99:
    print("Your shipping cost will be $9.95")
    ship = 9.95
else:
    print("Your shippping is FREE!")
    ship = 0

totalCost = costofItem + ship
print("The total cost of your item with shipping will be: $" + str(totalCost))








