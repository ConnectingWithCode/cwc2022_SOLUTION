import pygame
import sys


# --------------------------- Conversion helper functions ---------------------------


def get_row_col(mouse_x, mouse_y):
    """ Converts an x, y screen position into a row, col value. """
    # Note: the top row is row=0 (bottom row=2), left col is col=0 (right col=2)
    spacing_x = 86 + 8
    spacing_y = 98 + 5
    top_y = 50
    left_x = 50
    return (mouse_y - top_y) // spacing_y, (mouse_x - left_x) // spacing_x


def get_xy_position(row, col):
    """ Converts a row, col value into an x, y screen position (upper left corner of that location). """
    spacing_x = 86 + 11
    spacing_y = 98 + 8
    top_y = 50
    left_x = 50
    return left_x + col * spacing_x, top_y + row * spacing_y


# --------------------------- Model Object ---------------------------


class Game:
    def __init__(self):
        self.board = []
        self.game_state_string = "X's Turn"
        for row in range(3):
            current_row = []
            for col in range(3):
                current_row.append(".")
            self.board.append(current_row)
        # self.board = [["." for _ in range(3)] for _ in range(3)]  # Way too fancy!
        self.turn_counter = 0
        self.game_is_over = False

    def take_turn(self, row, col):
        """Handle the current turn of the player and update board array"""
        if self.game_is_over:
            return
        if row < 0 or row > 2 or col < 0 or col > 2:
            return
        if self.board[row][col] != ".":
            return

        if self.turn_counter % 2 == 0:
            self.board[row][col] = "X"
            self.game_state_string = "O's Turn"
        else:
            self.board[row][col] = "O"
            self.game_state_string = "X's Turn"

        self.turn_counter = self.turn_counter + 1
        self.check_for_game_over()

    def check_for_game_over(self):
        if self.turn_counter >= 9:
            self.game_is_over = True
            self.game_state_string = "Tie Game"

        lines = []
        lines.append(self.board[0][0] + self.board[0][1] + self.board[0][2])
        lines.append(self.board[1][0] + self.board[1][1] + self.board[1][2])
        lines.append(self.board[2][0] + self.board[2][1] + self.board[2][2])
        lines.append(self.board[0][0] + self.board[1][0] + self.board[2][0])
        lines.append(self.board[0][1] + self.board[1][1] + self.board[2][1])
        lines.append(self.board[0][2] + self.board[1][2] + self.board[2][2])
        lines.append(self.board[0][0] + self.board[1][1] + self.board[2][2])
        lines.append(self.board[0][2] + self.board[1][1] + self.board[2][0])
        for line in lines:
            if line == "OOO" or line == "XXX":
                self.game_is_over = True
                pygame.mixer.music.play()
                self.game_state_string = "X Wins!"
                if line == "OOO":
                    self.game_state_string = "O Wins!"


# --------------------------- View Controller ---------------------------

class ViewController:

    def __init__(self, screen):
        self.screen = screen
        self.game = Game()
        self.board_image = pygame.image.load("board.png")
        self.x_image = pygame.image.load("x_mark.png")
        self.o_image = pygame.image.load("o_mark.png")

    def check_event(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            click_x, click_y = pygame.mouse.get_pos()
            row, col = get_row_col(click_x, click_y)
            self.game.take_turn(row, col)
        if event.type == pygame.KEYDOWN:
            pressed_keys = pygame.key.get_pressed()
            if pressed_keys[pygame.K_SPACE]:
                self.game = Game()

    def draw(self):
        """ Draw the board based on the marked store in the board configuration array """
        self.screen.blit(self.board_image, get_xy_position(0, 0))
        for row in range(3):
            for col in range(3):
                mark = self.game.board[row][col]
                if mark == "X":
                    self.screen.blit(self.x_image, get_xy_position(row, col))
                elif mark == "O":
                    self.screen.blit(self.o_image, get_xy_position(row, col))
        pygame.display.set_caption(self.game.game_state_string)


# --------------------------- main ---------------------------


def main():
    pygame.init()
    pygame.mixer.music.load("win.mp3")
    screen = pygame.display.set_mode((380, 400))
    view_controller = ViewController(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            view_controller.check_event(event)
        screen.fill(pygame.Color("white"))
        view_controller.draw()
        pygame.display.update()


main()
