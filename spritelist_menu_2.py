import pyganim
import pygame

pygame.init()

WIDTH, HEIGHT = 1024, 768
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.mouse.set_visible(False)


FONT = pygame.font.Font('fonts/font3.ttf', 24)
FONT_SCORE = pygame.font.Font('fonts/font3.ttf', 16)
FONT_FPS = pygame.font.Font('fonts/font3.ttf', 10)

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

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
PAUSE_BACK = pygame.transform.scale(pygame.image.load('img/main_menu.png'), [330,340]).convert_alpha()
POS_PAUSE_BACK = PAUSE_BACK.get_rect(center=(WIDTH//2, HEIGHT//10*5))
PAUSE_BACK.set_alpha(100)

RECT_X_1 = 280
RECT_X_2 = 280
RECT_X_3 = 280
RECT_X_4 = 280

RECT_Y = 90



#UI


HEART = pygame.image.load('img/lvl1/heart.png').convert_alpha()
POS_HEART = HEART.get_rect()
POS_HEART.center = WIDTH//100*4, HEIGHT//100*5




speed = 8
acceleration = 1.0




