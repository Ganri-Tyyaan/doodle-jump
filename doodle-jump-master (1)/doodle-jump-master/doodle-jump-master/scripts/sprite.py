class Sprite:
    def __init__(self,center,image):
        """Класс-родитель для сех игровых ообьектов на сцене"""
        self.image=image.copy()
        self.rect=self.image.get_frect()
        self.rect.center=center
#blit отображает картинку по координатам/прямо
    def render(self,surface,offset_y):
        """Отобразить картинку спрайта"""
        rect=self.rect.move(0, - offset_y)
        surface.blit(self.image,self.rect)
    def collide_sprite(self,other):
        """Сталкивается ли текущий спрайт с другим спрайтом"""
        return self.rect.colliderect(other.rect)