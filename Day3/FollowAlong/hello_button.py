import play

# play.new_image(image='Circles.png', size=80)
play.new_image(image='Blue Sky.png', size=80)
inc_button = play.new_image("incButton.png", x=200, y=-40, size=25)
dec_button = play.new_image("decButton.png", x=-200, y=-40, size=25)
reset_button = play.new_image("resetButton.png",  y=-40, size=25)

message = play.new_text("0", y=150, font_size=300, color='purple')
message.counter = 0

@inc_button.when_clicked
def inc_clicked():
    print("You clicked inc")
    message.counter = message.counter + 1
    message.words = message.counter


@dec_button.when_clicked
def dec_clicked():
    print("You clicked dec")
    message.counter = message.counter - 1
    message.words = message.counter


@reset_button.when_clicked
def reset_clicked():
    print("You clicked reset")
    message.counter = 0
    message.words = message.counter


play.start_program()
