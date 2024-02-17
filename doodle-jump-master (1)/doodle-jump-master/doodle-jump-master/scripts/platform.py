from scripts.sprite import Sprite
from scripts.constants import display_size
class Platform(Sprite):
    type='Platform'
    def update(self):
        pass
    """Класс-родитель для всех платформ"""
class MovingPLatform(Platform):
    def __init__(self,center,image,speed):
        super().__init__(center,image)
        self.speed=speed
    def update(self):
        self.rect.x+= self.speed
        if self.rect.left<0:
            self.speed=abs(sel.speed)
        elif self.rect.right>display_size[0]:
            self.speed=abs(self.speed)

class BreakingPLatform(Platform):
    ...

class DisappearingPLatform(Platform):
    def __init__(self,center,image,disappearance_time):
        super().__init__(center,image)
        self.player_touched=False
        self.disappearance_start_time=disappearance_time
        self.disappearance_time=disappearance_time
    def update(self):
        if self.player_touched:
            self.disappearance_time -= 1
            mult=self.disappearance_time/self.disappearance_start_time
            self.image.set_alpha(int(255*mult))