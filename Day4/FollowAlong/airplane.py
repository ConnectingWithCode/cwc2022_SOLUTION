import play

background = play.new_image("background.png")
message = play.text("", y=-250)
airplane = play.new_image("plane.png", x=-400, y=-300, size=20)
airplane.counter = 0
parrots = []
dragons = []
airplane.is_game_over = False


@play.when_program_starts
def program_starts():
    for k in range(10):
        parrot = play.new_image("parrot.png", size=20)
        parrot.go_to(play.random_position())
        parrots.append(parrot)
    for k in range(3):
        dragon = play.new_image("dragon.png", size=20)
        dragon.go_to(play.random_position())
        dragon.y += 200
        dragons.append(dragon)


@play.repeat_forever
def forever_loop():
    if airplane.is_game_over:
        return

    airplane.point_towards(play.mouse)
    airplane.move(5)

    for parrot in parrots:
        if parrot.is_touching(airplane):
            airplane.counter += 1
            print(f"Birds = {airplane.counter}")
            message.words = f"Birds = {airplane.counter}"
            parrot.hide()
            parrot.x = 2000

    for dragon in dragons:
        dragon.point_towards(airplane)
        dragon.move(1)
        if dragon.is_touching(airplane):
            message.words = "Got ya!"
            airplane.go_to(-400, -300)

    if airplane.counter == 10:
        message.words = "You win!"
        airplane.is_game_over = True


play.start_program()
