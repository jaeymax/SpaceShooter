import pygame
import sys
from .menuscene import MainMenuScene


class Window:
    WIDTH:int = 1280
    HEIGHT:int = 720
    surface:pygame.Surface
    currentScene = None

    @staticmethod
    def init()->None:
        pygame.init()
        
        Window.surface = pygame.display.set_mode((Window.WIDTH, Window.HEIGHT))
        pygame.display.set_caption("")
        Window.currentScene = MainMenuScene("main_menu", "scene1.png", "menu1.mp3")
        Window.currentScene.init()
        #Window.currentScene.surface.fill((255, 0, 0))
        #Window.surface.blit(Window.currentScene.surface, (0, 0))
        

    @staticmethod 
    def changeScene(newScene)->None:
        Window.currentScene = newScene
        Window.currentScene.init()
      

    @staticmethod
    def pollEvents()->None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


    @staticmethod
    def run()->None:
        Window.init()
        while True:
            Window.pollEvents()
            Window.surface.blit(Window.currentScene.surface, (0, 0))
            Window.currentScene.update()
            pygame.display.update()
