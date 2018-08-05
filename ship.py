import pygame


class Ship():
    """A class to modilyze a ship."""

    def __init__(self, ai_settings, screen):
        """Initialize the ship and set it's starting position."""
        self.screen = screen
        self.ai_settings = ai_settings
        # Load the image and get it's rect.
        ship_image_path = '/home/user1/pythonTuto/py_crash_course/alian_invasion/'
        ship_image_path += 'images/ship.bmp'
        self.image = pygame.image.load(ship_image_path)
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Star each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Store a decimal value for the ship's center
        self.center = float(self.rect.centerx)

        # Moving flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on the movement flag."""
        # Updae the ship's center value, not the rect.
        if self.moving_right and self.rect.centerx < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.centerx > 0:
            self.center -= self.ai_settings.ship_speed_factor
        # Update rect object from self.center
        self.rect.centerx = self.center

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
