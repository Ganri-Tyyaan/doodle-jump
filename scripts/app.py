import pygame
import os
class App:
    def __init__(self) -> None:
        pygame.display.set_caption('DOODLE JUMP')
        pygame.display.set_icon(pygame.image.load(os.path.join('assets','icons','icon.ico')))

        self.display_size =(480,720)
        self.running=True
        self.maxFPS=66

        self.display=pygame.display.set_mode(self.display_size)
        self.clock=pygame.time.Clock()
        self.game=Game()
        def handle_events(self) -> None:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    self.running=False

        def update(self) -> None:
            ...
        def render(self) -> None:
            self.display.fill((0,0,0))
            pygame.display.update()

        def run(self) -> None:
            while self.running:
                self.handle_events()
                self.update()
                self.render()
                self.clock.tick(self.maxFPS)


