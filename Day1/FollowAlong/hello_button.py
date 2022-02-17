import play

inc_button = play.new_image(
        "plus.png",
        x=200
)


dec_button = play.new_image(
        "minus.png",
        x=-200
)


reset_button = play.new_image(
        "reset.png",
        size=18
)

message = play.new_text(
    "count = 0",
    y = 200,
    font_size = 70
)

message.counter = 0

@inc_button.when_clicked
def bob1():
    print("You clicked inc")
    message.counter = message.counter + 1
    message.words = "count = " + str(message.counter)

@dec_button.when_clicked
def do3():
    print("You clicked dec")
    message.counter = message.counter - 1
    message.words = f"count = {message.counter:.2f}"

@reset_button.when_clicked
def do():
    print("You clicked reset")
    message.counter = 0
    message.words = "count = " + str(message.counter)

play.start_program()