import pygame as pg


class Cup(pg.Surface):
    
    __YELLOW = (255, 225, 131)

    def __init__(self, start_x: int, start_y: int, text: str, current_item):
        super().__init__((50, 70))
        self.fill((160, 20, 20))
        self.current_item = current_item
        self.x = start_x
        self.y = start_y
        self.text = text
        self.cup = pg.image.load('cup.png')
        self.cup = pg.transform.scale(self.cup, (70, 70))

        # Инициализация шрифта
        pg.font.init()
        self.font = pg.font.SysFont('Arial', 20)
        self.text_surface = self.font.render(self.text, True, (255, 255, 255))

    def move_left(self, distance: int):
        if (self.x == 110):
            self.current_item['name'] = ""
            # self.current_item['is_payed'] = False
        self.x -= distance

    def draw(self, surface: pg.Surface):
        surface.blit(self.cup, (self.x, self.y))
        text_rect = self.text_surface.get_rect(center=(self.x + 35, self.y + 35))  # Центрируем текст по середине изображения
        surface.blit(self.text_surface, text_rect)
        pg.draw.rect(surface, self.__YELLOW, (270, 0, 230, 200))

    def resetPos(self):
        self.x = 270

class Window(pg.Surface):
    __GRAY = (169, 169, 169)
    __DARK_GRAY = (105, 105, 105)
    __YELLOW = (255, 225, 131)
    __YELLOW_SHADOW = (223, 197, 110)

    __WIDTH = 500
    __HEIGHT = 200
    
    def drawBox(self):
        pg.draw.rect(self, self.__DARK_GRAY, (20, 0, 250, self.__HEIGHT))
        pg.draw.rect(self, self.__GRAY, (25, 5, 240, self.__HEIGHT - 10))

        pg.draw.rect(self, (118, 118, 118), (80, 5, 125, 135))

        pg.draw.rect(self, self.__YELLOW, (40, 5, 200, 20))
        pg.draw.rect(self, self.__YELLOW_SHADOW, (40, 5, 200, 4))
        pg.draw.rect(self, self.__YELLOW, (130, 20, 20, 20))
        pg.draw.rect(self, self.__YELLOW_SHADOW, (130, 25, 20, 4))

        points = [(80, 140), (205, 140), (265, self.__HEIGHT - 5), (25, self.__HEIGHT - 5)]
        pg.draw.polygon(self, (95, 95, 95), points)


    def __init__(self):
        super().__init__((self.__WIDTH, self.__HEIGHT))
        self.fill(self.__YELLOW)
        
        self.drawBox()


        