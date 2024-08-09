import salesTaxModule

def title(): #function for the title
    print("Sales Tax Calculator")


def itemTotals(): #Totalling up the cost of all the items 
    total = 0.0
    print("ENTER ITEMS (ENTER 0 TO END): ")
    while True: #infinite loop
        cost = float(input("Cost of item: "))
        if cost == 0:
            break #ends the loop if 0 is entered by the 0
        total = total + cost #adds up every cost entered
    return total

def totalDisplay(total, salesTax, finalTotal): #Displaying the input from user
    print(f"Total:           {total:.2f}")
    print("Sales tax:      ", salesTax)
    print("Total after tax:", finalTotal)

def main():
    goAgain = "y"
    while goAgain.lower() == "y":
        total = itemTotals()
        salesTax = salesTaxModule.salesTax(total) #Calling the module
        finalTotal = salesTaxModule.totalWithTax(total) #Calling the module
        totalDisplay(total, salesTax, finalTotal)
        goAgain = input("Again? (y/n): ")
    
    print("Thanks, Bye!")
    return total, salesTax, finalTotal #returned so it can be used elsewhere

if __name__ == "__main__":
    title() #calls the title
    main() #calls the main function