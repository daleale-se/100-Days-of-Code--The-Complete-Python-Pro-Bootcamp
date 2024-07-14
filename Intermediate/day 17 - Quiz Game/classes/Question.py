class Question:

    def __init__(self, text, answer):
        self.__text = text
        self.__answer = answer

    def is_correct(self, guess):
        return self.__answer == guess

    def user_answer(self, nr_question):
        return input(f"Q.{nr_question} {self.__text} (True/False): ").lower()

    def print_correct_answer(self):
        print(f"The correct answer was: {self.__answer}")

    def check_answer(self, guess, score):
        if self.is_correct(guess):
            print("You got it right!")
            score.increase()
        else:
            print("That's wrong!")
