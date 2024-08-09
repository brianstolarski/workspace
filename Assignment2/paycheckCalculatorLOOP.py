tax = 18

print("Welcome to the paycheck calculator")

count = 0
continueAgain = "yes"

while continueAgain.lower() == "yes": #runs N number of times until user enters no
    hoursWorked = float(input("Enter the amount of hours worked: "))
    hourlyPay = float(input("Enter you hourly pay: "))
    grossPay = hoursWorked * hourlyPay
    taxAmount = grossPay * (tax / 100)
    takeHome = grossPay - taxAmount
    print("Hours worked:", hoursWorked)
    print("Hourly pay:", hourlyPay)
    print("Gross pay:", grossPay)
    print(f"Tax rate: {tax}%")
    print("Tax amount:", taxAmount)
    print("Take home:", takeHome)
    print("---------------------------------------------------------")
    continueAgain = input("Do you want to enter another employees pay? (yes/no): ")
    count = count + 1

print("Thank you for using the paycheck calculator!")
print(f"{count} user(s) have used the calculator this session.")





    

    




