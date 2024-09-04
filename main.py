#!/usr/bin/python3

import os
os.environ["SDL_VIDEODRIVER"]="x11"

import pygame
import sys
from settings import Settings

def run_game():
    # Initialize game & create screen object
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode(
        (game_settings.screen_width, game_settings.screen_height)
    )
    pygame.display.set_caption('Alien Invasion')

    # Set background color
    bg_color = (230, 230, 230)

    while True:
        # Watch for keyboard & mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        # Redraw screen during each pass through the loop
        screen.fill(game_settings.bg_color)
        # Make most recently drawn screen visible
        pygame.display.flip()


run_game()
