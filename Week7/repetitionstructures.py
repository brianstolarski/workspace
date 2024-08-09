#types of repetition: while, do while, for loop
#for and while: wecheck the condition, then we go inside (pre check)
#do while: even if condition is true or false, it executes at least once (post check)


#while loop#
number = 0 
while number <= 10:
    print(number)
    number = number + 1

#while loop#
count = 0
while count < 5:
    print("Hello")
    count = count + 1

#for loop#
numberList = [1, 2, 3, 4, 5]
for x in numberList:
    print(x)

#while loop#
choice = "y"
while choice.lower() == "y": #.lower() converts the string to lowercase after the first "Hello"
    print("Hello")
    choice = input("Say hello again? (y/n): ") #this is converted to lowercase
print("Bye!") #run loop ends when user does not enter Y

#while loop#
counter = 0 #counter set to 0
while counter < 5: #runs the while loop as long as its under 5
    print(counter, end=" ") #prints the number, with a space in between
    counter = counter + 1 #adds 1 each loop
print("\nThe loop has ended")

#while loop#
count = 0 
weight = float(input("Enter shipment weight: ")) #initial check if weight is >= 10
while weight >= 10:
    count = count + 1 #adds to count if weight is >= 10
    weight = float(input("Enter shipment Weight: ")) #second check if weight is >=10
print("The count of shipments that are greather than 10 tons is: ", count) 

#infinite loop#
keepGoing = "y"
while keepGoing == "y": #will keep going because keepgoing = y
    sales = float(input("Enter the amount of sales: "))
    commisionRate = float(input("Enter the commission rate: "))
    commisionRate = sales * commisionRate
    print("The comission is $:", f"{commisionRate:.2f}")
    exit() #stops the infinite loop


#while loop#
count = 0
while count < 3:
    count = count + 1
    print("Hello World")
print("The loop has concluded") #will print this after the initial loop has printed 3 times


#for loop
n = 4
for x in range(0,n): #prints from 0 to n which is 4-1 (3)
    print(x)

#infinite while loop
count = 0
while count <= 0:
    print("count:", count)
    count = count - 1 #count will always be <= 0 because we are subtracting 1
