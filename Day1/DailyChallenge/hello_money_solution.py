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
    message.money_cents += 100
    update_display()

@quarter_button.when_clicked
def do():
    print("You clicked the quarter button")
    message.money_cents += 25
    update_display()

@dime_button.when_clicked
def do():
    print("You clicked the dime button")
    message.money_cents += 10
    update_display()

@nickel_button.when_clicked
def do():
    print("You clicked the nickel button")
    message.money_cents += 5
    update_display()

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