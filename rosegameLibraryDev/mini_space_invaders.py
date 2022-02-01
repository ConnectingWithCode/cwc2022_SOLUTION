import pygame
import rosegame as rg
import space_invaders_enemy_fleet as enemy


##########################################################################################
# Disclaimer!
#
# This app is OBVIOUSLY too hard for the camp, I just wanted to push the rosegame library
#   so to see if it could handle more complex needs.
#
# MAYBE we could provide the EnemyFleet class and then they could do the rest.
##########################################################################################


def setup(game):
    game.my_fighter = rg.Sprite(game, "images/fighter.png", 40, 300)
    game.missiles = []
    game.enemy_fleet = enemy.EnemyFleet(3)


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
        fighter_top_y = game.my_fighter.center.y - game.my_fighter.height / 2
        laser_bottom_pt = rg.Point(game.my_fighter.center.x, fighter_top_y)
        laser_top_pt = rg.Point(game.my_fighter.center.x, fighter_top_y - 8)
        game.missiles.append(rg.Line(game, laser_top_pt, laser_bottom_pt))

    # Draw your Sprites
    game.my_fighter.draw()
    for missile in game.missiles:
        game.enemy_fleet.check_missle(missile)
        missile.move(0, -2)
        missile.draw()

    game.enemy_fleet.check_for_game_over(game.my_fighter)
    game.enemy_fleet.move()
    game.enemy_fleet.draw()


rg.init(setup, loop)
