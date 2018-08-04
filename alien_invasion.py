import pygame
import game_functions as gf
from settings import Settings
from ship import Ship
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
    # Start the main loop for the game.
    while True:
        # Watch for keybord and mouse events.
        gf.check_events(ai_settings, screen, ship, bullets)
        # Update ship position
        ship.update()
        bullets.update()

        # Get rid of bullets that have disappeared.
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
        # print()
        # Update screen
        gf.update_screen(ai_settings, screen, ship, bullets)


run_game()
