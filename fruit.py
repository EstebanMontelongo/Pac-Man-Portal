from rect_object import PacRects
import random
import pygame


class Fruit(PacRects):
    """ fruits for pac-man to eat throughout the game"""
    def __init__(self, x, y, width, height, maze, screen, stats, pacman):
        image = 'images/apple.png'
        super(Fruit, self).__init__(x, y, width, height, image)
        self.images = [pygame.image.load('images/apple.png'), pygame.image.load('images/cherry.png'),
                       pygame.image.load('images/peach.png'), pygame.image.load('images/strawberry.png')]
        self.restore_images = self.images
        self.maze = maze
        self.screen = screen
        self.stats = stats
        self.pac = pacman
        self.timer_index = 0
        self.timer_max = 1000
        self.ran_rect = random.randrange(len(self.maze.fruit))
        self.ran_index = random.randrange(len(self.images))

    def draw_random(self):
        self.collision()
        self.timer_index += 1
        if self.timer_index % self.timer_max == 0:
            self.timer_index = 0
            self.ran_rect = random.randrange(len(self.maze.fruit))
            self.ran_index = random.randrange(len(self.images))
        random_rect = self.maze.fruit[self.ran_rect].rect
        self.rect.x = random_rect.x
        self.rect.y = random_rect.y
        self.collision()
        self.screen.blit(self.images[self.ran_index], (self.rect.x, self.rect.y))

    def collision(self):
        if self.rect.colliderect(self.pac.rect):
            self.stats.score += 100
            # self.timer_index = self.timer_index
            self.ran_rect = random.randrange(len(self.maze.fruit))
