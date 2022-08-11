import pygame, sys, time, pyautogui,math
from pygame.constants import K_SPACE, K_ESCAPE, K_w, K_a, K_s, K_d
pygame.init()

size = width, height =  800, 800
# size = width, height = pygame.display.get_window_size()
cycle_time = 0.025

screen = pygame.display.set_mode(size)
# screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)

image = pygame.transform.scale(pygame.image.load("Animation/testing_pallet.xcf"), (320, 320))





x,y = 0,0
angle =0
pixel_size =
while 1:
    now = time.time()
    screen.fill((160, 160, 160))
    keys=pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        quit()
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    x +=1
    y+=1
    angle+=1
    pygame.draw.ellipse(screen, (255, 0, 0), pygame.Rect(x + math.cos(math.radians(angle+225.0))*212.13203435596427- (pixel_size*0.5, y + math.sin(math.radians(angle+225.0))*212.13203435596427 - (pixel_size*0.5, pixel_size, pixel_size))
    pygame.draw.ellipse(screen, (0, 29, 255), pygame.Rect(x + math.cos(math.radians(angle+251.56505117707798))*158.11388300841898- (pixel_size*0.5, y + math.sin(math.radians(angle+251.56505117707798))*158.11388300841898 - (pixel_size*0.5, pixel_size, pixel_size))
    pygame.draw.ellipse(screen, (106, 5, 248), pygame.Rect(x + math.cos(math.radians(angle+288.434948822922))*158.11388300841898- (pixel_size*0.5, y + math.sin(math.radians(angle+288.434948822922))*158.11388300841898 - (pixel_size*0.5, pixel_size, pixel_size))
    pygame.draw.ellipse(screen, (0, 255, 63), pygame.Rect(x + math.cos(math.radians(angle+315.0))*212.13203435596427- (pixel_size*0.5, y + math.sin(math.radians(angle+315.0))*212.13203435596427 - (pixel_size*0.5, pixel_size, pixel_size))
    pygame.draw.ellipse(screen, (255, 135, 0), pygame.Rect(x + math.cos(math.radians(angle+198.43494882292202))*158.11388300841898- (pixel_size*0.5, y + math.sin(math.radians(angle+198.43494882292202))*158.11388300841898 - (pixel_size*0.5, pixel_size, pixel_size))
    pygame.draw.ellipse(screen, (0, 110, 255), pygame.Rect(x + math.cos(math.radians(angle+225.0))*70.71067811865476- (pixel_size*0.5, y + math.sin(math.radians(angle+225.0))*70.71067811865476 - (pixel_size*0.5, pixel_size, pixel_size))
    pygame.draw.ellipse(screen, (234, 0, 255), pygame.Rect(x + math.cos(math.radians(angle+315.0))*70.71067811865476- (pixel_size*0.5, y + math.sin(math.radians(angle+315.0))*70.71067811865476 - (pixel_size*0.5, pixel_size, pixel_size))
    pygame.draw.ellipse(screen, (0, 255, 177), pygame.Rect(x + math.cos(math.radians(angle+341.565051177078))*158.11388300841898- (pixel_size*0.5, y + math.sin(math.radians(angle+341.565051177078))*158.11388300841898 - (pixel_size*0.5, pixel_size, pixel_size))
    pygame.draw.ellipse(screen, (254, 255, 0), pygame.Rect(x + math.cos(math.radians(angle+161.56505117707798))*158.11388300841898- (pixel_size*0.5, y + math.sin(math.radians(angle+161.56505117707798))*158.11388300841898 - (pixel_size*0.5, pixel_size, pixel_size))
    pygame.draw.ellipse(screen, (0, 218, 255), pygame.Rect(x + math.cos(math.radians(angle+135.0))*70.71067811865476- (pixel_size*0.5, y + math.sin(math.radians(angle+135.0))*70.71067811865476 - (pixel_size*0.5, pixel_size, pixel_size))
    pygame.draw.ellipse(screen, (255, 0, 202), pygame.Rect(x + math.cos(math.radians(angle+45.0))*70.71067811865476- (pixel_size*0.5, y + math.sin(math.radians(angle+45.0))*70.71067811865476 - (pixel_size*0.5, pixel_size, pixel_size))
    pygame.draw.ellipse(screen, (0, 252, 255), pygame.Rect(x + math.cos(math.radians(angle+18.43494882292201))*158.11388300841898- (pixel_size*0.5, y + math.sin(math.radians(angle+18.43494882292201))*158.11388300841898 - (pixel_size*0.5, pixel_size, pixel_size))
    pygame.draw.ellipse(screen, (0, 255, 9), pygame.Rect(x + math.cos(math.radians(angle+135.0))*212.13203435596427- (pixel_size*0.5, y + math.sin(math.radians(angle+135.0))*212.13203435596427 - (pixel_size*0.5, pixel_size, pixel_size))
    pygame.draw.ellipse(screen, (0, 255, 151), pygame.Rect(x + math.cos(math.radians(angle+108.43494882292201))*158.11388300841898- (pixel_size*0.5, y + math.sin(math.radians(angle+108.43494882292201))*158.11388300841898 - (pixel_size*0.5, pixel_size, pixel_size))
    pygame.draw.ellipse(screen, (255, 0, 108), pygame.Rect(x + math.cos(math.radians(angle+71.56505117707799))*158.11388300841898- (pixel_size*0.5, y + math.sin(math.radians(angle+71.56505117707799))*158.11388300841898 - (pixel_size*0.5, pixel_size, pixel_size))
    pygame.draw.ellipse(screen, (0, 124, 255), pygame.Rect(x + math.cos(math.radians(angle+45.0))*212.13203435596427- (pixel_size*0.5, y + math.sin(math.radians(angle+45.0))*212.13203435596427 - (pixel_size*0.5, pixel_size, pixel_size))
    
    pygame.display.flip()
    elapsed = time.time()-now
    if elapsed < cycle_time:
        time.sleep(cycle_time-elapsed)