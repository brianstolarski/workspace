price = 50
quantity = 9
amount = price * quantity

if amount > 100: #if the amount is greater than 100 itll go to the next if statement and check it
    if amount > 500:
        print("amount is greater than 500")
    else: #this ends this specific nested if block and will not go any further after it prints the value that is less than 500
        print("Amount is less than 500")
elif amount == 100:
    print(f"{amount} is equal to: {amount}")
else: #this ends the code
    print(f"Amount is {amount}")