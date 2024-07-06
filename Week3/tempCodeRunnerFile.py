salary = input("Enter your weekly salary: ")
print("The datatype for salary is:", type(salary))
salary = float(salary) #converting the string into a float for the rest of the code
print("In two weeks you will have: ", salary*2)
print("The new datatype of salary is now: ", type(salary))