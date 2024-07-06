#Problem 1:
#How would you compare the followings: (YES, yes), and (NO, no)? Hint: what methods would you use?
#Then use one of these methods to compare them with a user input and display the result (true or false)
#Then use a logical operator to combine both terms in one boolean expression to compare and display the result.

# yesUpper = "YES"
# yesLower = "yes"
# noUpper = "NO"
# noLower = "no"

# print("Does YES equal yes?:", yesUpper == yesLower)
# print("Does NO equal no?:", noUpper == noLower)

# yes1 = input("Please enter YES: ")
# yes2 = input("Please enter yes: ")
# no1 = input("Please enter NO: ")
# no2 = input("Please enter no: ")

# print(yes1 == yesUpper and yes2 == yesLower and no1 == noUpper and no2 == noLower) #compares the useripnut with the variables set at the start of the code

# Problem 2:
# Suppose that we have three variables (day, ticketPrice and status) – the day can be either weekday or weekend; the status can be one of the following: a student, a child less than 14 years old, or an elder greater than 65 years old.
# Use logical operators to test the three variable all in one line by joining them in a compound conditional expression. Then display the result (True or False)


discountDays = ["monday", "tuesday", "wednesday", "thursday", "friday"]
studentStatus = "student"
elderStatus = "elder"
childStatus = "child"
ticketPrice = 20
ticketPriceStudent = 15
ticketPriceChild = 10
ticketPriceElder = 5


print("Welcome to the concession, let us see if you qualify for our discount!")

statusInput = input("Please enter your status, are you a student, child of under 14 years of age, or an elder older than 65 years of age?: ").lower()
day = input("Please enter a day: ").lower()
if statusInput == studentStatus:
    age = None
else:
    age = int(input("Please enter your age: "))

if day in discountDays and statusInput == studentStatus:
    ticketPrice = ticketPriceStudent
    print("You qualify for our weekday student discount! The ticket price will be:",ticketPrice)
elif day in discountDays and statusInput == elderStatus and age > 65:
    ticketPrice = ticketPriceElder
    print("You qualify for the elder discount! Your ticket will cost: ", ticketPrice)
elif day in discountDays and statusInput == childStatus and age < 14:
    ticketPrice = ticketPriceChild
    print("You qualify for the child discount! Your ticket will cost:", ticketPrice)
elif statusInput == elderStatus and age < 65:
    print("Sorry but you are only considered an elder if you are over the age of 65! Your ticket price will be:", ticketPrice)
elif statusInput == childStatus and age > 14:
    print("Sorry but to be considered a child you must be under 14 years of age. Your ticket price will be:", ticketPrice)
elif day not in discountDays and (statusInput == elderStatus or statusInput == childStatus or statusInput == studentStatus):
    print("Sorry, you qualify but this discount is only available on weekdays!")
else:
    print("You do not meet any criterea for a discount, sorry! Your ticket price will be:", ticketPrice)