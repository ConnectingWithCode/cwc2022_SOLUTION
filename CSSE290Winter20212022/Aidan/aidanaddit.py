import rosegraphics as rg
import math


# I have reservations on whether the mathematical jargon used to inscribe the shapes may be confusing to
# younger folks with less geometry experience. Also, could refactor to recursively inscribe circles to a given depth

# The first click defines the center of the shape while the second click defines the radius of the outer circle

def main():
    window = rg.RoseWindow(400, 600, title="Click to draw inscribed squares and circles")
    pt1 = window.get_next_mouse_click()
    while True:
        pt2 = window.get_next_mouse_click()
        circle = rg.Circle(pt1, math.sqrt(((pt2.x - pt1.x) * (pt2.x - pt1.x)) + ((pt2.y - pt1.y) * (pt2.y - pt1.y))))
        square = rg.Square(pt1, math.sqrt(2) * math.sqrt(
            ((pt2.x - pt1.x) * (pt2.x - pt1.x)) + ((pt2.y - pt1.y) * (pt2.y - pt1.y))))
        inner_circle = rg.Circle(pt1, 0.5 * math.sqrt(2) * math.sqrt(
            ((pt2.x - pt1.x) * (pt2.x - pt1.x)) + ((pt2.y - pt1.y) * (pt2.y - pt1.y))))
        inner_square = rg.Square(pt1, math.sqrt(2) * (0.5 * math.sqrt(2) * math.sqrt(
            ((pt2.x - pt1.x) * (pt2.x - pt1.x)) + ((pt2.y - pt1.y) * (pt2.y - pt1.y)))))
        circle.attach_to(window)
        square.attach_to(window)
        inner_circle.attach_to(window)
        inner_square.attach_to(window)
        window.render(0.1)
        pt1 = window.get_next_mouse_click()


main()
