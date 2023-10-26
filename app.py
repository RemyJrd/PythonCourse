import random

class Question:
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

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

if __name__ == "__main__":
    questions = [
        Question("What is the capital of France?", ["Paris", "London", "Berlin"], "Paris"),
        Question("What is the largest planet in our solar system?", ["Jupiter", "Saturn", "Neptune"], "Jupiter"),
        Question("What is the smallest country in the world?", ["Monaco", "Vatican City", "San Marino"], "Vatican City"),
        Question("What is the highest mountain in the world?", ["Mount Everest", "K2", "Kangchenjunga"], "Mount Everest"),
        Question("What is the largest ocean in the world?", ["Atlantic Ocean", "Indian Ocean", "Pacific Ocean"], "Pacific Ocean"),
        Question("What is the smallest continent in the world?", ["Europe", "Australia", "South America"], "Australia"),
        Question("What is the largest country in the world by area?", ["Russia", "Canada", "China"], "Russia"),
        Question("What is the hottest planet in our solar system?", ["Venus", "Mercury", "Mars"], "Venus"),
        Question("What is the longest river in the world?", ["Nile", "Amazon", "Yangtze"], "Nile"),
        Question("What is the largest mammal in the world?", ["Elephant", "Blue Whale", "Giraffe"], "Blue Whale")
    ]
    quiz = Quiz(questions)
    quiz.run_quiz()