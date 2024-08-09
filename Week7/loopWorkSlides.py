print("Welcome to the area thing calculator!")


count = 0
while count < 2:
    count = count + 1
    circleInput = input("Please enter the area and the perimeter seperated by a semi-colon: ")
    areaPerimeter = circleInput.split(";")
    value1 = float(areaPerimeter[0])
    value2 = float(areaPerimeter[1])
    print(value1, value2, sep=(", "))
    


