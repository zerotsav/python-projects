import random

print("Welcome to the Number Guessing Game!")

# Generate a random number between 1 and 100
number = random.randint(1, 100)
tries = 0

while True:
    guess = input("Guess a number between 1 and 100: ")

    if not guess.isdigit():
        print("Please enter a valid number.")
        continue

    guess = int(guess)
    tries += 1

    if guess < number:
        print("Too low.")
    elif guess > number:
        print("Too high.")
    else:
        print(f"Correct! You guessed it in {tries} tries.")
        break

