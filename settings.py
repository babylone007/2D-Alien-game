class Settings():
    """A class to store all settings for Alien Invaison."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen Settings
        self.scrren_width = 800
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # Ship speed settings.
        self.ship_speed_factor = 1.5

        # Bullet settings
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
