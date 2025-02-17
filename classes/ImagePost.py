import pygame
from helpers import *
from constants import *
from Post import *

# done
class ImagePost(Post):
    def __init__(self,image):
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image,(POST_WIDTH,POST_HEIGHT))
    def display(self):
        screen.blit(self.image,(POST_X_POS,POST_Y_POS))
