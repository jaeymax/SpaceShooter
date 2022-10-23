import pygame
import sys
from .constants import Constants

from game.classes.level1scene import Level1Scene
from .menuscene import MainMenuScene


class Window:
    WIDTH:int = Constants.SCREEN_WIDTH
    HEIGHT:int = Constants.SCREEN_HEIGHT
    surface:pygame.Surface
    currentScene = None

    @staticmethod
    def init()->None:
        pygame.init()
        
        Window.surface = pygame.display.set_mode((Window.WIDTH, Window.HEIGHT))
        pygame.display.set_caption("")
        Window.currentScene = MainMenuScene("main_menu", "scene1.png", "menu1.mp3")
        

    @staticmethod 
    def changeScene(newScene)->None:
        Window.currentScene = newScene
      

    @staticmethod
    def pollEvents()->None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                sys.exit()    

        if Window.currentScene.name == "main_menu":
            if Window.currentScene.buttons[0].isClicked():
                Window.changeScene(Level1Scene("level1", "background6.jpg", "level1.ogg"))
            elif Window.currentScene.buttons[1].isClicked():
                sys.exit()


    @staticmethod
    def run()->None:
        Window.init()
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            Window.pollEvents()
            Window.surface.blit(Window.currentScene.surface, (0, 0))
            Window.currentScene.update()
            pygame.display.update()
