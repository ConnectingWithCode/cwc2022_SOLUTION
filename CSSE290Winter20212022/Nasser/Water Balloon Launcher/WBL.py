import play
import pygame
import math
import random


score_needed_to_win = 5

player1_power = 5
player1_angle = 20

bullet_speedx = (player1_angle * math.cos(player1_angle))
bullet_speedy = player1_power * math.sin(player1_angle)/2


play.set_backdrop('light gray')

message = play.new_text(
    words='Water Balloon Fight',
    x=0,
    y=play.screen.bottom + 20,
    angle=0,
    font=None,
    font_size=50,
    color='black',
    transparency=100
)

player1_scoreboard = play.new_text(
    words='player 1 hits: 0',
    x=play.screen.left + 90,
    y=play.screen.top - 20,
    angle=0,
    font=None,
    font_size=25,
    color='black',
    transparency=100
)

player2_scoreboard = play.new_text(
    words='player 2 hits: 0',
    x=play.screen.right - 100,
    y=play.screen.top - 20,
    angle=0,
    font=None,
    font_size=25,
    color='black',
    transparency=100
)

player1 = play.new_image(
    image='p1tank.png',
    x=-200,
    y=random.randint(play.screen.bottom + 100,play.screen.top - 100),
    angle=0,
    size=20,
    transparency=100
)

player2 = play.new_image(
    image='p2tank.png',
    x=200,
    y=random.randint(play.screen.bottom + 100,play.screen.top - 100),
    angle=0,
    size=20,
    transparency=100
)

original_bullet = play.new_image(
    image='bullet.png',
    x=-500,
    y=0,
    angle=0,
    size=10,
    transparency=100
)

bullet_list = []
bullet_list2 = []

player1.score = 0
player2.score = 0

player1.turn = True

def if_on_edge_remove(sprite):
    if sprite.x < play.screen.left:
        return True
    if sprite.y < play.screen.bottom:
        return True
    if sprite.x > play.screen.right:
        return True
    if sprite.y > play.screen.top:
        return True



async def reset_all():
    player2_scoreboard.words = f"player2: {player2.score}"
    player1_scoreboard.words = f"player1: {player1.score}"
    message.words = "Water Balloon Fight"
    await play.timer(2)

    for bullet in bullet_list:
        bullet.remove()
    bullet_list.clear()

    for bullet in bullet_list2:
        bullet.remove()
    bullet_list2.clear()





player1turn = 0



def check_shooting():
    if len(bullet_list)==0 and len(bullet_list2)==0:
        if player1.turn:
            player1_power = int(input("What do you want your power to be P1?"))
            player1_angle = int(input("What do you want your angle to be P1?"))
            new_bullet = original_bullet.clone()
            new_bullet.speed = player1_power
            new_bullet.y = player1.y
            new_bullet.x = player1.x
            new_bullet.angle = player1_angle
            bullet_list.append(new_bullet)
            player1.turn = False
        else:
            player2_power = int(input("What do you want your power to be P2?"))
            player2_angle = int(input("What do you want your angle to be P2?"))
            new_bullet = original_bullet.clone()
            new_bullet.speed = player2_power
            new_bullet.y = player2.y
            new_bullet.x = player2.x
            new_bullet.angle = 180-player2_angle
            bullet_list2.append(new_bullet)
            player1.turn = True


async def check_bullets():
    for bullet in bullet_list:
        bullet.move(bullet.speed)
        if bullet.angle >-90:
            bullet.angle = bullet.angle-bullet_speedy
        if if_on_edge_remove(bullet):
            bullet.remove()
            bullet_list.clear()

        if player2.is_touching(bullet):
            message.words = "player1 wins!"
            player1.score += 1
            await reset_all()

    for bullet in bullet_list2:
        bullet.move(bullet.speed)
        if bullet.angle < 270:
            bullet.angle = bullet.angle+bullet_speedy
        if if_on_edge_remove(bullet):
            bullet.remove()
            bullet_list2.clear()

        if player1.is_touching(bullet):
            message.words = "player2 wins!"
            player2.score += 1
            await reset_all()

async def check_score():
    if player1.score == score_needed_to_win or player2.score == score_needed_to_win:
        if player1.score > player2.score:
            message = "Player1 wins!"
        else:
            message = "Player2 wins!"
        play.new_text(
            words=message,
            font_size=50,
            color='black'
        )
        while True:
            await play.timer(seconds=0.5)

@play.repeat_forever
async def do():
    check_shooting()
    await check_bullets()
    await check_score()


play.start_program()
