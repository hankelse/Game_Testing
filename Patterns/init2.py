
import pygame, sys, time, random, math
from pygame.constants import K_SPACE, K_ESCAPE, K_w, K_a, K_s, K_d


pygame.init()

size = width, height =  1000, 1000
# size = width, height = pygame.display.get_window_size()
cycle_time = 0.0001

screen = pygame.display.set_mode(size)
# screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)

cell_size = 4
grid_width, grid_height = math.floor(width/cell_size), math.floor(height/cell_size)
colors = {
    0: (0, 0, 0),
    1: (255, 255, 255),
    2: (255, 0, 0),
    3: (200, 0, 0),
    4: (150, 0, 0),
    5: (100, 0, 0),
}

def create_grid():
    grid = []
    for i in range(int(height/cell_size)):
        row = []
        for n in range(int(width/cell_size)):
            row.append(0)
        grid.append(row)
    
    return grid


def get_neighbors(infection_range, row, item):
    options = []
    for i in range(-1*infection_range, infection_range+1):
        for n in range(-1*infection_range, infection_range+1):
            options.append([n + item, i + row])
    options.remove([item, row])

    final_options = []

    for option in options: 
        if option[0] >= 0 and option[1] >= 0 and option[0] < grid_height and option[1] < grid_width: final_options.append(option)
    return final_options


def draw(grid):
    for row in range(len(grid)):
        for item in range(len(grid[row])):
            pygame.draw.rect(screen, colors[grid[row][item]], pygame.Rect(item*cell_size, row*cell_size, cell_size, cell_size))

grid = create_grid()

class Patterns:
    def __init__(self, pattern):
        self.pattern = pattern
    def update(self, grid):
        if self.pattern == 1:
            grid = self.pattern_1(grid)
        elif self.pattern == 2:
            grid = self.pattern_2(grid)
        elif self.pattern == 3:
            grid = self.pattern_3(grid)
        elif self.pattern == 4:
            grid = self.pattern_4(grid)
        elif self.pattern == 5:
            grid = self.pattern_5(grid)
        

        return grid
    def pattern_1(self,old_grid):
        grid = old_grid.copy()
        for row in range(len(grid)):
            for item in range(len(grid[row])):
                options = get_neighbors(1, row, item)
                count = 0
                for option in options:

                    if grid[option[0]][option[1]] == 1:
                        count+= 1
                
                if count == 0 and random.randint(0, 400)==2: grid[row][item] = 1
                elif count >= 1 and count <=2: grid[row][item] = 1
                elif count > 2: grid[row][item] = 0
        return grid

    def pattern_2(self,old_grid):
        grid = old_grid.copy()
        for row in range(len(grid)):
            for item in range(len(grid[row])):
                options = get_neighbors(1, row, item)
                count = 0
                for option in options:
                    if grid[option[0]][option[1]] == 1:
                        count+= 1
                
                num = 6
                if count == 0 and random.randint(0, 600)==2: grid[row][item] = 1
                elif count == num:
                    for option in options: grid[option[0]][option[1]] =1
                elif count >= 1 and count <num: grid[row][item] = 1
                elif count > num: grid[row][item] = 0
                
        return grid
    def pattern_3(self, old_grid):
        grid = old_grid.copy() 
        for num in [1, 2, 3, 4, 5]: 
            for row in range(len(grid)):
                for item in range(len(grid[row])):
                    y = row
                    x = item
                    if grid[y][x] == num:
                        spreading = True
                        if random.randint(0, 10) == 2:
                            while spreading == True:
                                options = get_neighbors(1, y, x)
                                if random.randint(0, 200) == 8: spreading = False
                                choice = random.choice(options)
                                if grid[choice[0]][choice[1]] == num: spreading = False
                                else:
                                    grid[choice[0]][choice[1]] = num
                                    x, y = choice[1], choice[0]
        return grid

    def pattern_4(self, old_grid):
        grid = old_grid.copy()
        for row in range(len(grid)):
            for item in range(len(grid[row])):
                options = get_neighbors(1, row, item)
                count = 0
                nearby_activated = []
                for option in options:
                    if grid[option[0]][option[1]] != 0:
                        nearby_activated.append(option)
                if len(nearby_activated) == 8: break
                elif len(nearby_activated) > 5: 
                    for option in nearby_activated:
                        if random.randint(0, 20) == 1: grid[option[0]][option[1]] = 0
                elif len(nearby_activated) > 3: 
                    for option in nearby_activated:
                        if random.randint(0, 10) == 1: grid[option[0]][option[1]] = 0
                elif len(nearby_activated) >= 1: 
                    for option in nearby_activated:
                        if random.randint(0, 100) == 1: grid[option[0]][option[1]] = 0
                elif len(nearby_activated) == 0: 
                    for option in nearby_activated:
                        grid[option[0]][option[1]] = 0
        return grid
                





pattern_number = 4

if pattern_number == 3:
    grid[random.randint(0, grid_width-1)][random.randint(0, grid_height-1)] = 1
    grid[random.randint(0, grid_width-1)][random.randint(0, grid_height-1)] = 2
    grid[random.randint(0, grid_width-1)][random.randint(0, grid_height-1)] = 3
    grid[random.randint(0, grid_width-1)][random.randint(0, grid_height-1)] = 4
    grid[random.randint(0, grid_width-1)][random.randint(0, grid_height-1)] = 5

pattern = Patterns(pattern_number)

last_move = 0
delay = 0.01

#grid[10][100] = 1

while 1:
    now = time.time()
    screen.fill((160, 160, 160))
    keys=pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        quit()
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if pattern_number == 4 and event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            x, y = int(mx/cell_size), int(my/cell_size)
            options = get_neighbors(1, y, x)
            grid[y][x] = 1
            for option in options: grid[option[0]][option[1]] = 1
    

    #if keys[K_SPACE] and time.time()-last_move > delay: 
    for i in range(3): grid = pattern.pattern_3(grid)
    Wgrid = pattern.update(grid)
    last_move = time.time()
    draw(grid)
    pygame.display.flip()
    elapsed = time.time()-now
    if elapsed < cycle_time:
        time.sleep(cycle_time-elapsed)