# Unit Converter
print("Simple Unit Converter")
print("1. Kilometers to Miles")
print("2. Miles to Kilometers")
print("3. Kilograms to Pounds")
print("4. Pounds to Kilograms")
print("5. Meters to Feet")
print("6. Feet to Meters")

choice = input("Choose an option (1-6): ")
value = float(input("Enter value: "))

if choice == "1":
    print("Miles:", value * 0.621371)
elif choice == "2":
    print("Kilometers:", value / 0.621371)
elif choice == "3":
    print("Pounds:", value * 2.20462)
elif choice == "4":
    print("Kilograms:", value / 2.20462)
elif choice == "5":
    print("Feet:", value * 3.28084)
elif choice == "6":
    print("Meters:", value / 3.28084)
else:
    print("Invalid choice.")
