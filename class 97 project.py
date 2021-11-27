import random

randomNumber = random.randint(1,9)
chance = 0

print("Guess a number")

while chance<5 :
    guess = int(input("enter your guess"))
    if guess == randomNumber:
        print("congratulations you are right")
        break
    elif guess < randomNumber:
        print("the number you guessed is less than the random number")
    else:
        print("the number you guessed is greater than the random number")
    chance = chance+1

if chance >= 5:
    print("Sorry,your guesses were wrong")



