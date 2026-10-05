# Multiplication Table Generator
number = int(input("Enter a number: "))

print(f"\nMultiplication table of {number}")

for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")
