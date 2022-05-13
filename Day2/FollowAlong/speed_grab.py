import play
import random

p1_scoreboard = play.new_text(
    words='P1: 0',
    x=play.screen.left + 90,
    y=play.screen.top - 20,
    font_size=50,
)

p2_scoreboard = play.new_text(
    words='P2: 0',
    x=play.screen.right - 100,
    y=play.screen.top - 20,
    font_size=50,
)

p1 = play.new_image(
    image='images/mario.png',
    x=-200,
    y=0,
    size=5
)

p2 = play.new_image(
    image='images/luigi.png',
    x=200,
    y=0,
    size=7,
)

p1.score = 0
p2.score = 0

target = play.new_image(
    image='images/coin.png',
    x=random.randint(-250, 250),
    y=random.randint(-250, 250),
    size=20
)


def keep_sprite_on_screen(p):
    if p.x < play.screen.left:
        p.x = play.screen.left
    if p.y < play.screen.bottom:
        p.y = play.screen.bottom
    if p.x > play.screen.right:
        p.x = play.screen.right
    if p.y > play.screen.top:
        p.y = play.screen.top


@play.repeat_forever
async def do():
    if play.key_is_pressed('up'):
        p2.y += 10
    if play.key_is_pressed('down'):
        p2.y -= 10
    if play.key_is_pressed('left'):
        p2.x -= 10
    if play.key_is_pressed('right'):
        p2.x += 10
    keep_sprite_on_screen(p2)

    if play.key_is_pressed('w'):
        p1.y += 10
    if play.key_is_pressed('s'):
        p1.y -= 10
    if play.key_is_pressed('a'):
        p1.x -= 10
    if play.key_is_pressed('d'):
        p1.x += 10
    keep_sprite_on_screen(p1)

    if p1.is_touching(target):
        p1.score += 1
        p1_scoreboard.words = f"P1: {p1.score}"
        move_target()

    if p2.is_touching(target):
        p2.score += 1
        p2_scoreboard.words = f"P2: {p2.score}"
        move_target()


def move_target():
    target.x = random.randint(-250, 250)
    target.y = random.randint(-250, 250)
    while p1.is_touching(target) or p2.is_touching(target):
        target.x = random.randint(-250, 250)
        target.y = random.randint(-250, 250)


play.start_program()
