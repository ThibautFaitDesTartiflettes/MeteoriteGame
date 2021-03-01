import pygame
from Class.player import Player

# class game
class Game:

    def __init__(self):
        # instanciation du joueur
        self.player = Player()
        self.pressed = {}
