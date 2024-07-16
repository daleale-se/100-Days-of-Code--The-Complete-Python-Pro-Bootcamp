import turtle


def paddle_a_up():
    global a_speed_y

    a_speed_y = +15


def paddle_a_down():
    global a_speed_y

    a_speed_y = -15


def paddle_a_left():
    global a_speed_x

    a_speed_x = -15


def paddle_a_right():
    global a_speed_x

    a_speed_x = +15


def paddle_a_stop_y():
    global a_speed_y

    a_speed_y = 0


def paddle_a_stop_x():
    global a_speed_x

    a_speed_x = 0


def update_frame():
    x, y = paddle_a.position()

    y += a_speed_y
    x += a_speed_x

    paddle_a.goto(x, y)

    # here update position for other objects - ie. move ball

    # run again after 50ms
    wn.ontimer(update_frame, 50)  # 50ms means ~20 FPS (Frames Per Second) (1000/50 = 20)


# --- main ---

# default values at start
a_speed_x = 0
a_speed_y = 0

wn = turtle.Screen()
paddle_a = turtle.Turtle()

# run first time after 50ms
wn.ontimer(update_frame, 50)  # 50ms means ~20 FPS (Frames Per Second) (1000ms / 50ms = 20)

# binds
wn.onkeypress(paddle_a_up, "Up")
wn.onkeypress(paddle_a_down, "Down")
wn.onkeypress(paddle_a_left, "Left")
wn.onkeypress(paddle_a_right, "Right")

wn.onkeyrelease(paddle_a_stop_y, "Up")
wn.onkeyrelease(paddle_a_stop_y, "Down")
wn.onkeyrelease(paddle_a_stop_x, "Left")
wn.onkeyrelease(paddle_a_stop_x, "Right")

wn.listen()
wn.mainloop()
