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

CAR_2 = pygame.image.load('img/lvl1/car_crashed_1.png').convert_alpha()
CAR_2_WIDTH = CAR_2.get_width()
POS_CAR_2 = CAR_2.get_rect()
POS_CAR_2.center = WIDTH//100*20, HEIGHT//100*70
CAR_2_RIGHT = POS_CAR_2[0]+CAR_2_WIDTH

CAR_3 = pygame.image.load('img/lvl1/car_crashed_2.png').convert_alpha()
CAR_3_WIDTH = CAR_3.get_width()
POS_CAR_3 = CAR_3.get_rect()
POS_CAR_3.center = WIDTH//100*20, HEIGHT//100*70
CAR_3_RIGHT = POS_CAR_3[0]+CAR_3_WIDTH

CAR_4 = pygame.image.load('img/lvl1/car_crashed_3.png').convert_alpha()
CAR_4_WIDTH = CAR_4.get_width()
POS_CAR_4 = CAR_4.get_rect()
POS_CAR_4.center = WIDTH//100*20, HEIGHT//100*70
CAR_4_RIGHT = POS_CAR_4[0]+CAR_4_WIDTH



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

