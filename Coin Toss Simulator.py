# Coin Toss Simulator
import random

print("Coin Toss Simulator")

while True:
    result = random.choice(["Heads", "Tails"])
    print("Result:", result)

    again = input("Toss again? (y/n): ").lower()
    if again != "y":
        print("Goodbye!")
        break
