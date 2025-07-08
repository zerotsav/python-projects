import random

print("🎲 Welcome to the Dice Rolling Game!")
print("Roll a 6 to win!\n")

while True:
    input("Press Enter to roll the dice...")

    dice = random.randint(1, 6)
    print(f"You rolled a {dice}!")

    if dice == 6:
        print("You win! yayyyyyyyyyyyyyy")
        break
    else:
        again = input("Try again? (y/n): ").lower()
        if again != "y":
            print("Better luck next time! you got this hehe")
            break
