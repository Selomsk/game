import random

print("\t welcome to my Guess my Game")
print("\t-" * 30)
print("\t| \t GUESS NUMBER GAME   |")
print("\t-" * 30)

r = random.randrange(1, 10)
attempts = 4

while attempts > 0:
    guess = int(input("\n\nGuess a number between 1 and 10: "))
    if guess == r:
        print("\n\tCongratulations, you have guessed the number correctly")
        break
    elif guess < r:
        print("\n\tGuess again, you are way down the answer")
    else:
        print("\n\tGuess again, you are too far from the results")
    attempts -= 1

if attempts == 0:
    print("\n\tYou have run out of attempts. The correct answer was", r)
    
