import sys

num = 20
salary = 5000.98
valid = True    
name = "Brian Stolarski"

print(type(num), type(salary), type(valid), type(name))

x = 10
y = "Brian"
print(x)
print(y)


###########################################

variable, variable2, variable3 = "value1", "value2", "value3"
print(variable)
print(variable2)
print(variable3)

###########################################
var1 = var2 = var3 = "Samevalue"
print(var1)
print(var2)
print(var3)

###########################################
list = [1, 2, "three", 4, 5, "six"] #list are able to store multiple values in a single variable
list2 = ["brian", "patrick", "anna", "mika"] #list are able to be modified aka mutable but uses more memory
list[5] = "poop" #changing the value of the list at index 5
combined_list = list + list2 #combining the two lists and storing it into the variable combined_list
print("CombinedList: ", combined_list) #printing the combined list
print("OriginalList:", list)#printing the original list
print("NameList: ", list2)#printing the list of names
print("ListLength:*******", len(combined_list)) #printing the length of the combined list
print("Value of INDEX 7: ", combined_list[7])#printing the value at index 9 of the combined list

###########################################
tuple = (1, 2, 3, 4, 5) #Tuple are not able to be modified aka immutable, use if you know you don't need to change values and save memory
tuple2 = ("One", "Two", "Three", "Four", "Five") #Tuple are able to store multiple values in a single variable
print("tuple: ", tuple)#printing the tuple
print("CompbinedTuple: ", tuple + tuple2)#printing the combined tuple


###########################################
print("OriginalList:", sys.getsizeof(list)) #getting the size of the list
print("tuple: ", sys.getsizeof(tuple)) #getting the size of the tuple

