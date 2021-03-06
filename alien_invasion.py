import pygame
import game_functions as gf
from settings import Settings
from ship import Ship
from alien import Alien
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


def run_game():
    """Initialize pygame, settings, and screen objects."""
    pygame.init()
    ai_settings = Settings()

    screen = pygame.display.set_mode(
        (ai_settings.scrren_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make the play button
    play_button = Button(ai_settings, screen, "Play")
    # Creat an instance to store game statistics and create a scoreboard.
    stats = GameStats(ai_settings)
    # print("GameStats Initialization")
    print(stats.score)
    sb = Scoreboard(ai_settings, screen, stats)
    # Make a Ship
    ship = Ship(ai_settings, screen)
    # Make a group to store bullets in.
    bullets = Group()
    # Make an alien.
    alien = Alien(ai_settings, screen)
    # Make a group of aliend
    aliens = Group()
    # Create the fleet of aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)
    # Start the main loop for the game.
    while True:
        # Watch for keybord and mouse events.
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship,
                        aliens, bullets)

        if stats.game_active:
            # Update ship position
            ship.update()
            # Update bullets position and remove old once.
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens,
                              bullets)
            # Update alien position.
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens,
                             bullets)

        # Update screen
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets,
                         play_button)


run_game()
