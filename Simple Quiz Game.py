# Simple Quiz Game
score = 0

questions = [
    ("What is the capital of India?", "delhi"),
    ("How many days are there in a week?", "7"),
    ("Which language are we using for this project?", "python"),
    ("What is 5 + 3?", "8"),
    ("What is the largest planet in our solar system?", "jupiter")
]

print("Simple Quiz Game")
print()

for question, answer in questions:
    user_answer = input(question + " ").strip().lower()

    if user_answer == answer:
        print("Correct!")
        score += 1
    else:
        print("Wrong!")

print(f"\nYour score is {score}/{len(questions)}.")
