class Game:
    def __init__(self)->None:
        self.background = pygame.image.load(os.path.join('assets\images\background.png'))

    def render(self.surface:pygame.Surface)->None:
        surface.blit(self.background,image,(0,0))
        self.game.render(self.display)
        pygame.display.update()


