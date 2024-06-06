name = "Brian"
age = 28
salary = 1000.00

name = input("Enter your first name: ")
print("Hello there,", name)
print("Datatype of your name:", type(name))


age = input("Enter your age: ")
print("Data type of age", type(age))
print("In one year you will be:", (int(age)+1)) #converting the string into an int ONLY for the purpose of adding + 1


salary = input("Enter your weekly salary: ")
print("The datatype for salary is:", type(salary))
salary = float(salary) #converting the string into a float for the rest of the code
print("In two weeks you will have: ", (float(salary)*2))
print("The new datatype of salary is now: ", type(salary))


hoursworked = (int(input("Enter your hours worked: "))) #will only take an int value for input 
print("This datatype is: ", type(hoursworked))
print("In two weeks your hours worked will be:", hoursworked*2)

  
###################################################

