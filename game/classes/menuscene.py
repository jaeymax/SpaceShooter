from game.classes.constants import Constants
from .scene import Scene
import pygame
from .button import Button
import sys
#from .keylistener import KeyListener



class MainMenuScene(Scene):
    
    def __init__(self, name, bgImage, audioPath) -> None:
        super().__init__(name, bgImage, audioPath)
        self.init()
        self.buttons = [Button("START GAME", (500, 500)),Button("QUIT", (580, 600))]
        self.buttons[0].img_rect.x = self.buttons[0].x
        self.buttons[0].img_rect.y = self.buttons[0].y
        self.buttons[1].img_rect.x = self.buttons[1].x
        self.buttons[1].img_rect.y = self.buttons[1].y

    def init(self)->None:
        pass
       
    
    def update(self)->None:
        x, y = pygame.mouse.get_pos()
        self.surface.blit(self.bgImage, (0, 0))

        for button in self.buttons:
            button.update()
            self.surface.blit(button.image, button.img_rect)

        

       
        self.surface.blit(pygame.transform.scale(pygame.image.load(Constants.MISC_IMGAES_PATH + "/mousecursor.png"),(80, 80)), (x, y))