import pygame


class Scene:
    

    def __init__(self, name, bgImagePath, audioPath) -> None:
        self.name = name
        self.bgImage = pygame.transform.scale(pygame.image.load(bgImagePath), (1280, 720))
        self.music = pygame.mixer.music.load(audioPath)
        pygame.mixer.music.play()
        self.surface = pygame.Surface((1280, 720))


    #@staticmethod
    def init(self)->None:
       pass

    #@staticmethod
    def render(self)->None:
        pass

    #@staticmethod
    def update(self)->None:
        pass

