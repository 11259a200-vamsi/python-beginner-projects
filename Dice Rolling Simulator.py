# Dice Rolling Simulator
import random

while True:
    input("Press Enter to roll the dice...")
    roll = random.randint(1, 6)
    print("You rolled:", roll)

    again = input("Roll again? (y/n): ").lower()
    if again != "y":
        print("Thanks for playing!")
        break
