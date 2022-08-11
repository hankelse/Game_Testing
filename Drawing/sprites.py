import pygame, math, random


def sigmoid(x):
    return (1/(1+math.exp(-x)))


class Ball:
    def __init__(self, x, y, size, color):
        self.x, self.y = x, y
        self.size = size

        self.xv, self.yv = 0, 0
        self.max_xv, self.min_xv = 10, -10
        self.max_yv, self.min_yv= 10, -10

        self.acceleration = 0.5
        self.deceleration = 0.125

        self.color = color
    

    def decelerate(self, vel):
        if vel > self.deceleration: vel -= self.deceleration
        elif vel < -self.deceleration: vel += self.deceleration
        else: vel = 0


    def move(self, desired_x=None, desired_y=None):
        d_x, d_y = desired_x, desired_y
        print(d_x, d_y)
        if d_x != None or d_y != None: 
            
            if d_x < self.x and self.xv-self.acceleration > self.min_xv: 
                self.xv -= self.acceleration

            elif d_x > self.x and self.xv+self.acceleration < self.max_xv: 
                self.xv += self.acceleration
            
            else:
                self.decelerate(self.xv)

            if d_y < self.y and self.yv-self.acceleration > self.min_yv: 
                self.yv -= self.acceleration

            elif d_y > self.y and self.yv+self.acceleration < self.max_yv: 
                self.yv += self.acceleration
            
            else:
                self.decelerate(self.yv)


        else:
            self.decelerate(self.xv)
            self.decelerate(self.yv)
        
        self.x += self.xv
        self.y += self.yv
    
    def draw(self, screen):
        pygame.draw.ellipse(screen, self.color, pygame.Rect(self.x-self.size/2, self.y-self.size/2, self.size, self.size))



