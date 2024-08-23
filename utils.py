"""
Этот модуль используется для извлечения отдельных спрайтов из листа спрайтов.
"""
import pygame


class SpriteSheet:
    
    
    def __init__(self, file_name):
        """ Конструктор. Передаем имя файла спрайт-листа. """
        self.sprite_sheet = pygame.image.load(file_name).convert_alpha()

    def get_image(self, x, y, width, height):
        """ Берем одно изображение из большой таблицы
            Переходим в точку (х, у) - местоположение спрайта
        """
        image = pygame.Surface(
            [width, height], pygame.SRCALPHA).convert_alpha()
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        return image
