import pygame
import time
from rect_object import PacRects
from maze import Maze

# used to control fps
Clock = pygame.time.Clock()

# max fps
MAX_PFS = 30


class PacMan(PacRects):
    def __init__(self, x, y, width, height, image, screen, ai_settings, stats):
        super().__init__(x, y, width, height, image)

        # used for scores, lives, game over & game exit values
        self.stats = stats
        self.ai_settings = ai_settings
        # pacman settings
        self.pacman_size = ai_settings.size
        self.pacman_alive = ai_settings.pacman_alive
        self.screen = screen

        # pacman postitions
        self.rect.x = x
        self.rect.y = y
        self.pacman_x_speed = 5
        self.pacman_y_speed = 0
        self.default_x = 456
        self.default_y = 510
        self.ghost_fear = False
        self.hitbox = (self.rect.x, self.rect.y, self.pacman_size, self.pacman_size)

        # pacman image rotation variables
        self.direction = "right"
        # pacman animation images
        self.images = [pygame.image.load(image),
                       pygame.image.load('images/pacman_2.png'),
                       pygame.image.load('images/pacman_3.png'),
                       pygame.image.load('images/pacman_4.png'),
                       pygame.image.load('images/pacman_5.png'),
                       pygame.image.load('images/pacman_6.png'),
                       pygame.image.load('images/pacman_7.png')]

        self.a_index = 0

        # pacman death animation images
        self.death_images = [pygame.image.load('images/pacman_death_1.png'),
                             pygame.image.load('images/pacman_death_2.png'),
                             pygame.image.load('images/pacman_death_3.png'),
                             pygame.image.load('images/pacman_death_4.png'),
                             pygame.image.load('images/pacman_death_5.png'),
                             pygame.image.load('images/pacman_death_6.png'),
                             pygame.image.load('images/pacman_death_7.png'),
                             pygame.image.load('images/pacman_death_8.png'),
                             pygame.image.load('images/pacman_death_9.png')]

        self.d_index = 0
        self.maze = Maze(screen, self)

    def movement(self, event):
        if event.key == pygame.K_UP:
            self.pacman_y_speed = -5
            self.pacman_x_speed = 0
            self.direction = "up"
        if event.key == pygame.K_DOWN:
            self.pacman_y_speed = 5
            self.pacman_x_speed = 0
            self.direction = "down"
        if event.key == pygame.K_LEFT:
            self.pacman_x_speed = -5
            self.pacman_y_speed = 0
            self.direction = "left"
        if event.key == pygame.K_RIGHT:
            self.pacman_x_speed = 5
            self.pacman_y_speed = 0
            self.direction = "right"
        if event.key == pygame.K_r:
            self.reset_pac()

    def increase_a_index(self):
        self.ai_settings.timer_index += 1
        if self.ai_settings.timer_index % 2 == 0:
            self.ai_settings.timer_index = 0
            self.a_index += 1
            if self.a_index >= len(self.images):
                self.a_index = 0

    def increase_d_index(self):
        self.d_index += 1
        if self.d_index >= len(self.death_images):
            self.d_index = 0

    def width(self):
        return int(self.images[self.a_index].get_width())

    def height(self):
        return int(self.images[self.a_index].get_height())

    def death_draw(self):

        death_img = self.death_images[self.d_index]
        self.screen.blit(death_img, (self.rect.x, self.rect.y))
        # will decrease life only at the last index
        self.increase_d_index()
        # death cycled already
        if self.d_index == 0:
            self.stats.pacman_left -= 1
            time.sleep(0.25)
            self.pacman_alive = True

    def handle_collisions(self):
        self.wall_sheild_coll()
        self.def_tele_coll()
        self.pellet_coll()
        self.p_pellet_coll()

    def wall_sheild_coll(self):
        # handles wall and sheild collisions
        w_collision = False
        s_collision = False
        # checks is pacman updated position collides with wall
        for wall in self.maze.walls:
            if self.rect.colliderect(wall.rect):
                w_collision = True
        # checks is pacman updated position collides with shield
        # for shield in self.maze.sheilds:
        #    if self.rect.colliderect(shield.rect):
        #        s_collision = True
        if w_collision or s_collision:
            if self.direction == "up":
                self.rect.y -= self.pacman_y_speed
            if self.direction == "left":
                self.rect.x -= self.pacman_x_speed
            if self.direction == "down":
                self.rect.y -= self.pacman_y_speed
            if self.direction == "right":
                self.rect.x -= self.pacman_x_speed

    def def_tele_coll(self):
        # Handles default teleport!
        if self.rect.colliderect(self.maze.default_portals[0].rect) or\
                self.rect.colliderect(self.maze.default_portals[1].rect):
            self.update_movement()
            if self.direction == "left":
                self.set_pos(self.maze.default_portals[1].rect.x - 30, self.maze.default_portals[1].rect.y)
                # self.update_movement()
            elif self.direction == "right":
                self.set_pos(self.maze.default_portals[0].rect.x + 20, self.maze.default_portals[0].rect.y)
                # self.update_movement()

    def portal(self):
        pass

    def pellet_coll(self):
        # removes pellets when pacman collides
        for pellet in self.maze.pellets:
            # add points when a collision occurs
            if self.rect.colliderect(pellet.rect):
                self.maze.pellets.remove(pellet)
                self.stats.score += self.ai_settings.pellet

    def p_pellet_coll(self):
        # removes power pellet when collision occurs
        for p_pellet in self.maze.power_pellets:
            # if removal of pallet start ghost blinking
            if self.rect.colliderect(p_pellet.rect):
                self.maze.power_pellets.remove(p_pellet)
                self.stats.score += self.ai_settings.p_pellet
                self.ghost_fear = True

    def update_movement(self):
        self.rect.x += self.pacman_x_speed
        self.rect.y += self.pacman_y_speed

    def draw(self):
        img = self.images[self.a_index]
        # self.scale_image(10, 10)
        if self.direction == "right":
            img = pygame.transform.rotate(img, 0)
        if self.direction == "left":
            img = pygame.transform.rotate(img, 180)
        if self.direction == "up":
            img = pygame.transform.rotate(img, 90)
        if self.direction == "down":
            img = pygame.transform.rotate(img, 270)
        self.screen.blit(img, (self.rect.x, self.rect.y))

        # ================ used for debugging
        # self.hitbox = (self.rect.x, self.rect.y, 32, 32)
        # pygame.draw.rect(screen, (255, 0, 0), self.hitbox, 2)
        # ================
        self.increase_a_index()

    def reset_pac(self):
        self.pacman_y_speed = 0
        self.pacman_x_speed = 0
        self.direction = "right"
        self.rect.x = self.default_x
        self.rect.y = self.default_y
        self.pacman_alive = True

    def set_pos(self, x, y):
        self.rect.x = x
        self.rect.y = y
