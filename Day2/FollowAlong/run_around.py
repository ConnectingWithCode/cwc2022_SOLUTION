import play
harry_speed = 5

play.set_backdrop('light gray')


harry = play.new_image(
        image='harry_potter.png',
        x=-200,
        y=0,
        angle=0,
        size=20,
        transparency=100
    )


async def reset_all():

        harry.go_to(-200, 0)

def if_on_edge_stop(sprite):
        if sprite.x < play.screen.left:
                sprite.x = play.screen.left
        if sprite.y < play.screen.bottom:
                sprite.y = play.screen.bottom
        if sprite.x > play.screen.right:
                sprite.x = play.screen.right
        if sprite.y > play.screen.top:
                sprite.y = play.screen.top

@play.repeat_forever
async def do():
        if play.key_is_pressed('w'):
                harry.y += harry_speed
        if play.key_is_pressed('s'):
                harry.y -= harry_speed
        if play.key_is_pressed('d'):
                harry.x += harry_speed
        if play.key_is_pressed('a'):
                harry.x -= harry_speed
        if_on_edge_stop(harry)

play.start_program()