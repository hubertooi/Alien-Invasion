# Track game Statistics

from filepath import FilePaths
class GameStats: 
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game):
        """Initialize statistics"""
        self.settings = ai_game.settings
        self.reset_stats()

        # Start game in an inactive state.
        self.game_active = False

        # High score should never be reset.
        # Every high score will be recorded from previous high score.
        self.fp =FilePaths()
        self.filename = self.fp.record_high_score_path
        with open(self.filename,'r') as fh:
            for i in fh:
                self.high_score = int(i)

        # Level name
        self.level_name = "Level "

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1