import pygame, sys, time, random
from pygame.constants import K_SPACE, K_ESCAPE, K_w, K_a, K_s, K_d
from sprites import Ball
pygame.init()


cycle_time = 0.017

screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
size = width, height = pygame.display.get_window_size()




##SETTINGS--------
num_balls = 1
ball_size = 20

##SETUP----------
balls = []
for i in range(num_balls):
    balls.append(Ball(random.randint(50, width), random.randint(50, height), ball_size, (random.randint(50, 200),random.randint(50, 200),random.randint(50, 200))))

screen.fill((255, 255, 255))

while 1:
    now = time.time()
    
    keys=pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        quit()
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    
    mouse_x, mouse_y = pygame.mouse.get_pos()

    if keys[K_SPACE]:
        screen.fill((255, 255, 255))


    for i in range(len(balls)):
        if i == 0:
            balls[i].move(width, height, mouse_x, mouse_y)
        else:
            balls[i].move(width, height, balls[i-1].x, balls[i-1].y)
    
    for ball in balls: ball.draw(screen)
    
    pygame.display.flip()
    elapsed = time.time()-now
    if elapsed < cycle_time:
        time.sleep(cycle_time-elapsed)