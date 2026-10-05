# Age Calculator
from datetime import date

birth_year = int(input("Enter your birth year: "))
current_year = date.today().year

age = current_year - birth_year

if age < 0:
    print("Invalid birth year.")
else:
    print("Your approximate age is:", age)
