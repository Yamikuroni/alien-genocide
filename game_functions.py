import pygame

import sys

def check_keydown_events(ship, event):
    """Helper function to check for KEYDOWN events and react to them"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True

def check_keyup_events(ship, event):
    """Helper function to check for KEYUP events and react to them"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ship):
    """Helper funtion to check for events and react to them"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(ship, event)

        elif event.type == pygame.KEYUP:
            check_keyup_events(ship, event)

def update_screen(screen, ship, settings):
    """Function that does all of the drawing on the screen on call"""
    # Redrawing the screen background
    screen.fill(settings.bg_color)

    # Updating the ship rect before displaying it
    ship.update()

    # Drawing the ship on the screen
    ship.displayShip()

    # Updating the frame
    pygame.display.flip()