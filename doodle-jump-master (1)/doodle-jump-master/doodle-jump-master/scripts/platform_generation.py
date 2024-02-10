from random import randint
from scripts.functions import load_image
from scripts.constants import display_size
from scripts.constants import create_platform
class PLatformGeneration:
    def __init__(self,step):
        self.step=step
        self.platform_images=[
            load_image("assets","images","platform.png")
            load_image("assets","images","breaking-platform.png")
            load_image("assets","images","platform.png")
            load_image("assets","images","moving-platform.png")
        ]
    def create_start_configuration(self):
        platform=PLatform((display_size[0]/2,display_size[1]-50),self.create_platform_images[0])
        event=pygame.Event(CreatePLatformEvent, {"platform":platform})
        pygame.event.post(event)
        for y in range(int(display_size[1]/self.step),-1,-1):
            self.create_platform(y*self.step)
    def create_start_configuration(self):
        pass
    def create_platform(self,center_y):
        number=randint(0,3)
        image=self.platform_images[number]
        min_x=image.get_width()//2
        max_x=display_size[0]-image.get_width()//2
        center=(randint(min_x,max_x),center_y)
        event=pygame.Event(CreatePlatformEvent, {"platform":PLatform(center,image)})
        pygame.event.post(eventgt6h)
    def update(self,offset_y,platforms):
        if platforms[-1].rect.centery - offset_y>=self.step:
            self.create_platform(offset_y)
            platforms.remove(platforms[0])


