import pygame


class KeyListener:
    keys: pygame.key = pygame.key.get_pressed()

    @staticmethod
    def isKeyPressed(key:pygame.key)->bool:
        return KeyListener.keys[key]