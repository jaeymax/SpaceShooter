from game.classes.button import Button
from .aircraft import Aircraft
from .bullet import Bullet
from typing import List
import time

class PlayerAircraft(Aircraft):
    BULLET_COOLDOWN_TIME:int = 0.10


    def __init__(self, name: str, imagePath: str, pos: tuple[int, int]):
        super().__init__(name, imagePath, pos)
        self.speed = 5
        self.bullets:List = []
        self.can_shoot = True
        self.last_cooldown_time = time.time()

    def shoot(self) -> None:
        if self.can_shoot:
            bullet  = Bullet((self.img_rect.x, self.img_rect.y), "laser4.png", "laser3.wav")
            self.bullets.append(bullet)

    def update(self, surface) -> None:
        if time.time() - self.last_cooldown_time >= PlayerAircraft.BULLET_COOLDOWN_TIME:
            self.can_shoot = True
            self.last_cooldown_time = time.time()
        else:
            self.can_shoot = False    
        # for bullet in self.bullets:
        #     bullet.update()
        #     bullet.draw(surface)    
        #     if bullet.outOffBounds():
        #         self.bullets.remove(bullet)