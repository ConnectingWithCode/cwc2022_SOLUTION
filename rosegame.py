import random
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
        self.events = []

    def is_key_pressed(self, key):
        """

        :param key: The key to check
        :type key: int
        :return: Returns true if the key is being held down (being pressed)
        :rtype: bool
        """
        all_keys = pygame.key.get_pressed()
        return all_keys[key]

    def is_key_newly_pressed(self, key):
        for event in self.events:
            if event.type == pygame.KEYDOWN:
                if event.key == key:
                    return True
        return False

    @property
    def mouse_location(self):
        return Point(pygame.mouse.get_pos())

    @property
    def click_location(self):
        for event in self.events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                return Point(event.pow)
        return None

    def loop_forever(self):
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            self.events = pygame.event.get()
            for event in self.events:
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.background_color)
            self.loop_fcn(self)
            pygame.display.update()


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, x, y):
        self.x = self.x + x
        self.y = self.y + y

    def point_from_tuple(self, point_tuple):
        return Point(point_tuple[0], point_tuple[1])

    @property
    def as_tuple(self):
        return (self.x, self.y)


class GraphicsObject:

    def __init__(self, x, y):
        self.center = Point(x, y)
        self.width = 0
        self.height = 0

    def move(self, x, y):
        self.center.move(x, y)

    @property
    def collision_rect(self):
        return pygame.Rect(self.center_x - self.width / 2, self.center_y + self.height / 2,
                           self.width, self.height)

    def is_touching(self, another_object):
        self_rect = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())
        other_rect = pygame.Rect(another_object.x, another_object.y, another_object.image.get_width(), another_object.image.get_height())
        return self_rect.colliderect(other_rect)

    @property
    def is_off_screen(self):
        # TODO: Implement
        pass

    def draw(self):
        print("Draw should be overridden by every subclass of GraphicsObject")


class Sprite(GraphicsObject):

    def __init__(self, game, image_filename, x=None, y=None, size_percentage=100):
        self.game = game

        # TODO: Implement the size_percentage option
        self.image = pygame.image.load(image_filename)
        self.width = self.image.get_width()
        self.height = self.image.get_height()

        # TODO: Test the random starting position stuff.
        if x is None:
            x = (random.random() * self.game.screen.get_width() - self.width) + self.width / 2
        if y is None:
            y = (random.random() * self.game.screen.get_height() - self.height) + self.height / 2
        self.center = Point(x, y)

    def draw(self):
        self.game.screen.blit(self.image, (self.center.x - self.width / 2,
                                           self.center.y - self.height / 2))


class Line(GraphicsObject):

    def __init__(self, game, pt1, pt2, color=(128, 0, 0), thickness=4):
        self.game = game
        self.pt1 = pt1
        self.pt2 = pt2
        self.color = color
        self.thickness = thickness

    @property
    def center(self):
        self.center = Point((self.pt1.x - self.pt2.x) / 2, (self.pt1.y + self.pt2.y) / 2)

    @property
    def width(self):
        return abs(self.pt1.x - self.pt2.x)

    @property
    def height(self):
        return abs(self.pt1.y - self.pt2.y)

    def move(self, x, y):
        self.pt1.move(x, y)
        self.pt2.move(x, y)

    def draw(self):
        pygame.draw.line(self.game.screen, self.color, self.pt1.as_tuple, self.pt2.as_tuple, self.thickness)


