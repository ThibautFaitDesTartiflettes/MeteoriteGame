import pygame
from Class.player import Player
from Class.monster import Mummy
from Class.monster import Alien
from Class.comet_event import CometFallEvent
from Sound.sounds import SoundManager

# class game
class Game:

    def __init__(self, screen):
        # le jeu est commencé ?
        self.is_playing = False
        # constructeur
        self.screen = screen
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        self.comet_event = CometFallEvent(self)
        self.all_monster = pygame.sprite.Group()
        self.sound_manager = SoundManager()
        self.font = pygame.font.SysFont("monospace", 16)
        self.score = 0
        self.pressed = {}

    def start(self):
        self.is_playing = True
        self.spawn_monster(Mummy)
        self.spawn_monster(Mummy)
        self.spawn_monster(Alien)

    def update(self, screen):
        # afficher le score sur l'écran
        score_text = self.font.render(f"Score : {self.score}", True, (0, 0, 0))
        screen.blit(score_text, (20, 20))

        # appliquer l'image sur le joueur
        screen.blit(self.player.image, self.player.rect)

        # actualiser barre de vie du joueur
        self.player.update_heatlhbar(screen)

        # actualiser la barre de l'event des comets
        self.comet_event.update_bar(screen)

        # actualiser l'animation du joueur
        self.player.update_animation()

        # récupérer les projectiles + appliquer les images
        for projectile in self.player.all_projectiles:
            projectile.move()

        self.player.all_projectiles.draw(screen)

        # récupérer les monstres + appliquer les images
        for monster in self.all_monster:
            monster.walk()
            monster.update_heatlhbar(screen)
            monster.update_animation()

        self.all_monster.draw(screen)

        # récupérer les comètes + appliquer les images
        for comet in self.comet_event.all_comets:
            comet.fall()

        self.comet_event.all_comets.draw(screen)

        # lisser les déplacements
        if (self.pressed.get(pygame.K_RIGHT) or self.pressed.get(pygame.K_d)) \
                and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()
        elif (self.pressed.get(pygame.K_LEFT) or self.pressed.get(pygame.K_q)) \
                and self.player.rect.x > 0:
            self.player.move_left()

    def spawn_monster(self, monster_name):
        self.all_monster.add(monster_name.__call__(self))

    def check_colission(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def add_score(self, points):
        self.score += points

    def game_over(self):
        self.all_monster = pygame.sprite.Group()
        self.comet_event.all_comets = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.comet_event.reset_percentage()
        self.score = 0
        self.sound_manager.play("game_over")
        self.is_playing = False
