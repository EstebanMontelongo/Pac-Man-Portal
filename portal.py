import pygame
from rect_object import PacRects


class Portal(PacRects):
    def __init__(self, screen, pacman, x, y, width, height, image):
        size_w = width
        size_h = height
        super().__init__(x, y, size_w, size_h, image)
        self.screen = screen
        self.pac = pacman
        self.size = size_w

        self.rect.x = self.pac.rect.x
        self.rect.y = self.pac.rect.y

        self.rect_p2 = pygame.Rect(x, y, size_w, size_h)
        self.rect_p2.x = self.pac.rect.x
        self.rect_p2.y = self.pac.rect.y

        self.portals_rect = [self.rect, self.rect_p2]

        self.p1_color = (0, 0, 255)
        self.p2_color = (255, 97, 3)

        self.portal_speed = 20

        self.p1_print = False
        self.p2_print = False

        self.p1_coll = False
        self.p2_coll = False

        self.p1_stopped = False
        self.p2_stopped = False

        self.direction_fired = self.pac.direction

        self.toggle_index = 0

    def update_portal_start(self):
        # if both portals are stopped after collision fix( coll false) and user to want to print another
        # portal toggle print off and update portals start with pacman rect
        if self.p1_print and not self.p2_print:
            self.portals_rect[1].x = self.pac.rect.x
            self.portals_rect[1].y = self.pac.rect.y
        if not self.p1_print and not self.p2_print:
            self.portals_rect[0].x = self.pac.rect.x
            self.portals_rect[0].y = self.pac.rect.y

    def update_movement(self):
        # If i can print p1 and p1 is at a stop then increase position
        if self.p1_print and not self.p1_stopped:
            if self.direction_fired == "right":
                self.portals_rect[0].x += self.portal_speed
            if self.direction_fired == "left":
                self.portals_rect[0].x -= self.portal_speed
            if self.direction_fired == "up":
                self.portals_rect[0].y -= self.portal_speed
            if self.direction_fired == "down":
                self.portals_rect[0].y += self.portal_speed

        # If i can print p2 and p2 is at a stop then increase position
        elif self.p2_print and not self.p2_stopped:
            if self.direction_fired == "right":
                self.portals_rect[1].x += self.portal_speed
            if self.direction_fired == "left":
                self.portals_rect[1].x -= self.portal_speed
            if self.direction_fired == "up":
                self.portals_rect[1].y -= self.portal_speed
            if self.direction_fired == "down":
                self.portals_rect[1].y += self.portal_speed

        # handles portal collisions and fixed them
        self.portal_wall_coll()

    def portal_wall_coll(self):
        # check is the updated movement causes a collision,
        # if it does correct it and set coll to false and stopped true
        for wall in self.pac.maze.walls:
            if self.portals_rect[0].colliderect(wall.rect):
                self.p1_coll = True
        for sheild in self.pac.maze.sheilds:
            if self.portals_rect[0].colliderect(sheild.rect):
                self.p1_coll = True
        for wall in self.pac.maze.walls:
            if self.portals_rect[1].colliderect(wall.rect):
                self.p2_coll = True
        for sheild in self.pac.maze.sheilds:
            if self.portals_rect[1].colliderect(sheild.rect):
                self.p1_coll = True

        if self.p1_coll:
            if self.direction_fired == "up":
                self.portals_rect[0].y += self.portal_speed
            if self.direction_fired == "left":
                self.portals_rect[0].x += self.portal_speed
            if self.direction_fired == "down":
                self.portals_rect[0].y -= self.portal_speed
            if self.direction_fired == "right":
                self.portals_rect[0].x -= self.portal_speed
            self.p1_stopped = True
            self.p1_coll = False

        if self.p2_coll:
            if self.direction_fired == "up":
                self.portals_rect[1].y += self.portal_speed
            if self.direction_fired == "left":
                self.portals_rect[1].x += self.portal_speed
            if self.direction_fired == "down":
                self.portals_rect[1].y -= self.portal_speed
            if self.direction_fired == "right":
                self.portals_rect[1].x -= self.portal_speed
            self.p2_stopped = True
            self.p2_coll = False

    def draw_portals(self):
        if self.p1_print:
            pygame.draw.rect(self.screen, self.p1_color, self.portals_rect[0])
        if self.p2_print:
            pygame.draw.rect(self.screen, self.p2_color, self.portals_rect[1])

    def fire(self):
        self.update_movement()
        self.draw_portals()

    def teleport(self):
        if self.pac.rect.colliderect(self.portals_rect[0]) and self.p1_stopped and self.p2_print:
            self.pac.set_pos(self.portals_rect[1].x, self.portals_rect[1].y)
            self.p1_print = False
            self.p2_print = False
        if self.pac.rect.colliderect(self.portals_rect[1]) and self.p2_stopped and self.p1_print:
            self.pac.set_pos(self.portals_rect[0].x, self.portals_rect[0].y)
            self.p1_print = False
            self.p2_print = False

    def toggle(self):
        # set the direction of portal movement base of the direction pacman is facing

        if self.toggle_index == 0:
            self.p1_print = True
            self.p2_print = False
            self.toggle_index += 1
        elif self.toggle_index == 1:
            self.p2_print = True
            self.p1_print = True
            self.toggle_index += 1
        # user tries to fire after the second portal placed reset all
        elif self.toggle_index == 2:
            self.p1_print = False
            self.p2_print = False
            self.p1_coll = False
            self.p1_stopped = False
            self.p2_coll = False
            self.p2_stopped = False
            self.toggle_index = 0
        self.direction_fired = self.pac.direction
