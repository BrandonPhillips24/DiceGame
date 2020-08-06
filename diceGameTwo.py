import random

player = random.randint(1,6)
cp = random.randint(1,6)


if player > cp:
    result = "You win"
elif player < cp:
    result = "You lose"
else:
    result = "You tied"

print("you rolled a %d" %player + " and the computer rolled a %d" %cp + ", " + result)