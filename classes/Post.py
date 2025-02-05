import pygame
from helpers import *
from constants import *
from Comment import *


class Post:
    def __init__(self, username, location, description):
        self.username = username
        self.location = location
        self.description = description
        self.likes_counter = 0
        self.comments = []
        self.comments_display_index = 0

    def add_like(self):

        self.likes_counter += 1

    def add_comment(self,text):
        self.comments.append(Comment(text))


    def display(self):
        # screen.blit(self.location,[LOCATION_TEXT_X_POS,LOCATION_TEXT_Y_POS])
        # screen.blit(self.likes_counter,[LIKE_TEXT_X_POS,LIKE_TEXT_Y_POS])
        # screen.blit(self.description,[DESCRIPTION_TEXT_X_POS,DESCRIPTION_TEXT_Y_POS])
        # screen.blit(self.comments,[FIRST_COMMENT_X_POS,FIRST_COMMENT_Y_POS])
        self.display_content()
        self.display_header()
        self.display_likes()
        self.display_comments()

    def display_content(self):
        # display post itself
        pass

    def display_header(self):
        # display username, description,
        font = pygame.font.SysFont('chalkduster.ttf', UI_FONT_SIZE)
        name = font.render(self.username)
        screen.blit(name,[USER_NAME_X_POS,USER_NAME_Y_POS])

        font = pygame.font.SysFont('chalkduster.ttf', UI_FONT_SIZE)
        description = font.render(self.description)
        screen.blit(description, [DESCRIPTION_TEXT_X_POS, DESCRIPTION_TEXT_Y_POS])

        font = pygame.font.SysFont('chalkduster.ttf', UI_FONT_SIZE)
        location = font.render(self.location)
        screen.blit(location, [FIRST_COMMENT_X_POS, FIRST_COMMENT_Y_POS])



    def display_likes(self):
        # display likes count
        font = pygame.font.SysFont('chalkduster.ttf', UI_FONT_SIZE)
        likes = font.render(self.likes_counter)
        screen.blit(likes, [LIKE_TEXT_X_POS,LIKE_TEXT_Y_POS])

    def display_comments(self):
        position_index = self.comments_display_index
        for i in range(4):
            if position_index >= len(self.comments):
                position_index = 0
            self.comments[position_index].display(i)
            position_index += 1
    def  view_more_comments(self):
        if self.comments_display_index >= len(self.comment)-1:
            self.comments_display_index = 0
        else:
            self.comments_display_index += 1


    def reset_comments_display_index(self):
        pass
