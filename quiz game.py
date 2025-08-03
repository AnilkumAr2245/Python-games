questions=(("Which planet in our solar system has the most moons?",
            "What does “HTTP” stand for in a website address?",
            "Who was the main narrator of the Mahabharata?",
            "Which animal can hold its breath the longest underwater?",
            "Who was the first President of independent India?",
            "What is the next number in the sequence: 0, 2, 6, 12, 20, ?",
            "Which country is known for inventing paper?",
            "What is the capital city of the United States?",
            "What’s the smallest bone in the human body?",
            "In which movie series would you find the character “Jack Sparrow”?"))
options=(("A.Earth","B.Jupiter","C.Saturn","D.Neptune"),
         ("A.HyperText Transfer Protocol","B.HighText Transfer Process","C.HyperTransfer Text Process","D.Host Transfer Text Protocol"),
         ("A.Vyasa","B.Krishna","C.Sanjay","D.Arjuna"),
         ("A.Elephant","B.Sloth","C.Cuvier's beaked whale","D.Sea lion"),
         ("A.Jawaharlal Nehru","B.Dr. Rajendra Prasad","C.Sardar Vallabhbhai Patel","D. B. R. Ambedkar"),
         ("A.30","B.28","C.24","D.22"),
         ("A.Egypt","B.India","C.China","D.Greece"),
         ("A.New York","B.Washington, D.C.","C.Los Angeles","D.Chicago"),
         ("A.Femur","B.Stirrup (Stapes)","C.Radius","D.Ulna"),
         ("A.Harry Potter","B.Pirates of the Caribbean","C.Lord of the Rings","D.Star Wars"))
answers=("C","A","C","C","B","A","C","B","B","B")
guesses=[]
score=0
question_num=0
print("---🧠WELCOME TO PUZZLE---")
for question in questions:
    print("_________________________________________")
    print(question)
    for option in options[question_num]:
        print(option)
    guess = input("Enter the option(A,B,C,D):").upper()
    while guess not in ["A","B","C","D"]:
        print("😬INVALID OPTION!")
        guess = input("Enter the option(A,B,C,D):").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("✅CORRECT!")
    else:
        print(f"❌WRONG! {answers[question_num]} is the correct answer")

    question_num += 1
print("_____________________________________")
print("              RESULT                 ")
print("_____________________________________")
for answer in answers:
    print(answer,end=",")
print()
for guess in guesses:
    print(guess,end=",")
print()
print(f"🤖GAME OVER! Your score is:{score} out {len(questions)}")
if score == len(questions):
    print("PERFECT SCORE!")
elif score >=7:
    print("GOOD JOB!")
elif score>=4:
    print("KEEP FOCUSING")
else:
    print("BETTER LUCK NEXT TIME!")

