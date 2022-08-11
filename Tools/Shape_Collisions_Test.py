from cmath import pi
import pygame, sys, time, math
import Shape_Collisions as collisions
from pygame.constants import K_SPACE, K_ESCAPE, K_w, K_a, K_s, K_d
pygame.init()

size = width, height =  800, 800
cycle_time = 0.025

screen = pygame.display.set_mode(size)

class Shape:
    def __init__(self, x, y, xv, yv, size, shape):
        self.x, self.y, self.xv, self.yv = x, y, xv, yv
        self.size, self.shape = size, shape
    
    def move(self):
        newx, newy = self.x+self.xv, self.y+self.yv
        if newx > self.size/2 and newx < width-self.size/2:
            if newy > self.size/2 and newy < height-self.size/2:
                self.x, self.y = newx, newy
            else:
                self.yv *=-1
                self.move()
        else: 
            self.xv *=-1
            self.move()

    def draw(self):
        if self.shape == "circle":
            pygame.draw.ellipse(screen, (255, 0, 0), pygame.Rect(self.x-self.size/2, self.y-self.size/2, self.size, self.size))
        elif self.shape == "rect":
            pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(self.x-self.size/2, self.y-self.size/2, self.size, self.size))

class Triangle:
    def __init__(self, x, y, xv, yv, size):
        self.x, self.y, self.xv, self.yv = x, y, xv, yv
        self.size = size
        self.radius = size/2
        self.angle = pi/2
        self.shape = "triangle"
        self.color = (255, 0, 0)
    
    def move(self):
        newx, newy = self.x+self.xv, self.y+self.yv
        if newx > self.size/2 and newx < width-self.size/2:
            if newy > self.size/2 and newy < height-self.size/2:
                self.x, self.y = newx, newy
            else:
                self.yv *=-1
                self.move()
        else: 
            self.xv *=-1
            self.move()
    
    def draw(self):
        self.point1, self.point2, self.point3 = (self.x+self.radius*math.cos(self.angle), self.y-self.radius*math.sin(self.angle)), (self.x+self.radius*math.cos(self.angle-(2*pi/3)), self.y-self.radius*math.sin(self.angle-(2*pi/3))), (self.x+self.radius*math.cos(self.angle+(2*pi/3)), self.y-self.radius*math.sin(self.angle+(2*pi/3)))
        pygame.draw.polygon(screen, self.color, [self.point1, self.point2, self.point3], 10)




shape1 = Shape(600, 600, 1, 1, 200, "circle")
shape2 = Triangle(200, 200, -1, -1, 200)
#shape2 = Shape(700, 700, 3, -2, 200, "rect")





color = (160, 160, 160)
while 1:
    now = time.time()
    screen.fill(color)
    keys=pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        quit()
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    
    shape1.move()
    shape1.draw()

    shape2.move()
    shape2.draw()

    if collisions.collision(shape1, shape2, shape1.shape, shape2.shape)== True: color = (0, 0, 0)
    else: color = (160, 160, 160)
    
    pygame.display.flip()
    elapsed = time.time()-now
    if elapsed < cycle_time:
        time.sleep(cycle_time-elapsed)