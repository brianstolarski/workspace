print("Price Comparison", end="\n\n")

sixfour = float(input("Enter the price of the 64 oz size: "))
threetwo = float(input("Enter the price of the 32 oz size: "))

pposixfour = sixfour / 64
ppothreetwo = threetwo / 32   #ppo = price per oz

print() #adding a space
print("Prize per oz (64 oz):", round(pposixfour, 2))
print("Prize per oz (32 oz):", round(ppothreetwo, 2))