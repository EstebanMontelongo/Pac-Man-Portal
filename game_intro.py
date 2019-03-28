import pygame.font
import pygame
import pygame.sprite


class GameIntro:
    def __init__(self, screen, play_button, high_score_button, ai_setting):
        self.screen = screen
        self.size = 48
        self.ai_setting = ai_setting
        self.play_button = play_button
        self.score_button = high_score_button
        self.ghost_x = 0
        self.ghost_y = self.ai_setting.screen_height/2
        self.ghost_x_inc = 2
        self.dir_right = True
        self.basic_font1 = pygame.font.SysFont(None, 155)
        self.basic_font2 = pygame.font.SysFont(None, 100)
        self.text1 = self.basic_font1.render("PACMAN ", True, (255, 215, 0), (0, 0, 0))
        self.text1_rect = self.text1.get_rect()
        self.text1_rect.centerx = screen.get_rect().centerx
        self.text1_rect.centery = screen.get_rect().centery = 150

        # pacman animation images
        self.images = [pygame.image.load('images/pacman_1.png'),
                       pygame.image.load('images/pacman_2.png'),
                       pygame.image.load('images/pacman_3.png'),
                       pygame.image.load('images/pacman_4.png'),
                       pygame.image.load('images/pacman_5.png'),
                       pygame.image.load('images/pacman_6.png'),
                       pygame.image.load('images/pacman_7.png')]

        self.p_index = 0

        # fear animation
        self.fear_images = [pygame.image.load('images/ghost_fear_1.png'),
                            pygame.image.load('images/ghost_fear_2.png')]

        self.fear_warning = [pygame.image.load('images/ghost_fear_4.png'),
                             pygame.image.load('images/ghost_fear_1.png')]

        self.clyde_images = [pygame.image.load('images/clyde_1.png'), pygame.image.load('images/clyde_2.png')]
        self.pinky_images = [pygame.image.load('images/pinky_1.png'), pygame.image.load('images/pinky_2.png')]
        self.inky_images = [pygame.image.load('images/inky_1.png'), pygame.image.load('images/inky_2.png')]
        self.blinky_images = [pygame.image.load('images/blinky_1.png'), pygame.image.load('images/blinky_2.png')]
        self.rect = pygame.Rect(self.ai_setting.screen_width/2-30, self.ai_setting.screen_height/2+30, 32, 32)
        self.ghost_index = 0

    def draw(self):
        self.draw_ghost()
        self.draw_pacman()
        self.score_button.draw_button()
        self.play_button.draw_button()
        self.screen.blit(self.text1, self.text1_rect)

    def draw_ghost(self):
        if self.dir_right:
            cylde_img = self.clyde_images[self.ghost_index]
            pinky_img = self.pinky_images[self.ghost_index]
            inky_img = self.inky_images[self.ghost_index]
            blinky_img = self.blinky_images[self.ghost_index]

            cylde_img = pygame.transform.scale(cylde_img, (self.size, self.size))
            pinky_img = pygame.transform.scale(pinky_img, (self.size, self.size))
            inky_img = pygame.transform.scale(inky_img, (self.size, self.size))
            blinky_img = pygame.transform.scale(blinky_img, (self.size, self.size))

            self.screen.fill((0, 0, 0))
            self.screen.blit(cylde_img, (self.ghost_x + self.ghost_x_inc + self.size, self.ghost_y))
            self.screen.blit(pinky_img, (self.ghost_x + self.ghost_x_inc + self.size*2, self.ghost_y))
            self.screen.blit(inky_img, (self.ghost_x + self.ghost_x_inc + self.size*3, self.ghost_y))
            self.screen.blit(blinky_img, (self.ghost_x + self.ghost_x_inc + self.size*4, self.ghost_y))
            self.play_button.draw_button()
            self.score_button.draw_button()
        elif not self.dir_right and self.ghost_x > self.ai_setting.screen_width/3:
            f_img_1 = self.fear_images[self.ghost_index]
            f_img_1 = pygame.transform.scale(f_img_1, (self.size, self.size))
            self.screen.fill((0, 0, 0))
            self.screen.blit(f_img_1, (self.ghost_x + self.ghost_x_inc + self.size, self.ghost_y))
            self.screen.blit(f_img_1, (self.ghost_x + self.ghost_x_inc + self.size*2, self.ghost_y))
            self.screen.blit(f_img_1, (self.ghost_x + self.ghost_x_inc + self.size*3, self.ghost_y))
            self.screen.blit(f_img_1, (self.ghost_x + self.ghost_x_inc + self.size*4, self.ghost_y))
        elif not self.dir_right and self.ghost_x <= self.ai_setting.screen_width / 3:
            fw_img_1 = self.fear_warning[self.ghost_index]
            fw_img_1 = pygame.transform.scale(fw_img_1, (self.size, self.size))
            self.screen.fill((0, 0, 0))
            self.screen.blit(fw_img_1, (self.ghost_x + self.ghost_x_inc + self.size, self.ghost_y))
            self.screen.blit(fw_img_1, (self.ghost_x + self.ghost_x_inc + self.size*2, self.ghost_y))
            self.screen.blit(fw_img_1, (self.ghost_x + self.ghost_x_inc + self.size*3, self.ghost_y))
            self.screen.blit(fw_img_1, (self.ghost_x + self.ghost_x_inc + self.size*4, self.ghost_y))
        self.increace_g_index()
        self.increase_ghost_pos()

    def draw_pacman(self):
        img = self.images[self.p_index]
        img = pygame.transform.scale(img, (self.size, self.size))
        if self.dir_right:
            img = pygame.transform.rotate(img, 0)
            self.screen.blit(img, (self.ghost_x + self.ghost_x_inc + self.size*5 + 10, self.ghost_y))
        if not self.dir_right:
            img = pygame.transform.rotate(img, 180)
            self.screen.blit(img, (self.ghost_x + self.ghost_x_inc + self.size*5 + 10, self.ghost_y))
        self.increase_p_index()

    def increace_g_index(self):
        self.ai_setting.timer_index += 1
        if self.ai_setting.timer_index % 5 == 0:
            self.ai_setting.timer_index = 0
            self.ghost_index += 1
            if self.ghost_index >= len(self.clyde_images):
                self.ghost_index = 0

    def increase_p_index(self):

        self.ai_setting.timer_index += 1
        if self.ai_setting.timer_index % 5 == 0:
            self.ai_setting.timer_index = 0
            self.p_index += 1
            if self.p_index >= len(self.images):
                self.p_index = 0

    def increase_ghost_pos(self):
        if self.ghost_x <= -300:
            self.dir_right = True
        if self.ghost_x >= self.ai_setting.screen_width + 250:
            self.dir_right = False
        if not self.dir_right:
            self.ghost_x -= self.ghost_x_inc
        if self.dir_right:
            self.ghost_x += self.ghost_x_inc

    def check_play_button(self, stats, play_button, mouse_x, mouse_y):
        """Start a new game when the player clicks the play button."""
        play_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
        print(play_clicked)
        if play_clicked and not stats.game_exit:
            # Hide the mouse cursor.
            if play_clicked:
                # Reset the game statistics
                stats.reset_stats()
                stats.game_exit = False
                stats.score_table = False
                # maze
                self.screen.fill((0, 0, 0))

    @staticmethod
    def check_high_score_button(stats, play_button, score_table, high_score_button, mouse_x, mouse_y):
        """Start a new game when the player clicks Play."""
        score_clicked = high_score_button.rect.collidepoint(mouse_x, mouse_y)
        if score_clicked:
            # Reset the game settings.
            stats.reset_stats()
            # display highscore table
            # Display the list of high scores 1-10
            score_table.display_table()
            pygame.display.update()
            play_button.draw_button()
            stats.score_table = True
