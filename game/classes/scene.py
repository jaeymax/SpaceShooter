import pygame


class Scene:
    

    def __init__(self, name:str, bgImagePath:str, audioPath:str) -> None:
        self.name = name
        self.bgImage = pygame.transform.scale(pygame.image.load(bgImagePath).convert_alpha(), (1280, 720))
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

