from data import question_data
from classes.Quiz import Quiz


def main():

    game = Quiz(question_data)
    while game.has_questions():
        game.play_current_question()
    game.show_result()

    return 0


main()
