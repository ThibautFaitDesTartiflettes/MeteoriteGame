import pygame
import random


# classe des monstres
class Monster(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 0.3
        self.velocity = 1
        self.image = pygame.image.load("./assets/mummy.png")
        self.rect = self.image.get_rect()
        self.rect.x = 1080 + random.randint(0, 300)
        self.rect.y = 540

    def update_heatlhbar(self, surface):
        # couleur + position + largeur et épaisseur de la barre de vie
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 10, self.rect.y - 20, self.max_health, 5])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 10, self.rect.y - 20, self.health, 5])

    def walk(self):
        if not self.game.check_colission(self, self.game.all_players):
            self.rect.x -= self.velocity
        else:
            self.game.player.damage(self.attack)

    def damage(self, dmg):
        self.health -= dmg

        if self.health <= 0:
            # réapparition comme un nouveau monstre
            self.rect.x = 1080 + random.randint(0, 300)
            self.health = self.max_health
