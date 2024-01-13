from scripts.functions import load_image
from scripts.sprite import Sprite
import pygame
class Game:
    def __init__(self)->None:
        self.background = load_image('assets\images\background.png')
        self.player =Sprite((200,200),load_image("assets","images","player,png"))
    def render(self,surface:pygame.Surface)->None:
        surface.blit(self.background,image,(0,0))
        self.player.render(surface)



