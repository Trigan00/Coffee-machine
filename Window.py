import pygame as pg

class Cup(pg.Surface):
    def __init__(self, start_x: int, start_y: int, text: str):
        super().__init__((50, 70))
        self.fill((160, 20, 20))
        self.x = start_x
        self.y = start_y
        self.text = text
    
    def move_left(self, distance: int):
        self.x -= distance
    
    def draw(self, surface: pg.Surface):
        surface.blit(self, (self.x, self.y))

class Window(pg.Surface):
    __GRAY = (169, 169, 169)
    __DARK_GRAY = (105, 105, 105)
    __YELLOW = (255, 225, 131)
    __YELLOW_SHADOW = (223, 197, 110)

    __WIDTH = 500
    __HEIGHT = 200
    
    def __drawBox(self):
        pg.draw.rect(self, self.__DARK_GRAY, (20, 0, 250, self.__HEIGHT))
        pg.draw.rect(self, self.__GRAY, (25, 5, 240, self.__HEIGHT - 10))

        pg.draw.rect(self, (118, 118, 118), (80, 5, 125, 135))

        pg.draw.rect(self, self.__YELLOW, (40, 5, 200, 20))
        pg.draw.rect(self, self.__YELLOW_SHADOW, (40, 5, 200, 4))
        pg.draw.rect(self, self.__YELLOW, (130, 20, 20, 20))
        pg.draw.rect(self, self.__YELLOW_SHADOW, (130, 25, 20, 4))

        #points = [top_left, top_right, bottom_right, bottom_left]
        points = [(80, 140), (205, 140), (265, self.__HEIGHT - 5), (25, self.__HEIGHT - 5)]
        pg.draw.polygon(self, (95, 95, 95), points)


    def __init__(self, flags):
        self.flags = flags
        super().__init__((self.__WIDTH, self.__HEIGHT))
        self.fill(self.__YELLOW)
        
        self.__drawBox()

    def draw_cup(self, text: str):
        self.cup = Cup(270, self.__HEIGHT - 80, text)
        self.cup.draw(self)
        pg.draw.rect(self, self.__YELLOW, (270, 0, 230, self.__HEIGHT))


    def cupMove(self):
        if (self.cup.x == 120):
            self.flags["isCupMove"] = False
        self.cup.move_left(2)
        
    def cupDraw(self):
        self.__drawBox()
        self.cup.draw(self)
        pg.draw.rect(self, self.__YELLOW, (270, 0, 230, self.__HEIGHT))



        