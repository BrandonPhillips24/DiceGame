import random

number = random.randint(1,100)

print("What is your name?")

name = input("")

print("Okay " + name + ", I am thinking of a number between 1 and 100; You have ten tries to guess it")

game = True
attempt = 1
while (game):
    guess = input("Enter your guess(attempt %d" %attempt + "): ")

    try:
       int(guess)
    except:
        print("You can't do that man")
        exit()

    if int(guess) == number:
        print("You are correct!!!")
        game = False
    else:
        attempt = attempt + 1
        if (attempt < 11) & (int(guess) > number):
            print("Too high, try again")
        elif (attempt < 11) & (int(guess) < number):
            print("Too low, try again")
        else:
            print("You lose!")
            game = False

