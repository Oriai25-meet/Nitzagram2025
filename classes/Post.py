import pygame
from helpers import *
from constants import *
class Post:
    def __init__(self,username,location,description):
        self.username = username
        self.location = location
        self.description = description
        self.likes_counter = 0
        self.comments = []

    def add_like(self):

        self.likes_counter +=1

    def add_comment(self,text):
        self.comments.append(Comment(text))


    def display(self):
        screen.blit(self.username,[USER_NAME_X_POS,USER_NAME_Y_POS])
        screen.blit(self.location,[LOCATION_TEXT_X_POS,LOCATION_TEXT_Y_POS])
        screen.blit(self.likes_counter,[LIKE_TEXT_X_POS,LIKE_TEXT_Y_POS])
        screen.blit(self.description,[DESCRIPTION_TEXT_X_POS,DESCRIPTION_TEXT_Y_POS])
        screen.blit(self.comments,[FIRST_COMMENT_X_POS,FIRST_COMMENT_Y_POS])


