import play
import random

background = play.new_image(image="background.png")
background.is_game_over = False

message = play.new_text('Shark = 0 Octopus = 0', y=-250, font_size=70)

shark = play.new_image(image="shark.png", x=350, y=-250, size=25)
shark.score = 0

octopus = play.new_image(image="octopus.png", x=-350, y=-250, size=25)
octopus.score = 0

fish = play.new_image(image="fish.png", y=250, size=25)


def if_on_edge_stop(sprite):
    if sprite.x < play.screen.left:
        sprite.x = play.screen.left
    if sprite.y < play.screen.bottom:
        sprite.y = play.screen.bottom
    if sprite.x > play.screen.right:
        sprite.x = play.screen.right
    if sprite.y > play.screen.top:
        sprite.y = play.screen.top


def move_on_key_pressed(sprite, speed, up_key, down_key, left_key, right_key):
    if play.key_is_pressed(up_key):
        sprite.y += speed
    if play.key_is_pressed(down_key):
        sprite.y -= speed
    if play.key_is_pressed(left_key):
        sprite.x -= speed
    if play.key_is_pressed(right_key):
        sprite.x += speed
    if_on_edge_stop(sprite)


def move_the_fish():
    message.words = f"Shark = {shark.score} Octopus = {octopus.score}"
    while True:
        fish.go_to(play.random_position())
        if fish.distance_to(shark) > 200 and fish.distance_to(octopus) > 200:
            break


@play.repeat_forever
def forever_loop():
    if background.is_game_over:
        return
    move_on_key_pressed(shark, 10, 'up', 'down', 'left', 'right')
    move_on_key_pressed(octopus, 10, 'w', 's', 'a', 'd')

    if shark.is_touching(fish):
        shark.score = shark.score + 1
        move_the_fish()

    if octopus.is_touching(fish):
        octopus.score = octopus.score + 1
        move_the_fish()

    if shark.score == 10:
        message.words = "Shark Wins!"
        background.is_game_over = True

    if octopus.score == 10:
        message.words = "Octopus Wins!"
        background.is_game_over = True


play.start_program()