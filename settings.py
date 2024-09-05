#!/usr/bin/python3

# settings module

class Settings():
    """
    store all settings related to the game
    """
    def __init__(self):
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        
        # Ship settings
        self.ship_speed_factor = 1.5