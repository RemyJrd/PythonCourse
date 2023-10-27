import unittest
from quizz_app import Quiz
from question_app import Question

class TestQuiz(unittest.TestCase):
    def setUp(self):
        self.questions = [
            Question("Q1", [], "A"),
            Question("Q2", [], "B"),
            Question("Q3", [], "C"),
        ]
        self.quiz = Quiz(self.questions)

    def test_shuffle_questions(self):
        initial_order = self.quiz.questions.copy()
        self.quiz.shuffle_questions()
        self.assertNotEqual(self.quiz.questions, initial_order)

    def test_shuffle_choices(self):
        question = Question("Test Question", ["Choice 1", "Choice 2", "Choice 3"], "Choice 2")
        quiz = Quiz([question])
        initial_choices = question.choices.copy()
        self.quiz.shuffle_choices(question)
        self.assertNotEqual(question.choices, initial_choices)

if __name__ == "__main__":
    unittest.main()