numberList = [124.23, 233.34, 58.89, 90]

def printRoundedNumbers(numbers):
    numbers[0] = 23
    for num in numbers:
        print(f"{round(num,1):.1f}")

printRoundedNumbers(numbers = numberList)
print(numberList)