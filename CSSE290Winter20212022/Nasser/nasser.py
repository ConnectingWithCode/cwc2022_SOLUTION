import rosegraphics as rg


def main():
    sides = int(input("How many sides do you want?"))
    window = rg.RoseWindow(400, 600, title="Click to draw a square")
    # sides = 4;
    pt1 = window.get_next_mouse_click()

    while True:
        if sides>0:
            pt2 = window.get_next_mouse_click()
            line = rg.Line(pt1, pt2)
            line.attach_to(window)
            pt1 = pt2
            sides -= 1

        window.render(0.1)




main()