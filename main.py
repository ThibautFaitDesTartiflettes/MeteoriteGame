# ajout / initialisation de la librairie pygame
import pygame
import math
# ajout référence game
from Class.game import Game

pygame.init()

# générer la fenêtre de notre jeu
pygame.display.set_caption("MeteoriteFallGame")
screen = pygame.display.set_mode((1080, 720))

# importer l'arrière plan
background = pygame.image.load("assets/bg.jpg")

# importer la bannière
banner = pygame.image.load("assets/banner.png")
banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 4)

# importer le bouton
play_button = pygame.image.load("assets/button.png")
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 3.33)
play_button_rect.y = math.ceil(screen.get_height() / 2)

# charger le jeu
game = Game()

running = True

# boucle du jeu
while running:

    # appliquer l'arrière plan et mettre a jour
    screen.blit(background, (0, -200))

    # vérifier si le jeu a commencé
    if game.is_playing:
        game.update(screen)
    else:
        screen.blit(play_button, play_button_rect)
        screen.blit(banner, banner_rect)

    pygame.display.flip()

    # on récupère tous les évents
    for event in pygame.event.get():
        # la fenêtre est-elle en train d'être fermée ?
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        # appuyer sur le bouton jouer
        if event.type == pygame.MOUSEBUTTONDOWN:
            if play_button_rect.collidepoint(event.pos):
                game.start()

        # détection des touches + remplir dictionnaire
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            # detection de la touche de lancement d'un projectile
            if event.key == pygame.K_SPACE or event.key == pygame.K_e:
                game.player.launch_projectile()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
