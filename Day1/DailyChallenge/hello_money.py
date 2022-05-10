import play

penny_button = play.new_image(
        "images/penny.png",
        x=-300,
        y=50,
        size=20
)

@penny_button.when_clicked
def do():
    print("You clicked the penny button")
    message.money_cents += 1
    update_display()

message = play.new_text(
    "$0.00",
    y = -200,
    font_size = 70
)

message.money_cents = 0


def update_display():
    message.words = f"${message.money_cents / 100:.2f}"

play.start_program()