from rect_object import PacRects


class Maze:
    def __init__(self, screen, pacman):
        self.screen = screen
        self.fruit = []
        self.walls = []
        self.pellets = []
        self.power_pellets = []
        self.sheilds = []
        self.default_portals = []
        self.ghosts = []
        self.pac_x = 0
        self.pac_y = 0
        self.pac = pacman
        self.inky_default_x = 0
        self.inky_default_y = 0
        self.pinky_default_x = 0
        self.pinky_default_y = 0
        self.blinky_default_x = 0
        self.blinky_default_y = 0
        self.clyde_default_x = 0
        self.clyde_default_y = 0
        self.maze_load = ["XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
                          "X---------------------XX---------------------X",
                          "X-@-+.+.+.+.+.+.+.+.+-XX-+.+.+.+.+.+.+.+.+-@-X",
                          "X---------------------XX---------------------X",
                          "X---XXXXX-.-XXXXXXX-.-XX-.-XXXXXXX-.-XXXXX---X",
                          "X-+-XXXXX-+-XXXXXXX-+-XX-+-XXXXXXX-+-XXXXX-+-X",
                          "X--------------------------------------------X",
                          "X-+.+.+.+.+.+.+.+.+.+.+..+.+.+.+.+.+.+.+.+.+-X",
                          "X-.----------------------------------------.-X",
                          "X-.-XXXXX-.-XX-.-XXXXXXXXXXXX-.-XX-.-XXXXX-.-X",
                          "X-+-XXXXX-+-XX-+-XXXXXXXXXXXX-+-XX-+-XXXXX-+-X",
                          "X-.-.......-XX-.------XX------.-XX-.-------.-X",
                          "X-+.+.+.+.+-XX-+..+.+-XX-+.+..+-XX-+.+.+.+.+-X",
                          "X---------.-XX------.-XX-.------XX-.-------.-X",
                          "XXXXXXXXX-+-XXXXXXX-+-XX-+-XXXXXXX-+-XXXXXXXXX",
                          "--------X-.-XXXXXXX-.-XX-.-XXXXXXX-.-X--------",
                          "--------X-+-XX------------------XX-+-X--------",
                          "--------X-.-XX-+.+.+.+.+.+.+..+-XX-.-X--------",
                          "--------X-+-XX------------------XX-+-X--------",
                          "--------X-.-XX-+-XXXXooooXXXX.+-XX-.-X--------",
                          "XXXXXXXXX-+-XX-.-X----------X-.-XX-+-XXXXXXXXX",
                          "---------------+-X.---------X-+---------------",
                          "v.+.+.+.+.+.+...-X-I-P-C-B--X....+.+.+.+.+.+.v",
                          "---------------+-X----------X-+---------------",
                          "XXXXXXXXX-+-XX-.-X----------X-.-XX-+-XXXXXXXXX",
                          "--------X-.-XX-+-XXXXXXXXXXXX-+-XX-.-X--------",
                          "--------X-+-XX-.----------------XX-+-X--------",
                          "--------X-.-XX-+.+.+.+.+M..+..+-XX-.-X--------",
                          "--------X-+-XX------------------XX-+-X--------",
                          "--------X-.-XX-+-XXXXXXXXXXXX.+-XX-.-X--------",
                          "XXXXXXXXX-+-XX-.-XXXXXXXXXXXX..-XX-+-XXXXXXXXX",
                          "X---------------------XX---------------------X",
                          "X-+.+.+.+.+.+.+.+.+.+.XX.+.+.+.+.+.+.+.+.+.+-X",
                          "X---------------------XX---------------------X",
                          "X-.-XXXXX-+-XXXXXXX-+-XX-+-XXXXXXX-+-XXXXX-.-X",
                          "X-+-XXXXX-.-XXXXXXX-.-XX-.-XXXXXXX-.-XXXXX-+-X",
                          "X-.----XX-+------------------------+-XX------X",
                          "X-+..+-XX-...+.+.+.+.+.+.+.+.+.+.+..-XX-+..+-X",
                          "X------XX-+-------------------.----+-XX------X",
                          "XXXX-+-XX-.-XX-.-XXXXXXXXXXXX-.-XX-.-XX-+-XXXX",
                          "XXXX-.-XX-+-XX-+-XXXXXXXXXXXX-+-XX-+-XX-.-XXXX",
                          "X----.-----.XX-.-----XXX--------XX-----------X",
                          "X-+.+.+.+.+-XX-+.+.+.XXX.+.+..+-XX.+.+.+.+.+-X",
                          "X-----------XX-----.-XXX--------XX---------.-X",
                          "X-+-XXXXXXXXXXXXXX-+-XXX-+-XXXXXXXXXXXXXXX-+-X",
                          "X-.-XXXXXXXXXXXXXX-.-XXX-.-XXXXXXXXXXXXXXX-.-X",
                          "X-+-XXXXXXXXXXXXXX-+-XXX-+-XXXXXXXXXXXXXXX-+-X",
                          "X--------------------------------------------X",
                          "X-@.-+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.@-X",
                          "X--------------------------------------------X",
                          "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"]
        self.load_maze()

    def load_maze(self):
        y = 0
        for line in self.maze_load:
            x = 0
            for char in line:
                if char == 'X':
                    block = PacRects(x, y, 19, 19, "images/wall.png")
                    self.walls.append(block)
                if char == "M":
                    self.pac.default_x = x
                    self.pac.default_y = y-8
                    self.pac.set_pos(x, y-8)
                if char == "+":
                    block = PacRects(x, y, 19, 19, "images/pellet.png")
                    self.pellets.append(block)
                if char == "@":
                    block = PacRects(x, y, 19, 19, "images/pellet.png")
                    self.power_pellets.append(block)
                if char == "o":
                    block = PacRects(x, y, 19, 19, "images/sheild.png")
                    self.sheilds.append(block)
                if char == "v":
                    block = PacRects(x, y, 19, 19, "images/invis_portal.png")
                    self.default_portals.append(block)
                if char == "I":
                    self.inky_default_x = x
                    self.inky_default_y = y
                if char == "P":
                    self.pinky_default_x = x
                    self.pinky_default_y = y
                if char == "C":
                    self.clyde_default_x = x
                    self.clyde_default_y = y
                if char == "B":
                    self.blinky_default_x = x
                    self.blinky_default_y = y
                if char == '.':
                    block = PacRects(x, y, 19, 19, "images/invis_portal.png")
                    self.fruit.append(block)
                x += 19
            y += 19

    def render_level(self):
        for wall in self.walls:
            wall.scale_image(19, 19)
            self.screen.blit(wall.object, wall.rect)

            # # ================ used for debugging
            # self.hitbox = (wall.rect.x, wall.rect.y, 19, 19)
            # pygame.draw.rect(self.screen, (255, 0, 0), self.hitbox, 2)
            # # ================

        for sheild in self.sheilds:
            sheild.scale_image(19, 19)
            self.screen.blit(sheild.object, sheild.rect)

            # # ================ used for debugging
            # self.hitbox = (sheild.rect.x, sheild.rect.y, 19, 19)
            # pygame.draw.rect(self.screen, (255, 0, 0), self.hitbox, 2)
            #  # ================

        for pellet in self.pellets:
            pellet.scale_image(12, 12)
            self.screen.blit(pellet.object, pellet.rect)

        for power in self.power_pellets:
            power.scale_image(24, 24)
            self.screen.blit(power.object, power.rect)

        for def_p in self.default_portals:
            def_p.scale_image(19, 19)
            self.screen.blit(def_p.object, def_p.rect)
