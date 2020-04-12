import sys

import pygame

from settings import Settings
from ship import Ship
from game_functions import check_events, update_screen

def run_game():
    """Game entry point, creates a screen object."""
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Alien Genocide")

    ship = Ship(screen=screen)

    while True:
        # Watching for keyboard and mouse events.
        check_events(ship)

        # Drawing updates to screen
        update_screen(screen=screen, ship=ship, settings=settings)

run_game()