
questions = [
    {
        "question": "What is the capital of Pakistan?",
        "options": ["A. Lahore", "B. Karachi", "C. Islamabad", "D. Quetta"],
        "answer": "C"
    },
    {
        "question": "Which language are we learning?",
        "options": ["A. Java", "B. Python", "C. C++", "D. HTML"],
        "answer": "B"
    },
    {
        "question": "Which one is a Python data type?",
        "options": ["A. Integer", "B. Keyboard", "C. Monitor", "D. Mouse"],
        "answer": "A"
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "options": ["A. //", "B. #", "C. @", "D. &"],
        "answer": "B"
    },
    {
        "question": "Which function is used to display output?",
        "options": ["A. input()", "B. type()", "C. print()", "D. int()"],
        "answer": "C"
    }
]

score = 0

print("===== Welcome to the Python Quiz Game =====")

name = input("Enter your name: ")

print("\nHello", name + "!")

playing = True
while playing:
    print("Answer the following questions.")
    print("Choose A, B, C, or D.\n")

    for question in questions:
        print(question["question"])

        for option in question["options"]:
            print(option)

        answer = input("Your answer: ").upper()

        if answer == question["answer"]:
            print("Correct answer!\n")
            score += 1
        else:
            print("Wrong answer!")
            print("Correct answer:", question["answer"], "\n")

    print("===== Quiz Finished =====")
    print("Player:", name)
    print("Your score:", score, "out of", len(questions))

    if score == len(questions):
        print("Excellent! You got all answers correct.")
    elif score >= 3:
        print("Good job! Keep practicing.")
    else:
        print("Keep learning and try again!")

    replay_choice = input("\nWould you like to play again? (y/n): ").lower()
    if replay_choice == "n":
        playing = False
        print(f"\nThank you for playing, {name}! Goodbye!")
        break

