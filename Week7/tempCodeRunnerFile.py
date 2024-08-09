
count = 0
while count < 3:
    score = int(input("Enter your 3 scores (0-100): "))
    if score <= 0 or score <= 100:
        count = count + 1
        scoreSum = scoreSum + score
    else:
        print("Score must be greater than 0 or less than 100, please try again.")

print(f"The total sum of the 3 scores is {scoreSum}")