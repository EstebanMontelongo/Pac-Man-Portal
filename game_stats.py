# MAKE IT WORK WITH PAC-MAN CODE #


class GameStats:
    """Statistics for Pac-Man"""
    def __init__(self, ai_settings):
        """Initialization of stats"""
        self.ai_settings = ai_settings
        self.reset_stats()
        # Start Pan-man in an active state
        self.score_table = False
        self.game_exit = False
        self.game_over = False
        self.intro = True
        # High score should never be reset.
        self.high_score = 0
        # Flag for highscore table
        self.flag_score_table = False
        self.pacman_left = self.ai_settings.pacman_lives
        self.score = 0
        self.level = 1
        self.ghost_speed = 5

    def reset_stats(self):
        """Initialize stats that change while game is running"""
        self.game_exit = False
        self.game_over = False
        self.intro = False
        self.pacman_left = self.ai_settings.pacman_lives
        self.score = 0
        self.level = 1
        self.ghost_speed = 5
