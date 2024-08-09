import random

def title():
    print("Dice Roller")

def dieRoll():
    diceRoll = random.randint(1, 6)
    return diceRoll

def specialMessage(diceOne, diceTwo):
    if diceOne == 1 and diceTwo == 1:
        print("Snake eyes!")
    elif diceOne == 6 and diceTwo == 6:
        print("Boxcars!")

def totalDie(diceOne, diceTwo):
    total = diceOne + diceTwo
    return total

def main():
    rollDice = "y"
    while rollDice.lower() == "y":
        diceOne = dieRoll()
        diceTwo = dieRoll()
        print("Die 1:", diceOne)
        print("Die 2:", diceTwo)
       
        total = totalDie(diceOne, diceTwo)
        print("Total:", total) 

        specialMessage(diceOne, diceTwo) 

        rollDice = input("\nRoll again? (y/n)?: ")

    print("Thanks, bye!")   

if __name__ == "__main__":
    title()
    main()
    