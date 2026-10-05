# Character Counter
text = input("Enter some text: ")

print("Total characters:", len(text))
print("Characters excluding spaces:", len(text.replace(" ", "")))
