import pygame
from Class.comet import Comet


# classe de la pluie de comète
class CometFallEvent:

    def __init__(self, game):
        self.percent = 0
        self.percent_speed = 5
        self.all_comets = pygame.sprite.Group()
        self.fall_mode = False
        self.surface = game.screen
        self.game = game

    def add_precentage(self):
        self.percent += self.percent_speed / 200

    def reset_percentage(self):
        self.percent = 0

    def is_full(self):
        return self.percent >= 100

    def update_bar(self, surface):

        self.add_precentage()

        pygame.draw.rect(surface, (0, 0, 0), [
            0,
            surface.get_height() - 20,
            surface.get_width(),
            10
        ])
        pygame.draw.rect(surface, (187, 11, 11), [
            0,
            surface.get_height() - 20,
            (surface.get_width() / 100) * self.percent,
            10
        ])

        # remplir la barre
        self.add_precentage()

    def comet_fall(self):
        for i in range(1, 10):
            self.all_comets.add(Comet(self))

    def start_fall(self):
        if self.is_full() and len(self.game.all_monster) == 0:
            self.comet_fall()
            self.fall_mode = True
