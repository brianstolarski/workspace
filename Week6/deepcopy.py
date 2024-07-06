import copy #imports the shadllow copy and deepy copy functions

listone = [1, 2, 3, 4, 5]
listtwo = copy.deepcopy(listone) #Takes the original and creating an original new list without changing the original list
listtwo[1] = 9
item = 6
if item not in listone:
    listtwo.append(item)
if item in listtwo:
    listtwo.remove(item)
print("Old list", listone)
print("New list", listtwo)