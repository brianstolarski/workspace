# a = 400
# b = 300

# if b > a:
#     print("b is greater than a")
# elif a == b:
#     print("a and b are equal")
# else:
#     print("a is greater than b")

# age = int(input("enter your age: "))
# if age > 65:
#     print("You are elderly!")
# elif age > 18:
#     print("You are an adult!")
# else:
#     print("You are still a child!")


# invoiceTotal = float(input("Please enter your invoice total: "))
# if invoiceTotal >= 500.0:
#     print("Your discount will be 2%.")
# elif invoiceTotal >= 250.0:
#     print("Your discount will be 1%.")
# elif invoiceTotal >= 0.0:
#     print("You will not recieve a discount. You must spend at least $250.")
# else:
#     print("Invoice total must be greater than zero.")


#A program that takes a users number grade and converts it into a letter grade.

# grade = float(input("Please enter your number grade: "))
# if grade >= 90:
#    letter = "A"
# elif grade >= 80:
#     letter = "B"
# elif grade >= 70:
#     letter = "C"
# elif grade >= 60:
#     letter = "D"
# else:
#     letter = "F"
# print("Your letter grade is:", letter)



#A program that gets age and ticket price from the uer then it checks if age >= 65 or age <= 12, a discount is then applied on the ticket price. The program then calculates the final cost of the ticket.

age = int(input("Please enter your age:"))
ticketPrice = float(input("Please enter a ticket price:"))

if age >= 65:
    ticketDiscount = 0.50
    print("You qualify for the 50% elderly discount! ")
elif age <= 12:
    ticketDiscount = 0.25
    print("You qualify for the 75% Child discount! ")
else:
    print("You do not qualify for a discount.")
    ticketDiscount = 1

afterDiscount = ticketPrice * ticketDiscount
print("Your price after discount is: $"+(str(afterDiscount)))



x = int(input("enter a number between 20 and 40: "))
if x >= 20 and x <= 40:
    print("the value of x is greater or equal to 20 and less than or equal to 40")
else:
    print("you entered the wrong value")