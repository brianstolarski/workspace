#Create user account

userFullName = input("Enter your full name: ")
userID = (input("enter your id number: "))

#saleAmount = float(input("enter your total sales f or today: "))

userFullNameSplit = userFullName.split()
print(userFullNameSplit)
firstname = userFullNameSplit[0]
lastname = userFullNameSplit[1]


#logical and relation operators (and or >= > <= < == !=)
if (userID.isdigit() and firstname.isalpha() and lastname.isalpha()):
    print("User entered an id and name correctly.")
    if(firstname.alpha() and lastname.isalpha()):
        print("User entered the name correctly.")
        print("%-10s %10s %5s"%(firstname, lastname, userID))
    else:
        print("user entered the name wrong")
else:
    print("user entered wrong ID pattern")



# if(firstname.isalpha()):
#     print("User enter a first name as string.")
# else:
#     print("user entered a first name not as a string.")

#userFirstName = input("Enter your first name: ")
#userLastName = input("Enter your last name: ")

# print(userID.isdigit())