#!/usr/bin/python3

import os
os.environ["SDL_VIDEODRIVER"]="x11"

import pygame
import sys
from settings import Settings

def run_game():
    # initialize game & create screen object
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode(
        (game_settings.screen_width, game_settings.screen_height)
    )
    pygame.display.set_caption('Alien Invasion')

    # set background color
    bg_color = (230, 230, 230)

    while True:
        # watch for keyboard & mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        # redraw screen during each pass through loop
        screen.fill(game_settings.bg_color)
        # make most recently drawn screen visible
        pygame.display.flip()


run_game()