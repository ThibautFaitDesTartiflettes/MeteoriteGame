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
        self.spawn_monster(2)
        self.pressed = {}

    def spawn_monster(self, number):
        while number != 0:
            self.all_monster.add(Monster(self))
            number = number - 1

    def check_colission(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)
