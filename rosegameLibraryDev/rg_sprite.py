import rosegame as rg


def setup(game):
    print("TODO: Setup stuff")
    game.my_fighter = rg.Sprite(game, "fighter.png", 40, 300)


def loop(game):
    print("Loop")
    game.my_fighter.draw()
    game.my_fighter.move(0, -1)


rg.init(setup, loop)
