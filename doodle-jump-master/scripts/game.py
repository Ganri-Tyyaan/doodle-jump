from scripts.functions import load_image
from scripts.sprite import Sprite
import pygame
from scripts.player import Player
from scripts.platform import Platform
import os
from scripts.constants import display_size

class Game:
    def __init__(self)->None:

        self.background = load_image("assets","images","background.png")
        self.offset_y=0
        self.player=Player(
            (240,600),
            load_image("assets","images","player.png"),
            5,20,0.65
        )
        self.platforms=[
            Platform((240,700), load_image("assets","images","platform.png")),
            Platform((100,450), load_image("assets","images","platform.png")),
            Platform((400,200), load_image("assets","images","platform.png")),
        ]
    def render(self,surface:pygame.Surface)->None:
        surface.blit(self.background,(0,0))
        for platform in self.platforms:
            platform.render(surface, self.offset_y)
        self.player.render(surface, self.offset_y)
    def handle_key_down_event(self,key):
        if key== pygame.K_a:
            self.player.is_walking_left=True
        elif key==pygame.K_d:
            self.player.is_walking_right=True
    def handle_key_up_event(self,key):
        if key == pygame.K_a:
            self.player.is_walking_left=False
        elif key == pygame.K_d:
            self.player.is_walking_right=False
    def update(self):
        self.player.update()

        for platform in self.platforms:
            if self.player.collide_sprite(platform):
                self.player.on_platform=True
        if self.player.rect.bottom-self.offset_y<display_size[1] / 3:
            self.offset_y=self.player.rect.bottom -display_size[1] / 3