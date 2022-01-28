import random

import pygame
import sys

def init(setup_fnc, loop_fcn, title="Rosegame", width=640, height=480, color=(255, 255, 255)):
    pygame.init()
    rg = Rosegame(setup_fnc, loop_fcn, title, width, height, color)
    setup_fnc(rg)
    rg.loop_forever()

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def point_from_tuple(self, point_tuple):
        return Point(point_tuple[0], point_tuple[1])

class Rosegame:

    def __init__(self, setup_fcn, loop_fcn, window_title, window_width, window_height, background_color):
        self.setup_fcn = setup_fcn
        self.loop_fcn = loop_fcn
        self.background_color = background_color
        pygame.display.set_caption(window_title)
        self.screen = pygame.display.set_mode((window_width, window_height))

    def is_key_pressed(self, key):
        all_keys = pygame.key.get_pressed()
        return all_keys[key]

    def is_key_pressed_event(self, key):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == key:
                    return True
        return False

    def mouse_location(self):
        return Point(pygame.mouse.get_pos())

    def click_location(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                return Point(event.pow)
        return None

    def loop_forever(self):
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.background_color)
            self.loop_fcn(self)
            pygame.display.update()


class Sprite:

    def __init__(self, game, image_filename, x=None, y=None, size_percentage=100):
        self.game = game
        if x is None:
            x = random.random() * self.game.screen.get_width()
        self.x = x
        if y is None:
            y = random.random() * self.game.screen.get_height()
        self.y = y
        # TODO: Implement the size_percentage option
        self.image = pygame.image.load(image_filename)
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def move(self, x, y):
        self.x = self.x + x
        self.y = self.y + y

    def draw(self):
        self.game.screen.blit(self.image, (self.x, self.y))

    def is_touching(self, another_object):
        self_rect = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())
        other_rect = pygame.Rect(another_object.x, another_object.y, another_object.image.get_width(), another_object.image.get_height())
        return self_rect.colliderect(other_rect)

