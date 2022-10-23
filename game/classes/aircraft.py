import pygame

class Aircraft:

    def __init__(self, name:str, imagePath:str, pos:tuple[int, int]):
        self.name = name
        self.image = pygame.transform.scale(pygame.image.load(imagePath).convert_alpha(), (200, 200))
        self.img_rect = self.image.get_rect()
        self.img_rect.x = pos[0]
        self.img_rect.y = pos[1]
        self.health = 100
        self.max_health = 100

    def shoot(self)->None:
        pass

    def move(self)->None:
        pass

    def draw(self, surface):
        surface.blit(self.image, self.img_rect)

        