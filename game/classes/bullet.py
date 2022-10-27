import pygame

from game.classes.constants import Constants

class Bullet:

    def __init__(self, pos:tuple[int, int], imagePath:str, soundPath:str) -> None:
        self.image = pygame.image.load(imagePath).convert_alpha()
        self.img_rect = self.image.get_rect()
        self.img_rect.x = pos[0]
        self.img_rect.y = pos[1]
        self.speed = 8
        self.sound = pygame.mixer.Sound(soundPath)
        self.sound.play()

    def draw(self, surface)->None:
        surface.blit(self.image, self.img_rect)

    def outOffBounds(self)->bool:
        return self.img_rect.top <= 0 or self.img_rect.top >= Constants.SCREEN_HEIGHT

    def update(self)->None:
        self.img_rect.y -= self.speed    