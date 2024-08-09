print("Welcome to the price comparison tool")

repeatCode = "yes" #initialize while loop 

bigOz = 64 #oz size is 64
smallOz = 32 #oz size is 32

while repeatCode.lower() == "yes": #runs N number of times until user enters no
    bigSize = float(input("\nEnter the price of the 64 oz size: "))
    smallSize = float(input("Enter the price of the 32 oz size: "))
    bigPrice = bigSize / bigOz
    smallPrice = smallSize / smallOz
    print(f"\nPrice per oz (64 oz): {bigPrice:.2f}")
    print(f"Price per oz (32 oz): {smallPrice:.2f}") 
    repeatCode = input("\nWould you like to compare prices again? (yes/no): ") 


print("\nThanks for using the price comparison tool!")