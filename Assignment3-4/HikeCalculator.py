def title(): #Function for the title
    print("Hike Calculator") 

def main(): #Function that stores the user input for the total distance walked
    distance = float(input("How many miles did you walk?: "))
    return distance

def conversion(distance):
    feet = distance * 5280 #1 mile = 5280 feet
    return int(feet) #converts feet into an integer
    

if __name__ == "__main__":
    title()
    totaldistance = main()
    feetconverted = conversion(totaldistance)
    print((f"You walked {feetconverted} feet."))
