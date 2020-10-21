# creating scoreboard display

import pygame.font
from  pygame.sprite import Group

from ship import Ship
from filepath import FilePaths
class Scoreboard:
    """A class to report scoring information."""

    def __init__(self, ai_game):
        """Initialize scorekeeping attributes."""
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # Font settings for scoring information.
        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None, 48)
        # Prepare the initial score image.
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

        # Bring in file path
        self.fp = FilePaths()
        self.record_high_filename = self.fp.record_high_score_path

    def prep_score(self):
        """ Turn the score into a rendered image."""
        rounded_score = round(self.stats.score, -1) # round with -1 as second argument will round the value to neareset 10
        score_str = "Score "+"{:,}".format(rounded_score) # Add comma to numbers
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        # Display the score at the top right of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20 # score is 20 pixel off right screen
        self.score_rect.top = 20 # score is 20 below the top screen

    def prep_high_score(self):
        """ Turn the high score into a rendered image."""
        high_score = round(self.stats.high_score, -1) # round with -1 as second argument will round the value to neareset 10
        high_score_str = "High Score "+"{:,}".format(high_score) # Add comma to numbers
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.settings.bg_color)

        # Center the high score at the top of the screen.
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx # set high score the center of screen 
        self.high_score_rect.top = self.score_rect.top        # set the high score the same as scoreboard

    def prep_level(self):
        """ Turn the level into a render image."""
        level_str =self.stats.level_name + str(self.stats.level)
        self.level_image = self.font.render(level_str,True,self.text_color,self.settings.bg_color)

        # Position the level below the score.
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.screen_rect.right - 20
        self.level_rect.top = self.score_rect.bottom + 20

    def prep_ships(self):
        """Show how many ships are left."""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_game)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    def check_high_score(self):
        """Check to see if there is a new high score."""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            with open(self.record_high_filename,'w') as fh:
                fh.write(str(self.stats.high_score))
            self.prep_high_score()

    def show_score(self):
        """Draw score to the screen."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image,self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)