import pygame
from Class.player import Player
from Class.monster import Monster

# class game
class Game:

    def __init__(self):
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        self.all_monster = pygame.sprite.Group()
        self.spawn_monster()
        self.pressed = {}

    def spawn_monster(self):
        self.all_monster.add(Monster(self))

    def check_colission(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)
