""" This file manage the behavior of the player's ship"""

import pygame
from pygame.sprite import Sprite

from filepath import FilePaths

class Ship(Sprite):
    """A class to manage the ship"""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect() #This place the ship in the correct location on the screen
        self.settings = ai_game.settings 

        # Load the ship image and get its rect.
        # Load FilePaths class as self.fp
        self.fp = FilePaths()
        # Load Ship image
        self.image = pygame.image.load(self.fp.ship_image_path)
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom #Use rect attribute to position ship at the center bottom screen

        # Store a decimal value for the ship's horizontal position.
        self.x = float(self.rect.x)

        #Movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on the movement flag."""
        # Update the ship's x value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        
        # Update rect object from self.x.
        self.rect.x = self.x

    def blitme(self):
        """Draw the ship at it current location."""
        self.screen.blit(self.image,self.rect)

    def center_ship(self):
        """Center the ship on the screen."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)