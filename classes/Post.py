import pygame
from helpers import screen, from_text_to_array
from constants import *
from classes.Comment import *

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

    def add_comment(self, text):
        self.comments.append(Comment(text))

    def display(self):
        self.display_header()
        self.display_likes()
        self.display_comments()
        #pygame.display.update()

    def display_header(self):
        font = pygame.font.SysFont('Arial', UI_FONT_SIZE)
        name_text = font.render(self.username, True, BLACK)
        location_text = font.render(self.location, True, GREY)

        screen.blit(name_text, (USER_NAME_X_POS, USER_NAME_Y_POS))
        screen.blit(location_text, (LOCATION_TEXT_X_POS, LOCATION_TEXT_Y_POS))

        description_lines = from_text_to_array(self.description)
        y_offset = DESCRIPTION_TEXT_Y_POS
        for line in description_lines:
            desc_text = font.render(line, True, BLACK)
            screen.blit(desc_text, (DESCRIPTION_TEXT_X_POS, y_offset))
            y_offset += UI_FONT_SIZE

    def display_likes(self):
        font = pygame.font.SysFont('Arial', UI_FONT_SIZE)
        likes_text = font.render(f'Likes: {self.likes_counter}', True, BLACK)
        screen.blit(likes_text, (LIKE_TEXT_X_POS, LIKE_TEXT_Y_POS))

    def display_comments(self):
        font = pygame.font.SysFont('Arial', COMMENT_TEXT_SIZE)
        y_offset = FIRST_COMMENT_Y_POS

        for comment in self.comments[self.comments_display_index:self.comments_display_index + NUM_OF_COMMENTS_TO_DISPLAY]:
            comment_text = font.render(comment.text, True, BLACK)
            screen.blit(comment_text, (FIRST_COMMENT_X_POS, y_offset))
            y_offset += COMMENT_LINE_HEIGHT

    def view_more_comments(self):
        if self.comments_display_index + NUM_OF_COMMENTS_TO_DISPLAY < len(self.comments):
            self.comments_display_index += NUM_OF_COMMENTS_TO_DISPLAY
        else:
            self.comments_display_index = 0
