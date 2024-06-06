print("Welcome to the MPG calculator, please enter the amount of miles you have driven and the amount of gasoline your car has used: ")
milesdriven = float(input("Please enter the amount of miles driven by your vehicle today: "))
gallonsused = float(input("Please enter the amount of gasoline used by your vehicle today in galons: "))
mpg = milesdriven / gallonsused
print(f"Your MPG is: {mpg:.2f}")