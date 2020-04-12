import pygame

import sys

from projectile import Projectile

def check_keydown_events(ship, projectiles, event, screen, settings):
    """Helper function to check for KEYDOWN events and react to them"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        new_projectile = Projectile(settings, screen, ship)
        projectiles.add(new_projectile)
        

def check_keyup_events(ship, event):
    """Helper function to check for KEYUP events and react to them"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ship, projectiles, screen, settings):
    """Helper funtion to check for events and react to them"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(ship, projectiles, event, screen, settings)

        elif event.type == pygame.KEYUP:
            check_keyup_events(ship, event)

def update_screen(screen, ship, projectiles, settings):
    """Function that does all of the drawing on the screen on call"""
    # Redrawing the screen background
    screen.fill(settings.bg_color)

    # Updating the ship rect before displaying it
    ship.update()

    # Drawing the ship on the screen
    ship.displayShip()

    # Updaating the projectile info
    update_projectiles(screen, projectiles, settings)

    # Updating the frame
    pygame.display.flip()

def update_projectiles(screen, projectiles, settings):
    """Function to update most of the info about projectiles"""
    # Updating the projectile rect before displaying it
    projectiles.update()

    # Drawing the projectiles on the screen
    for projectile in projectiles.sprites():
        projectile.draw()
    
    # Removing used projectiles
    for projectile in projectiles.copy():
        if projectile.rect.bottom <= 0:
            projectiles.remove(projectile)
    