#!/usr/bin/python3

class Ship():
    # initialize Ship & set the starting position
    def __init__(self, screen):
        self.screen = screen

        # load ship image & get its rect
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image..get_rect()
        self.screen_rect = screen.get_rect()

        # start each new ship at bottom of centre of screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        # draw ship at current location
        self.screen.blit(self.image, self.rect)