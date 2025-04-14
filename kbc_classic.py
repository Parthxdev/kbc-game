# KBC Quiz Game

# List of Question , Options and their correct answers
questions = [
    {   "question" : "What is the capital of India?",
        "options" : ["A. Mumbai","B. New Delhi","C. Kolkata","D. Chennai"],
        "answer": "B"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Saturn"] ,
        "answer": "B" ,
    },
    {
        "question" : "How many continents are there on Earth?",
        "options" : ["A. 5", "B. 6", "C. 7", "D. 8"],
        "answer" : "C"
    },
    {
        "question" :"What is the national animal of India?",
        "options" :  ["A. Elephant", "B. Tiger", "C. Lion", "D. Deer"],
        "answer": "B"
    },
    {
        "question" :"Which city is known as the Silicon Valley of India ?" ,
        "options" :  ["A. Mumbai", "B. Banglore", "C. Chennai", "D. Delhi"],
        "answer": "B"
    }
]

#prizes
your_prize = [1000,5000,10000,15000,20000]
total_winnings = 0

print("🎉 Welcome to KBC (Kaun Banega Crorepati)!  🎉")


#start loop on question , option, and their answer one by one..
for i ,q in enumerate(questions):
    print(f"Question {i+1}: {q['question']}")
    for option in q["options"]:
        print(option)

    answer = input("Enter Your Answer as a A/B/C/D :").strip().upper()

    if answer == q["answer"]:
        print("Correct Answer!")
        total_winnings += your_prize[i]
    else:
        print("Wrong Answer")
        break

    print(f"Your total winnings {total_winnings}")
print(f"🎊Congratulations! you taking home ₹{total_winnings}")

