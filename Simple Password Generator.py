# Simple Password Generator
import random
import string

length = int(input("Enter password length: "))

if length <= 0:
    print("Password length must be greater than 0.")
else:
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for _ in range(length))
    print("Generated password:", password)
