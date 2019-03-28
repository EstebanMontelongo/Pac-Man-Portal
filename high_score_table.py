import pygame.font


class HighScoreTable:
    def __init__(self, screen):
        self.screen = screen
        self.high_score_table = list()
        self.basic_font = pygame.font.SysFont(None, 50)
        self.read_scores()
        self.high_score_msg = self.basic_font.render("HIGH SCORES", True, (255, 215, 0), (0, 0, 0))
        self.high_score_msg_rect = self.high_score_msg.get_rect()
        self.text = self.basic_font.render('test',
                                           True, (255, 255, 255), (0, 0, 0))
        self.text_rect = self.text.get_rect()

    def update_score_list(self, score):
        if len(self.high_score_table) >= 10:
            self.high_score_table.pop(10)
        self.high_score_table.insert(0, score)
        self.high_score_table.sort(reverse=True)
        self.update_scores()

    # will update the file with proper list sequence
    def update_scores(self):
        with open('high_scores.txt', 'w') as f:
            f.write(str(self.high_score_table))
        f.close()

    # will read the file into the list
    def read_scores(self):
        with open('high_scores.txt', 'r') as f:
            self.high_score_table = eval(f.readline())
        f.close()

    def display_table(self):
        self.screen.fill((0, 0, 0))
        self.high_score_msg = self.basic_font.render("HIGH SCORES", True, (255, 215, 0), (0, 0, 0))
        self.high_score_msg_rect = self.high_score_msg.get_rect()
        self.high_score_msg_rect.centerx = self.screen.get_rect().centerx
        self.high_score_msg_rect.centery = self.screen.get_rect().centery = 115
        self.screen.blit(self.high_score_msg, self.high_score_msg_rect)
        for x in range(0, (len(self.high_score_table))):
            if x == 0:
                self.text = self.basic_font.render(str(self.high_score_table[x]),
                                                   True, (255, 255, 255), (0, 0, 0))
                self.text_rect = self.text.get_rect()
                self.text_rect.centerx = self.screen.get_rect().centerx
                self.text_rect.centery = self.screen.get_rect().centery = 150
                self.screen.blit(self.text, self.text_rect)
            elif x < 10:
                self.text = self.basic_font.render(str(self.high_score_table[x]),
                                                   True, (255, 255, 255), (0, 0, 0))
                self.text_rect = self.text.get_rect()
                self.text_rect.centerx = self.screen.get_rect().centerx
                self.text_rect.centery = self.screen.get_rect().centery = 150+(x*35)
                self.screen.blit(self.text, self.text_rect)
