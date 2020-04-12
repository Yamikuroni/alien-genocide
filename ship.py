import pygame

class Ship():

    def __init__(self, screen):
        """Initializing the the Ship class"""
        self.screen = screen

        # Loading the image of the ship
        self.image = pygame.image.load("images/player.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Setting the ship position at the bottom of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Movement flags
        self.moving_left = False
        self.moving_right = False

    def displayShip(self):
        """Drawing the ship at the the current location"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Updating the ship state"""
        if self.moving_left:
            self.rect.centerx -= 1
        if self.moving_right:
            self.rect.centerx += 1
