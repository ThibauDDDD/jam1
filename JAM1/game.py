#!/usr/bin/env python3
import pygame

pygame.init()

clock = pygame.time.Clock()
fps = 60

#game wind
bottom_panel = 200
screen_width = 1200
screen_height = 604 + bottom_panel

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Battle')

# DOWNLOAD image
background_image = pygame.image.load('ressource/image/water_background.png').convert_alpha()
panel_image = pygame.image.load('ressource/image/panel.png').convert_alpha()


#define font here
font = pygame.font.SysFont('ressource/image/ARIAL.TTF', 26)
font_comicate = pygame.font.SysFont('ressource/image/COMICATE.TTF', 50)

#define color here
blue = (0, 128, 255)
red = (255, 0, 0)
white = (255, 255, 255)

def draw_background():
    screen.blit(background_image, (0, 0))

def draw_panel():
    screen.blit(panel_image, (0, screen_height - bottom_panel))
    draw_text(f'{knight.image_name}', font, blue, 100, screen_height - bottom_panel + 10)
    draw_text(f'Zorotl', font, blue, 850, screen_height - bottom_panel + 10)

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col) 
    screen.blit(img, (x, y))


#class ici:
class Fighter():
    def __init__(self, x, y, folder, image_name, max_hp, strength, potions):
        self.folder = folder
        self.image_name = image_name
        self.max_hp = max_hp
        self.hp = max_hp
        self.strength = strength
        self.start_potions = potions
        self.potions = potions
        self.alive = True
        self.image = pygame.image.load(f'ressource/image/{self.folder}/{image_name}.png')
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
    
    def draw(self):
        screen.blit(self.image, self.rect)

    def draw_finish(self):
        draw_text(f'Blue has 0 HP, he is dead, you loose !', font_comicate, white, 250, 350 + 10)
        
    def draw_finish_zorotl(self):
        draw_text(f'Zorotl has 0 HP, he is dead, you win !', font_comicate, white, 250, 350 + 10)


class HealthBar():
    def __init__(self, x, y, hp, max_hp):
        self.x = x
        self.y = y
        self.hp = hp
        self.max_hp = max_hp

    def draw(self, hp):
        self.hp = hp
        ratio = self.hp / self.max_hp
        pygame.draw.rect(screen, red, (self.x, self.y, 150, 20))
        pygame.draw.rect(screen, blue, (self.x, self.y, 150 * ratio, 20))

color_light = (170,170,170) 
color_dark = (000,000,100) 
width = screen.get_width()
height = screen.get_height() 
smallfont = pygame.font.SysFont('Corbel',35)   
text = smallfont.render('Attack' , True , (255,255,255)) 



knight = Fighter(200, 350, 'Knight', 'blue', 150, 10, 3)
zorotl = Fighter(1000, 350, 'Zorotl', 'zorotl_alone', 50, 5, 1)
zorotl_nine = Fighter(1000, 350, 'Zorotl', 'zorotl_9', 300, 5, 1)
zorotl_thirtyfive = Fighter(1000, 350, 'Zorotl', 'zorotl_35', 1000, 5, 1)
zorotl_thousand = Fighter(1000, 350, 'Zorotl', 'zorotl_1000', 5000, 5, 1)

#healthbar pour les personnages150
blue_healtbar = HealthBar(100, screen_height - bottom_panel + 40, knight.hp, knight.max_hp)
zorotl_alone_healtbar = HealthBar(850, screen_height - bottom_panel + 40, zorotl.hp, zorotl.max_hp)
zorotl_nine_healtbar = HealthBar(850, screen_height - bottom_panel + 40, zorotl_nine.hp, zorotl_nine.max_hp)
zorotl_thirtyfive_healtbar = HealthBar(850, screen_height - bottom_panel + 40, zorotl_thirtyfive.hp, zorotl_thirtyfive.max_hp)
zorotl_thousand_healtbar = HealthBar(850, screen_height - bottom_panel + 40, zorotl_thousand.hp, zorotl_thousand.max_hp)
    
music = pygame.mixer.music.load("ressource/musique_ilbre_de_droit.mp3")
pygame.mixer.music.play()
run = True
while run:

    clock.tick(fps)
    #draw
    draw_background()
    draw_panel()
    blue_healtbar.draw(knight.hp)
    zorotl_alone_healtbar.draw(zorotl.hp)

    if knight.hp > 0:
        knight.draw()
    else:
        knight.draw_finish()
    
    mouse = pygame.mouse.get_pos() 

    if zorotl.hp > 0:
        zorotl.draw()
        mechant = 1
    elif zorotl_nine.hp > 0:
        zorotl_nine.draw()
        mechant = 2
    elif zorotl_thirtyfive.hp > 0:
        zorotl_thirtyfive.draw()
        mechant = 3
    elif zorotl_thousand.hp > 0:
        zorotl_thousand.draw()
        mechant = 4
    else:
        knight.hp = 150
        knight.draw_finish_zorotl()

    if mechant == 1:
        zorotl_alone_healtbar.draw(zorotl.hp)
        blue_healtbar.draw(knight.hp)
    elif mechant == 2:
        zorotl_nine_healtbar.draw(zorotl_nine.hp)
        blue_healtbar.draw(knight.hp)
    elif mechant == 3:
        zorotl_thirtyfive_healtbar.draw(zorotl_thirtyfive.hp)
        blue_healtbar.draw(knight.hp)
    elif mechant == 4:
        zorotl_thousand_healtbar.draw(zorotl_thousand.hp)
        blue_healtbar.draw(knight.hp)

    if pygame.time.get_ticks() % 100 <= 10:
        knight.hp -= 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN: 
            if width/2-100 <= mouse[0] <= width/2+40 and height/2+250 <= mouse[1] <= height/2+290: 
                if mechant == 1:
                    zorotl.hp -= 20
                if mechant == 2:
                    zorotl_nine.hp -= 20
                if mechant == 3:
                    zorotl_thirtyfive.hp -= 20
                if mechant == 4:
                    zorotl_thousand.hp -= 20
                knight.hp += 1
    
    pygame.draw.rect(screen,color_dark,[width/2-100,height/2+250,140,40])
    screen.blit(text , (width/2-100,height/2+250))

    pygame.display.update()

    
        
pygame.quit()

