import rosegraphics as rg

# Create a new window
window = rg.RoseWindow(400, 600, title="Bob's window")


# Create a point
pt1 = rg.Point(100,100)
pt1.outline_color = "green"
pt1.fill_color = "green"
pt1.attach_to(window)

# Create a square
square = rg.Square(rg.Point(200,300), 50)
square.attach_to(window)

pt2 = window.get_next_mouse_click()
pt1.x = pt2.x
pt1.y = pt2.y

# Animate by drawing the point in a new location - go across screen
for k in range (200):
    pt1.x+=1
    window.render(0.1)
    print(window.mouse.position)

# window.render() redraws the window
window.render()
window.close_on_mouse_click()