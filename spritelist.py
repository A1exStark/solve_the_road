import pyganim
import pygame

pygame.init()

WIDTH, HEIGHT = 1024, 768
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.mouse.set_visible(False)


FONT = pygame.font.Font('fonts/font3.ttf', 32)

WHITE = (255, 255, 255)
RED = (255, 0, 0)

MAIN_MENU_SPRITE = pyganim.PygAnimation([
    ('main_menu1024/main_menu1024_000.jpg', 100),
    ('main_menu1024/main_menu1024_001.jpg', 100),
    ('main_menu1024/main_menu1024_002.jpg', 100),
    ('main_menu1024/main_menu1024_003.jpg', 100),
    ('main_menu1024/main_menu1024_004.jpg', 100),
    ('main_menu1024/main_menu1024_005.jpg', 100),
    ('main_menu1024/main_menu1024_006.jpg', 100),
    ('main_menu1024/main_menu1024_007.jpg', 100),
    ('main_menu1024/main_menu1024_008.jpg', 100),
    ('main_menu1024/main_menu1024_009.jpg', 100),
    ('main_menu1024/main_menu1024_010.jpg', 100),
    ('main_menu1024/main_menu1024_011.jpg', 100),
    ('main_menu1024/main_menu1024_012.jpg', 100),
    ('main_menu1024/main_menu1024_013.jpg', 100),
    ('main_menu1024/main_menu1024_014.jpg', 100),
    ('main_menu1024/main_menu1024_015.jpg', 100),
    ('main_menu1024/main_menu1024_016.jpg', 100),
    ('main_menu1024/main_menu1024_017.jpg', 100),
    ('main_menu1024/main_menu1024_018.jpg', 100),
    ('main_menu1024/main_menu1024_019.jpg', 100),
    ('main_menu1024/main_menu1024_020.jpg', 100),
    ('main_menu1024/main_menu1024_021.jpg', 100),
    ('main_menu1024/main_menu1024_022.jpg', 100),
    ('main_menu1024/main_menu1024_023.jpg', 100),
    ('main_menu1024/main_menu1024_024.jpg', 100),
    ('main_menu1024/main_menu1024_025.jpg', 100),
    ('main_menu1024/main_menu1024_026.jpg', 100),
    ('main_menu1024/main_menu1024_027.jpg', 100),
    ('main_menu1024/main_menu1024_028.jpg', 100),
    ('main_menu1024/main_menu1024_029.jpg', 100),
    ('main_menu1024/main_menu1024_030.jpg', 100),
    ('main_menu1024/main_menu1024_031.jpg', 100),
    ('main_menu1024/main_menu1024_032.jpg', 100),
    ('main_menu1024/main_menu1024_033.jpg', 100),
    ('main_menu1024/main_menu1024_034.jpg', 100),
    ('main_menu1024/main_menu1024_035.jpg', 100),
    ('main_menu1024/main_menu1024_036.jpg', 100),
    ('main_menu1024/main_menu1024_037.jpg', 100),
    ('main_menu1024/main_menu1024_038.jpg', 100),
    ('main_menu1024/main_menu1024_039.jpg', 100),
    ('main_menu1024/main_menu1024_040.jpg', 100),
    ('main_menu1024/main_menu1024_041.jpg', 100),
    ('main_menu1024/main_menu1024_042.jpg', 100),
    ('main_menu1024/main_menu1024_043.jpg', 100),
    ('main_menu1024/main_menu1024_044.jpg', 100),
    ('main_menu1024/main_menu1024_045.jpg', 100)
])

MAIN_MENU_BACK = pygame.image.load('img/main_menu.png').convert_alpha()
POS_BACK = MAIN_MENU_BACK.get_rect(center=(WIDTH//2, HEIGHT//10*5))
MAIN_MENU_BACK.set_alpha(100)

RECT_X_1 = 250
RECT_X_2 = 320
RECT_X_3 = 280

RECT_Y = 90



#LVL1
BG = pygame.image.load('img/lvl1/bg.jpg')
POS_BG = BG.get_rect(center=(WIDTH//2, HEIGHT//2))

MOUNTAINS = pygame.image.load('img/lvl1/mountains.png').convert_alpha()
POS_MOUNTAINS = MOUNTAINS.get_rect(center=(WIDTH//2, HEIGHT//2))
LEFT_FOREST = pygame.image.load('img/lvl1/left_forest.png').convert_alpha()
POS_LEFT_FOREST = LEFT_FOREST.get_rect(center=(WIDTH//2, HEIGHT//2))
RIGHT_FOREST = pygame.image.load('img/lvl1/right_forest.png').convert_alpha()
POS_RIGHT_FOREST = RIGHT_FOREST.get_rect(center=(WIDTH//2, HEIGHT//2))
ROAD = pygame.image.load('img/lvl1/road.png').convert_alpha()
POS_ROAD = ROAD.get_rect(center=(WIDTH//2, HEIGHT//2))
