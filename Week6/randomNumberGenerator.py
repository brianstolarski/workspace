import random #imports the random module which allows you to randomize certain things

numberList = [1,2,3,4,5,6,7,8,9,10]

numbers = random.choice(numberList) #Will choose a random number from the list
random.shuffle(numberList) #this will randomize the order of the numbers in the list
poppedItem = numberList.pop(1) #removes a number after shuffling occured in the 1st index

print("The random number is: ", numbers) #will print the single random number from the list
print("Shuffled list: ", numberList) #this will print the randomized list
print("The removed item was: ", poppedItem)


