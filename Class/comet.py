import pygame
import random


# classe des comètes
class Comet(pygame.sprite.Sprite):

    def __init__(self, comet_event):
        super().__init__()
        self.velocity = random.randint(1, 3)
        self.image = pygame.image.load("./assets/comet.png")
        self.rect = self.image.get_rect()
        self.comet_event = comet_event
        self.rect.x = random.randint(20, comet_event.surface.get_width() - 80)
        self.rect.y = - random.randint(0, comet_event.surface.get_height() / 2)

    def remove(self):
        self.comet_event.all_comets.remove(self)

        if len(self.comet_event.all_comets) == 0:
            self.comet_event.game.start()

    def fall(self):
        self.rect.y += self.velocity

        if self.rect.y >= 500:
            self.remove()

        if len(self.comet_event.all_comets) == 0:
            self.comet_event.reset_percentage()
            self.comet_event.fall_mode = False

        if self.comet_event.game.check_colission(self, self.comet_event.game.all_players):
            self.remove()
            self.comet_event.game.player.damage(20)
