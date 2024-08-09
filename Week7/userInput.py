hoursWorked = int(input("Enter the number of hours worked: "))

while hoursWorked <= 0:
    print("Hours worked must be more than 0. Please try again.")
    hoursWorked = int(input("Enter the number of hours worked: "))

payRate = float(input("Enter your hourly pay rate: "))

while payRate <= 0:
    print("Pay rate must be more than 0. Please try again.")
    payRate = int(input("Enter your hourly pay rate: "))

grossPay = hoursWorked * payRate
print(f"Your gross pay is: ${grossPay}")