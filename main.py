# ajout / initialisation de la librairie pygame
import pygame
# ajout référence game
from Class.game import Game

pygame.init()

# générer la fenêtre de notre jeu
pygame.display.set_caption("MeteoriteFallGame")
screen = pygame.display.set_mode((1080, 720))

# importer l'arrière plan
background = pygame.image.load("assets/bg.jpg")

# charger le jeu
game = Game()

running = True

# boucle du jeu
while running:

    # appliquer l'arrière plan et mettre a jour
    screen.blit(background, (0, -200))

    # appliquer l'image sur le joueur
    screen.blit(game.player.image, game.player.rect)

    # récupérer les projectiles + appliquer les images
    for projectile in game.player.all_projectiles:
        projectile.move()

    game.player.all_projectiles.draw(screen)

    # récupérer les monstres + appliquer les images
    for monster in game.all_monster:
        monster.walk()

    game.all_monster.draw(screen)

    # lisser les déplacements
    if (game.pressed.get(pygame.K_RIGHT) or game.pressed.get(pygame.K_d))\
            and game.player.rect.x + game.player.rect.width < screen.get_width():
        game.player.move_right()
    elif (game.pressed.get(pygame.K_LEFT) or game.pressed.get(pygame.K_q)) \
            and game.player.rect.x > 0:
        game.player.move_left()

    pygame.display.flip()

    # on récupère tous les évents
    for event in pygame.event.get():
        # la fenêtre est-elle en train d'être fermée ?
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        # détection des touches + remplir dictionnaire
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            # detection de la touche de lancement d'un projectile
            if event.key == pygame.K_SPACE or event.key == pygame.K_e:
                game.player.launch_projectile()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
