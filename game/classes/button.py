import pygame
pygame.font.init()
from .colors import Colors

class Button:
    font:pygame.font.SysFont = pygame.font.SysFont("segio ui", 50, True)
    

    def __init__(self, name:str, coord:tuple[int,int]):
        self.name = name
        self.x, self.y = coord
        self.color = Colors.GRAY
        self.image = Button.font.render(self.name, True, self.color)
        self.img_rect = self.image.get_rect()

    def isClicked(self)->bool:
        x, y = pygame.mouse.get_pos()
        return self.img_rect.collidepoint(x, y) and pygame.mouse.get_pressed()[0] == 1

    def update(self)->None:
        mouse_pos = pygame.mouse.get_pos()
        if self.img_rect.collidepoint(mouse_pos):
            self.color = Colors.WHITE
        else:
            self.color = Colors.GRAY    
        self.image = Button.font.render(self.name, True, self.color)
