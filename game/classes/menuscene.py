from .scene import Scene
import pygame
from .button import Button

startButton:Button = Button("START GAME", (500, 600))

class MainMenuScene(Scene):
    
    def __init__(self, name, bgImage, audioPath) -> None:
        super().__init__(name, bgImage, audioPath)


    def init(self)->None:
        #pygame.mouse.set_visible(False)
        pass
        

    def update(self)->None:
        startButton.update()
        self.surface.blit(self.bgImage, (0, 0))

        x, y = pygame.mouse.get_pos()

        

        if startButton.image.get_rect().collidepoint(x, y):
            print("yes")
            startButton.color = (255, 255, 255)
        else:
            print("no")
            startButton.color = (150, 150, 150)    

        self.surface.blit(startButton.image, (startButton.x, startButton.y))

        self.surface.blit(pygame.transform.scale(pygame.image.load("mousecursor.png"),(80, 80)), (x, y))