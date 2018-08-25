class Settings():
    """A class to store all settings for Alien Invaison."""

    def __init__(self):
        """Initialize the game's static settings."""
        # Screen Settings
        self.scrren_width = 1200
        self.screen_height = 700
        self.bg_color = (230, 230, 230)

        # Ship speed settings.
        self.ship_limit = 3

        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)

        # Alien Settings
        self.fleet_drop_speed = 10

        # How quickly the game speed up
        self.speedup_scale = 1.1
        # How quickly the alien point values increses.
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1

        # fleet_direction of 1 represent right and -1 represent left.
        self.fleet_direction = 1

        # Scoring
        self.alien_points = 50

    def increase_speed(self):
        """Increese speed settings."""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
