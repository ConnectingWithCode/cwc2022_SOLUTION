import nyan
import random
import time

nyan.set_backdrop('white')

message = nyan.new_text(
    words="Bank your dice rolls!",
    x=0,
    y=nyan.screen.bottom + 20,
    angle=0,
    font=None,
    font_size=50,
    color='black'
)

instruction = nyan.new_text(
    words="First to 20 wins!",
    x=0,
    y=nyan.screen.top - 20,
    angle=0,
    font=None,
    font_size=50,
    color='black'
)

p1_die = nyan.new_image(
    image='../assets/1.png',
    x=-200,
    y=0,
    angle=0,
    size=80
)

p2_die = nyan.new_image(
    image='../assets/1.png',
    x=200,
    y=0,
    angle=0,
    size=80
)

p1_scoreboard = nyan.new_text(
    words='P1: 0',
    x=-200,
    y=-80,
    angle=0,
    font_size=50,
    color='green'
)

p2_scoreboard = nyan.new_text(
    words='P2: 0',
    x=200,
    y=-80,
    angle=0,
    font_size=50,
    color='black'
)

curr_val_scoreboard = nyan.new_text(
    words='Current Roll Value: 0',
    x=0,
    y=100,
    angle=0,
    font_size=50,
    color='black'
)

game_state = 'P1'

p1_die.score = 0
p2_die.score = 0

curr_val = 0


def roll():
    add_val = random.randint(0, 6)
    global curr_val
    global game_state
    if game_state == 'P1_Rolling':
        if add_val != 0:
            curr_val += add_val
            curr_val_scoreboard.words = f"Current Roll Value: {curr_val}"
            if add_val == 1:
                p1_die.image = '../assets/1.png'
            if add_val == 2:
                p1_die.image = '../assets/2.png'
            if add_val == 3:
                p1_die.image = '../assets/3.png'
            if add_val == 4:
                p1_die.image = '../assets/4.png'
            if add_val == 5:
                p1_die.image = '../assets/5.png'
            if add_val == 6:
                p1_die.image = '../assets/6.png'
            time.sleep(0.1)
            game_state = 'P1'
        if add_val == 0:
            curr_val = 0
            curr_val_scoreboard.words = f"Current Roll Value: {curr_val}"
            p1_die.image = '../assets/redx.png'
            time.sleep(0.1)
            p1_scoreboard.color = 'black'
            p2_scoreboard.color = 'green'
            game_state = 'P2'
    if game_state == 'P2_Rolling':
        if add_val != 0:
            curr_val += add_val
            curr_val_scoreboard.words = f"Current Roll Value: {curr_val}"
            if add_val == 1:
                p2_die.image = '../assets/1.png'
            if add_val == 2:
                p2_die.image = '../assets/2.png'
            if add_val == 3:
                p2_die.image = '../assets/3.png'
            if add_val == 4:
                p2_die.image = '../assets/4.png'
            if add_val == 5:
                p2_die.image = '../assets/5.png'
            if add_val == 6:
                p2_die.image = '../assets/6.png'
            time.sleep(0.1)
            game_state = 'P2'
        if add_val == 0:
            curr_val = 0
            curr_val_scoreboard.words = f"Current Roll Value: {curr_val}"
            p2_die.image = '../assets/redx.png'
            time.sleep(0.1)
            p2_scoreboard.color = 'black'
            p1_scoreboard.color = 'green'
            game_state = 'P1'


@nyan.repeat_forever
async def do():
    global game_state
    global curr_val
    if p1_die.score >= 20:
        instruction.words = "P1 Won!"
    if p2_die.score >= 20:
        instruction.words = "P2 Won!"
    if game_state == 'P1':
        time.sleep(0.1)
        if nyan.key_is_pressed('r'):
            game_state = 'P1_Rolling'
            roll()
        if nyan.key_is_pressed('e'):
            p1_scoreboard.color = 'black'
            p2_scoreboard.color = 'green'
            updated_score = p1_die.score + curr_val
            p1_scoreboard.words = f"P1: {updated_score}"
            curr_val = 0
            curr_val_scoreboard.words = f"Current Roll Value: {curr_val}"
            game_state = 'P2'
    if game_state == 'P2':
        time.sleep(0.1)
        if nyan.key_is_pressed('r'):
            game_state = 'P2_Rolling'
            roll()
        if nyan.key_is_pressed('e'):
            p1_scoreboard.color = 'green'
            p2_scoreboard.color = 'black'
            p2_scoreboard.words = f"P2: {p2_die.score + curr_val}"
            curr_val = 0
            curr_val_scoreboard.words = f"Current Roll Value: {curr_val}"
            game_state = 'P1'

nyan.start_program()
