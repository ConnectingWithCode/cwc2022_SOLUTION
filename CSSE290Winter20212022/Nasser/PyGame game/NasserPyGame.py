import play
import pygame


bullet_speed = 15
cowboy1_speed = 10
cowboy2_speed = 10

play.set_backdrop('light gray')

message = play.new_text(
        words='Wild West Shootout',
        x=0,
        y=play.screen.bottom + 20,
        angle=0,
        font=None,
        font_size=50,
        color='black',
        transparency=100
    )

cowboy1_scoreboard = play.new_text(
        words='cowboy1: 0',
        x=play.screen.left + 90,
        y=play.screen.top - 20,
        angle=0,
        font=None,
        font_size=50,
        color='black',
        transparency=100
    )

cowboy2_scoreboard = play.new_text(
        words='cowboy2: 0',
        x=play.screen.right - 100,
        y=play.screen.top - 20,
        angle=0,
        font=None,
        font_size=50,
        color='black',
        transparency=100
    )

cowboy1 = play.new_image(
        image='cowboy2.jpg',
        x=-200,
        y=0,
        angle=0,
        size=10,
        transparency=100
    )

cowboy2 = play.new_image(
        image='cowboy1.jpg',
        x=200,
        y=0,
        angle=0,
        size=40,
        transparency=100
    )

original_bulletLeft = play.new_image(
        image='bullet_left.png',
        x=-500,
        y=0,
        angle=0,
        size=5,
        transparency=100
    )

original_bulletRight = play.new_image(
        image='bullet_right.png',
        x=-500,
        y=0,
        angle=180,
        size=5,
        transparency=100
    )

bulletLeft_list = []
bulletRight_list = []
cowboy1.score = 0
cowboy2.score = 0


def if_on_edge_stop(sprite):
    if sprite.x < play.screen.left:
        sprite.x = play.screen.left
    if sprite.y < play.screen.bottom:
        sprite.y = play.screen.bottom
    if sprite.x > play.screen.right:
        sprite.x = play.screen.right
    if sprite.y > play.screen.top:
        sprite.y = play.screen.top

async def reset_all():
    cowboy2_scoreboard.words = f"Cowboy2: {cowboy2.score}"
    cowboy1_scoreboard.words = f"Cowboy1: {cowboy1.score}"
    await play.timer(2)

    for bullet in bulletLeft_list:
        bullet.remove()
    bulletLeft_list.clear()

    for bullet in bulletRight_list:
        bullet.remove()
    bulletRight_list.clear()
    message.words = ""

    cowboy1.go_to(-200, 0)
    cowboy2.go_to(200, 0)


@play.repeat_forever
async def do():
        if play.key_is_pressed('up'):
                cowboy2.y += cowboy2_speed
        if play.key_is_pressed('down'):
                cowboy2.y -= cowboy2_speed
        if play.key_is_pressed('right'):
                cowboy2.x += cowboy2_speed
        if play.key_is_pressed('left'):
                cowboy2.x -= cowboy2_speed
        if play.key_is_pressed('space'):
                new_bullet = original_bulletRight.clone()
                new_bullet.y = cowboy1.y
                new_bullet.x = cowboy1.x
                bulletRight_list.append(new_bullet)
        if_on_edge_stop(cowboy2)

        if play.key_is_pressed('w'):
                cowboy1.y += cowboy1_speed
        if play.key_is_pressed('s'):
                cowboy1.y -= cowboy1_speed
        if play.key_is_pressed('d'):
                cowboy1.x += cowboy1_speed
        if play.key_is_pressed('a'):
                cowboy1.x -= cowboy1_speed
        if play.key_is_pressed('/'):
            new_bullet = original_bulletLeft.clone()
            new_bullet.y = cowboy2.y
            new_bullet.x = cowboy2.x
            bulletLeft_list.append(new_bullet)
        if_on_edge_stop(cowboy1)


#         TODO: make all bullets move
        for bullet in bulletRight_list:
            bullet.move(-bullet_speed)

            if cowboy2.is_touching(bullet):
                message.words = "cowboy1 wins!"
                cowboy1.score += 1
                await reset_all()

        for bullet in bulletLeft_list:
            bullet.move(-bullet_speed)

            if cowboy1.is_touching(bullet):
                message.words = "cowboy2 wins!"
                cowboy2.score += 1
                await reset_all()


play.start_program()

