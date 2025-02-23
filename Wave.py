import pygame
import math

class Wave:

    WAVE_COLOR = (255, 255, 255, 50)
    

    def __init__(self, start_x, start_y, height, width, speed):
        self.start_x = start_x
        self.start_y = start_y
        self.height = height
        self.speed = speed
        self.width = width
        self.current_height = 0

    def update(self):
        self.current_height += self.speed
        if self.current_height >= self.height:
            self.current_height = 0

    def draw(self, surface):
        wave_surface = pygame.Surface((surface.get_width(), surface.get_height()), pygame.SRCALPHA)
        for i in range(10):
            offset = math.sin((self.current_height / self.height) * math.pi + (i * 1.2)) * self.width
            pygame.draw.circle(wave_surface, self.WAVE_COLOR, 
                               (self.start_x + int(offset), 
                                self.start_y - int(self.current_height * (i / 10))), 
                               self.width)
        surface.blit(wave_surface, (0, 0))
