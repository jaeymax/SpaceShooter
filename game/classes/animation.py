import os
import pygame

class Animation:

    def __init__(self, name:str, path:str, ext:str):
        self.name = name
        self.frame_index = 0
        self.speed = 30
        self.done = False
        self.animation_directory = path
        self.num_of_sprites = len(os.listdir(path))
        self.last_update_time = pygame.time.get_ticks()
        self.images = [pygame.image.load(f"{path}/{name}{idx}{ext}") for idx in range(1, self.num_of_sprites + 1)]
        

    def show(self, surface:pygame.Surface, x, y):
        if not self.done:
            surface.blit(self.images[self.frame_index], (x, y))
            if pygame.time.get_ticks() - self.last_update_time >= self.speed:
                self.frame_index += 1
                self.last_update_time = pygame.time.get_ticks()

            if self.frame_index == self.num_of_sprites - 1:
                self.done = True


class Explosion(Animation):

    def __init__(self, name: str, path: str, ext: str):
        super().__init__(name, path, ext)