import pygame, sys, time, pyautogui, math
from pygame.constants import K_SPACE, K_ESCAPE, K_w, K_a, K_s, K_d, K_UP, K_DOWN, K_LEFT, K_RIGHT, K_LSHIFT, K_RSHIFT
pygame.init()

width, height =  pyautogui.size()
width, height = width*9/10, height*9/10
size = width, height

cycle_time = 0.025

screen = pygame.display.set_mode(size)

#-------SETTINGS------#
bindings = {
    "shoot": [K_SPACE, K_SPACE],
    "up" : [K_w, K_UP],
    "down": [K_s, K_DOWN],
    "left": [K_a, K_LEFT],
    "right": [K_d, K_RIGHT],
    "switch_movement": [K_LSHIFT, K_RSHIFT]
}

#---PLAYER SETTINGS---#

player_acceleration = 1
player_deceleration = 0.5
player_rotate_speed = 0.2
player_rotate_acceleration = 0.001
player_boost_speed = 90

class Player:
    def __init__(self, x, y, acceleration, deceleration,rotate_speed, rotate_acceleration, boost_speed):
        self.x, self.y, self.rotate_speed, self.rotate_acceleration = x, y, rotate_speed, rotate_acceleration
        self.base_rotate_speed = self.rotate_speed
        self.boost_speed = boost_speed

        self.xv, self.yv = 0, 0
        self.acceleration = acceleration
        self.deceleration = deceleration
        self.vel_range = [-5, 5]
        self.angle = 0
        self.mode = "walking" #walking/spinning

        self.color = (0, 0, 0)
        self.size = 20

        self.pointer_length = self.size*2
        self.boost_xv = 0
        self.boost_yv = 0 

        self.last_change = 0
        self.change_delay = 2
    
    def move(self, bindings, map_size, keys):
        if time.time()-self.last_change > self.change_delay:
            if keys[bindings["switch_movement"][0]] or keys[bindings["switch_movement"][1]]:
                self.last_change = time.time()
                if self.mode == "walking": self.mode = "aiming"
                elif self.mode == "aiming": 
                    self.mode = "walking"
                    self.rotate_speed = self.base_rotate_speed

        if self.mode == "walking":
            self.get_vel_changes(bindings, keys)
            self.implement_velocities(map_size)
        
        elif self.mode == "aiming":

            if keys[bindings["shoot"][0]] or keys[bindings["shoot"][1]]:
                self.boost_xv, self.boost_yv = math.cos(self.angle)*self.boost_speed, math.sin(self.angle)*self.boost_speed
                self.mode = "walking"
            
            else:
                self.angle += self.rotate_speed
                self.rotate_speed += self.rotate_acceleration 


            
        
        # print("xv",self.xv, "yv", self.yv)
        # print("x",self.x, "y", self.y)


    def get_vel_changes(self, bindings, keys):
            if keys[bindings["up"][0]] or keys[bindings["up"][1]]:
                if self.yv - self.acceleration > self.vel_range[0]:
                    self.yv -= self.acceleration
                elif self.yv != self.vel_range[0]: self.yv = self.vel_range[0]
        
            elif keys[bindings["down"][0]] or keys[bindings["down"][1]]:
                    if self.yv + self.acceleration < self.vel_range[1]:
                        self.yv += self.acceleration
                    elif self.yv != self.vel_range[1]: self.yv = self.vel_range[1]
            
            #decelerate Y
            elif self.yv != 0: 
                if self.yv > 0: 
                    if self.yv >= self.deceleration: self.yv -= self.deceleration
                    else: self.yv = 0
                
                elif self.yv < 0: 
                    if self.yv <= self.deceleration: self.yv += self.deceleration
                    else: self.yv = 0
                
            if keys[bindings["left"][0]] or keys[bindings["left"][1]]:
                if self.xv - self.acceleration > self.vel_range[0]:
                    self.xv -= self.acceleration
                elif self.xv != self.vel_range[0]: self.xv = self.vel_range[0]
            
            elif keys[bindings["right"][0]] or keys[bindings["right"][1]]:
                if self.xv + self.acceleration < self.vel_range[1]:
                    self.xv += self.acceleration
                elif self.xv != self.vel_range[1]: self.xv = self.vel_range[1]
            
            #decelerate X
            elif self.xv != 0: 
                if self.xv > 0: 
                    if self.xv >= self.deceleration: self.xv -= self.deceleration
                    else: self.xv = 0
                
                elif self.xv < 0: 
                    if self.xv <= self.deceleration: self.xv += self.deceleration
                    else: self.xv = 0
            
            if self.boost_xv != 0: 
                if self.boost_xv > 0:
                    if self.boost_xv - self.deceleration*2 > 0: self.boost_xv -= self.deceleration*2
                    else: self.boost_xv = 0
                elif self.boost_xv < 0:
                    if self.boost_xv + self.deceleration*2 < 0: self.boost_xv += self.deceleration*2
                    else: self.boost_xv = 0
            
            if self.boost_yv != 0: 
                if self.boost_yv > 0:
                    if self.boost_yv - self.deceleration > 0: self.boost_yv -= self.deceleration
                    else: self.boost_yv = 0
                elif self.boost_yv < 0:
                    if self.boost_yv + self.deceleration < 0: self.boost_yv += self.deceleration
                    else: self.boost_yv = 0

    def implement_velocities(self, map_size):
        if self.xv + self.boost_xv > 0:
            if self.xv + self.x + self.boost_xv < map_size[0] - self.size/2: self.x += self.xv + self.boost_xv
        elif self.xv < 0:
            if self.xv + self.x + self.boost_xv > 0 + self.size/2: self.x += self.xv + self.boost_xv

        if self.yv + self.boost_yv > 0:
            if self.yv + self.y + self.boost_yv < map_size[1] - self.size/2: self.y += self.yv + self.boost_yv
        elif self.yv < 0:
            if self.yv + self.y + self.boost_yv> 0 + self.size/2: self.y += self.yv + self.boost_yv
    
    def draw(self, screen):

        if self.mode == "aiming":
            pygame.draw.line(screen, self.color, (self.x, self.y), (self.x + math.cos(self.angle)*self.pointer_length, self.y + math.sin(self.angle)*self.pointer_length), 10)

        pygame.draw.ellipse(screen, self.color, pygame.Rect(self.x-self.size/2, self.y-self.size/2, self.size, self.size))


player = Player(width/2, height/2, player_acceleration, player_deceleration, player_rotate_speed, player_rotate_acceleration, player_boost_speed)


while 1:
    now = time.time()
    screen.fill((160, 160, 160))
    keys=pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        quit()
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    
    player.move(bindings, size, keys)

    player.draw(screen)
    

    
    pygame.display.flip()
    elapsed = time.time()-now
    if elapsed < cycle_time:
        time.sleep(cycle_time-elapsed)