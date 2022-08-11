import pygame, sys, time
from pygame.constants import K_SPACE, K_w, K_a, K_s, K_d
pygame.init()

size = width, height =  800, 800
grid_size = 7
grid_unit_size = int(width/grid_size)
cycle_time = 0.025

screen = pygame.display.set_mode(size)

class Grid:
    def __init__(self, grid_size):
        self.grid_unit_size = grid_size
    def print_grid(self):
        for grid_row in range(0,height,self.grid_unit_size):
            for grid_space in range(0,width,self.grid_unit_size):
                pygame.draw.rect(screen, (200, 200, 255), pygame.Rect(grid_space+(int(self.grid_unit_size/20)), grid_row+(int(self.grid_unit_size/20)), self.grid_unit_size-(int(self.grid_unit_size/10)),self.grid_unit_size-(int(self.grid_unit_size/10))))
                pygame.draw.rect(screen, (190, 190, 190), pygame.Rect(grid_space+(int(self.grid_unit_size/10)), grid_row+(int(self.grid_unit_size/10)), self.grid_unit_size-(int(self.grid_unit_size/5)),self.grid_unit_size-(int(self.grid_unit_size/5))))
    def convert(self, x, convert_from="", mode=""): #convert_from: "grid" or "coord", mode: "move" or "set"
        if convert_from == "coord":
            if mode == "set":
                return((x+grid_unit_size/2)/grid_unit_size)
            elif mode =="move":
                return(x/grid_unit_size)
            else: print(mode, "is not a valid mode")
        elif convert_from == "grid":
            if mode == "set":
                return(x*grid_unit_size-(round(grid_unit_size/2)))
            elif mode == "move":
                return(round(x*grid_unit_size))
            else: print(mode, "is not a valid mode")
        else: print(convert_from, "is not a valid form")

grid = Grid(grid_unit_size)

while 1:
    now = time.time()
    screen.fill((160, 160, 160))
    keys=pygame.key.get_pressed()
    if keys[K_SPACE]:
        quit()
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    grid.print_grid()
    
    pygame.display.flip()
    elapsed = time.time()-now
    if elapsed < cycle_time:
        time.sleep(cycle_time-elapsed)