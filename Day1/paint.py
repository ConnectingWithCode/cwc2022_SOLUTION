import rosegraphics as rg

def main():
    window = rg.RoseWindow(400, 600, title="Click to draw lines")
    pt1 = window.get_next_mouse_click()
    while True:
        pt2 = window.get_next_mouse_click()
        line = rg.Line(pt1, pt2)
        line.attach_to(window)
        window.render(0.1)
        pt1 = pt2

main()