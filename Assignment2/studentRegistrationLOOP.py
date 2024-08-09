print("Welcome to the student registration form!")

n = int(input("How many students are registering?: "))

for x in range(n): #runs within the range of user inputted number 
    firstName = input("Please enter your first name: ")
    lastName = input("Please enter your last name: ")
    birthYear = input("Please enter your birth year: ")        
    
    print("\nRegistration Form")
    print("\nFirst name:", firstName)
    print("Last name:", lastName)
    print("Birth year:", birthYear)
    print("\nWelcome", firstName + " " + lastName)
    print("Your registration is complete.")
    password = firstName + '*' + birthYear
    print("Your temporary password is:", password)
    print("--------------------------------------------------------------")



if n == 1:
    print(f"Registration is complete! {n} student has registered.") #different grammar usage if only 1 is entered
else:
    print(f"Registration is complete! {n} students have registered.")