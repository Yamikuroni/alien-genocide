import pygame
from pygame.sprite import Sprite

class Projectile(Sprite):
    """Class to manage projectiles fired from a ship"""
    def __init__(self, settings, screen, ship):
        super().__init__()
        self.screen = screen

        # Creating the bullet and then settings its position
        self.rect = pygame.rect.Rect(
            ship.rect.left+14, ship.rect.top-7, 
            settings.projectile_width, settings.projectile_height
            )
        
        #The only pos variable thats going to change
        self.y = float(self.rect.y)

        self.color = settings.projectile_color
        self.speed_factor = settings.projectile_speed_factor

    def update(self):
        """Update the projectile position in y axis"""
        self.y -= self.speed_factor
        self.rect.y = self.y
    
    def draw(self):
        """Draw the projectile on screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)