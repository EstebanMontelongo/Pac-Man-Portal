import pygame
from rect_object import PacRects
import random


class Blinky(PacRects):

    def __init__(self, x, y, width, height, image, screen, pacman):
        super().__init__(x, y, width, height, image)

        # ============== Testing Random Movement ==============
        self.m_index = 0
        self.m_counter = 0
        # =====================================================

        # current
        self.rect.x = x
        self.rect.y = y
        self.pac = pacman
        self.ghost_speed_x = 5
        self.ghost_speed_y = 0

        self.ghost_timer = 0

        self.screen = screen

        # default position for Blinky using maze
        self.defualt_x = self.pac.maze.blinky_default_x
        self.default_y = self.pac.maze.blinky_default_y

        # ghost alive
        self.ghost_alive = True
        # ghost fear mode
        self.ghost_fear = False
        self.w_collision = False
        # direction
        self.direction = "right"

        # animation images
        self.images = [pygame.image.load(image),
                       pygame.image.load('images/blinky_2.png')]

        self.a_index = 0

        self.counter = 250

        # death animation images
        self.death_image = pygame.image.load('images/ghost_eyes.png')

        # fear animation
        self.fear_images = [pygame.image.load('images/ghost_fear_1.png'),
                            pygame.image.load('images/ghost_fear_2.png'),
                            pygame.image.load('images/ghost_fear_3.png'),
                            pygame.image.load('images/ghost_fear_4.png')]
        self.f_index = 0
        self.w_collision = False
        self.reset_ghost()

    def reset_ghost(self):
        self.rect.x = self.defualt_x
        self.rect.y = self.default_y
        self.direction = "right"
        self.w_collision = False

    def increase_a_index(self):
        self.ghost_timer += 1
        if self.ghost_timer % 10 == 0:
            self.ghost_timer = 0
            self.a_index += 1
            if self.a_index >= len(self.images):
                self.a_index = 0

    def increase_f_index(self):
        self.ghost_timer += 1
        if self.ghost_timer % 10 == 0:
            self.ghost_timer = 0
            self.f_index += 1
            if self.f_index >= len(self.images):
                self.f_index = 0

    # figure out how to slow down animation with timer maybe?
    def draw_(self):
        img = self.images[self.a_index]
        self.screen.blit(img, (self.rect.x, self.rect.y))
        self.increase_a_index()

    def pac_coll(self):
        # collision with fear ghost and pacman
        if self.rect.colliderect(self.pac.rect) and self.pac.ghost_fear and self.ghost_alive:
            self.pac.pacman_alive = True
            self.ghost_alive = False
            self.pac.stats.score += 200
            self.ghost_fear = False
        # collision with pac-man and regular ghost
        elif self.rect.colliderect(self.pac.rect) and not self.pac.ghost_fear and self.ghost_alive:
            self.pac.pacman_alive = False

    def death(self):
        if self.counter > 0:
            self.screen.blit(self.death_image, (self.rect.x, self.rect.y))
            self.counter -= 1
        if self.counter <= 0:
            self.pac.ghost_fear = False
            if not self.ghost_alive:
                self.ghost_alive = True
            self.counter = 250

        # have to implement timer so fear disapears after some time
        # also must figure out a way to switch between images 1,2 with images 3,4
        # to signal warning also with a timer

    def fear(self):

        if self.counter > 0:
            img = self.fear_images[self.f_index]
            self.screen.blit(img, (self.rect.x, self.rect.y))
            self.increase_f_index()
            self.counter -= 1
        if self.counter <= 0:
            self.pac.ghost_fear = False
            if not self.ghost_alive:
                self.ghost_alive = True
            self.counter = 250

        # self.fear_warning()

    def update_movement(self):

        if self.direction == "up":
            self.ghost_speed_x = 0
            self.ghost_speed_y = -5

        if self.direction == "down":
            self.ghost_speed_y = 5
            self.ghost_speed_x = 0

        if self.direction == "left":
            self.ghost_speed_x = -5
            self.ghost_speed_y = 0

        if self.direction == "right":
            self.ghost_speed_x = 5
            self.ghost_speed_y = 0

        self.rect.x += self.ghost_speed_x
        self.rect.y += self.ghost_speed_y

        self.handle_w_coll()

    # will take a direction from the A* algorithm
    def ai_movement(self):

        if self.m_counter % 5 == 0:
            self.m_index = random.randrange(1, 4)
            self.m_counter = 0
        self.m_counter += 1

        if self.m_index == 1:
            self.direction = "left"
            self.ghost_speed_x = -5
            self.ghost_speed_y = 0
        if self.m_index == 2:
            self.direction = "right"
            self.ghost_speed_x = 5
            self.ghost_speed_y = 0
        if self.m_index == 3:
            self.direction = "up"
            self.ghost_speed_x = 0
            self.ghost_speed_y = -5
        if self.m_index == 4:
            self.direction = "down"
            self.ghost_speed_y = 5
            self.ghost_speed_x = 0

        self.handle_w_coll()

    def handle_w_coll(self):
        # checks if ghost updated position collides with wall
        for wall in self.pac.maze.walls:
            if self.rect.colliderect(wall.rect):
                #  print("wall collision")
                self.w_collision = True
                break
                # if there is a collision fix the position
        if self.w_collision:
            if self.direction == "up":
                self.rect.y -= self.ghost_speed_y
                self.direction = "down"
                #  print("direction switched from up => down")

            elif self.direction == "left":
                self.rect.x -= self.ghost_speed_x
                self.direction = "right"
                #   print("direction switched from left => right")

            elif self.direction == "down":
                self.rect.y -= self.ghost_speed_y
                self.direction = "up"
                #  print("direction switched from down => up")

            elif self.direction == "right":
                self.rect.x -= self.ghost_speed_x
                self.direction = "left"
                #  print("direction switched from right => left")

        self.w_collision = False
