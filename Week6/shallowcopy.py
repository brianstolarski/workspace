listone = [1, 2, 3, 4, 5]
listtwo = listone
listtwo[1] = 9
print("Old List", listone)
print("New List", listtwo) #Both lists will be changed since it's just using the original list as a reference and not actually copying it

