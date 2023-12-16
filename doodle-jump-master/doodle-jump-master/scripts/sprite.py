class Sprite:
    def __init__(self,center,image):
        self.image=image.copy()
        self.rect=self.image.get_frect()
        self.rect.center=center
#blit отображает картинку по координатам/прямо
    def render(self,surface):
        surface.blit(self.image,self.rect)