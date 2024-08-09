def mpgCalculator():

    miles, gallonsUsed = input("Entier miles driven and gallons split with ;: ").split(";")
    miles, gallonsUsed = float(miles), float(gallonsUsed)
    
    
    if (miles <= 0):
        miles = float(input("Enter a value higher than 0: "))
    if (gallonsUsed <= 0):
        gallonsUsed = float(input("Enter a value higher than 0: "))

    mpg = miles / gallonsUsed
    print(f"MPG: {mpg:.2f}")

if __name__ == "__main__":
    mpgCalculator()