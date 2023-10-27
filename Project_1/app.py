from quizz_app import Quiz
from question_app import Question


if __name__ == "__main__":
    questions = [
        Question("What is the capital of France?", ["Paris", "London", "Berlin"], "Paris"),
        Question("What is the capital of the USA?", ["Washington, D.C.", "New York", "Los Angeles"], "Washington, D.C."),
        Question("What is the capital of the UK?", ["London", "Manchester", "Liverpool"], "London"),
        Question("What is the capital of Spain?", ["Madrid", "Barcelona", "Valencia"], "Madrid"),
        Question("What is the capital of Italy?", ["Rome", "Milan", "Florence"], "Rome"),
        Question("What is the capital of Switzerland?", ["Bern", "Zurich", "Geneva"], "Bern"),
        Question("What is the capital of China?", ["Beijing", "Shanghai", "Guangzhou"], "Beijing"),
        Question("What is the capital of Russia?", ["Moscow", "St. Petersburg", "Novosibirsk"], "Moscow"),
        Question("What is the capital of Germany?", ["Berlin", "Munich", "Hamburg"], "Berlin"),
        Question("What is the capital of Belgium?", ["Brussels", "Antwerp", "Ghent"], "Brussels")
    ]  
    quiz = Quiz(questions)
    quiz.run_quiz()
    