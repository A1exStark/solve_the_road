import pyganim
import pygame

pygame.init()

WIDTH, HEIGHT = 1024, 768
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.mouse.set_visible(False)


FONT = pygame.font.Font('fonts/font3.ttf', 24)
FONT_SCORE = pygame.font.Font('fonts/font3.ttf', 16)

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
FOREST = pygame.image.load('img/lvl1/forest.png').convert_alpha()
POS_FOREST = FOREST.get_rect(center=(WIDTH//2, HEIGHT//2))

ROAD = pygame.image.load('img/lvl1/road.png').convert_alpha()
# POS_ROAD = ROAD.get_rect(center=(WIDTH//2, HEIGHT//2))

# ROAD = pygame.image.load('img/lvl1/road.png').convert_alpha()
# POS_ROAD = ROAD.get_rect()
# POS_ROAD.center = WIDTH//2, HEIGHT//2

CAR = pygame.image.load('img/lvl1/car.png').convert_alpha()
CAR_WIDTH = CAR.get_width()
POS_CAR = CAR.get_rect()
POS_CAR.center = WIDTH//100*20, HEIGHT//100*70
CAR_RIGHT = POS_CAR[0]+CAR_WIDTH

POS_CAR_0 = CAR.get_rect(center=(WIDTH//100*20, HEIGHT//100*50))
POS_CAR_1 = CAR.get_rect(center=(WIDTH//100*20, HEIGHT//100*70))
POS_CAR_2 = CAR.get_rect(center=(WIDTH//100*20, HEIGHT//100*90))

#UI
TASK = pygame.image.load('img/lvl1/task.png').convert_alpha()
POS_TASK = TASK.get_rect(center=(WIDTH//2, HEIGHT//100*8))

HEART = pygame.image.load('img/lvl1/heart.png').convert_alpha()
POS_HEART = HEART.get_rect()
POS_HEART.center = WIDTH//100*4, HEIGHT//100*5

SCORE = pygame.image.load('img/lvl1/score.png').convert_alpha()
POS_SCORE = SCORE.get_rect(center=(WIDTH//100*92, HEIGHT//100*99+30))

PAUSE = pygame.image.load('img/lvl1/pause.png').convert_alpha()
POS_PAUSE = PAUSE.get_rect(center=(WIDTH//100*92, HEIGHT//100*6))

speed = 8
acceleration = 1.0

ST_OFFSET_TUNNEL_0 = WIDTH+100
ST_OFFSET_TUNNEL_1 = WIDTH+100+100
ST_OFFSET_ANSWER = WIDTH+185

TUNNEL_0 = pygame.image.load('img/lvl1/tunnel_0.png').convert_alpha()
POS_TUNNEL_0_0 = TUNNEL_0.get_rect()
POS_TUNNEL_0_0.center = ST_OFFSET_TUNNEL_0, HEIGHT//100*46
POS_TUNNEL_0_1 = TUNNEL_0.get_rect()
POS_TUNNEL_0_1.center = ST_OFFSET_TUNNEL_0, HEIGHT//100*66
POS_TUNNEL_0_2 = TUNNEL_0.get_rect()
POS_TUNNEL_0_2.center = ST_OFFSET_TUNNEL_0, HEIGHT//100*88

TUNNEL_1 = pygame.image.load('img/lvl1/tunnel_1.png').convert_alpha()
POS_TUNNEL_1_0 = TUNNEL_1.get_rect()
POS_TUNNEL_1_0.center = ST_OFFSET_TUNNEL_1, HEIGHT//100*46
POS_TUNNEL_1_1 = TUNNEL_1.get_rect()
POS_TUNNEL_1_1.center = ST_OFFSET_TUNNEL_1, HEIGHT//100*66
POS_TUNNEL_1_2 = TUNNEL_1.get_rect()
POS_TUNNEL_1_2.center = ST_OFFSET_TUNNEL_1, HEIGHT//100*88

