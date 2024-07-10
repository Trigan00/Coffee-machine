import pygame

pygame.init()

class CoffeeMenu:
    def __init__(self, screen, coffee_types, coffee_prices, flags, button_size=(150, 30), button_color=(200, 200, 200), text_color=(0, 0, 0)):
        self.screen = screen
        self.coffee_types = coffee_types
        self.coffee_prices = coffee_prices
        self.flags = flags
        self.button_size = button_size
        self.button_color = button_color
        self.text_color = text_color
        self.font = pygame.font.Font(None, 20)
        self.buttons = self.create_buttons()

    def create_buttons(self):
        buttons = []
        for i, coffee in enumerate(self.coffee_types):
            button_rect = pygame.Rect(440, 350 + i * 50, *self.button_size)
            buttons.append((button_rect, coffee))
        return buttons

    def draw_buttons(self):
        i = 0
        for button_rect, coffee in self.buttons:
            pygame.draw.rect(self.screen, self.button_color, button_rect)
            pygame.draw.rect(self.screen, self.text_color, button_rect, 2)
            text_surface = self.font.render(coffee + self.coffee_prices[i], True, self.text_color)
            text_rect = text_surface.get_rect(center=button_rect.center)
            self.screen.blit(text_surface, text_rect)
            i += 1

    def check_click(self, pos):
        for button_rect, coffee in self.buttons:
            if button_rect.collidepoint(pos):
                self.flags[coffee] = True
        

