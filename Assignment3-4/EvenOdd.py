def main():
    number = int(input("Enter an integer: "))
    return number #Returns the value that's stored in number so that it can be called upon later

def checknum(number):
    if number % 2 == 0: #Checks the number if it's odd or even
        print ("The number is even")
    else:
        print("The number is odd")

if __name__ == "__main__":
    number = main()
    checknum(number)
