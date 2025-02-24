import pygame
from constants import *
from helpers import *
from classes.Post import Post

class TextPost(Post):
    text_color = (23, 23, 32)
    back_color = (124, 123, 123)

    def __init__(self, username, location, description, info=None):
        super().__init__(username, location, description)
        self.info = info if info else "No content"  # הגדרת טקסט ברירת מחדל

    def add_like(self):
        super().add_like()

    def display(self):
        super().display()
        font = pygame.font.SysFont('Arial', TEXT_POST_FONT_SIZE)  # שינוי פונט
        text_surface = font.render(self.info, True, self.text_color)
        screen.blit(text_surface, center_text(5, text_surface, 0))

    def display_comments(self):
        super().display_comments()
