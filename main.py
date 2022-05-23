import pygame
from pygame.locals import *
from spritelist_menu import *
from osts import *
import lvl1


pygame.display.set_caption('Solve The Road')

MAIN_MENU_START = FONT.render('START', 0, WHITE)
MAIN_MENU_OPTIONS = FONT.render('УРОВЕНЬ', 0, WHITE)
MAIN_MENU_EXIT = FONT.render('ВЫХОД', 0, WHITE)

POS_START = MAIN_MENU_START.get_rect(center=(WIDTH//2, HEIGHT//10*4))
POS_OPTIONS = MAIN_MENU_OPTIONS.get_rect(center=(WIDTH//2, HEIGHT//10*5))
POS_EXIT = MAIN_MENU_EXIT.get_rect(center=(WIDTH//2, HEIGHT//10*6))



def lvl1():
    print('lvl1')

def draw_menu():
    
    MAIN_MENU_SPRITE.play()
    MAIN_MENU_SPRITE.blit(WIN, (0, (HEIGHT-582)/2))
    WIN.blit(MAIN_MENU_BACK, POS_BACK)
    WIN.blit(MAIN_MENU_START, POS_START)
    WIN.blit(MAIN_MENU_OPTIONS, POS_OPTIONS)
    WIN.blit(MAIN_MENU_EXIT, POS_EXIT)



def main():
    run = True
    counter = 0
    while run:
        
        draw_menu()

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE) or (counter == 2 and event.type == KEYDOWN and event.key == K_RETURN):
                run = False
            if event.type == KEYDOWN and event.key == K_DOWN:
                MAIN_MENU_SELECT_SONUD.play()
                counter += 1
            if event.type == KEYDOWN and event.key == K_UP:
                MAIN_MENU_SELECT_SONUD.play()
                counter -= 1
            if counter == 0 and event.type == KEYDOWN and event.key == K_RETURN:
                lvl1()

        if counter == 0:
            pygame.draw.rect(WIN, WHITE, (WIDTH//2-RECT_X_1//2, HEIGHT//10*4-RECT_Y//2, RECT_X_1, RECT_Y), 7)
        elif counter == 1:
            pygame.draw.rect(WIN, WHITE, (WIDTH//2-RECT_X_2//2, HEIGHT//2-RECT_Y//2, RECT_X_2, RECT_Y), 7)
        elif counter == 2:
            pygame.draw.rect(WIN, WHITE, (WIDTH//2-RECT_X_3//2, HEIGHT//10*6-RECT_Y//2, RECT_X_3, RECT_Y), 7)
        elif counter > 2:
            counter = 0
        elif counter < 0:
            counter = 2

        pygame.display.update()

    
    
if __name__ == "__main__":
    main()
