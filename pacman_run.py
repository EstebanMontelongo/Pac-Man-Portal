import time
import pygame
from pacman_ import PacMan
from ghost_pinky import Pinky
from ghost_blinky import Blinky
from ghost_inky import Inky
from ghost_clyde import Clyde
from settings import Settings
from game_stats import GameStats
from button import Button
from game_intro import GameIntro
from high_score_table import HighScoreTable
from score_board import Scoreboard
from fruit import Fruit
from portal import Portal

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 215, 0)
ORANGE = (255, 97, 3)
GREEN = (0, 155, 0)
BLUE = (0, 0, 255)
LIGHT_BLUE = (0, 238, 238)
GREY = (107, 107, 107)

# initializing pygame modules
pygame.init()

# Game settings
ai_settings = Settings()

# game surface
screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))

# game caption
pygame.display.set_caption('Pacman')

# initailizing game stats
stats = GameStats(ai_settings)

# pac man object
pac = PacMan(ai_settings.pac_default_x, ai_settings.pac_default_y, ai_settings.size, ai_settings.size,
             'images/pacman_1.png', screen, ai_settings, stats)

# ghosts 0-3, pinky [0], blinky[1], inky[2], clyde[3]

ghosts = [Pinky(0, 0, ai_settings.size, ai_settings.size, 'images/pinky_1.png', screen, pac),
          Blinky(0, 0, ai_settings.size, ai_settings.size, 'images/blinky_1.png', screen, pac),
          Inky(0, 0, ai_settings.size, ai_settings.size, 'images/inky_1.png', screen, pac),
          Clyde(0, 0, ai_settings.size, ai_settings.size, 'images/clyde_1.png', screen, pac)]

# Make the buttons
play_button = Button(screen, "PLAY GAME", (ai_settings.screen_width/2,
                                           ai_settings.screen_height - 400), (255, 255, 255), (0, 0, 0))
high_score_button = Button(screen, "HIGHSCORES", (ai_settings.screen_width/2,
                                                  ai_settings.screen_height - 300), (255, 255, 255), (0, 0, 0))

score_table = HighScoreTable(screen)
# used to control fps
clock = pygame.time.Clock()

# max fps
MAX_PFS = 30

# game intro object
intro = GameIntro(screen, play_button, high_score_button, ai_settings)

score_board = Scoreboard(ai_settings, screen, stats, score_table)

fruit = Fruit(0, 0, 19, 19, pac.maze, screen, stats, pac)

portal = Portal(screen, pac, pac.rect.x, pac.rect.y, 32, 32, 'images/invis_portal.png')

fire = False


def gameloop():
    # temporary fix for variables will create classes and clean the code
    global fire
    while not stats.game_exit:
        # debugging
        # print(str(pac.rect.x) + ", " + str(pac.rect.y))
        # print(pac.stats.score)
        # print(pac.stats.pacman_left)

        while stats.game_over or stats.intro:
            time.sleep(0.01)
            intro.draw()
            # ========== will be game over me & sent back to menu ======
            # screen.fill(BLACK)
            # # maze.render_level()
            # msg_to_screen('Game over, press C to play again or Q to quit!', WHITE)
            pygame.display.update()
            # ==========================================================

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    pac.reset_pac()
                    intro.check_play_button(stats, play_button, mouse_x, mouse_y)
                    intro.check_high_score_button(stats, play_button, score_table, high_score_button, mouse_x, mouse_y)

                # print(event)
                if event.type == pygame.QUIT:
                    stats.game_exit = True
                    stats.game_over = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        stats.game_exit = True
                        stats.game_over = False
                    # reset all default values
                    elif event.key == pygame.K_c:
                        pac.reset_pac()
                        pac.stats.reset_stats()
                        stats.game_exit = False
                        stats.game_over = False
                        stats.intro = False
        # events
        if stats.high_score:
            score_table.display_table()
        for event in pygame.event.get():
            # allows the user to quit
            if event.type == pygame.QUIT:
                stats.game_exit = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                intro.check_play_button(stats, play_button, mouse_x, mouse_y)
                intro.check_high_score_button(stats, play_button, score_table, high_score_button, mouse_x, mouse_y)
            # handle movement events
            if event.type == pygame.KEYDOWN:
                pac.movement(event)
                if event.key == pygame.K_c:
                    pac.stats.pacman_left = 0
                if event.key == pygame.K_SPACE:
                    portal.toggle()

        # if pellets are finished reset pacmans position and increase ghost speed
        if len(pac.maze.pellets) == 0:
            pac.reset_pac()
            pac.maze.load_maze()
            pac.maze.render_level()
            stats.ghost_speed += ai_settings.ghost_speedup_factor

        if pac.pacman_alive and not stats.game_over and not stats.intro and not stats.score_table:
            screen.fill(BLACK)
            pac.maze.render_level()
            pac.update_movement()
            portal.teleport()
            pac.handle_collisions()
            pac.draw()
            portal.fire()
            portal.update_portal_start()
            fruit.draw_random()
            score_board.show_score()
            # everything ghost....
            # initializing ghost fear members
            for ghost in ghosts:
                ghost.ghost_fear = pac.ghost_fear
            for ghost in ghosts:
                ghost.update_movement()
                ghost.ai_movement()
                ghost.pac_coll()
                if not ghost.ghost_fear and ghost.ghost_alive:
                    ghost.draw_()
                elif ghost.ghost_fear and ghost.ghost_alive:
                    ghost.fear()
                elif not ghost.ghost_alive:
                    ghost.death()
                    # add ghost return home function
        elif not pac.pacman_alive and not stats.game_over:
            pac.death_draw()
            time.sleep(0.15)
            if pac.stats.pacman_left == 0:
                stats.game_over = True
                score_table.update_score_list(stats.score)
                # ai_settings.stop_bgm()
                # pygame.mixer.music.load('sound/game-end.wav')
                # pygame.mixer.music.play()
                pac.maze.load_maze()
            if pac.pacman_alive:
                pac.reset_pac()
                for ghost in ghosts:
                    ghost.reset_ghost()
        pygame.display.update()
        clock.tick(MAX_PFS)


gameloop()
