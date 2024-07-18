import turtle
import pandas
from pandas import DataFrame


def main():
    screen = turtle.Screen()
    screen.title("US States Game")

    text = turtle.Turtle()
    text.penup()
    text.hideturtle()
    text.color("black")

    image = "blank_states_img.gif"
    screen.addshape(image)
    turtle.shape(image)

    data = pandas.read_csv("50_states.csv")
    stored_states = []

    score = 0
    while score < 50:
        answer_state = screen.textinput(title=f"{score}/50 States Correct", prompt="What's another state name?").title()
        if answer_state == "Exit":
            break
        if len(data[data.state == answer_state]) > 0:
            if answer_state not in stored_states:
                score += 1
                row_data: DataFrame = data[data.state == answer_state]
                # x_cor = float(row_data.to_numpy()[0][1])
                # y_cor = float(row_data.to_numpy()[0][2])
                text.goto(row_data.x.item(), row_data.y.item())
                text.write(arg=f"{answer_state}", font=("Sans", 10, "normal"), move=False, align="center")
                stored_states.append(answer_state)

    df = data.copy()
    for state in stored_states:
        df = df.drop(df[df.state == state].index)
    missing_states = df.state
    missing_states.to_csv("states_to_learn.csv", index=False)

    screen.exitonclick()


main()
