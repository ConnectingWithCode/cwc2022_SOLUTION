import rosegraphics as rg

def main():
    window = rg.TurtleWindow()
    turtle = rg.SimpleTurtle()
    draw_function(turtle, "blue", 15)
    window.close_on_mouse_click()

def draw_function(turtle, color, distance):
    turtle.pen = rg.Pen(color, 10)
    for _ in range(distance):
        turtle.backward(distance)
        turtle.left(15)
        turtle.forward(distance)
        turtle.forward(distance)

main()