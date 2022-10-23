from game.classes.button import Button
from .aircraft import Aircraft
from .bullet import Bullet
from typing import List

class PlayerAircraft(Aircraft):

    def __init__(self, name: str, imagePath: str, pos: tuple[int, int]):
        super().__init__(name, imagePath, pos)
        self.speed = 3
        self.bullets:List = []


    def shoot(self) -> None:
        bullet  = Bullet((self.img_rect.x, self.img_rect.y), "laser4.png")
        self.bullets.append(bullet)

    def update(self, surface) -> None:
        pass
        # for bullet in self.bullets:
        #     bullet.update()
        #     bullet.draw(surface)    
        #     if bullet.outOffBounds():
        #         self.bullets.remove(bullet)