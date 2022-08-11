import pygame, sys, time
from pygame.constants import K_SPACE, K_ESCAPE, K_w, K_a, K_s, K_d, K_RETURN, K_q, K_e
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
        self.width, self.height = 100, 25

        self.colors = [
            (100, 100, 100),
            (100, 100, 140)
        ]


        # delay = 0.3
        # last_action = 0
        
    def is_clicked(self, x, y):
        if abs(self.x - x) <= self.width and abs(self.y-y) <= self.height: return True
        return False

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



walls = []
selected = None
delay = 0.15
last_action = 0
while 1:
    now = time.time()
    screen.fill((160, 160, 160))
    keys=pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        quit()
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.MOUSEBUTTONUP:
            click_x, click_y = pygame.mouse.get_pos()
            if selected == None:
                for wall in walls: 
                    if wall.is_clicked(click_x, click_y)== True: 
                        selected = wall
                        break
                if selected == None:
                    walls.append(Wall(click_x, click_y))
            else:
                selected.x, selected.y = click_x, click_y
                selected = None
    
    if selected != None and time.time()-last_action >= delay:
        if keys[K_q]: 
            selected.rotation -= 90
            last_action = time.time()
        elif keys[K_e]: 
            selected.rotation += 90
            last_action = time.time()


            
    for wall in walls: wall.draw(screen)

    if selected != None: selected.draw(screen, True)

    
    pygame.display.flip()
    elapsed = time.time()-now
    if elapsed < cycle_time:
        time.sleep(cycle_time-elapsed)