import nyan
import random

nyan.set_backdrop('light gray')

message = nyan.new_text(
    words="Race to the coin!",
    x=0,
    y=nyan.screen.bottom + 20,
    angle=0,
    font=None,
    font_size=50,
    color='black'
)

p1_scoreboard = nyan.new_text(
    words='P1: 0',
    x=nyan.screen.left + 90,
    y=nyan.screen.top - 20,
    angle=0,
    font=None,
    font_size=50,
    color='black',
)

p2_scoreboard = nyan.new_text(
    words='P2: 0',
    x=nyan.screen.right - 100,
    y=nyan.screen.top - 20,
    angle=0,
    font=None,
    font_size=50,
    color='black'
)

p1 = nyan.new_image(
    image='../assets/mario.png',
    x=-200,
    y=0,
    angle=0,
    size=5
)

p2 = nyan.new_image(
    image='../assets/luigi.png',
    x=200,
    y=0,
    angle=0,
    size=7,
)

p1.score = 0
p2.score = 0

target = nyan.new_image(
    image='../assets/coin.png',
    x=random.randint(-250, 250),
    y=random.randint(-250, 250),
    angle=0,
    size=20
)


def boundary(p):
    if p.x < nyan.screen.left:
        p.x = nyan.screen.left
    if p.y < nyan.screen.bottom:
        p.y = nyan.screen.bottom
    if p.x > nyan.screen.right:
        p.x = nyan.screen.right
    if p.y > nyan.screen.top:
        p.y = nyan.screen.top


@nyan.repeat_forever
async def do():
    if nyan.key_is_pressed('up'):
        p2.y += 10
    if nyan.key_is_pressed('down'):
        p2.y -= 10
    if nyan.key_is_pressed('left'):
        p2.x -= 10
    if nyan.key_is_pressed('right'):
        p2.x += 10
    boundary(p2)

    if nyan.key_is_pressed('w'):
        p1.y += 10
    if nyan.key_is_pressed('s'):
        p1.y -= 10
    if nyan.key_is_pressed('a'):
        p1.x -= 10
    if nyan.key_is_pressed('d'):
        p1.x += 10
    boundary(p1)

    if p1.is_touching(target):
        p1.score += 1
        p1_scoreboard.words = f"P1: {p1.score}"
        target.x = random.randint(-250, 250)
        target.y = random.randint(-250, 250)
        while p1.is_touching(target) or p2.is_touching(target):
            target.x = random.randint(-250, 250)
            target.y = random.randint(-250, 250)

    if p2.is_touching(target):
        p2.score += 1
        p2_scoreboard.words = f"P2: {p2.score}"
        target.x = random.randint(-250, 250)
        target.y = random.randint(-250, 250)
        while p1.is_touching(target) or p2.is_touching(target):
            target.x = random.randint(-250, 250)
            target.y = random.randint(-250, 250)


nyan.start_program()
