# https://github.com/replit/play
# pip install replit-play

import play

head = play.new_circle(
    color="gold",
    x=0,
    y=0,
    radius=250,
)

left_eye = play.new_circle(
    color="white",
    x=-100,
    y=120,
    radius=50,
)

right_eye = play.new_circle(
    color="white",
    x=100,
    y=120,
    radius=50,
)

mouth = play.new_box(
    color="black",
    x=0,
    y=-125,
    width=300,
    height=10,
)

nose = play.new_circle(
    color="black",
    x=0,
    y=0,
    radius=20,
)

left_eye_middle = play.new_circle(
    color="black",
    x=-90,
    y=125,
    radius=20,
)

right_eye_middle = play.new_circle(
    color="black",
    x=110,
    y=125,
    radius=20,
)

play.new_text()

play.start_program()
