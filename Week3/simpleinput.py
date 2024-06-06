items = (int(input("Enter the amount of items you bought: "))) #assigns the input as an int
print("You've bought this many items: ", items) #displays how many items have bee bought
costofitems = (float(input("How much did you pay per item?: "))) #assigns the input as a float
totalcost = items * costofitems #adds both the int and float values
print(f"Total:  {totalcost:.2f}") #prints the total to the 2nd decimal point

############################

a, b = input("Enter two number to be added: ").split() #allows the user to enter 2 numbers but must put a space in between
a, b = (float(a)), (float(b)) #assign the two numbers entered to float
print("The sum of these two numbers are: ", a+b) #adds both numbers
print(type(a), (type(b)))

##############################
