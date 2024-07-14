from .Score import Score
from .Question import Question


class Quiz:

    def __init__(self, question_data):
        self.__questions = self.__create_questions(question_data)
        self.__nr_question = 0
        self.__score = Score()

    @staticmethod
    def __create_questions(question_data):
        questions = []
        for question in question_data:
            questions.append(Question(question["text"], question["answer"].lower()))
        return questions

    def play_current_question(self):
        print()
        current_question = self.__questions[self.__nr_question]
        self.__nr_question += 1
        guess = current_question.user_answer(self.__nr_question)
        current_question.check_answer(guess, self.__score)
        current_question.print_correct_answer()
        self.__score.print_score("current", self.__nr_question)

    def show_result(self):
        print()
        print("You've completed the quiz.")
        self.__score.print_score("final", self.__nr_question)

    def has_questions(self):
        return self.__nr_question < len(self.__questions)
