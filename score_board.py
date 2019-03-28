import pygame.font


class Scoreboard:
    """Score Information"""
    def __init__(self, ai_settings, screen, stats, score_table):
        """Initialization of attributes"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats
        self.score_table = score_table

        # Font for scoring text
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Render the score images.
        self.prep_curr_score()
        self.prep_h_score()

        self.level_image = self.font.render(str(self.stats.level), True,
                                            self.text_color, self.ai_settings.bg_color)
        self.level_rect = 0
        self.score_image = 0
        self.high_score_image = self.font.render('', True,
                                                 self.text_color, self.ai_settings.bg_color)
        self.score_rect = self.high_score_image.get_rect()
        self.high_score_rect = 0

    def prep_curr_score(self):
        """Render image score image."""
        score_rounded = int(round(self.stats.score, -1))
        score_string = "{:,}".format(score_rounded)
        self.score_image = self.font.render(score_string, True, self.text_color,
                                            self.ai_settings.bg_color)

        # Display the score.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 5

    def prep_h_score(self):
        """Rendered high score image."""
        high_score = int(round(self.score_table.high_score_table[0], -1))
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True,
                                                 self.text_color, self.ai_settings.bg_color)

        # Center the high score at the top of the screen.
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def show_score(self):
        """Draw the high score and current score to the screen"""
        self.prep_curr_score()
        self.prep_h_score()
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
