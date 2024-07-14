class Score:
    def __init__(self):
        self.__value = 0

    def increase(self):
        self.__value += 1

    def print_score(self, state ,nr_question):
        print(f"Your {state} score is: {self.__value}/{nr_question}")
