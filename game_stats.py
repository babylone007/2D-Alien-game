class GameStats():
    """Track statistics for the game."""

    def __init__(self, ai_settings):
        """Initialize statistics."""
        self.ai_settings = ai_settings
        self.rest_stats()
        # Start game in an inactive state.
        self.game_active = False
        # High score (shouldn't be restarted)
        self.high_score = 0

    def rest_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
