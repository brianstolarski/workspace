tax = 18.00 #Change this if tax rate ever changes

print("Welcome to the paycheck Calculator!")
hoursworked = float(input("Please enter the amount of hours you have worked: "))
hourlypay = float(input("Please enter your hourly pay rate: "))
#tax = float(input("Enter the amount you get taxxed in your region: ")) #We can also ask the user to enter their tax amount instead of assigning it a value like in line 1

grosspay = round(hoursworked * hourlypay, 2) #rounds the next 3 values to a maximum of 2 decimal places
taxamount = round(grosspay * (tax / 100), 2)
takehomepay = round(grosspay - taxamount, 2)


print("Hours worked:", hoursworked)
print("Hourly Pay Rate:", hourlypay, end="\n\n")
print("Gross Pay:", grosspay)
print("Tax Rate:", tax, "%")
print("Tax Amount:", taxamount)
print("Take Home Pay:", takehomepay)

