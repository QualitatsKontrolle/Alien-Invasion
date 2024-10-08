#!/usr/bin/python3

import pygame

class Ship():

    def __init__(self, game_settings, screen):
        """initialize Ship & set the starting position."""
        self.screen = screen
        self.game_settings = game_settings

        # load ship image & get its rect
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # start each new ship at bottom of centre of screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
        #Store decimal value for ship's center
        self.center = float(self.rect.centerx)
        
        # Movement flag
        self.moving_right = False
        self.moving_left = False
    
    def update(self):
        """Update ship's position based on movement flag"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.game_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.game_settings.ship_speed_factor
        
        # Update rect object from self.center
        self.rect.centerx = self.center

    def blitme(self):
        # draw ship at current location
        self.screen.blit(self.image, self.rect)
