import pygame

class Ship():

    def __init__(self, screen, settings):
        """Initializing the the Ship class"""
        self.screen = screen
        self.settings = settings

        # Loading the image of the ship
        self.image = pygame.image.load("images/player.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Setting the ship position at the bottom of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Centerx only stores integers, so we need a workaround..
        self.centerx = float(self.rect.centerx)

        # Movement flags
        self.moving_left = False
        self.moving_right = False

    def displayShip(self):
        """Drawing the ship at the the current location"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Updating the ship state"""
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.centerx -= self.settings.ship_speed_factor
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.settings.ship_speed_factor
        
        # Updating the actual rect values of the ship now
        self.rect.centerx = self.centerx
    
