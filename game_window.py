import sys

import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from game_functions import check_events, update_screen, create_alien_army


def run_game():
    """Game entry point, creates a screen object."""
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Alien Genocide")

    ship = Ship(screen=screen, settings=settings)

    # Group to store aliens
    aliens = Group()

    # Group to store projectiles
    projectiles = Group()

    while True:
        # Watching for keyboard and mouse events.
        check_events(ship, projectiles, screen, settings)

        # Drawing alien row
        create_alien_army(aliens, ship, screen, settings)

        # Drawing updates to screen
        update_screen(screen=screen, ship=ship, settings=settings, projectiles=projectiles, aliens=aliens)

run_game()