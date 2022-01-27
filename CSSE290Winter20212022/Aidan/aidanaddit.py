import rosegraphics as rg
import math


def second_point_calc(pt1, pt2):
    outer_circle = math.sqrt(((pt2.x - pt1.x) * (pt2.x - pt1.x)) + ((pt2.y - pt1.y) * (pt2.y - pt1.y)))
    outer_square = math.sqrt(2) * outer_circle
    inner_circle = 0.5 * outer_square
    inner_square = math.sqrt(2) * inner_circle
    return [outer_circle, outer_square, inner_circle, inner_square]


def main():
    window = rg.RoseWindow(400, 600, title="Click to draw inscribed squares and circles")
    pt1 = window.get_next_mouse_click()
    while True:
        pt2 = window.get_next_mouse_click()
        second_points = second_point_calc(pt1, pt2)
        circle = rg.Circle(pt1, second_points[0])
        square = rg.Square(pt1, second_points[1])
        inner_circle = rg.Circle(pt1, second_points[2])
        inner_square = rg.Square(pt1, second_points[3])
        circle.attach_to(window)
        square.attach_to(window)
        inner_circle.attach_to(window)
        inner_square.attach_to(window)
        window.render(0.1)
        pt1 = window.get_next_mouse_click()


main()
