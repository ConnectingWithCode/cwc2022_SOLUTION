import pygame
import rosegame as rg


def setup(game):
    game.my_fighter = rg.Sprite(game, "fighter.png", 40, 300)
    game.missiles = []


def loop(game):
    if game.is_key_pressed(pygame.K_UP):
        game.my_fighter.move(0, -5)
    if game.is_key_pressed(pygame.K_DOWN):
        game.my_fighter.move(0, 5)
    if game.is_key_pressed(pygame.K_LEFT):
        game.my_fighter.move(-5, 0)
    if game.is_key_pressed(pygame.K_RIGHT):
        game.my_fighter.move(5, 0)

    if game.is_key_newly_pressed(pygame.K_SPACE):
        fighter_center_x = game.my_fighter.center.x
        fighter_top_y = game.my_fighter.center.y - game.my_fighter.height / 2
        laser_bottom_pt = rg.Point(fighter_center_x, fighter_top_y)
        laser_top_pt = rg.Point(fighter_center_x, fighter_top_y - 10)
        game.missiles.append(rg.Line(game, laser_top_pt, laser_bottom_pt))

    # Draw your Sprites
    game.my_fighter.draw()
    for missile in game.missiles:
        missile.move(0, -2)
        missile.draw()


rg.init(setup, loop)
