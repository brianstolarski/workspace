name = "Hello World!"
print("The index of 11 is:", name[11]) #prints the 11th index
print("The length of Hello World! is:", len(name)) #tells us the length of the string
print(name[1:4]) #print from idex 1 to 3 aka slicing the index
print(name[:7]) #prints from index 0 to 6 (no number means everything till index 7)
print(name[1:]) #prints everything from index till the end
print(name[-5:-2]) #negative index starts from the opposite side of the string
print(name[:-1]) #prints everything until the last character (!)
print(name[:11]) #prints from index 0 to 11

#####################################################

print("lol" * 20) #repeats the string 20 times
print("Hello there " * 3) #repeates the string 3 times

#####################################################

name = "Brian"
name = name + " " + "Stolarski"
print(name)
print(len(name)) #length will be 14 + 1 = 15

######################################################

#message = "Hello world!" 
#message[0] = "Y" # this will not work because message was assigned a value of str and those are immutable
#print(message)

######################################################

date = "11/9/1972"
date = date.split("/") #divides the string by indenfitying the seperator in this case the "/"
print(date)
month = int(date[0]) #the month is now split and is considered index 0
day = int(date[1]) #the day is now split and is considered index 1
year = int(date[2]) #the year is now split and is sconsidered index 2
print(month)
print(day)
print(year)

######################################################

ssn = input("enter your ssn: ")
ssn = ssn.strip() #this removes any spaces before and after the string to make it more neat
print(ssn)

######################################################

entry = "12345"
isint = entry.isdigit() #returns a value of true or false is the string called entry contains only digits in this case it would be true and stores it in isint
print("Is", entry, "a digit?:",isint)

######################################################

book = "Who controls the Internet?"
isword = book.startswith("Who") #checks if the value 'book' starts with the word "Who", in this case it would be true and stores it in isword
#print(book.startswith("Who"))
print("Does", book, "start with 'Who'?:", isword)

######################################################
wordcheck = "People love chocolate" #giving the value of wordcheck
check = input("Enter the word you are looking for: ") #entering the word we are checking
print(check, "is in:", wordcheck,":","True/False:", check in wordcheck) #checks if the input is in the string
print(check, "is in:", wordcheck,":","True/False:", check not in wordcheck) #checks if the input is NOT in the string

######################################################

message = "Welcome to the meeting Brian"
print(message.title()) #converts the starting letter of each word to a capital letter

######################################################

address = ["Brian", "3015 Parkerhill Road", "Canada", "ON", "L5B 4B2"] #a list of strings containing an address
address = " | ".join(address) #will join each item in the list and add | in between each item in the list
print(address)

schoolname = ["S","h","e","r","i","d","a","n"]
schoolname = "".join(schoolname) #will join each item in the list with whatever you put in between ""
print(schoolname)

######################################################

print("Hello my name is \"Brian\", nice to meet you") #\"\" allows me to add double quotes inside of other double quotes 
print("Title:\t\tPython Programming\nQuanitity:\t5") #\t allows me to add a tab in between words
print("C:\\BriansPC\\Documents") #you must use \\ if you want to display a backward slash \

######################################################

name = input("Enter your name: ")
greeting = "Hello, {}!".format(name)
print(greeting)

instructor = input("Enter the prof's name: ")
instructor = instructor.capitalize() #capitalizes the first letter of the previous input
subject = input("Enter the name of the course: ")
subject = subject.capitalize() #capitalizes the first letter of the previous input
term = input("Enter the term: ")
term = term.capitalize() #capitalizes the first letter of the previous input
print("{} will teach {} in term {}".format(instructor, subject, term)) #format will plug into the three {} placeholders using instructor, subject, and term
#print("{2} will teach {1} in term {0}".format(instructor, subject, term)) #You can also plug index numbers into the place holders to choose which order to print the variables in

######################################################

######!!!!!NEGATIVE MEANS AFTER THE WORD OR ITEM, POSITIVE MEANS BEFORE THE WORD OR ITEM!!!!!#####

firstname = "Raed"
lastname = "Karim"
print("%s%15s" %(firstname, lastname)) #places 11 space between Raed and Karim because Raed is already 4 characters long 15-4 = 11

firstname = input("Please enter your first name: ")
print("%15s" %firstname) #will place the amount of spaces before the first name depending how many characters it is after 15 - input
print("%-15s" %firstname) #places spaces after your first name, also 15 - input

print("%10d" %123456)
print("%-10d" %1234)
print("%-10d%-10d%-10d" %(123, 456, 789), end="|")

print("960987392750127")
print("%-4d%10d" %(1, 900))
print("%-4d%10d" %(2, 9000))
print("%-4d%10d" %(3, 90000))
print("%-4d%10d" %(4, 9000000))

print("%-15s%-15d%s%-15.2f"%("Sales1", 8, "$", 1200.0))
print("%-15s%-15d%s%-15.2f"%("Sales2", 11, "$", 1345.8))
print("%-15s%-15d%s%-15.2f"%("Sales3", 9, "$", 1778.8))

x = 123.45678
print("1234567890")
print("%10.4f" %x) #prints up to 4 decimal points
print("%-10.2f" %x) #prints up to 2 decimal points


######################################################

age, city = input("Enter your age and your city seperated with a comma: ").split(",")
print (int(age) >= 65 and city == "Toronto")

age = 65; status = "retired"
print (age >=65 or age <=18 or status == "retired")
print ((age >=65 and status == "retired") or age < 18) #paranthesis is used to calrify order or precedence, so it will check the first block first no matter what

grade = 84
passed = (grade >= 50)
#passed = "Congrats! You passed" # youcan also assign the value of true a new string
print("Passed: ", passed)
