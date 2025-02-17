import pygame
from helpers import *
from constants import WINDOW_WIDTH, WINDOW_HEIGHT, BLACK
from buttons import *
from classes.TextPost import TextPost
from classes.ImagePost import ImagePost
from classes.Comment import Comment
from classes.Post import Post
def create_ImagePost(image):
    image = ImagePost(image)
    return image
def create_post(username, location, description):
    post = Post(username, location, description)
    return post
def main():
    # Set up the game display, clock and headline
    pygame.init()

    # Change the title of the window
    pygame.display.set_caption('Nitzagram')

    clock = pygame.time.Clock()

    # Set up background image
    background = pygame.image.load('Images/background.png')
    background = pygame.transform.scale(background,(WINDOW_WIDTH, WINDOW_HEIGHT))



    # TODO: add a post here
    Posts = []
    Posts.append(create_post('Noamlev1_','United States','Ani HOMO',create_ImagePost('Images/ronaldo.jpg')))
    Posts.append(create_post('Ori Aikort','Israel','Ani ohed Beitar',create_ImagePost('Images/noa_kila.jpg')))


    running = True
    while running:
        # Grabs events such as key pressed, mouse pressed and so.
        # Going through all the events that happened in the last clock tick
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Display the background, presented Image, likes, comments, tags and location(on the Image)
        screen.fill(BLACK)
        screen.blit(background, (0, 0))

        # Update display - without input update everything
        pygame.display.update()

        # Set the clock tick to be 60 times per second. 60 frames for second.
        clock.tick(60)
    pygame.quit()
    quit()


main()
