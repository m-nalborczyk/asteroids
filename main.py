# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

def main():

    # Initialize pygame
    pygame.init()
    print("Starting Asteroids!")

    # Create the game window (800x600)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Set up the clock for FPS control
    clock = pygame.time.Clock()
    dt = 0  # delta time (time between frames)

    # Game loop
    running = True
    while running:

        # Handle events (close the window when the user clicks the close button)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Fill the screen with black
        screen.fill((0, 0, 0))

        # Update the display
        pygame.display.flip()

        # Cap the frame rate to 60 FPS and calculate delta time
        dt = clock.tick(60) / 1000  # convert from milliseconds to seconds

if __name__ == "__main__":
    main()