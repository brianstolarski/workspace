print("Change Caclulator")

keepGoing = "y" #loop


while keepGoing.lower() == "y":
    cents = int(input("Enter number of cents (0-99): ")) #assuming user will enter a valid integer
    quarters = cents // 25 #integer division to get whole numbers (//)
    remainder = cents % 25
    dimes = remainder // 10
    remainder = remainder % 10
    nickels = remainder // 5
    pennies = remainder % 5

    print("Quarters:", quarters)
    print("Dimes:", dimes)
    print("nickels:", nickels)
    print("pennies:", pennies)

    keepGoing = input("Continue? (y/n): ") #exits or continues based on user input


print("\nBye! Thanks for using the change calculator.")