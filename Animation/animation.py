import pygame


# classe des animations
class AnimateSprite(pygame.sprite.Sprite):

    def __init__(self, name, size=(200, 200)):
        super().__init__()
        self.size = size
        self.image = pygame.image.load(f"./assets/{name}.png")
        self.image = pygame.transform.scale(self.image, size)
        self.current_image = 0
        self.images = animations.get(name)
        self.animation = False

    # méthode de démarrage de l'animation
    def start_animation(self):
        self.animation = True

    # animation des sprites
    def animate(self, loop=False):

        if self.animation:
            # passer à l'image suivante
            self.current_image += 1

            if self.current_image >= len(self.images):
                # remettre à zéro l'image
                self.current_image = 0

                if loop is False:
                    self.animation = False

            # modification de l'image d'animation
            self.image = self.images[self.current_image]
            self.image = pygame.transform.scale(self.image, self.size)


# charger les images d'un sprite
def load_animation_images(name):
    images = []
    path = f"./assets/{name}/{name}"

    for num in range(1, 24):
        image_path = path + str(num) + ".png"
        images.append(pygame.image.load(image_path))

    return images


# dictionnaire avec les images de chaques sprites
animations = {
    "mummy": load_animation_images("mummy"),
    "player": load_animation_images("player"),
    "alien": load_animation_images("alien")
}