import pygame
from helpers import screen
from constants import *


class Comment:
    def __init__(self, text):
        self.text = text

    def display(self, comment_number):
        if not self.text:
            return

        comment_font = pygame.font.SysFont('Arial', UI_FONT_SIZE)
        comment_to_display = comment_font.render(self.text, True, (0, 0, 0))

        screen.blit(comment_to_display,
                    (FIRST_COMMENT_X_POS,
                     FIRST_COMMENT_Y_POS +
                     (comment_number * COMMENT_LINE_HEIGHT)))
