import play
import pygame

fawkes_speed = 5
harry_speed = 5
snake_speed = 10
fawkes_release_time = 0.5

play.set_backdrop('light gray')
# pygame.display.set_mode((1400, 800))  # TODO: Adjust for your monitor!

message = play.new_text(
        words='Harry Potter',
        x=0,
        y=play.screen.bottom + 20,
        angle=0,
        font=None,
        font_size=50,
        color='black',
        transparency=100
    )
harry_scoreboard = play.new_text(
        words='Harry: 0',
        x=play.screen.left + 80,
        y=play.screen.top - 20,
        angle=0,
        font=None,
        font_size=50,
        color='black',
        transparency=100
    )

snake_scoreboard = play.new_text(
        words='Snake: 0',
        x=play.screen.right - 80,
        y=play.screen.top - 20,
        angle=0,
        font=None,
        font_size=50,
        color='black',
        transparency=100
    )

snake = play.new_image(
        image='basilisk.png',
        x=200,
        y=0,
        angle=0,
        size=10,
        transparency=100
    )

harry = play.new_image(
        image='harry_potter.png',
        x=-200,
        y=0,
        angle=0,
        size=20,
        transparency=100
    )

original_fawkes = play.new_image(
        image='fawkes_right.png',
        x=-500,
        y=0,
        angle=0,
        size=20,
        transparency=100
    )

fawkes_list = []
harry.score = 0
snake.score = 0

async def reset_all():
        snake_scoreboard.words = f"Snake: {snake.score}"
        harry_scoreboard.words = f"Harry: {harry.score}"
        await play.timer(2)
        for fawkes in fawkes_list:
                fawkes.remove()
        fawkes_list.clear()
        message.words = ""

        harry.go_to(-200, 0)
        snake.go_to(200, 0)

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
        new_fawkes = original_fawkes.clone()
        new_fawkes.y = play.random_number(lowest=-300, highest=300)
        fawkes_list.append(new_fawkes)
        await play.timer(seconds=fawkes_release_time)

@play.repeat_forever
async def do():
        if play.key_is_pressed('up'):
                snake.y += snake_speed
        if play.key_is_pressed('down'):
                snake.y -= snake_speed
        if play.key_is_pressed('right'):
                snake.x += snake_speed
        if play.key_is_pressed('left'):
                snake.x -= snake_speed
        if_on_edge_stop(snake)

        if play.key_is_pressed('w'):
                harry.y += harry_speed
        if play.key_is_pressed('s'):
                harry.y -= harry_speed
        if play.key_is_pressed('d'):
                harry.x += harry_speed
        if play.key_is_pressed('a'):
                harry.x -= harry_speed
        if_on_edge_stop(harry)

        if snake.is_touching(harry):
                message.words = "The Snake wins!"
                snake.score += 1
                await reset_all()

        for fawkes in fawkes_list:
                fawkes.move(fawkes_speed)

                if snake.is_touching(fawkes):
                        message.words = "Harry wins!"
                        harry.score += 1
                        await reset_all()

play.start_program()