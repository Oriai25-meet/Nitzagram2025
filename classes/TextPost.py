import pygame
from constants import *
from helpers import *
from classes.Post import Post

class TextPost(Post):
    text_color = (23, 23, 32)
    back_color = (124, 123, 123)

    def __init__(self, username, location, description, info=None):
        super().__init__(username, location, description)
        self.info = info if info else "No content"
    def add_like(self):
        super().add_like()

    def display(self):
        super().display()
        pygame.draw.rect(screen, self.back_color,
                         pygame.Rect(POST_X_POS, POST_Y_POS, POST_WIDTH, POST_HEIGHT), border_radius=10)


        font = pygame.font.SysFont('Arial', TEXT_POST_FONT_SIZE)
        text_surface = font.render(self.info, True, self.text_color)


        text_rect = text_surface.get_rect(center=(POST_X_POS + POST_WIDTH // 2, POST_Y_POS + POST_HEIGHT // 2))
        screen.blit(text_surface, text_rect)
    def display_comments(self):
        super().display_comments()
