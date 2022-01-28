import pygame
import rosegame as rg


def setup(game):
    print("Setup stuff")
    game.my_fighter = rg.Sprite(game, "fighter.png", 40, 300)


def loop(game):
    if game.is_key_pressed(pygame.K_UP):
        game.my_fighter.move(0, -5)
    if game.is_key_pressed(pygame.K_DOWN):
        game.my_fighter.move(0, 5)
    if game.is_key_pressed(pygame.K_LEFT):
        game.my_fighter.move(-5, 0)
    if game.is_key_pressed(pygame.K_RIGHT):
        game.my_fighter.move(5, 0)

    game.my_fighter.draw()


rg.init(setup, loop)
