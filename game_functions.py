import pygame

import sys

from projectile import Projectile
from alien import Alien

def check_keydown_events(ship, projectiles, event, screen, settings):
    """Helper function to check for KEYDOWN events and react to them"""
    if event.key == pygame.K_ESCAPE:
        sys.exit()
    elif event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_projectile(screen, projectiles, ship, settings)

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

def update_screen(screen, ship, projectiles, settings, aliens):
    """Function that does all of the drawing on the screen on call"""
    # Redrawing the screen background
    screen.fill(settings.bg_color)

    # Updating the ship rect before displaying it
    ship.update()

    # Drawing the ship on the screen
    ship.displayShip()

    # Updating the projectile info and displaying projectiles
    update_projectiles(screen, projectiles, settings)

    # Drawing the alien on top layer
    aliens.update()
    aliens.draw(screen)

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

def fire_projectile(screen, projectiles, ship, settings):
    if len(projectiles) < settings.magazine:
        new_projectile = Projectile(settings, screen, ship)
        projectiles.add(new_projectile)

def get_alien_row_num(screen, ship, settings):
#     """Get the number of rows availible to add on screen"""
    margin_alien = Alien(screen, settings)
    alien_height = margin_alien.rect.height
    ship_height = ship.rect.height

    available_space_y = (settings.screen_height -
    (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    
    return number_rows

def get_num_of_aliens(screen, settings):
    margin_alien = Alien(screen, settings)
    availible_space_x = settings.screen_width - (margin_alien.rect.width * 2)
    num_of_aliens_x = round(availible_space_x / (margin_alien.rect.width * 2))

    return num_of_aliens_x

def create_alien(screen, settings, alien_index, row_number = 0):
    alien = Alien(screen, settings)
    alien.x = alien.rect.width + (2 * alien.rect.width * alien_index)
    alien.y = alien.rect.height + (2 * alien.rect.height * row_number)
    alien.rect.x = alien.x
    alien.rect.y = alien.y

    return alien

def create_alien_row(aliens, screen, settings, row_number = 0):
    num_of_aliens_x = get_num_of_aliens(screen, settings)

    for alien_index in range(num_of_aliens_x):
        alien = create_alien(screen, settings, alien_index, row_number)
        aliens.add(alien)

def create_alien_army(aliens, ship, screen, settings):
    num_of_alien_rows = get_alien_row_num(screen, ship, settings)
    num_of_alien_rows -= 1
    for row_number in range(num_of_alien_rows):
        create_alien_row(aliens, screen, settings, row_number=row_number)
        

