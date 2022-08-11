
import pygame
pygame.init()
size = width, height =  800, 800


class Button:
    def __init__(self, x, y, button_width, button_height, border_color, border_size, color, text, text_color, text_font):
        self.x, self.y, self.width, self.height = x, y, button_width, button_height
        self.color, self.text, self.text_color, self.font = color, text, text_color, text_font
        self.border_color, self.border_size = border_color, border_size
    def pressed(self, mouse_pos):
        if mouse_pos == None: return False
        mouse_click_x, mouse_click_y = mouse_pos[0], mouse_pos[1]
        if mouse_click_x <= self.x + self.width/2 and mouse_click_x >= self.x - self.width/2 and mouse_click_y <= self.y + self.height/2 and mouse_click_y >= self.y - self.height/2:
            return True
        return False
    def draw(self, screen):
        button_text = self.font.render(self.text, 1, self.text_color)
        pygame.draw.rect(screen,self.border_color, pygame.Rect(self.x-self.width/2, self.y-self.height/2, self.width, self.height))
        pygame.draw.rect(screen,self.color, pygame.Rect(self.x-self.width/2 +self.border_size/2, self.y-self.height/2 +self.border_size/2, self.width-self.border_size, self.height-self.border_size))
        screen.blit(button_text, (self.x-(self.width*(3/8)), self.y-self.height/4))
        