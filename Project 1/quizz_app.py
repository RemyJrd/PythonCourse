import random

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def shuffle_questions(self):
        random.shuffle(self.questions)

    def shuffle_choices(self, question):
        random.shuffle(question.choices)

    def display_question(self, question, choice_letters):
        print(question.question)
        self.shuffle_choices(question)
        for i, choice in enumerate(question.choices):
            print(f"{choice_letters[i]}. {choice}")

    def get_answer_choice(self):
        choice = input("Your answer (A/B/C): ").upper()
        while choice not in ["A", "B", "C"]:
            choice = input("Invalid choice. Please choose A, B, or C: ").upper()
        return choice

    def check_answer(self, question, choice):
        if question.choices[ord(choice) - 65] == question.answer:
            print("Correct!")
            self.score += 1
        else:
            print(f"Incorrect. The correct answer is {question.answer}.")

    def run_quiz(self):
        self.shuffle_questions()
        choice_letters = ['A', 'B', 'C']
        for question in self.questions:
            self.display_question(question, choice_letters)
            choice = self.get_answer_choice()
            self.check_answer(question, choice)
        self.display_score()

    def display_score(self):
        print(f"Final score: {self.score}/{len(self.questions)}")
        print("Correct answers:")
        for i, question in enumerate(self.questions):
            print(f"{i + 1}. {question.answer}")