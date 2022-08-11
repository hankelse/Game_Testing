import pygame, sys, time, pyautogui, math
from PIL import Image
from pygame.constants import K_SPACE, K_ESCAPE, K_w, K_a, K_s, K_d
pygame.init()

size = width, height =  800, 800
# size = width, height = pygame.display.get_window_size()
cycle_time = 0.025

screen = pygame.display.set_mode(size)
# screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)


image_link = "Animation/testing_pallet.xcf"
image = pygame.image.load(image_link)

image= Image.open('Animation/testing_pallet.png')
width, height = image.size

pixels_raw = image.load()
pixels = []

for w in range(width):
    pixels.append([])
    for h in range(height):
        pixels[w].append(pixels_raw[w,h])

# pixels=[
#     [(100, 0, 0), (150, 50, 0), (200, 100, 0), (250, 150, 50)],
#     [(0, 100, 0), (50, 150, 0), (100, 200, 0), (150, 250, 50)],
#     [(0, 0, 100), (0, 50, 100), (0, 100, 200), (50, 150, 250)],
#     [(0, 100, 125), (0, 20, 0), (255, 200, 73), (0, 255, 0)],
#     [(100, 0, 0), (150, 50, 0), (200, 100, 0), (250, 150, 50)],
#     [(0, 100, 0), (50, 150, 0), (100, 200, 0), (150, 250, 50)],
#     [(0, 0, 100), (0, 50, 100), (0, 100, 200), (50, 150, 250)],
#     [(0, 100, 125), (0, 20, 0), (255, 200, 73), (0, 255, 0)],
#     ]
# pixels=[
#     [(100, 0, 0), (150, 50, 0)],
#     [(0, 100, 0), (50, 150, 0)]
#     ]
centerx, centery = 2, 2
pixel_size= 100


        

angle = 0
x, y = 400, 400

while 1:
    angle += 10
    now = time.time()
    screen.fill((160, 160, 160))
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(370, 370, 60, 60))
    keys=pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        quit()
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    
    for row in range(len(pixels)):
        for p in range(len(pixels[row])):
            xdis, ydis = (int(p-len(pixels[row])/2)+1/2)*pixel_size, (int(row-len(pixels)/2)+1/2)*pixel_size
            distance = math.sqrt(xdis**2 + ydis**2)

            angle_adjustment = math.degrees(math.atan(ydis/xdis))
            if xdis <0: angle_adjustment += 180
            angle_adjustment = angle_adjustment %360
            if angle_adjustment <0: angle_adjustment = 360 + angle_adjustment
            #angle_adjustment = str(angle_adjustment)
            #distance = str(distance)

            pixel_color = pixels[row][p]
            #pixel_size = str(pixel_size)


            #print("pygame.draw.ellipse(screen, "+pixel_color+", pygame.Rect(math.cos(angle+"+angle_adjustment+")*"+distance+",math.sin(angle+"+angle_adjustment+")*"+distance+", "+pixel_size+", "+pixel_size)

            #angle = 0
            pygame.draw.ellipse(screen, pixel_color, pygame.Rect(x + math.cos(math.radians(angle+angle_adjustment))*distance- (pixel_size*len(pixels[row]))/(len(pixels[row])*2), y + math.sin(math.radians(angle+angle_adjustment))*distance - (pixel_size*len(pixels))/(len(pixels)*2), pixel_size, pixel_size))
            pixel_color, angle_adjustment, distance = str(pixel_color), str(angle_adjustment), str(distance)
            print( "pygame.draw.ellipse(screen, "+pixel_color+", pygame.Rect(x + math.cos(math.radians(angle+"+angle_adjustment+"))*"+distance+"- (pixel_size*"+str(len(pixels[row])/(len(pixels[row])*2))+", y + math.sin(math.radians(angle+"+angle_adjustment+"))*"+distance+" - (pixel_size*"+str(len(pixels)/(len(pixels)*2))+", pixel_size, pixel_size))")

    quit()
    pygame.display.flip()
    elapsed = time.time()-now
    if elapsed < cycle_time:
        time.sleep(cycle_time-elapsed)