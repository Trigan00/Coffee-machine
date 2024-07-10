import pygame


class Terminal:

    total = 0
    __TERMINAL_COLOR = (154, 180, 151)
    __TERMINAL_BORDER = (27, 38, 42)

    def __init__(self, screen, button_types, current_item, button_size=(50, 25), button_color=(200, 200, 200), text_color=(0, 0, 0)):
        self.screen = screen
        self.button_types = button_types
        self.current_item = current_item
        self.button_size = button_size
        self.button_color = button_color
        self.text_color = text_color
        self.font = pygame.font.Font(None, 20)
        self.buttons = self.create_buttons()
        self.pay_but_rec = pygame.Rect(440, 260, 100, 30)
        self.reset_but_rec = pygame.Rect(440, 320, 165, 30)

    def create_buttons(self):
        buttons = []
        for i, type in enumerate(self.button_types):
            if i <= 1: 
                button_rect = pygame.Rect(440, 200 + i * 30, *self.button_size)
                buttons.append((button_rect, type))
            else:
                button_rect = pygame.Rect(490, 200 + (i-2)*30, *self.button_size)
                buttons.append((button_rect, type))
        return buttons

    def draw_buttons(self):
        pygame.draw.rect(self.screen, self.__TERMINAL_BORDER, (430, 130, 120, 170))
        pygame.draw.rect(self.screen, self.__TERMINAL_COLOR, (440, 140, 100, 30))

        pygame.draw.rect(self.screen, self.button_color, (440, 180, 70, 5))
        pygame.draw.circle(self.screen, self.button_color, (530, 185), 10)

        font = pygame.font.SysFont('Arial', 18)
        if self.current_item['is_payed'] == False:
            text = font.render(str(self.total), True, (0,0,0))
        else:
            text = font.render(f"Сдача: {self.total} р.", True, (0,0,0))
        self.screen.blit(text, (445, 145, 100, 50))

        for button_rect, type in self.buttons:
            pygame.draw.rect(self.screen, self.button_color, button_rect)
            pygame.draw.rect(self.screen, self.text_color, button_rect, 2)
            text_surface = self.font.render(f"{type} р.", True, self.text_color)
            text_rect = text_surface.get_rect(center=button_rect.center)
            self.screen.blit(text_surface, text_rect)
        
        pygame.draw.rect(self.screen, self.button_color, self.pay_but_rec)
        pygame.draw.rect(self.screen, self.text_color, self.pay_but_rec, 2)
        text_surface = self.font.render("Оплатить", True, self.text_color)
        text_rect = text_surface.get_rect(center=self.pay_but_rec.center)
        self.screen.blit(text_surface, text_rect)
        
        pygame.draw.rect(self.screen, self.button_color, self.reset_but_rec)
        pygame.draw.rect(self.screen, self.text_color, self.reset_but_rec, 2)
        text_surface = self.font.render("Забрать товар и сдачу", True, self.text_color)
        text_rect = text_surface.get_rect(center=self.reset_but_rec.center)
        self.screen.blit(text_surface, text_rect)


    def check_click(self, pos):
        for button_rect, type in self.buttons:
            if button_rect.collidepoint(pos):
                self.total += type
                return False
        if self.pay_but_rec.collidepoint(pos):
                self.total = self.total - self.current_item['price']
                self.current_item['is_payed'] = True
                return False
        if self.reset_but_rec.collidepoint(pos):
                self.total = 0
                self.current_item['name'] = ""
                self.current_item['price'] = 0
                self.current_item['is_payed'] = False
                return True

