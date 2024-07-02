import pygame as pg
import numpy as np

class CoffeeMachine(pg.Surface):
    __BROWN = (101, 67, 33)
    __BROWN_SHADOW = (73, 48, 24)
    __YELLOW = (255, 225, 131)
    __YELLOW_SHADOW = (223, 197, 110)
    __BLUE = (77, 208, 228)

    __WIDTH = 500
    __HEIGHT = 750
    
    def __change_color(self, image, old_color, new_color):
        image_array = pg.surfarray.pixels3d(image)
        mask = np.all(image_array == old_color, axis=-1)
        image_array[mask] = new_color
        del image_array

    def __draw_rounded_rect(self, surface, color, rect, radius):
        x, y, width, height = rect
        pg.draw.rect(surface, color, (x, y, width, height - radius))  # основной прямоугольник
        pg.draw.rect(surface, color, (x + radius, y + height - radius, width - 2 * radius, radius))  # нижняя часть
        pg.draw.circle(surface, color, (x + radius, y + height - radius), radius)  # левый нижний угол
        pg.draw.circle(surface, color, (x + width - radius, y + height - radius), radius)  # правый нижний угол

        pg.draw.rect(surface, self.__BROWN_SHADOW, (x, y, width, 7))

        coffee_image = pg.image.load('coffee-cup.png')
        coffee_image = pg.transform.scale(coffee_image, (80, 80))
        self.__change_color(coffee_image, (0, 0, 0), (255, 255, 255))
        surface.blit(coffee_image, (width // 2 - 40 + x, height // 2 - 80))

        small_font = pg.font.SysFont('Arial', 26)
        small_font.set_italic(True)
        text = small_font.render('Coffee time', True, (255, 255, 255))
        text_rect = text.get_rect(center=(width // 2 + x, 180))
        surface.blit(text, text_rect)

    def __draw_bottom(self, surface):
        pg.draw.rect(surface, self.__YELLOW_SHADOW, (0, self.__HEIGHT-150, self.__WIDTH, 4))
        for i in range(5):
            pg.draw.rect(surface, self.__YELLOW_SHADOW, (self.__WIDTH - 100, self.__HEIGHT-(130 - i * 7), 70, 3))

    def __init__(self):
        super().__init__((self.__WIDTH+20, self.__HEIGHT+5))
        self.fill(self.__BLUE)

        # Рисование коричневого прямоугольника
        pg.draw.rect(self, self.__BROWN, (0, 0, self.__WIDTH+20, 60))
        # Рисование желтого прямоугольника
        pg.draw.rect(self, self.__YELLOW, (40, 10, self.__WIDTH-60, 40))
        # Отображение текста
        font = pg.font.SysFont('Arial', 28)
        text = font.render('COFFEE TO GO', True, self.__BROWN)
        text_rect = text.get_rect(center=(self.__WIDTH//2, 30))
        self.blit(text, text_rect)

        container = pg.Surface((self.__WIDTH, self.__HEIGHT-60))
        container.fill(self.__YELLOW)
        pg.draw.rect(container, self.__YELLOW_SHADOW, (0, 0, self.__WIDTH, 7))
        self.__draw_rounded_rect(container, self.__BROWN, (40, 0, 200, 250), 70)

        self.__draw_bottom(container)

        self.blit(container, (10, 60))

        pg.draw.rect(self, self.__BROWN_SHADOW, (30, self.__HEIGHT, 70, 5))
        pg.draw.rect(self, self.__BROWN_SHADOW, (self.__WIDTH+20-70-30, self.__HEIGHT, 70, 5))


        