import pygame
from helpers import screen, read_comment_from_user
from constants import *
from buttons import *
from classes.TextPost import TextPost
from classes.ImagePost import ImagePost
from classes.Comment import Comment
from classes.Post import Post


def create_ImagePost(username, location, description, image):
    return ImagePost(username, location, description, image)


def create_post(username, location, description):
    return Post(username, location, description)


def main():
    pygame.init()
    pygame.display.set_caption('Nitzagram')
    clock = pygame.time.Clock()

    background = pygame.image.load('Images/background.png')
    background = pygame.transform.scale(background, (WINDOW_WIDTH, WINDOW_HEIGHT))


    Posts = [
        create_ImagePost('Noamlev1_', 'United States', 'Ani HOMO', 'Images/ronaldo.jpg'),
        create_ImagePost('Ori Aikort', 'Israel', 'Ani ohed Beitar', 'Images/noa_kirel.jpg'),
        create_post('User123', 'Paris, France', 'Best trip ever!')
    ]

    current_post_index = 0

    running = True
    while running:
        screen.fill(WHITE)
        screen.blit(background, (0, 0))


        Posts[current_post_index].display()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()


                if like_button.x_pos < mouse_pos[0] < like_button.x_pos + like_button.width and \
                        like_button.y_pos < mouse_pos[1] < like_button.y_pos + like_button.height:
                    Posts[current_post_index].add_like()


                elif comment_button.x_pos < mouse_pos[0] < comment_button.x_pos + comment_button.width and \
                        comment_button.y_pos < mouse_pos[1] < comment_button.y_pos + comment_button.height:
                    new_comment = read_comment_from_user()
                    Posts[current_post_index].add_comment(new_comment)


                elif view_more_comments_button.x_pos < mouse_pos[
                    0] < view_more_comments_button.x_pos + view_more_comments_button.width and \
                        view_more_comments_button.y_pos < mouse_pos[
                    1] < view_more_comments_button.y_pos + view_more_comments_button.height:
                    Posts[current_post_index].view_more_comments()


                elif click_post_button.x_pos < mouse_pos[0] < click_post_button.x_pos + click_post_button.width and \
                        click_post_button.y_pos < mouse_pos[1] < click_post_button.y_pos + click_post_button.height:
                    current_post_index = (current_post_index + 1) % len(Posts)

        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    quit()


main()
