print("Welcome to the student registration form! Please enter your details when prompted.")
firstname = input("Please enter your first name: ")
lastname = input("Please enter your last name: ")
birthyear = int(input("Please enter you birthyear: "))
print("\n")
print("Registration Form")
print("First name:  ", firstname)
print("Last Name:   ", lastname)
print("Birth Year:  ", birthyear)
print("Welcome", firstname + " " + lastname + "!", end="\n\n")
print("Your registration is complete.", end="\n\n")
print("Your temporary password is:", firstname + "*" + str(birthyear))