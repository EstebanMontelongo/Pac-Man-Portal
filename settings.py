from pygame import mixer


class Settings:
    """A class to store all setting in Pac-Man"""

    def __init__(self):
        """Initialization of pac-man static settings"""
        # Screen Settings
        self.screen_width = 874
        self.screen_height = 969
        self.bg_color = (0, 0, 0)
        # default block size
        self.size = 32

        # pellet pints
        self.pellet = 10
        self.p_pellet = 50

        # ghost fear points
        self.ghost_fear_points = [200, 400, 800, 1600]
        self.fear_index = 0

        # pacman settings
        self.pacman_alive = True
        self.pacman_lives = 3
        self.pacman_speed = 10
        self.pac_default_x = 456
        self.pac_default_y = 513

        self.timer_index = 0

        # sound settings
        self.audio_channels = 5
        self.pacman_channel = mixer.Channel(0)
        self.ghost_channel = mixer.Channel(1)
        self.death_channel = mixer.Channel(2)
        self.music_channel = mixer.Channel(4)
        self.music_interval = 725
        self.music_interval = self.music_interval
        self.music_incr = 25
        self.bgm = 0
        self.last_beat = None
        self.timer_index = 0

        # ghost speed up
        self.ghost_speedup_factor = 1.1

    def initialize_audio_settings(self):
        """Initialization of pygame audio sett."""
        mixer.init()
        mixer.set_num_channels(self.audio_channels)
        self.music_channel.set_volume(0.5)

    def continue_bgm(self):
        pass

    def stop_bgm(self):
        pass

    def increase_speed_level(self):
        """Increase speed settings."""
        if self.ghost_speedup_factor < self.pacman_speed:
            self.ghost_speedup_factor += 2*self.ghost_speedup_factor
