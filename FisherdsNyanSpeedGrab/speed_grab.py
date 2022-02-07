import random
import play

penguin_speed = 5
polar_bear_speed = 6
score_needed_to_win = 5

# Background
play.new_image(
    image='background.jpeg',
    size=100
)

penguin_scoreboard = play.new_text(
    words='Penguin: 0',
    x=play.screen.left + 120,
    y=play.screen.top - 20,
    angle=0,
    font=None,
    font_size=50,
    color='black',
    transparency=100
)

bear_scoreboard = play.new_text(
    words='Polar Bear: 0',
    x=play.screen.right - 140,
    y=play.screen.top - 20,
    angle=0,
    font=None,
    font_size=50,
    color='black',
    transparency=100
)

polar_bear = play.new_image(
    image='polar_bear.png',
    x=-200,
    y=0,
    angle=0,
    size=20,
    transparency=100
)

penguin = play.new_image(
    image='penguin.png',
    x=200,
    y=0,
    angle=0,
    size=20,
    transparency=100
)

penguin.score = 0
polar_bear.score = 0

fish = play.new_image(
    image='fish1.png',
    size=40
)


async def move_the_fish():
    fish_images = ['fish1.png', 'fish2.png']
    fish.image = random.choice(fish_images)
    while True:
        fish.go_to(play.random_position())
        if fish.distance_to(polar_bear) > 200 and fish.distance_to(penguin) > 200:
            break
    bear_scoreboard.words = f"Penguin: {penguin.score}"
    penguin_scoreboard.words = f"Polar Bear: {polar_bear.score}"

    if penguin.score == score_needed_to_win or polar_bear.score == score_needed_to_win:
        if polar_bear.score > penguin.score:
            message = "Polar Bear wins!"
        else:
            message = "Penguin wins!"
        play.new_text(
            words=message,
            font_size=50,
            color='black'
        )
        while True:
            await play.timer(seconds=0.5)


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


def move_on_key_pressed_udlr(sprite, speed):
    move_on_key_pressed(sprite, speed, 'up', 'down', 'left', 'right')


def move_on_key_pressed_wasd(sprite, speed):
    move_on_key_pressed(sprite, speed, 'w', 's', 'a', 'd')

#Optional fish move on start...

# @play.when_program_starts
# async def do():
#   await move_the_fish()

@play.repeat_forever
async def do():
    move_on_key_pressed_udlr(penguin, penguin_speed)
    move_on_key_pressed_wasd(polar_bear, polar_bear_speed)
    if penguin.is_touching(fish):
        penguin.score += 1
        await move_the_fish()
    if polar_bear.is_touching(fish):
        polar_bear.score += 1
        await move_the_fish()

play.start_program()