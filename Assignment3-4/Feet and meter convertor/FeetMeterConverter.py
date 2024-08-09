import converter_module

def title():
    print("Feet and Meters Converter")

def menu():
    print("Conversions Menu: ")
    print("a. Feet to Meters")
    print("b. Meters to Feet")

def main():
    title() #calls the title function
    goAgain = "Y"
    while goAgain.lower() == "y":
        menu() #calls the menu function
        option = input("Select a conversion (a/b): ") #User inputs a or b
        if option.lower() == "a": #will convert whatever input to lowercase a so it matches both a and A
            feet = float(input("Enter feet: "))
            meters = converter_module.feettometers(feet)
            print(f"{meters:.2f} meters")
        else:    
            meters = float(input("Enter meters: "))
            feet = converter_module.meterstofeet(meters)
            print(f"{feet:.2f} feet")
        goAgain = input("Would you like to go again? Y/N: ")
    print("Thanks, bye!!!")
  


if __name__ == "__main__":
    main()