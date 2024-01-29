# -*- coding: utf-8 -*-
"""Game_Louis-Melchior.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15YcZXJdjCLi4zh740chqa23X9_hIeCHz
"""

import sys

def ask_question(question, correct_answer):
    print(question)
    user_answer = input("Your answer: ").strip().lower()
    return user_answer == correct_answer.strip().lower()

def run_quiz(questions, high_score):
    score = 0
    for question, correct_answer in questions:
        if ask_question(question, correct_answer):
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was: {correct_answer}\n")

    if score > high_score:
        print(f"New high score! You scored {score}.\n")
        return score
    else:
        print(f"Your score was {score}. The high score is {high_score}.\n")
        return high_score

def main():
    # Questions format: ("Question", "Correct Answer")
    questions = [
        ("What is the capital of France?", "Paris"),
        ("Who wrote 'To be or not to be'?", "William Shakespeare"),
        ("What is the smallest planet in our solar system?", "Mercury"),
        ("In what year did the Titanic sink?", "1912"),
        ("What is the chemical symbol for gold?", "Au"),
        ("Who painted the Mona Lisa?", "Leonardo da Vinci"),
        ("What is the hardest natural substance on Earth?", "Diamond"),
        # More questions can be added here.
    ]

    high_score = 0
    total_questions = len(questions)

    while True:
        high_score = run_quiz(questions, high_score)
        print(f"Quiz complete! High score is {high_score} out of {total_questions}.")
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            break

if __name__ == "__main__":
    main()