#!/usr/bin/env python3
import pygame, sys

pygame.init()

pygame.display.set_caption("Menu")
screen = pygame.display.set_mode((1200, 700))

background = pygame.image.load('ressource/image/start_game.png')

class Button():
    def __init__(self, image, pos, text_input, font, base_color, hovering_color):
        self.image = image
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.font = font
        self.base_color, self.hovering_color = base_color, hovering_color
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, self.base_color)
        if self.image is None:
            self.image = self.text
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def update(self, screen):
            if self.image is not None:
                screen.blit(self.image, self.rect)
            screen.blit(self.text, self.text_rect)

    def checkForInput(self, position):
            if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                return True
            return False
        
    def changeColor(self, position):
            if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                self.text = self.font.render(self.text_input, True, self.hovering_color)
            else:
                self.text = self.font.render(self.text_input, True, self.base_color)

def play():

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
        def __init__(self, x, y, folder, image_name, max_hp, strength):
            self.folder = folder
            self.image_name = image_name
            self.max_hp = max_hp
            self.hp = max_hp
            self.strength = strength
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

    width = screen.get_width()
    height = screen.get_height() 
    smallfont = pygame.font.SysFont('Corbel',35)   
    text = smallfont.render('Attack' , True , (255,255,255)) 



    knight = Fighter(200, 350, 'Knight', 'blue', 150, 10)
    zorotl = Fighter(1000, 350, 'Zorotl', 'zorotl_alone', 50, 5)
    zorotl_nine = Fighter(1000, 350, 'Zorotl', 'zorotl_9', 300, 5)
    zorotl_thirtyfive = Fighter(1000, 350, 'Zorotl', 'zorotl_35', 1000, 5)
    zorotl_thousand = Fighter(1000, 350, 'Zorotl', 'zorotl_1000', 5000, 5)

    #healthbar pour les personnages150
    blue_healtbar = HealthBar(100, screen_height - bottom_panel + 40, knight.hp, knight.max_hp)
    zorotl_alone_healtbar = HealthBar(850, screen_height - bottom_panel + 40, zorotl.hp, zorotl.max_hp)
    zorotl_nine_healtbar = HealthBar(850, screen_height - bottom_panel + 40, zorotl_nine.hp, zorotl_nine.max_hp)
    zorotl_thirtyfive_healtbar = HealthBar(850, screen_height - bottom_panel + 40, zorotl_thirtyfive.hp, zorotl_thirtyfive.max_hp)
    zorotl_thousand_healtbar = HealthBar(850, screen_height - bottom_panel + 40, zorotl_thousand.hp, zorotl_thousand.max_hp)

    #play music    
    pygame.mixer.music.load("ressource/musique_ilbre_de_droit.mp3")
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
                pygame.quit()
                sys.exit()
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
        
        pygame.draw.rect(screen, (000,000,100),[width/2-100,height/2+250,140,40])
        screen.blit(text , (width/2-70,height/2+258))

        pygame.display.update()

        
            
    pygame.quit()


def main_menu():
    pygame.display.set_caption("Menu")

    while True:
        screen.blit(background, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = pygame.font.SysFont('ressource/image/ARIAL.TTF', 26).render("MAIN MENU", True, "#b68f40")
        MENU_RECT =  MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("ressource/image/start_bouton.png"), pos=(640, 400), text_input="", font=pygame.font.SysFont('ressource/image/ARIAL.TTF', 75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("ressource/image/exit_bouton.png"), pos=(640, 550), text_input="", font=pygame.font.SysFont('ressource/image/ARIAL.TTF', 75), base_color="#d7fcd4", hovering_color="White")

        screen.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
        
        pygame.display.update()

main_menu()