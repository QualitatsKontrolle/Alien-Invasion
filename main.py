#!/usr/bin/python3

import os
os.environ["SDL_VIDEODRIVER"]="x11"

import pygame, sys
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    # Initialize game & create screen object
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode(
        (game_settings.screen_width, game_settings.screen_height)
    )
    pygame.display.set_caption('Alien Invasion Game')
    
    # Make a ship
    ship = Ship(game_settings, screen)
    # Make group to store bullets in
    bullets = Group()

    # Set background color
    bg_color = (230, 230, 230)

    # Start main loop for game
    while True:
        # Watch for keyboard & mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        gf.check_events(game_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(game_settings, screen, ship, bullets)
        
        # Get rid of bullets that have disappeared
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
        
        gf.update_screen(game_settings, screen, ship, bullets)
     
        # Redraw screen during each pass through the loop
        screen.fill(game_settings.bg_color)
        ship.blitme()
        # Make most recently drawn screen visible
        pygame.display.flip()


run_game()
