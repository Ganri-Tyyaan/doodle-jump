import pygame
import os
from scripts.game import Game
from scripts.functions import load_image

class App:
    def __init__(self) -> None:
        self.display_size =(480,720)
        self.running=True
        self.maxFPS=567

        self.display=pygame.display.set_mode(self.display_size)
        self.clock=pygame.time.Clock()
        self.game=Game()

        pygame.display.set_caption('DOODLE JUMP')
        pygame.display.set_icon(load_image("assets","icons","icon.ico"))

        def handle_events(self) -> None:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    self.running=False

        def update(self) -> None:
            ...
        def render(self) -> None:
            self.display.fill((0,0,0))
            self.game.render(self.display)
            pygame.display.update()

        def run(self) -> None:
            while self.running:
                self.handle_events()
                self.update()
                self.render()
                self.clock.tick(self.maxFPS)


