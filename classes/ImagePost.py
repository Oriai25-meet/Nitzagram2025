import pygame
from helpers import *
from constants import *
from classes.Post import *

# done
class ImagePost(Post):
    def __init__(self,username, location, description, image = None):
        super().__init__(username, location, description)
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image,(POST_WIDTH,POST_HEIGHT))
    def display(self):
        super().display()
        screen.blit(self.image,(POST_X_POS,POST_Y_POS))

    def display_comments(self):
        super().display_comments()

    def view_more_comments(self):
        super().view_more_comments()