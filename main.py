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

flags = {
    "Latte": False,
    "Mocha": False
}

currnet_item = {
    'name': "",
    'price': 0
}

coffeeMachine = CoffeeMachine()
(cMX, cMY) = coffeeMachine.get_size()
window = Window()

cupArr = []
cupArr.append(Cup(270, 200 - 80, "Latte", flags))
cupArr.append(Cup(270, 200 - 80, "Mocha", flags))

coffee_types = ["Latte", "Mocha"]
coffee_prices = [" 100 руб.", " 150 руб."]
coffee_menu = CoffeeMenu(screen, coffee_types, coffee_prices, flags)

button_types = [100, 200, 5, 10]
terminal = Terminal(screen, button_types)


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
            terminal.check_click(event.pos)

            # if terminal.button_rect.collidepoint(event.pos):
            #     terminal.select_note()


    screen.blit(coffeeMachine, (WIDTH // 2 - 250, 40))

    # terminal.display_amount()
    # screen.blit(terminal.surface, (440, 200))
    
    coffeeMachine.blit(window, (10, cMY//1.8))
    coffee_menu.draw_buttons()
    terminal.draw_buttons()
    

    for cup in cupArr:
        if (flags[cup.text] == True):
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
