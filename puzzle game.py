# Puzzle Quiz Game

questions = [
    {
        "question": "1. Which planet in our solar system has the most moons?",
        "options": ["A) Earth", "B) Jupiter", "C) Saturn", "D) Neptune"],
        "answer": "C"
    },
    {
        "question": "2. What does 'HTTP' stand for in a website address?",
        "options": ["A) HyperText Transfer Protocol", "B) HighText Transfer Process", "C) HyperTransfer Text Process",
                    "D) Host Transfer Text Protocol"],
        "answer": "A"
    },
    {
        "question": "3. Who was the main narrator of the Mahabharata?",
        "options": ["A) Vyasa", "B) Krishna", "C) Sanjaya", "D) Arjuna"],
        "answer": "C"
    },
    {
        "question": "4. Which animal can hold its breath the longest underwater?",
        "options": ["A) Elephant", "B) Sloth", "C) Cuvier's beaked whale", "D) Sea lion"],
        "answer": "C"
    },
    {
        "question": "5. Who was the first President of independent India?",
        "options": ["A) Jawaharlal Nehru", "B) Dr. Rajendra Prasad", "C) Sardar Vallabhbhai Patel",
                    "D) B. R. Ambedkar"],
        "answer": "B"
    },
    {
        "question": "6. What is the next number in the sequence: 2, 6, 12, 20, ?",
        "options": ["A) 30", "B) 28", "C) 24", "D) 22"],
        "answer": "A"
    },
    {
        "question": "7. Which country is known for inventing paper?",
        "options": ["A) Egypt", "B) India", "C) China", "D) Greece"],
        "answer": "C"
    },
    {
        "question": "8. What is the capital city of the United States?",
        "options": ["A) New York", "B) Washington, D.C.", "C) Los Angeles", "D) Chicago"],
        "answer": "B"
    },
    {
        "question": "9. What’s the smallest bone in the human body?",
        "options": ["A) Femur", "B) Stirrup (Stapes)", "C) Radius", "D) Ulna"],
        "answer": "B"
    },
    {
        "question": "10. In which movie series would you find the character 'Jack Sparrow'?",
        "options": ["A) Harry Potter", "B) Pirates of the Caribbean", "C) Lord of the Rings", "D) Star Wars"],
        "answer": "B"
    }
]

score = 0

print("🧠 Welcome to the Puzzle Quiz Game!")
print("------------------------------------\n")

for q in questions:
    print(q["question"])
    for option in q["options"]:
        print(option)

    user_answer = input("Your answer (A/B/C/D): ").strip().upper()

    if user_answer == q["answer"]:
        print("✅ Correct!\n")
        score += 1
    else:
        print(f"❌ Wrong! The correct answer was {q['answer']}.\n")

print(f"🎉 Game Over! You scored {score} out of {len(questions)}.")

if score == len(questions):
    print("🏆 Perfect Score! You're a quiz master!")
elif score >= 7:
    print("👏 Great job!")
elif score >= 4:
    print("🙂 Not bad, keep practicing!")
else:
    print("😅 Better luck next time!")

