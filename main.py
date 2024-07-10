import pygame as pg
from CoffeeMachine import CoffeeMachine
from Wave import Wave
from Window import Window, Cup
from Menu import CoffeeMenu
from Terminal import Terminal

WIDTH = 750
HEIGHT = 900

WAVE_WIDTH = 20
WAVE_HEIGHT = 50
WAVE_COUNT = 5

FPS = 30

BLUE = (77, 208, 228)

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Coffee to go")
clock = pg.time.Clock()

current_item = {
    'name': "",
    'price': 0,
    'is_payed': False
}

coffeeMachine = CoffeeMachine()
(cMX, cMY) = coffeeMachine.get_size()
window = Window()

cupArr = []
cupArr.append(Cup(270, 200 - 80, "Latte", current_item))
cupArr.append(Cup(270, 200 - 80, "Mocha", current_item))
cupArr.append(Cup(270, 200 - 80, "Raf", current_item))

coffee_types = ["Latte", "Mocha", "Raf"]
coffee_prices = [100, 150, 200]
coffee_menu = CoffeeMenu(screen, coffee_types, coffee_prices, current_item)

button_types = [100, 200, 5, 10]
terminal = Terminal(screen, button_types, current_item)


steam = [Wave(WIDTH - 180, 
              HEIGHT - 160, 
              WAVE_HEIGHT + i * 20, 
              WAVE_WIDTH, 1 + i * 0.7) for i in range(WAVE_COUNT)]

running = True
screen.fill(BLUE)


while running:
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            coffee_menu.check_click(event.pos)
            isReset = terminal.check_click(event.pos)
            if isReset:
                for cup in cupArr:
                    cup.resetPos()
            # if terminal.button_rect.collidepoint(event.pos):
            #     terminal.select_note()


    screen.blit(coffeeMachine, (WIDTH // 2 - 250, 40))

    # terminal.display_amount()
    # screen.blit(terminal.surface, (440, 200))
    
    coffeeMachine.blit(window, (10, cMY//1.8))
    coffee_menu.draw_buttons()
    terminal.draw_buttons()
    

    for cup in cupArr:
        if (current_item['name'] == cup.text and current_item['is_payed']):
            cup.move_left(2)
    
    window.drawBox()
    for cup in cupArr:
        cup.draw(window)
    
    for wave in steam:
        wave.update()
        wave.draw(screen)

    pg.display.flip()
    clock.tick(FPS)

pg.quit()
