import pygame, sys, time
from pygame.constants import K_SPACE, K_ESCAPE, K_w, K_a, K_s, K_d
from button import Button
pygame.init()

size = width, height =  800, 800
cycle_time = 0.025

screen = pygame.display.set_mode(size)

font = pygame.font.SysFont("monospace", 50)

#x, y, button_width, button_height, border_color, border_size, color, text, text_color, text_font)
button = Button(400, 400, 200, 100, (0, 0, 0), 10, (255, 255, 255), "START", (0, 0, 0), font)

color = (255, 255, 255)
while 1:
    now = time.time()
    screen.fill(color)
    keys=pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        quit()
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_pos = pygame.mouse.get_pos()
            if button.pressed(mouse_pos) == True: 
                color = (0, 0, 0)
            else: color = (255, 255, 255)
    
    
    
    #pygame.draw.ellipse(screen, (0, 0, 0), pygame.Rect(390, 390, 20, 20))

    button.draw(screen)
    pygame.display.flip()
    elapsed = time.time()-now
    if elapsed < cycle_time:
        time.sleep(cycle_time-elapsed)