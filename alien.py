import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Class representing an alien object"""
    def __init__(self, screen, settings):
        super().__init__() 

        self.settings = settings
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.image = pygame.image.load("images/alien.bmp")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def display(self):
        """Function to display the Alien obj"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Function to update alien position"""
        self.x += 0
        self.rect.x = self.x
        
        