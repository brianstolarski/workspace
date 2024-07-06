interestrate = [2.99, 5.99, 9.99]
print(interestrate * 3) #this will repeat the list three times
interest1 = interestrate[2] #acceses the 2nd index and assigning it to interest1
interest1 = interest1 * 5
print("Index 2 is,", interest1)

usernames = ["brian", "dav1d", "johnn"]
student1 = usernames[0] + " | 1234123" #assigning student 1 to brian and adding a student id
student2 = usernames[1] + " | 8437423"
student3 = usernames[2] + " | 8414721"
print("student information", student1, sep=" | ")
print("student information", student2, sep=" | ") 
print("student information", student3, sep=" | ")



#SLICING!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
numbers = [52, 54, 56, 58, 60, 62, 64]
print(numbers[0:2]) #Lower range is included but Upper range isn't included
print(numbers[:2]) #The same as 0:2
print(numbers[2:]) #Second index to the end of the list
print(numbers[0:7:2]) #[start:stop:step]
print(numbers[::-1]) #double :: prints the entire list in reverse
print(numbers[:-1]) #singele : prints everything but the last index (minus the last index in -1)