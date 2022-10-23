from .scene import Scene
import pygame
from .PlayerAircraft import PlayerAircraft
from .constants import Constants

class Level1Scene(Scene):
    
    def __init__(self, name, bgImagePath, audioPath) -> None:
        super().__init__(name, bgImagePath, audioPath)
        self.init()

    def init(self) -> None:
        global player
        player = PlayerAircraft("player1", "aircraft1.png", (500, 300))

    def update(self) -> None:
        keys = pygame.key.get_pressed()   
        self.surface.blit(self.bgImage, (0, 0))
        player.update(self.surface)
        player.draw(self.surface)
        for bullet in player.bullets:
            bullet.update()
            bullet.draw(self.surface)    
            if bullet.outOffBounds():
               player.bullets.remove(bullet)

        if keys[pygame.K_LEFT] and player.img_rect.x >= 0:
            player.img_rect.x -= player.speed
        if keys[pygame.K_RIGHT] and player.img_rect.right <= Constants.SCREEN_WIDTH:
            player.img_rect.x += player.speed
        if keys[pygame.K_UP] and player.img_rect.top >= 0:
            player.img_rect.y -= player.speed
        if keys[pygame.K_DOWN] and player.img_rect.bottom <= Constants.SCREEN_HEIGHT:
            player.img_rect.y += player.speed    

        if keys[pygame.K_SPACE]:
            player.shoot()