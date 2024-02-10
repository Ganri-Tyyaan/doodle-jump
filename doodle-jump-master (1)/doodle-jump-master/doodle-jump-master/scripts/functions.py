import pygame
import os


def load_image(*paths):
    #путь к картинке
    path=os.path.join(*paths)
    #ЗАГРУЖАЕМ КАРТИНКУ
    image=pygame.image.load(path).convert()
    image.set_colorkey((0,0,0))
    #ЫОЗВРАЩАЕМ КАРТИНКУ
    return image
    
    
