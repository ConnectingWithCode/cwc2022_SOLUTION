import pygame
import sys

def init(setup_fnc, loop_fcn, title="Rosegame", width=640, height=480, color=(255, 255, 255)):
    pygame.init()
    rg = Rosegame(setup_fnc, loop_fcn, title, width, height, color)
    setup_fnc(rg)
    rg.loop_forever()

class Rosegame:

    def __init__(self, setup_fcn, loop_fcn, window_title, window_width, window_height, background_color):
        self.setup_fcn = setup_fcn
        self.loop_fcn = loop_fcn
        self.background_color = background_color
        pygame.display.set_caption(window_title)
        self.screen = pygame.display.set_mode((window_width, window_height))

    def loop_forever(self):
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            click_position = None
            key_pressed = None
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    click_position = event.pos
                if event.type == pygame.KEYDOWN:
                    key_pressed
                if event.type == pygame.QUIT:
                    sys.exit()
            mouse_position = pygame.mouse.get_pos()
            all_keys = pygame.key.get_pressed()
            all_events = pygame.event.get()
            self.screen.fill(self.background_color)
            self.loop_fcn(self, click_position, key_pressed, mouse_position, all_keys, all_events)
            pygame.display.update()
