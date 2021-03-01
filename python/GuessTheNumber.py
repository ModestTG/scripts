import random
target, guess = random.randint(1, 10), 0
while target != guess:
	guess = int(input("Guess a numb er that is between 1 and 10: "))
print("That's right!")
