# Temperature Converter
print("Temperature Converter")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

choice = input("Choose an option (1/2): ")
temperature = float(input("Enter temperature: "))

if choice == "1":
    fahrenheit = (temperature * 9 / 5) + 32
    print(f"Fahrenheit: {fahrenheit:.2f}")
elif choice == "2":
    celsius = (temperature - 32) * 5 / 9
    print(f"Celsius: {celsius:.2f}")
else:
    print("Invalid choice.")
