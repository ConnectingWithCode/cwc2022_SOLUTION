import play

penny_button = play.new_image(
        "images/penny.png",
        x=-300,
        y=50,
        size=20
)

nickel_button = play.new_image(
        "images/nickel.png",
        x=-115,
        y=50,
        size=18
)

dime_button = play.new_image(
        "images/dime.png",
        x=75,
        y=50,
        size=14
)

quarter_button = play.new_image(
        "images/quarter.png",
        x=275,
        y=50,
        size=28
)

dollar_button = play.new_image(
        "images/dollar_bill.jpeg",
        y=225,
        size=25
)

@dollar_button.when_clicked
def do():
    print("You clicked the one dollar button")

@quarter_button.when_clicked
def do():
    print("You clicked the quarter button")

@dime_button.when_clicked
def do():
    print("You clicked the dime button")

@nickel_button.when_clicked
def do():
    print("You clicked the nickel button")

@penny_button.when_clicked
def do():
    print("You clicked the penny button")


# dec_button = play.new_image(
#         "minus.png",
#         x=-200
# )
#
#
# reset_button = play.new_image(
#         "reset.png",
#         size=18
# )
#
# message = play.new_text(
#     "count = 0",
#     y = 200,
#     font_size = 70
# )

# message.counter = 0

# @inc_button.when_clicked
# def do():
#     print("You clicked inc")
#     message.counter = message.counter + 1
#     message.words = "count = " + str(message.counter)
#
# @dec_button.when_clicked
# def do():
#     print("You clicked dec")
#     message.counter = message.counter - 1
#     message.words = f"count = {message.counter:.2f}"
#
# @reset_button.when_clicked
# def do():
#     print("You clicked reset")
#     message.counter = 0
#     message.words = "count = " + str(message.counter)

play.start_program()