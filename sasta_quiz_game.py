print("📝 Welcome to the Quiz!")

questions = [
    {
        "question": "What is the capital of France?",
        "options": ["1. Paris", "2. London", "3. Rome", "4. Berlin"],
        "answer": "1"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["1. Earth", "2. Mars", "3. Jupiter", "4. Venus"],
        "answer": "2"
    },
    {
        "question": "What is 5 + 7?",
        "options": ["1. 10", "2. 11", "3. 12", "4. 13"],
        "answer": "3"
    }
]

score = 0

for q in questions:
    print("\n" + q["question"])
    for option in q["options"]:
        print(option)
    answer = input("Your answer (1-4): ")

    if answer == q["answer"]:
        print("Correct!")
        score += 1
    else:
        print("Wrong!")

print(f"\nYou got {score} out of {len(questions)} correct!")
print("Thanks for playing!")
