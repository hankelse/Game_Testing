import pygame, sys, time, random
from pygame.constants import K_SPACE, K_ESCAPE, K_w, K_a, K_s, K_d
pygame.init()

size = width, height =  800, 800
cycle_time = 0

screen = pygame.display.set_mode(size)

grid_width, grid_height = int( width/4 ), int( height/4 )
cell_size = width/grid_width

#settings

num_infected = 4 #number of blocks around an infected a block that may get infected
infection_range = 1 #the distance the infection can spread to: 1 = 3x3, 2 = 5x5...


colors = {
    0 : (240, 255, 240),
    1 : (100, 115, 100)
}

def switch(num):
    if num == 0:
        return (1)
    elif num == 1:
        return (0)

def infect(num):
    return(1)

def get_infection_options(infection_range, row, item):
    options = []
    for i in range(-1*infection_range, infection_range+1):
        for n in range(-1*infection_range, infection_range+1):
            options.append([i + item, n + row])
    options.remove([item, row])

    final_options = []

    for option in options: 
        if option[0] >= 0 and option[1] >= 0 and option[0] < grid_width and option[1] < grid_height: final_options.append(option)
    return final_options

def create_grid():
    grid = []
    for i in range(grid_height):
        row = []
        for n in range(grid_width):
            row.append(0)
        grid.append(row)
    return grid

#pattern 2
# class Cell:
#         def __init__(self, status):
#             self.status = 0
#             self.neighbors = 0
# def create_grid():
#     grid = []
#     for i in range(grid_height):
#         row = []
#         for n in range(grid_width):
#             row.append(Cell(0))
#         grid.append(row)
#     return grid



def pattern_1(old_grid):
    grid = old_grid
    for row in range(len(grid)):
        for item in range(len(grid[row])):
            if grid[row][item] == 1:
                options = get_infection_options(infection_range)
                for i in range(num_infected):
                    if len(options) == 0: break
                    choice = random.choice(options)
                    options.remove(choice)
                    while row + choice[0] < 0 or row + choice[0] >= grid_height or item + choice[1] < 0 or item + choice[1] >= grid_width:
                        if len(options) == 0: break
                        choice = random.choice(options)
                        options.remove(choice)
                    else:
                        #print(row + choice[0],item + choice[1] )
                        grid[row + choice[0]][item + choice[1]] = switch( grid[row + choice[0]][item + choice[1]])
    return old_grid

def pattern_2(old_grid):

    grid = old_grid.copy()
    for row in range(len(grid)):
        for item in range(len(grid[row])):
            if grid[row][item] == 1:
                options = get_infection_options(infection_range, row, item)
                for i in range(num_infected):
                    if len(options) == 0: break
                    choice = random.choice(options)
                    options.remove(choice)
                    grid[choice[0]][choice[1]] = infect( grid[choice[0]][choice[1]])
    return grid

def pattern_3(old_grid):
    grid = old_grid.copy()
    for row in range(len(grid)):
        for item in range(len(grid[row])):
            options = get_infection_options(infection_range, row, item)
            count = 0
            for option in options:
                if grid[option[0]][option[1]] == 1:
                    count+= 1
            
            if count == 0 and random.randint(0, 400)==2: grid[row][item] = 1
            elif count >= 1 and count <=4: grid[row][item] = 1
            elif count > 4: grid[row][item] = 0
    return grid

def pattern_3(old_grid):
    grid = old_grid.copy()
    for row in range(len(grid)):
        for item in range(len(grid[row])):
            options = get_infection_options(infection_range, row, item)
            count = 0
            for option in options:
                if grid[option[0]][option[1]] == 1:
                    count+= 1
            
            if count == 0 and random.randint(0, 400)==2: grid[row][item] = 1
            elif count >= 1 and count <=2: grid[row][item] = 1
            elif count > 2: grid[row][item] = 0
    return grid




def draw(grid):
    for row in range(len(grid)):
        for item in range(len(grid[row])):
            pygame.draw.rect(screen, colors[grid[row][item]], pygame.Rect(item*cell_size, row*cell_size, cell_size, cell_size))






def main():
    grid = create_grid()
    grid[int( grid_width/2 )][int( grid_height/2 )] = 1


    grid = pattern_3(grid)
    draw(grid)
    while 1:
        now = time.time()
        #screen.fill((160, 160, 160))
        keys=pygame.key.get_pressed()
        if keys[K_ESCAPE]:
            quit()
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
        if keys[K_SPACE]:
            grid = pattern_3(grid)
            draw(grid)


        
        pygame.display.flip()
        elapsed = time.time()-now
        if elapsed < cycle_time:
            time.sleep(cycle_time-elapsed)

main()