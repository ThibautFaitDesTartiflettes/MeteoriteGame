# ajout / initialisation de la librairie pygame
import pygame
pygame.init()

# générer la fenêtre de notre jeu
pygame.display.set_caption("MeteoriteFallGame")
screen = pygame.display.set_mode((1080, 720))

#importer l'arrière plan
background = pygame.image.load("assets/bg.jpg")

running = True

# boucle du jeu
while (running):

    #appliquer l'arrière plan et mettre a jour
    screen.blit(background, (0, -200))
    pygame.display.flip()

    # on récupère tous les évents
    for event in pygame.event.get():
        # la fenêtre est-elle en train d'être fermée ?
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()