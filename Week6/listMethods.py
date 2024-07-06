


stats = [48.1, 22, 23.0, 100.0, 94.2]
print(stats)
stats.append(99.99) #append adds 99.99 to the END of the list
print(stats)

#####################################################################################################################

inventory = ["staff", "hats", "shoes", "bread", "potion"]
print("Inventory:", inventory)
inventory.insert(3, "robe") #inserts robe into the third index of the list
print("New inventory:", inventory)  #prints out the new list
inventory.remove("shoes") #removes shoes from the list
print("Inventory with shoes removed:", inventory) #prints new list with shoes removed
print("The index of the item staff: ", inventory.index("staff")) #prints out which index "staff" is located

item = inventory.pop(1) #removes an item from the list according to the index provided, if no value given then last item will be removed
print("Inventory after removing the last item using pop method: ", inventory)

#####################################################################################################################

foodlist = ["orange", "apple", "Pear", "banana"]
foodlist.sort() #will not sort because by default pythons default sorting is case-sensitive
print(foodlist)
foodlist.sort(key = str.lower) #using a key argument so that it sorts purely alphabetically without cosidering lower/upper-case
print(foodlist)

#####################################################################################################################
import random

janSales = [2145.9, 4358.5, 4090.0]
febSales = [4232.1, 2211.1, 3492.2]
febSales.extend(janSales) #includes janSales list in febSales list
random.shuffle(febSales) #shuffles both lists after extending them
print(febSales)

#####################################################################################################################

numlist = [5, 15, 84, 3, 14, 2, 8, 10, 14, 25]
minimum = min(numlist) #finds the lowest value in the list
print("The minimum value: ", minimum)
maximum = max(numlist) #finds the highest value in the list
print("The maximum Value: ", maximum)
total1 = sum(numlist)
total2 = sum(numlist, start = 100) # start means the initial value is 100 and the list will be added onto that value
print("The first total is: ", total1)
print("The second total after adding 100 is: ", total2)

#####################################################################################################################

lastName = input("Enter your last name: ")
mylist = list(lastName)
print("My name in a list: ", mylist)
enumList = enumerate(mylist) #enumarate is a function that returns all the items in a list with their corresponding indexes
print(list(enumList))

#####################################################################################################################
import random #the random module provides function for generating random numbers, used for game development

numberlist = [5, 15, 84, 3, 14, 2, 8, 10, 14, 25]
choice = random.choice(numberlist) #will randomly choose 1 item from the list using the random module
random.shuffle(numberlist) #will shuffle the entire list randomly using the random module
print("The randomly selected item: ", choice)
print("The numlist after shuffling: ", numberlist)

#####################################################################################################################

inventory1 = ["staff", "hats", "shoes", "bread", "potion"]
print(inventory1)
item = "bread"
if item in inventory1:
    inventory1.remove(item) #will check if the item is in inventory and remove if it is, if it doesn't exist it will return an error
print("With removed item: ", inventory1)

#####################################################################################################################
#Code that uses range() function to generate lists
print(list(range(4))) #generates a list from 0 through 3 (begin-1)
coolList = list(range(5, 13)) #generates a list from 5 through 12 (begin, end-1)
print(coolList)
coolList1 = list(range(5, 13, 3)) #generates a list from 5 through 12 and increments by 2 (begin, end-1, step)
print(coolList1)

