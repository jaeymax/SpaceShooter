from .scene import Scene
import pygame

class MainMenuScene(Scene):
    
    def __init__(self, name) -> None:
        super().__init__(name)


    def init()->None:
        pass


    def update(self)->None:
        self.surface.fill((255, 0, 0))     