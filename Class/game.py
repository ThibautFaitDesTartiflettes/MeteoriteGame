import pygame
from Class.player import Player
from Class.monster import Monster


# class game
class Game:

    def __init__(self):
        # le jeu est commencé ?
        self.is_playing = False
        # constructeur
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        self.all_monster = pygame.sprite.Group()
        self.pressed = {}

    def start(self):
        self.is_playing = True
        self.spawn_monster(2)

    def update(self, screen):
        # appliquer l'image sur le joueur
        screen.blit(self.player.image, self.player.rect)

        # actualiser barre de vie du joueur
        self.player.update_heatlhbar(screen)

        # récupérer les projectiles + appliquer les images
        for projectile in self.player.all_projectiles:
            projectile.move()

        self.player.all_projectiles.draw(screen)

        # récupérer les monstres + appliquer les images
        for monster in self.all_monster:
            monster.walk()
            monster.update_heatlhbar(screen)

        self.all_monster.draw(screen)

        # lisser les déplacements
        if (self.pressed.get(pygame.K_RIGHT) or self.pressed.get(pygame.K_d)) \
                and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()
        elif (self.pressed.get(pygame.K_LEFT) or self.pressed.get(pygame.K_q)) \
                and self.player.rect.x > 0:
            self.player.move_left()

    def spawn_monster(self, number):
        while number != 0:
            self.all_monster.add(Monster(self))
            number = number - 1

    def check_colission(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def game_over(self):
        self.all_monster = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.is_playing = False
