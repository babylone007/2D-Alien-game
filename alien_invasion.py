import pygame
import game_functions as gf
from settings import Settings
from ship import Ship
from alien import Alien
from pygame.sprite import Group


def run_game():
    """Initialize pygame, settings, and screen objects."""
    pygame.init()
    ai_settings = Settings()

    screen = pygame.display.set_mode(
        (ai_settings.scrren_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make a Ship
    ship = Ship(ai_settings, screen)
    # Make a group to store bullets in.
    bullets = Group()
    # Make an alien.
    alien = Alien(ai_settings, screen)
    # Make a group of alien
    aliens = Group()
    # Create the fleet of aliens
    gf.create_fleet(ai_settings, screen, aliens)
    # Start the main loop for the game.
    while True:
        # Watch for keybord and mouse events.
        gf.check_events(ai_settings, screen, ship, bullets)
        # Update ship position
        ship.update()
        # Update bullets position and remove old once.
        gf.update_bullets(bullets)
        # Update screen
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)


run_game()
