import pygame
pygame.font.init()

class Button:
    font:pygame.font.SysFont = pygame.font.SysFont("monospace", 50, True)
    

    def __init__(self, name:str, coord:tuple[int,int]):
        self.name = name
        self.x, self.y = coord
        self.color = (150, 150, 150)
        self.image = Button.font.render(self.name, True, self.color)
        self.img_rect = self.image.get_rect()

    def update(self)->None:
        self.image = Button.font.render(self.name, True, self.color)
