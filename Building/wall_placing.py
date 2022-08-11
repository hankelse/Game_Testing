import pygame, sys, time
from pygame.constants import K_SPACE, K_ESCAPE, K_w, K_a, K_s, K_d
pygame.init()

size = width, height =  800, 800
# size = width, height = pygame.display.get_window_size()
cycle_time = 0.025

screen = pygame.display.set_mode(size)
# screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)

class Wall:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.rotation = 0
        self.width, self.height = 80, 40

        self.colors = [
            (100, 100, 100),
            (100, 100, 140)
        ]


        # delay = 0.3
        # last_action = 0
        
    def is_clicked(self, x, y):
        if abs(self.x - x) <= self.width and abs(self.y-y) <= self.height: return True
        return False

    def snap_to_grid(self):
        remainderx, remaindery = (self.x-self.width/2) %40, (self.y-self.height/2)%40
        print(remaindery)

        if remainderx <= 20: self.x -= remainderx
        else: self.x += (40-remainderx)

        if remaindery <= 20: self.y -= remaindery
        else: self.y += (40-remaindery)

    def draw(self, screen, selected=None):
        self.rotation = self.rotation % 360
        if self.rotation < 0: 360+self.rotation 

        if selected == None: self.color = self.colors[0]
        elif selected == True: self.color = self.colors[1]

        if self.rotation == 0 or self.rotation == 180: width, height = self.width, self.height
        elif self.rotation == 90 or self.rotation == 270: width, height = self.height, self.width
        else:
            print("unknown:", self.rotation)
        pygame.draw.rect(screen, self.color, pygame.Rect(self.x-width/2, self.y-height/2, width, height))


wall = Wall(400, 400)
selected = None

while 1:
    now = time.time()
    screen.fill((160, 160, 160))

    for i in range(0, 800, 40):
        pygame.draw.line(screen, (0, 0, 0), (0, i), (800, i))
        pygame.draw.line(screen, (0, 0, 0), (i, 0), (i, 800))


    keys=pygame.key.get_pressed()
    mouse_pos = mouse_x, mouse_y = pygame.mouse.get_pos()
    if keys[K_ESCAPE]:
        quit()
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and wall.is_clicked(mouse_x, mouse_y) == True:
            if selected == None:
                selected = wall
            else: 
                selected.snap_to_grid()
                selected = None

        elif event.type == pygame.MOUSEBUTTONUP and selected != None:pass
            #selected = None
    
    if selected != None: selected.x, selected.y = mouse_x, mouse_y
    

    wall.draw(screen)
    if selected != None: selected.draw(screen, True)

    
    pygame.display.flip()
    elapsed = time.time()-now
    if elapsed < cycle_time:
        time.sleep(cycle_time-elapsed)