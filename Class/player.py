import pygame
from Class.projectile import Projectile
from Animation import animation


# classe joueur
class Player(animation.AnimateSprite):

    def __init__(self, game):
        super().__init__("player")
        self.game = game
        self.health = 150
        self.max_health = 150
        self.attack = 10
        self.velocity = 5
        self.all_projectiles = pygame.sprite.Group()
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500

    def update_animation(self):
        self.animate()

    def update_heatlhbar(self, surface):
        # couleur + position + largeur et épaisseur de la barre de vie
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 25, self.rect.y + 10, self.max_health, 7])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 25, self.rect.y + 10, self.health, 7])

    def move_right(self):
        if not self.game.check_colission(self, self.game.all_monster):
            self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity

    def launch_projectile(self):
        self.all_projectiles.add(Projectile(self))
        self.start_animation()
        self.game.sound_manager.play("tir")

    def damage(self, dmg):
        if self.health - dmg >= dmg:
            self.health -= dmg
        else:
            self.game.game_over()
