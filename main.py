import pygame as pg
from CoffeeMachine import CoffeeMachine
from Wave import Wave
from Window import Window

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
    "isCupMove": False
}

coffeeMachine = CoffeeMachine()
(cMX, cMY) = coffeeMachine.get_size()
window = Window(flags)
window.draw_cup(text="Ayaz")


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
            if event.button == 1:  # Левая кнопка мыши
                flags["isCupMove"] = True

    screen.blit(coffeeMachine, (WIDTH // 2 - 250, 40))
    coffeeMachine.blit(window, (10, cMY//1.8))

    if flags["isCupMove"]:
        window.cupMove()
    window.cupDraw()

    for wave in steam:
        wave.update()
        wave.draw(screen)

    pg.display.flip()
    clock.tick(FPS)

pg.quit()
