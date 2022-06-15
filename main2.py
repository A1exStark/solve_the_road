import pygame
from pygame.locals import *
import random
import math
from spritelist_menu_2 import *
from osts import *

pygame.display.set_caption('MATH RIDER')

MAIN_MENU_START = FONT.render('START', 0, WHITE)
MAIN_MENU_OPTIONS = FONT.render('УРОВЕНЬ', 0, WHITE)
MAIN_MENU_EXIT = FONT.render('ВЫХОД', 0, WHITE)

MAIN_MENU_LVL_1 = FONT.render('+', 0, WHITE)
MAIN_MENU_LVL_2 = FONT.render('-', 0, WHITE)
MAIN_MENU_LVL_3 = FONT.render('*', 0, WHITE)
MAIN_MENU_LVL_4 = FONT.render(':', 0, WHITE)

POS_START = MAIN_MENU_START.get_rect(center=(WIDTH//2, HEIGHT//10*4))
POS_OPTIONS = MAIN_MENU_OPTIONS.get_rect(center=(WIDTH//2, HEIGHT//10*5))
POS_EXIT = MAIN_MENU_EXIT.get_rect(center=(WIDTH//2, HEIGHT//10*6))

POS_MAIN_MENU_LVL_1 = MAIN_MENU_LVL_1.get_rect(center=(WIDTH//2, HEIGHT//100*40))
POS_MAIN_MENU_LVL_2 = MAIN_MENU_LVL_2.get_rect(center=(WIDTH//2, HEIGHT//100*50))
POS_MAIN_MENU_LVL_3 = MAIN_MENU_LVL_3.get_rect(center=(WIDTH//2, HEIGHT//100*60))
POS_MAIN_MENU_LVL_4 = MAIN_MENU_LVL_4.get_rect(center=(WIDTH//2, HEIGHT//100*70))

menu_main_page = True
menu_lvl_choose_page = False


def menu_select_sound():
    MAIN_MENU_SELECT_SONUD.play()
def menu_selected_sound():
    MAIN_MENU_SELECTED_SONUD.play()
def lvl_start_sound():
    LVL_START_SOUND.play()
def gate_sound():
    GATE_SOUND.play()


def car_hit_sound():
    CAR_HIT_SOUND.play()
def car_hit_sound_2():
    CAR_HIT_SOUND_2.play()
    
def lvl_complete_sound():
    pygame.mixer.music.stop()
    LVL_COMPLETE_SOUND.play()
def game_over_sound():
    pygame.mixer.music.stop()
    GAME_OVER_SOUND.play()
    

def main_menu_music():
    pygame.mixer.music.stop()
    pygame.mixer.music.load('ost/main_menu.ogg')
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(loops=-1, start=0.0, fade_ms=300)

def lvl1_music():
    pygame.mixer.music.stop()
    lvl_start_sound()
    pygame.mixer.music.load('ost/lvl1.ogg')
    pygame.mixer.music.set_volume(0.18)
    pygame.mixer.music.play(loops=-1, start=0.0, fade_ms=300)

def lvl2_music():
    pygame.mixer.music.stop()
    lvl_start_sound()
    pygame.mixer.music.load('ost/lvl2.ogg')
    pygame.mixer.music.set_volume(0.15)
    pygame.mixer.music.play(loops=-1, start=0.0, fade_ms=300)
    
def lvl3_music():
    pygame.mixer.music.stop()
    lvl_start_sound()
    pygame.mixer.music.load('ost/lvl3.ogg')
    pygame.mixer.music.set_volume(0.18)
    pygame.mixer.music.play(loops=-1, start=0.0, fade_ms=300) 

def lvl4_music():
    pygame.mixer.music.stop()
    lvl_start_sound()
    pygame.mixer.music.load('ost/lvl4.ogg')
    pygame.mixer.music.set_volume(0.15)
    pygame.mixer.music.play(loops=-1, start=0.0, fade_ms=300)
    

def lvl1():
    
    lvl1_music()
    
    BG = pygame.image.load('img/lvl1/bg.jpg')

    POS_BG = BG.get_rect(center=(WIDTH//2, HEIGHT//2))

    MOUNTAINS = pygame.image.load('img/lvl1/mountains.png').convert_alpha()
    POS_MOUNTAINS = MOUNTAINS.get_rect(center=(WIDTH//2, HEIGHT//2))
    FOREST = pygame.image.load('img/lvl1/forest.png').convert_alpha()
    POS_FOREST = FOREST.get_rect(center=(WIDTH//2, HEIGHT//2))

    ROAD = pygame.image.load('img/lvl1/road.png').convert_alpha()
    
    CAR = pygame.image.load('img/lvl1/car.png').convert_alpha()
    CAR_WIDTH = CAR.get_width()
    POS_CAR = CAR.get_rect()
    POS_CAR.center = WIDTH//100*20, HEIGHT//100*70
    CAR_RIGHT = POS_CAR[0]+CAR_WIDTH

    CAR_W = pygame.image.load('img/lvl1/car_w.png').convert_alpha()
    CAR_W_WIDTH = CAR_W.get_width()
    POS_CAR_W = CAR_W.get_rect()
    POS_CAR_W.center = WIDTH//100*20, HEIGHT//100*70
    CAR_W_RIGHT = POS_CAR_W[0]+CAR_W_WIDTH

    CAR_2 = pygame.image.load('img/lvl1/car_crashed_1.png').convert_alpha()
    CAR_2_WIDTH = CAR_2.get_width()
    POS_CAR_2 = CAR_2.get_rect()
    POS_CAR_2.center = WIDTH//100*20, HEIGHT//100*70
    CAR_2_RIGHT = POS_CAR_2[0]+CAR_2_WIDTH

    CAR_2_W = pygame.image.load('img/lvl1/car_crashed_1_w.png').convert_alpha()
    CAR_2_W_WIDTH = CAR_2_W.get_width()
    POS_CAR_2_W = CAR_2_W.get_rect()
    POS_CAR_2_W.center = WIDTH//100*20, HEIGHT//100*70
    CAR_2_W_RIGHT = POS_CAR_2_W[0]+CAR_2_W_WIDTH

    CAR_3 = pygame.image.load('img/lvl1/car_crashed_2.png').convert_alpha()
    CAR_3_WIDTH = CAR_3.get_width()
    POS_CAR_3 = CAR_3.get_rect()
    POS_CAR_3.center = WIDTH//100*20, HEIGHT//100*70
    CAR_3_RIGHT = POS_CAR_3[0]+CAR_3_WIDTH

    CAR_3_W = pygame.image.load('img/lvl1/car_crashed_2_w.png').convert_alpha()
    CAR_3_W_WIDTH = CAR_3_W.get_width()
    POS_CAR_3_W = CAR_3_W.get_rect()
    POS_CAR_3_W.center = WIDTH//100*20, HEIGHT//100*70
    CAR_3_W_RIGHT = POS_CAR_3_W[0]+CAR_3_W_WIDTH

    CAR_4 = pygame.image.load('img/lvl1/car_crashed_3.png').convert_alpha()
    CAR_4_WIDTH = CAR_4.get_width()
    POS_CAR_4 = CAR_4.get_rect()
    POS_CAR_4.center = WIDTH//100*20, HEIGHT//100*70
    CAR_4_RIGHT = POS_CAR_4[0]+CAR_4_WIDTH
    
    TASK = pygame.image.load('img/lvl1/task.png').convert_alpha()
    POS_TASK = TASK.get_rect(center=(WIDTH//2, HEIGHT//100*8))
    SCORE = pygame.image.load('img/lvl1/score.png').convert_alpha()
    POS_SCORE = SCORE.get_rect(center=(WIDTH//100*92, HEIGHT//100*99+30))
    PAUSE = pygame.image.load('img/lvl1/pause.png').convert_alpha()
    POS_PAUSE = PAUSE.get_rect(center=(WIDTH//100*92, HEIGHT//100*6))
    
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

    run_lvl = True
    clock = pygame.time.Clock()
    i = 0
    exercises = 10
    FPS = 60
    NEW_TIMER = 0
    ROAD_LANES = 1
    lives = 3
    score = 0
    score_limit = 1
    COLLISION = False
    COLLISION_PAUSE = 1000
    game_is_on = True  
    current_time = 0
    speed = 8
    acceleration = 1.0
    GAME_OVER_SOUND_FLAG = False
    CAR_HIT_SOUND_FLAG = False
    CAR_HIT_2_SOUND_FLAG = False
    WIN_CONDITION = False
    pressed = pygame.key.get_pressed()

    all_exercises, all_answers, all_answer_flag, all_answer_flags_last = [], [], [], []

    for exercise in range(10):
        first_sum = random.randint(1, 97)
        second_sum = random.randint(1, 100-first_sum-1)
        sum_true = first_sum + second_sum
    
        if sum_true > 89:
            sum_fake_1 = sum_true + random.randint(-10, -1)
            sum_fake_2 = sum_true + random.randint(-10, -1)
        elif sum_true < 11:
            sum_fake_1 = sum_true + random.randint(1, 10)
            sum_fake_2 = sum_true + random.randint(1, 10)
        else:
            sum_fake_1 = sum_true + random.randint(-10, 10)
            sum_fake_2 = sum_true + random.randint(-10, 10)
        if sum_true == sum_fake_1 or sum_fake_1 == sum_fake_2:
            sum_fake_1 = random.randint(1, 97)
        if sum_true == sum_fake_2:
            sum_fake_2 = random.randint(1, 97)
        
        #if sum_true == sum_fake_1 or sum_true == sum_fake_2 or sum_fake_1 == sum_fake_2:
        #    print(f'{sum_true} {sum_fake_1} {sum_fake_2}')

        # if sum_true == sum_fake_1 or sum_true
        all_exercises.append(
            [first_sum, second_sum, sum_true, sum_fake_1, sum_fake_2])
        all_answers.append([sum_true, sum_fake_1, sum_fake_2])

    print(all_exercises)
    # print(all_answers)

    for all_answer in all_answers:
        new_answers = all_answer
        random.shuffle(new_answers)

    # print(all_answers)

    jj = 0

    for all_answer in all_answers:
        for a_a in all_answer:
            kk = math.floor(jj/3)
            jj += 1
            if a_a == all_exercises[kk][2]:
                all_answer_flag.append(True)
            else:
                all_answer_flag.append(False)
            # print(f'{kk} {a_a} {all_exercises[kk][2]}')
    # print(all_answer_flag)

    TUNNEL_EQUALS_0_0 = FONT.render(f'{all_answers[0][0]}', 0, WHITE)
    POS_TUNNEL_EQUALS_0_0 = TUNNEL_EQUALS_0_0.get_rect()
    POS_TUNNEL_EQUALS_0_0.center = ST_OFFSET_ANSWER, HEIGHT//100*46
    TUNNEL_LOGIC_0_0 = all_answer_flag[0]

    TUNNEL_EQUALS_0_1 = FONT.render(f'{all_answers[0][1]}', 0, WHITE)
    POS_TUNNEL_EQUALS_0_1 = TUNNEL_EQUALS_0_1.get_rect()
    POS_TUNNEL_EQUALS_0_1.center = ST_OFFSET_ANSWER, HEIGHT//100*66
    TUNNEL_LOGIC_0_1 = all_answer_flag[1]

    TUNNEL_EQUALS_0_2 = FONT.render(f'{all_answers[0][2]}', 0, WHITE)
    POS_TUNNEL_EQUALS_0_2 = TUNNEL_EQUALS_0_2.get_rect()
    POS_TUNNEL_EQUALS_0_2.center = ST_OFFSET_ANSWER, HEIGHT//100*88
    TUNNEL_LOGIC_0_2 = all_answer_flag[2]

    TUNNEL_EQUALS_1_0 = FONT.render(f'{all_answers[1][0]}', 0, WHITE)
    POS_TUNNEL_EQUALS_1_0 = TUNNEL_EQUALS_1_0.get_rect()
    POS_TUNNEL_EQUALS_1_0.center = ST_OFFSET_ANSWER, HEIGHT//100*46
    TUNNEL_LOGIC_1_0 = all_answer_flag[3]

    TUNNEL_EQUALS_1_1 = FONT.render(f'{all_answers[1][1]}', 0, WHITE)
    POS_TUNNEL_EQUALS_1_1 = TUNNEL_EQUALS_1_1.get_rect()
    POS_TUNNEL_EQUALS_1_1.center = ST_OFFSET_ANSWER, HEIGHT//100*66
    TUNNEL_LOGIC_1_1 = all_answer_flag[4]

    TUNNEL_EQUALS_1_2 = FONT.render(f'{all_answers[1][2]}', 0, WHITE)
    POS_TUNNEL_EQUALS_1_2 = TUNNEL_EQUALS_1_2.get_rect()
    POS_TUNNEL_EQUALS_1_2.center = ST_OFFSET_ANSWER, HEIGHT//100*88
    TUNNEL_LOGIC_1_2 = all_answer_flag[5]

    TUNNEL_EQUALS_2_0 = FONT.render(f'{all_answers[2][0]}', 0, WHITE)
    POS_TUNNEL_EQUALS_2_0 = TUNNEL_EQUALS_2_0.get_rect()
    POS_TUNNEL_EQUALS_2_0.center = ST_OFFSET_ANSWER, HEIGHT//100*46
    TUNNEL_LOGIC_2_0 = all_answer_flag[6]

    TUNNEL_EQUALS_2_1 = FONT.render(f'{all_answers[2][1]}', 0, WHITE)
    POS_TUNNEL_EQUALS_2_1 = TUNNEL_EQUALS_2_1.get_rect()
    POS_TUNNEL_EQUALS_2_1.center = ST_OFFSET_ANSWER, HEIGHT//100*66
    TUNNEL_LOGIC_2_1 = all_answer_flag[7]

    TUNNEL_EQUALS_2_2 = FONT.render(f'{all_answers[2][2]}', 0, WHITE)
    POS_TUNNEL_EQUALS_2_2 = TUNNEL_EQUALS_2_2.get_rect()
    POS_TUNNEL_EQUALS_2_2.center = ST_OFFSET_ANSWER, HEIGHT//100*88
    TUNNEL_LOGIC_2_2 = all_answer_flag[8]

    TUNNEL_EQUALS_3_0 = FONT.render(f'{all_answers[3][0]}', 0, WHITE)
    POS_TUNNEL_EQUALS_3_0 = TUNNEL_EQUALS_3_0.get_rect()
    POS_TUNNEL_EQUALS_3_0.center = ST_OFFSET_ANSWER, HEIGHT//100*46
    TUNNEL_LOGIC_3_0 = all_answer_flag[9]

    TUNNEL_EQUALS_3_1 = FONT.render(f'{all_answers[3][1]}', 0, WHITE)
    POS_TUNNEL_EQUALS_3_1 = TUNNEL_EQUALS_3_1.get_rect()
    POS_TUNNEL_EQUALS_3_1.center = ST_OFFSET_ANSWER, HEIGHT//100*66
    TUNNEL_LOGIC_3_1 = all_answer_flag[10]

    TUNNEL_EQUALS_3_2 = FONT.render(f'{all_answers[3][2]}', 0, WHITE)
    POS_TUNNEL_EQUALS_3_2 = TUNNEL_EQUALS_3_2.get_rect()
    POS_TUNNEL_EQUALS_3_2.center = ST_OFFSET_ANSWER, HEIGHT//100*88
    TUNNEL_LOGIC_3_2 = all_answer_flag[11]

    TUNNEL_EQUALS_4_0 = FONT.render(f'{all_answers[4][0]}', 0, WHITE)
    POS_TUNNEL_EQUALS_4_0 = TUNNEL_EQUALS_4_0.get_rect()
    POS_TUNNEL_EQUALS_4_0.center = ST_OFFSET_ANSWER, HEIGHT//100*46
    TUNNEL_LOGIC_4_0 = all_answer_flag[12]

    TUNNEL_EQUALS_4_1 = FONT.render(f'{all_answers[4][1]}', 0, WHITE)
    POS_TUNNEL_EQUALS_4_1 = TUNNEL_EQUALS_4_1.get_rect()
    POS_TUNNEL_EQUALS_4_1.center = ST_OFFSET_ANSWER, HEIGHT//100*66
    TUNNEL_LOGIC_4_1 = all_answer_flag[13]

    TUNNEL_EQUALS_4_2 = FONT.render(f'{all_answers[4][2]}', 0, WHITE)
    POS_TUNNEL_EQUALS_4_2 = TUNNEL_EQUALS_4_2.get_rect()
    POS_TUNNEL_EQUALS_4_2.center = ST_OFFSET_ANSWER, HEIGHT//100*88
    TUNNEL_LOGIC_4_2 = all_answer_flag[14]

    TUNNEL_EQUALS_5_0 = FONT.render(f'{all_answers[5][0]}', 0, WHITE)
    POS_TUNNEL_EQUALS_5_0 = TUNNEL_EQUALS_5_0.get_rect()
    POS_TUNNEL_EQUALS_5_0.center = ST_OFFSET_ANSWER, HEIGHT//100*46
    TUNNEL_LOGIC_5_0 = all_answer_flag[15]

    TUNNEL_EQUALS_5_1 = FONT.render(f'{all_answers[5][1]}', 0, WHITE)
    POS_TUNNEL_EQUALS_5_1 = TUNNEL_EQUALS_5_1.get_rect()
    POS_TUNNEL_EQUALS_5_1.center = ST_OFFSET_ANSWER, HEIGHT//100*66
    TUNNEL_LOGIC_5_1 = all_answer_flag[16]

    TUNNEL_EQUALS_5_2 = FONT.render(f'{all_answers[5][2]}', 0, WHITE)
    POS_TUNNEL_EQUALS_5_2 = TUNNEL_EQUALS_5_2.get_rect()
    POS_TUNNEL_EQUALS_5_2.center = ST_OFFSET_ANSWER, HEIGHT//100*88
    TUNNEL_LOGIC_5_2 = all_answer_flag[17]

    TUNNEL_EQUALS_6_0 = FONT.render(f'{all_answers[6][0]}', 0, WHITE)
    POS_TUNNEL_EQUALS_6_0 = TUNNEL_EQUALS_6_0.get_rect()
    POS_TUNNEL_EQUALS_6_0.center = ST_OFFSET_ANSWER, HEIGHT//100*46
    TUNNEL_LOGIC_6_0 = all_answer_flag[18]

    TUNNEL_EQUALS_6_1 = FONT.render(f'{all_answers[6][1]}', 0, WHITE)
    POS_TUNNEL_EQUALS_6_1 = TUNNEL_EQUALS_6_1.get_rect()
    POS_TUNNEL_EQUALS_6_1.center = ST_OFFSET_ANSWER, HEIGHT//100*66
    TUNNEL_LOGIC_6_1 = all_answer_flag[19]

    TUNNEL_EQUALS_6_2 = FONT.render(f'{all_answers[6][2]}', 0, WHITE)
    POS_TUNNEL_EQUALS_6_2 = TUNNEL_EQUALS_6_2.get_rect()
    POS_TUNNEL_EQUALS_6_2.center = ST_OFFSET_ANSWER, HEIGHT//100*88
    TUNNEL_LOGIC_6_2 = all_answer_flag[20]

    TUNNEL_EQUALS_7_0 = FONT.render(f'{all_answers[7][0]}', 0, WHITE)
    POS_TUNNEL_EQUALS_7_0 = TUNNEL_EQUALS_7_0.get_rect()
    POS_TUNNEL_EQUALS_7_0.center = ST_OFFSET_ANSWER, HEIGHT//100*46
    TUNNEL_LOGIC_7_0 = all_answer_flag[21]

    TUNNEL_EQUALS_7_1 = FONT.render(f'{all_answers[7][1]}', 0, WHITE)
    POS_TUNNEL_EQUALS_7_1 = TUNNEL_EQUALS_7_1.get_rect()
    POS_TUNNEL_EQUALS_7_1.center = ST_OFFSET_ANSWER, HEIGHT//100*66
    TUNNEL_LOGIC_7_1 = all_answer_flag[22]

    TUNNEL_EQUALS_7_2 = FONT.render(f'{all_answers[7][2]}', 0, WHITE)
    POS_TUNNEL_EQUALS_7_2 = TUNNEL_EQUALS_7_2.get_rect()
    POS_TUNNEL_EQUALS_7_2.center = ST_OFFSET_ANSWER, HEIGHT//100*88
    TUNNEL_LOGIC_7_2 = all_answer_flag[23]

    TUNNEL_EQUALS_8_0 = FONT.render(f'{all_answers[8][0]}', 0, WHITE)
    POS_TUNNEL_EQUALS_8_0 = TUNNEL_EQUALS_8_0.get_rect()
    POS_TUNNEL_EQUALS_8_0.center = ST_OFFSET_ANSWER, HEIGHT//100*46
    TUNNEL_LOGIC_8_0 = all_answer_flag[24]

    TUNNEL_EQUALS_8_1 = FONT.render(f'{all_answers[8][1]}', 0, WHITE)
    POS_TUNNEL_EQUALS_8_1 = TUNNEL_EQUALS_8_1.get_rect()
    POS_TUNNEL_EQUALS_8_1.center = ST_OFFSET_ANSWER, HEIGHT//100*66
    TUNNEL_LOGIC_8_1 = all_answer_flag[25]

    TUNNEL_EQUALS_8_2 = FONT.render(f'{all_answers[8][2]}', 0, WHITE)
    POS_TUNNEL_EQUALS_8_2 = TUNNEL_EQUALS_8_2.get_rect()
    POS_TUNNEL_EQUALS_8_2.center = ST_OFFSET_ANSWER, HEIGHT//100*88
    TUNNEL_LOGIC_8_2 = all_answer_flag[26]

    TUNNEL_EQUALS_9_0 = FONT.render(f'{all_answers[9][0]}', 0, WHITE)
    POS_TUNNEL_EQUALS_9_0 = TUNNEL_EQUALS_9_0.get_rect()
    POS_TUNNEL_EQUALS_9_0.center = ST_OFFSET_ANSWER, HEIGHT//100*46
    TUNNEL_LOGIC_9_0 = all_answer_flag[27]

    TUNNEL_EQUALS_9_1 = FONT.render(f'{all_answers[9][1]}', 0, WHITE)
    POS_TUNNEL_EQUALS_9_1 = TUNNEL_EQUALS_9_1.get_rect()
    POS_TUNNEL_EQUALS_9_1.center = ST_OFFSET_ANSWER, HEIGHT//100*66
    TUNNEL_LOGIC_9_1 = all_answer_flag[28]

    TUNNEL_EQUALS_9_2 = FONT.render(f'{all_answers[9][2]}', 0, WHITE)
    POS_TUNNEL_EQUALS_9_2 = TUNNEL_EQUALS_9_2.get_rect()
    POS_TUNNEL_EQUALS_9_2.center = ST_OFFSET_ANSWER, HEIGHT//100*88
    TUNNEL_LOGIC_9_2 = all_answer_flag[29]

    def draw_all():
        if lives != 0:
            WIN.blit(BG, POS_BG)
            WIN.blit(MOUNTAINS, POS_MOUNTAINS)
            WIN.blit(FOREST, POS_FOREST)
            WIN.blit(ROAD, (i, 0))
            WIN.blit(ROAD, (WIDTH+i, 0))
            # WIN.blit(ROAD, POS_ROAD)
            WIN.blit(TASK, POS_TASK)

            # WIN.blit(HEART, POS_HEART_0)
            # WIN.blit(HEART, POS_HEART_1)
            # WIN.blit(HEART, POS_HEART_2)

            WIN.blit(SCORE, POS_SCORE)
            WIN.blit(PAUSE, POS_PAUSE)

            WIN.blit(TUNNEL_0, POS_TUNNEL_0_0)
            WIN.blit(TUNNEL_0, POS_TUNNEL_0_1)
            WIN.blit(TUNNEL_0, POS_TUNNEL_0_2)

        ostatok = current_time // 250 % 2
        
        if lives == 3 and ostatok == 0:
            WIN.blit(CAR, POS_CAR)
        elif lives == 3 and ostatok != 0:
            WIN.blit(CAR_W, (POS_CAR_W[0], POS_CAR_W[1]+2))
        if lives == 2 and ostatok == 0:
            WIN.blit(CAR_2, POS_CAR_2)
        elif lives == 2 and ostatok != 0:
            WIN.blit(CAR_2_W, (POS_CAR_2_W[0], POS_CAR_2_W[1]+2))
        if lives == 1 and ostatok == 0:
            WIN.blit(CAR_3, POS_CAR_3)
        elif lives == 1 and ostatok != 0:
            WIN.blit(CAR_3_W, (POS_CAR_3_W[0], POS_CAR_3_W[1]+2))
        if lives == 0:
            WIN.blit(CAR_4, POS_CAR_4)

        if lives != 0:
            WIN.blit(TUNNEL_1, POS_TUNNEL_1_0)
            WIN.blit(TUNNEL_1, POS_TUNNEL_1_1)
            WIN.blit(TUNNEL_1, POS_TUNNEL_1_2)

            WIN.blit(TUNNEL_EQUALS_0_0, POS_TUNNEL_EQUALS_0_0)
            WIN.blit(TUNNEL_EQUALS_0_1, POS_TUNNEL_EQUALS_0_1)
            WIN.blit(TUNNEL_EQUALS_0_2, POS_TUNNEL_EQUALS_0_2)

            WIN.blit(TUNNEL_EQUALS_1_0, POS_TUNNEL_EQUALS_1_0)
            WIN.blit(TUNNEL_EQUALS_1_1, POS_TUNNEL_EQUALS_1_1)
            WIN.blit(TUNNEL_EQUALS_1_2, POS_TUNNEL_EQUALS_1_2)

            WIN.blit(TUNNEL_EQUALS_2_0, POS_TUNNEL_EQUALS_2_0)
            WIN.blit(TUNNEL_EQUALS_2_1, POS_TUNNEL_EQUALS_2_1)
            WIN.blit(TUNNEL_EQUALS_2_2, POS_TUNNEL_EQUALS_2_2)

            WIN.blit(TUNNEL_EQUALS_3_0, POS_TUNNEL_EQUALS_3_0)
            WIN.blit(TUNNEL_EQUALS_3_1, POS_TUNNEL_EQUALS_3_1)
            WIN.blit(TUNNEL_EQUALS_3_2, POS_TUNNEL_EQUALS_3_2)

            WIN.blit(TUNNEL_EQUALS_4_0, POS_TUNNEL_EQUALS_4_0)
            WIN.blit(TUNNEL_EQUALS_4_1, POS_TUNNEL_EQUALS_4_1)
            WIN.blit(TUNNEL_EQUALS_4_2, POS_TUNNEL_EQUALS_4_2)

            WIN.blit(TUNNEL_EQUALS_5_0, POS_TUNNEL_EQUALS_5_0)
            WIN.blit(TUNNEL_EQUALS_5_1, POS_TUNNEL_EQUALS_5_1)
            WIN.blit(TUNNEL_EQUALS_5_2, POS_TUNNEL_EQUALS_5_2)

            WIN.blit(TUNNEL_EQUALS_6_0, POS_TUNNEL_EQUALS_6_0)
            WIN.blit(TUNNEL_EQUALS_6_1, POS_TUNNEL_EQUALS_6_1)
            WIN.blit(TUNNEL_EQUALS_6_2, POS_TUNNEL_EQUALS_6_2)

            WIN.blit(TUNNEL_EQUALS_7_0, POS_TUNNEL_EQUALS_7_0)
            WIN.blit(TUNNEL_EQUALS_7_1, POS_TUNNEL_EQUALS_7_1)
            WIN.blit(TUNNEL_EQUALS_7_2, POS_TUNNEL_EQUALS_7_2)

            WIN.blit(TUNNEL_EQUALS_8_0, POS_TUNNEL_EQUALS_8_0)
            WIN.blit(TUNNEL_EQUALS_8_1, POS_TUNNEL_EQUALS_8_1)
            WIN.blit(TUNNEL_EQUALS_8_2, POS_TUNNEL_EQUALS_8_2)

            WIN.blit(TUNNEL_EQUALS_9_0, POS_TUNNEL_EQUALS_9_0)
            WIN.blit(TUNNEL_EQUALS_9_1, POS_TUNNEL_EQUALS_9_1)
            WIN.blit(TUNNEL_EQUALS_9_2, POS_TUNNEL_EQUALS_9_2)

    while run_lvl:
        def reset_tunnels():
            POS_TUNNEL_0_0[0] = ST_OFFSET_TUNNEL_0+33
            POS_TUNNEL_0_1[0] = ST_OFFSET_TUNNEL_0+33
            POS_TUNNEL_0_2[0] = ST_OFFSET_TUNNEL_0+33

            POS_TUNNEL_1_0[0] = ST_OFFSET_TUNNEL_1
            POS_TUNNEL_1_1[0] = ST_OFFSET_TUNNEL_1
            POS_TUNNEL_1_2[0] = ST_OFFSET_TUNNEL_1
            
        def move_tunnels():
            POS_TUNNEL_0_0[0] -= speed*acceleration
            POS_TUNNEL_0_1[0] -= speed*acceleration
            POS_TUNNEL_0_2[0] -= speed*acceleration

            POS_TUNNEL_1_0[0] -= speed*acceleration
            POS_TUNNEL_1_1[0] -= speed*acceleration
            POS_TUNNEL_1_2[0] -= speed*acceleration

        def equals_reset_0():
            POS_TUNNEL_EQUALS_0_0[0] = -WIDTH
            POS_TUNNEL_EQUALS_0_1[0] = -WIDTH
            POS_TUNNEL_EQUALS_0_2[0] = -WIDTH
        def equals_reset_1():
            POS_TUNNEL_EQUALS_1_0[0] = -WIDTH
            POS_TUNNEL_EQUALS_1_1[0] = -WIDTH
            POS_TUNNEL_EQUALS_1_2[0] = -WIDTH
        def equals_reset_2():
            POS_TUNNEL_EQUALS_2_0[0] = -WIDTH
            POS_TUNNEL_EQUALS_2_1[0] = -WIDTH
            POS_TUNNEL_EQUALS_2_2[0] = -WIDTH
        def equals_reset_3():
            POS_TUNNEL_EQUALS_3_0[0] = -WIDTH
            POS_TUNNEL_EQUALS_3_1[0] = -WIDTH
            POS_TUNNEL_EQUALS_3_2[0] = -WIDTH
        def equals_reset_4():
            POS_TUNNEL_EQUALS_4_0[0] = -WIDTH
            POS_TUNNEL_EQUALS_4_1[0] = -WIDTH
            POS_TUNNEL_EQUALS_4_2[0] = -WIDTH
        def equals_reset_5():
            POS_TUNNEL_EQUALS_5_0[0] = -WIDTH
            POS_TUNNEL_EQUALS_5_1[0] = -WIDTH
            POS_TUNNEL_EQUALS_5_2[0] = -WIDTH
        def equals_reset_6():
            POS_TUNNEL_EQUALS_6_0[0] = -WIDTH
            POS_TUNNEL_EQUALS_6_1[0] = -WIDTH
            POS_TUNNEL_EQUALS_6_2[0] = -WIDTH
        def equals_reset_7():
            POS_TUNNEL_EQUALS_7_0[0] = -WIDTH
            POS_TUNNEL_EQUALS_7_1[0] = -WIDTH
            POS_TUNNEL_EQUALS_7_2[0] = -WIDTH
        def equals_reset_8():
            POS_TUNNEL_EQUALS_8_0[0] = -WIDTH
            POS_TUNNEL_EQUALS_8_1[0] = -WIDTH
            POS_TUNNEL_EQUALS_8_2[0] = -WIDTH
        def equals_reset_9():
            POS_TUNNEL_EQUALS_9_0[0] = -WIDTH
            POS_TUNNEL_EQUALS_9_1[0] = -WIDTH
            POS_TUNNEL_EQUALS_9_2[0] = -WIDTH
            
        def car_hits():
            if lives == 2:
                car_hit_sound()
            elif lives == 1:
                car_hit_sound_2()
            if lives > 0:
                pygame.time.wait(COLLISION_PAUSE)
        # print(f'{current_time} {NEW_TIMER}')

        draw_all()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.mixer.music.stop()                
                menu_selected_sound()
                run_lvl = False
                NEW_TIMER = 0
                main_menu_music()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    ROAD_LANES += 1
                if event.key == pygame.K_UP:
                    ROAD_LANES -= 1
                if event.key == pygame.K_0:
                    game_is_on = True
                    # current_time = pygame.time.get_ticks()
                if event.key == pygame.K_9:
                    game_is_on = False

            if (event.type == pygame.KEYDOWN and event.key == K_RIGHT) or (event.type == pygame.KEYUP and event.key == K_LEFT):
                acceleration += 0.5
            if (event.type == pygame.KEYDOWN and event.key == K_LEFT) or (event.type == pygame.KEYUP and event.key == K_RIGHT):
                acceleration -= 0.5
            if event.type == pygame.KEYDOWN and event.key == K_RETURN and WIN_CONDITION:
                run_lvl = False
                lvl2()

        if lives == 3:
            WIN.blit(HEART, POS_HEART)
            WIN.blit(HEART, (POS_HEART[0]+60, POS_HEART[1]))
            WIN.blit(HEART, (POS_HEART[0]+120, POS_HEART[1]))
        elif lives == 2:
            WIN.blit(HEART, POS_HEART)
            WIN.blit(HEART, (POS_HEART[0]+60, POS_HEART[1]))
        elif lives == 1:
            WIN.blit(HEART, POS_HEART)

        if i <= -WIDTH:
            WIN.blit(ROAD, (i+WIDTH, 0))
            i = 0
        i -= speed*acceleration

        if ROAD_LANES == 0:
            POS_CAR[1] = HEIGHT//100*40
            POS_CAR_W[1] = HEIGHT//100*40
            POS_CAR_2[1] = HEIGHT//100*40
            POS_CAR_2_W[1] = HEIGHT//100*40
            POS_CAR_3[1] = HEIGHT//100*40
            POS_CAR_3_W[1] = HEIGHT//100*40
            POS_CAR_4[1] = HEIGHT//100*40
            # print(ROAD_LANES)
        elif ROAD_LANES == 1:
            POS_CAR[1] = HEIGHT//100*60
            POS_CAR_W[1] = HEIGHT//100*60
            POS_CAR_2[1] = HEIGHT//100*60
            POS_CAR_2_W[1] = HEIGHT//100*60
            POS_CAR_3[1] = HEIGHT//100*60
            POS_CAR_3_W[1] = HEIGHT//100*60
            POS_CAR_4[1] = HEIGHT//100*60
            # print(ROAD_LANES)
        elif ROAD_LANES == 2:
            POS_CAR[1] = HEIGHT//100*80
            POS_CAR_W[1] = HEIGHT//100*80
            POS_CAR_2[1] = HEIGHT//100*80
            POS_CAR_2_W[1] = HEIGHT//100*80
            POS_CAR_3[1] = HEIGHT//100*80
            POS_CAR_3_W[1] = HEIGHT//100*80
            POS_CAR_4[1] = HEIGHT//100*80
            # print(ROAD_LANES)
        elif ROAD_LANES > 2:
            ROAD_LANES = 2
        elif ROAD_LANES < 0:
            ROAD_LANES = 0

        if lives != 0 and game_is_on:
            if 0 < NEW_TIMER < 3000:
                COLLISION = False

                equals_reset_0()

                reset_tunnels()

                POS_TUNNEL_EQUALS_0_0[0] = ST_OFFSET_ANSWER+35
                POS_TUNNEL_EQUALS_0_1[0] = ST_OFFSET_ANSWER+35
                POS_TUNNEL_EQUALS_0_2[0] = ST_OFFSET_ANSWER+35

            if 3000 < NEW_TIMER < 8000:
                TASK_1 = FONT.render(
                    f'{all_exercises[0][0]}+{all_exercises[0][1]}', 0, WHITE)
                POS_TASK_1 = TASK_1.get_rect()
                POS_TASK_1.center = (WIDTH//2, HEIGHT//100*8)
                WIN.blit(TASK_1, POS_TASK_1)
                
                move_tunnels()
                
                POS_TUNNEL_EQUALS_0_0[0] -= speed*acceleration
                POS_TUNNEL_EQUALS_0_1[0] -= speed*acceleration
                POS_TUNNEL_EQUALS_0_2[0] -= speed*acceleration

                if CAR_RIGHT-6 <= POS_TUNNEL_1_0[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_0_0 == False and ROAD_LANES == 0 and COLLISION == False:
                    COLLISION = True
                    lives -= 1
                    car_hits()
                    equals_reset_0()
                elif CAR_RIGHT-6 <= POS_TUNNEL_1_0[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_0_0 == True and ROAD_LANES == 0 and COLLISION == False:
                    COLLISION = True
                    gate_sound()
                    score += score_limit
                if CAR_RIGHT-6 <= POS_TUNNEL_1_1[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_0_1 == False and ROAD_LANES == 1 and COLLISION == False:
                    COLLISION = True
                    lives -= 1
                    car_hits()
                    equals_reset_0()
                elif CAR_RIGHT-6 <= POS_TUNNEL_1_1[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_0_1 == True and ROAD_LANES == 1 and COLLISION == False:
                    COLLISION = True
                    gate_sound()
                    score += score_limit
                if CAR_RIGHT-6 <= POS_TUNNEL_1_2[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_0_2 == False and ROAD_LANES == 2 and COLLISION == False:
                    COLLISION = True
                    lives -= 1
                    car_hits()
                    equals_reset_0()
                elif CAR_RIGHT-6 <= POS_TUNNEL_1_2[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_0_2 == True and ROAD_LANES == 2 and COLLISION == False:
                    COLLISION = True
                    gate_sound()
                    score += score_limit

                # print(f'{POS_TUNNEL_1_0[0]} {CAR_RIGHT} {score}')

            if 8000 < NEW_TIMER < 10000:
                COLLISION = False

                equals_reset_0()

                reset_tunnels()

                POS_TUNNEL_EQUALS_1_0[0] = ST_OFFSET_ANSWER+35
                POS_TUNNEL_EQUALS_1_1[0] = ST_OFFSET_ANSWER+35
                POS_TUNNEL_EQUALS_1_2[0] = ST_OFFSET_ANSWER+35

            if 10000 < NEW_TIMER < 15000:
                TASK_1 = FONT.render(
                    f'{all_exercises[1][0]}+{all_exercises[1][1]}', 0, WHITE)
                POS_TASK_1 = TASK_1.get_rect()
                POS_TASK_1.center = (WIDTH//2, HEIGHT//100*8)
                WIN.blit(TASK_1, POS_TASK_1)

                move_tunnels()

                POS_TUNNEL_EQUALS_1_0[0] -= speed*acceleration
                POS_TUNNEL_EQUALS_1_1[0] -= speed*acceleration
                POS_TUNNEL_EQUALS_1_2[0] -= speed*acceleration

                if CAR_RIGHT-6 <= POS_TUNNEL_1_0[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_1_0 == False and ROAD_LANES == 0 and COLLISION == False:
                    COLLISION = True
                    lives -= 1
                    car_hits()
                    equals_reset_1()
                elif CAR_RIGHT-6 <= POS_TUNNEL_1_0[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_1_0 == True and ROAD_LANES == 0 and COLLISION == False:
                    COLLISION = True
                    gate_sound()
                    score += score_limit
                if CAR_RIGHT-6 <= POS_TUNNEL_1_1[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_1_1 == False and ROAD_LANES == 1 and COLLISION == False:
                    COLLISION = True
                    lives -= 1
                    car_hits()
                    equals_reset_1()
                elif CAR_RIGHT-6 <= POS_TUNNEL_1_1[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_1_1 == True and ROAD_LANES == 1 and COLLISION == False:
                    COLLISION = True
                    gate_sound()
                    score += score_limit
                if CAR_RIGHT-6 <= POS_TUNNEL_1_2[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_1_2 == False and ROAD_LANES == 2 and COLLISION == False:
                    COLLISION = True
                    lives -= 1
                    car_hits()
                    equals_reset_1()
                elif CAR_RIGHT-6 <= POS_TUNNEL_1_2[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_1_2 == True and ROAD_LANES == 2 and COLLISION == False:
                    COLLISION = True
                    gate_sound()
                    score += score_limit

                # print(f'{POS_TUNNEL_1_0[0]} {CAR_RIGHT} {score}')

            if 15000 < NEW_TIMER < 17000:
                COLLISION = False

                equals_reset_1()

                reset_tunnels()

                POS_TUNNEL_EQUALS_2_0[0] = ST_OFFSET_ANSWER+35
                POS_TUNNEL_EQUALS_2_1[0] = ST_OFFSET_ANSWER+35
                POS_TUNNEL_EQUALS_2_2[0] = ST_OFFSET_ANSWER+35

            if 17000 < NEW_TIMER < 22000:
                TASK_1 = FONT.render(
                    f'{all_exercises[2][0]}+{all_exercises[2][1]}', 0, WHITE)
                POS_TASK_1 = TASK_1.get_rect()
                POS_TASK_1.center = (WIDTH//2, HEIGHT//100*8)
                WIN.blit(TASK_1, POS_TASK_1)

                move_tunnels()

                POS_TUNNEL_EQUALS_2_0[0] -= speed*acceleration
                POS_TUNNEL_EQUALS_2_1[0] -= speed*acceleration
                POS_TUNNEL_EQUALS_2_2[0] -= speed*acceleration

                if CAR_RIGHT-6 <= POS_TUNNEL_1_0[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_2_0 == False and ROAD_LANES == 0 and COLLISION == False:
                    COLLISION = True
                    lives -= 1
                    car_hits()
                    equals_reset_2()
                elif CAR_RIGHT-6 <= POS_TUNNEL_1_0[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_2_0 == True and ROAD_LANES == 0 and COLLISION == False:
                    COLLISION = True
                    gate_sound()
                    score += score_limit
                if CAR_RIGHT-6 <= POS_TUNNEL_1_1[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_2_1 == False and ROAD_LANES == 1 and COLLISION == False:
                    COLLISION = True
                    lives -= 1
                    car_hits()
                    equals_reset_2()
                elif CAR_RIGHT-6 <= POS_TUNNEL_1_1[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_2_1 == True and ROAD_LANES == 1 and COLLISION == False:
                    COLLISION = True
                    gate_sound()
                    score += score_limit
                if CAR_RIGHT-6 <= POS_TUNNEL_1_2[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_2_2 == False and ROAD_LANES == 2 and COLLISION == False:
                    COLLISION = True
                    lives -= 1
                    car_hits()
                    equals_reset_2()
                elif CAR_RIGHT-6 <= POS_TUNNEL_1_2[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_2_2 == True and ROAD_LANES == 2 and COLLISION == False:
                    COLLISION = True
                    gate_sound()
                    score += score_limit

                # print(f'{POS_TUNNEL_1_0[0]} {CAR_RIGHT} {score}')

            if 22000 < NEW_TIMER < 24000:
                COLLISION = False

                equals_reset_2()

                reset_tunnels()

                POS_TUNNEL_EQUALS_3_0[0] = ST_OFFSET_ANSWER+35
                POS_TUNNEL_EQUALS_3_1[0] = ST_OFFSET_ANSWER+35
                POS_TUNNEL_EQUALS_3_2[0] = ST_OFFSET_ANSWER+35

            if 24000 < NEW_TIMER < 29000:
                TASK_1 = FONT.render(
                    f'{all_exercises[3][0]}+{all_exercises[3][1]}', 0, WHITE)
                POS_TASK_1 = TASK_1.get_rect()
                POS_TASK_1.center = (WIDTH//2, HEIGHT//100*8)
                WIN.blit(TASK_1, POS_TASK_1)

                move_tunnels()

                POS_TUNNEL_EQUALS_3_0[0] -= speed*acceleration
                POS_TUNNEL_EQUALS_3_1[0] -= speed*acceleration
                POS_TUNNEL_EQUALS_3_2[0] -= speed*acceleration

                if CAR_RIGHT-6 <= POS_TUNNEL_1_0[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_3_0 == False and ROAD_LANES == 0 and COLLISION == False:
                    COLLISION = True
                    lives -= 1
                    car_hits()
                    equals_reset_3()
                elif CAR_RIGHT-6 <= POS_TUNNEL_1_0[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_3_0 == True and ROAD_LANES == 0 and COLLISION == False:
                    COLLISION = True
                    gate_sound()
                    score += score_limit
                if CAR_RIGHT-6 <= POS_TUNNEL_1_1[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_3_1 == False and ROAD_LANES == 1 and COLLISION == False:
                    COLLISION = True
                    lives -= 1
                    car_hits()
                    equals_reset_3()
                elif CAR_RIGHT-6 <= POS_TUNNEL_1_1[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_3_1 == True and ROAD_LANES == 1 and COLLISION == False:
                    COLLISION = True
                    gate_sound()
                    score += score_limit
                if CAR_RIGHT-6 <= POS_TUNNEL_1_2[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_3_2 == False and ROAD_LANES == 2 and COLLISION == False:
                    COLLISION = True
                    lives -= 1
                    car_hits()
                    equals_reset_3()
                elif CAR_RIGHT-6 <= POS_TUNNEL_1_2[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_3_2 == True and ROAD_LANES == 2 and COLLISION == False:
                    COLLISION = True
                    gate_sound()
                    score += score_limit

                # print(f'{POS_TUNNEL_1_0[0]} {CAR_RIGHT} {score}')

            if 29000 < NEW_TIMER < 31000:
                COLLISION = False

                equals_reset_3()

                reset_tunnels()

                POS_TUNNEL_EQUALS_4_0[0] = ST_OFFSET_ANSWER+35
                POS_TUNNEL_EQUALS_4_1[0] = ST_OFFSET_ANSWER+35
                POS_TUNNEL_EQUALS_4_2[0] = ST_OFFSET_ANSWER+35

            if 31000 < NEW_TIMER < 36000:
                TASK_1 = FONT.render(
                    f'{all_exercises[4][0]}+{all_exercises[4][1]}', 0, WHITE)
                POS_TASK_1 = TASK_1.get_rect()
                POS_TASK_1.center = (WIDTH//2, HEIGHT//100*8)
                WIN.blit(TASK_1, POS_TASK_1)

                move_tunnels()

                POS_TUNNEL_EQUALS_4_0[0] -= speed*acceleration
                POS_TUNNEL_EQUALS_4_1[0] -= speed*acceleration
                POS_TUNNEL_EQUALS_4_2[0] -= speed*acceleration

                if CAR_RIGHT-6 <= POS_TUNNEL_1_0[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_4_0 == False and ROAD_LANES == 0 and COLLISION == False:
                    COLLISION = True
                    lives -= 1
                    car_hits()
                    equals_reset_4()
                elif CAR_RIGHT-6 <= POS_TUNNEL_1_0[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_4_0 == True and ROAD_LANES == 0 and COLLISION == False:
                    COLLISION = True
                    gate_sound()
                    score += score_limit
                if CAR_RIGHT-6 <= POS_TUNNEL_1_1[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_4_1 == False and ROAD_LANES == 1 and COLLISION == False:
                    COLLISION = True
                    lives -= 1
                    car_hits()
                    equals_reset_4()
                elif CAR_RIGHT-6 <= POS_TUNNEL_1_1[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_4_1 == True and ROAD_LANES == 1 and COLLISION == False:
                    COLLISION = True
                    gate_sound()
                    score += score_limit
                if CAR_RIGHT-6 <= POS_TUNNEL_1_2[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_4_2 == False and ROAD_LANES == 2 and COLLISION == False:
                    COLLISION = True
                    lives -= 1
                    car_hits()
                    equals_reset_4()
                elif CAR_RIGHT-6 <= POS_TUNNEL_1_2[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_4_2 == True and ROAD_LANES == 2 and COLLISION == False:
                    COLLISION = True
                    gate_sound()
                    score += score_limit

                # print(f'{POS_TUNNEL_1_0[0]} {CAR_RIGHT} {score}')

            if 36000 < NEW_TIMER < 38000:
                COLLISION = False

                equals_reset_4()

                reset_tunnels()

                POS_TUNNEL_EQUALS_5_0[0] = ST_OFFSET_ANSWER+35
                POS_TUNNEL_EQUALS_5_1[0] = ST_OFFSET_ANSWER+35
                POS_TUNNEL_EQUALS_5_2[0] = ST_OFFSET_ANSWER+35

            if 38000 < NEW_TIMER < 43000:
                TASK_1 = FONT.render(
                    f'{all_exercises[5][0]}+{all_exercises[5][1]}', 0, WHITE)
                POS_TASK_1 = TASK_1.get_rect()
                POS_TASK_1.center = (WIDTH//2, HEIGHT//100*8)
                WIN.blit(TASK_1, POS_TASK_1)

                move_tunnels()

                POS_TUNNEL_EQUALS_5_0[0] -= speed*acceleration
                POS_TUNNEL_EQUALS_5_1[0] -= speed*acceleration
                POS_TUNNEL_EQUALS_5_2[0] -= speed*acceleration

                if CAR_RIGHT-6 <= POS_TUNNEL_1_0[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_5_0 == False and ROAD_LANES == 0 and COLLISION == False:
                    COLLISION = True
                    lives -= 1
                    car_hits()
                    equals_reset_5()
                elif CAR_RIGHT-6 <= POS_TUNNEL_1_0[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_5_0 == True and ROAD_LANES == 0 and COLLISION == False:
                    COLLISION = True
                    gate_sound()
                    score += score_limit
                if CAR_RIGHT-6 <= POS_TUNNEL_1_1[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_5_1 == False and ROAD_LANES == 1 and COLLISION == False:
                    COLLISION = True
                    lives -= 1
                    car_hits()
                    equals_reset_5()
                elif CAR_RIGHT-6 <= POS_TUNNEL_1_1[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_5_1 == True and ROAD_LANES == 1 and COLLISION == False:
                    COLLISION = True
                    gate_sound()
                    score += score_limit
                if CAR_RIGHT-6 <= POS_TUNNEL_1_2[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_5_2 == False and ROAD_LANES == 2 and COLLISION == False:
                    COLLISION = True
                    lives -= 1
                    car_hits()
                    equals_reset_5()
                elif CAR_RIGHT-6 <= POS_TUNNEL_1_2[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_5_2 == True and ROAD_LANES == 2 and COLLISION == False:
                    COLLISION = True
                    gate_sound()
                    score += score_limit

                # print(f'{POS_TUNNEL_1_0[0]} {CAR_RIGHT} {score}')

            if 43000 < NEW_TIMER < 45000:
                COLLISION = False

                equals_reset_5()

                reset_tunnels()

                POS_TUNNEL_EQUALS_6_0[0] = ST_OFFSET_ANSWER+35
                POS_TUNNEL_EQUALS_6_1[0] = ST_OFFSET_ANSWER+35
                POS_TUNNEL_EQUALS_6_2[0] = ST_OFFSET_ANSWER+35

            if 45000 < NEW_TIMER < 50000:
                TASK_1 = FONT.render(
                    f'{all_exercises[6][0]}+{all_exercises[6][1]}', 0, WHITE)
                POS_TASK_1 = TASK_1.get_rect()
                POS_TASK_1.center = (WIDTH//2, HEIGHT//100*8)
                WIN.blit(TASK_1, POS_TASK_1)

                move_tunnels()

                POS_TUNNEL_EQUALS_6_0[0] -= speed*acceleration
                POS_TUNNEL_EQUALS_6_1[0] -= speed*acceleration
                POS_TUNNEL_EQUALS_6_2[0] -= speed*acceleration

                if CAR_RIGHT-6 <= POS_TUNNEL_1_0[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_6_0 == False and ROAD_LANES == 0 and COLLISION == False:
                    COLLISION = True
                    lives -= 1
                    car_hits()
                    equals_reset_6()
                elif CAR_RIGHT-6 <= POS_TUNNEL_1_0[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_6_0 == True and ROAD_LANES == 0 and COLLISION == False:
                    COLLISION = True
                    gate_sound()
                    score += score_limit
                if CAR_RIGHT-6 <= POS_TUNNEL_1_1[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_6_1 == False and ROAD_LANES == 1 and COLLISION == False:
                    COLLISION = True
                    lives -= 1
                    car_hits()
                    equals_reset_6()
                elif CAR_RIGHT-6 <= POS_TUNNEL_1_1[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_6_1 == True and ROAD_LANES == 1 and COLLISION == False:
                    COLLISION = True
                    gate_sound()
                    score += score_limit
                if CAR_RIGHT-6 <= POS_TUNNEL_1_2[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_6_2 == False and ROAD_LANES == 2 and COLLISION == False:
                    COLLISION = True
                    lives -= 1
                    car_hits()
                    equals_reset_6()
                elif CAR_RIGHT-6 <= POS_TUNNEL_1_2[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_6_2 == True and ROAD_LANES == 2 and COLLISION == False:
                    COLLISION = True
                    gate_sound()
                    score += score_limit

                # print(f'{POS_TUNNEL_1_0[0]} {CAR_RIGHT} {score}')

            if 50000 < NEW_TIMER < 52000:
                COLLISION = False

                equals_reset_6()

                reset_tunnels()

                POS_TUNNEL_EQUALS_7_0[0] = ST_OFFSET_ANSWER+35
                POS_TUNNEL_EQUALS_7_1[0] = ST_OFFSET_ANSWER+35
                POS_TUNNEL_EQUALS_7_2[0] = ST_OFFSET_ANSWER+35

            if 52000 < NEW_TIMER < 57000:
                TASK_1 = FONT.render(
                    f'{all_exercises[7][0]}+{all_exercises[7][1]}', 0, WHITE)
                POS_TASK_1 = TASK_1.get_rect()
                POS_TASK_1.center = (WIDTH//2, HEIGHT//100*8)
                WIN.blit(TASK_1, POS_TASK_1)

                move_tunnels()

                POS_TUNNEL_EQUALS_7_0[0] -= speed*acceleration
                POS_TUNNEL_EQUALS_7_1[0] -= speed*acceleration
                POS_TUNNEL_EQUALS_7_2[0] -= speed*acceleration

                if CAR_RIGHT-6 <= POS_TUNNEL_1_0[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_7_0 == False and ROAD_LANES == 0 and COLLISION == False:
                    COLLISION = True
                    lives -= 1
                    car_hits()
                    equals_reset_7()
                elif CAR_RIGHT-6 <= POS_TUNNEL_1_0[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_7_0 == True and ROAD_LANES == 0 and COLLISION == False:
                    COLLISION = True
                    gate_sound()
                    score += score_limit
                if CAR_RIGHT-6 <= POS_TUNNEL_1_1[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_7_1 == False and ROAD_LANES == 1 and COLLISION == False:
                    COLLISION = True
                    lives -= 1
                    car_hits()
                    equals_reset_7()
                elif CAR_RIGHT-6 <= POS_TUNNEL_1_1[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_7_1 == True and ROAD_LANES == 1 and COLLISION == False:
                    COLLISION = True
                    gate_sound()
                    score += score_limit
                if CAR_RIGHT-6 <= POS_TUNNEL_1_2[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_7_2 == False and ROAD_LANES == 2 and COLLISION == False:
                    COLLISION = True
                    lives -= 1
                    car_hits()
                    equals_reset_7()
                elif CAR_RIGHT-6 <= POS_TUNNEL_1_2[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_7_2 == True and ROAD_LANES == 2 and COLLISION == False:
                    COLLISION = True
                    gate_sound()
                    score += score_limit

                # print(f'{POS_TUNNEL_1_0[0]} {CAR_RIGHT} {score}')

            if 57000 < NEW_TIMER < 59000:
                COLLISION = False

                equals_reset_7()

                reset_tunnels()

                POS_TUNNEL_EQUALS_8_0[0] = ST_OFFSET_ANSWER+35
                POS_TUNNEL_EQUALS_8_1[0] = ST_OFFSET_ANSWER+35
                POS_TUNNEL_EQUALS_8_2[0] = ST_OFFSET_ANSWER+35

            if 59000 < NEW_TIMER < 64000:
                TASK_1 = FONT.render(
                    f'{all_exercises[8][0]}+{all_exercises[8][1]}', 0, WHITE)
                POS_TASK_1 = TASK_1.get_rect()
                POS_TASK_1.center = (WIDTH//2, HEIGHT//100*8)
                WIN.blit(TASK_1, POS_TASK_1)

                move_tunnels()

                POS_TUNNEL_EQUALS_8_0[0] -= speed*acceleration
                POS_TUNNEL_EQUALS_8_1[0] -= speed*acceleration
                POS_TUNNEL_EQUALS_8_2[0] -= speed*acceleration

                if CAR_RIGHT-6 <= POS_TUNNEL_1_0[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_8_0 == False and ROAD_LANES == 0 and COLLISION == False:
                    COLLISION = True
                    lives -= 1
                    car_hits()
                    equals_reset_8()
                elif CAR_RIGHT-6 <= POS_TUNNEL_1_0[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_8_0 == True and ROAD_LANES == 0 and COLLISION == False:
                    COLLISION = True
                    gate_sound()
                    score += score_limit
                if CAR_RIGHT-6 <= POS_TUNNEL_1_1[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_8_1 == False and ROAD_LANES == 1 and COLLISION == False:
                    COLLISION = True
                    lives -= 1
                    car_hits()
                    equals_reset_8()
                elif CAR_RIGHT-6 <= POS_TUNNEL_1_1[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_8_1 == True and ROAD_LANES == 1 and COLLISION == False:
                    COLLISION = True
                    gate_sound()
                    score += score_limit
                if CAR_RIGHT-6 <= POS_TUNNEL_1_2[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_8_2 == False and ROAD_LANES == 2 and COLLISION == False:
                    COLLISION = True
                    lives -= 1
                    car_hits()
                    equals_reset_8()
                elif CAR_RIGHT-6 <= POS_TUNNEL_1_2[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_8_2 == True and ROAD_LANES == 2 and COLLISION == False:
                    COLLISION = True
                    gate_sound()
                    score += score_limit

                # print(f'{POS_TUNNEL_1_0[0]} {CAR_RIGHT} {score}')

            if 64000 < NEW_TIMER < 66000:
                COLLISION = False

                equals_reset_8()

                reset_tunnels()

                POS_TUNNEL_EQUALS_9_0[0] = ST_OFFSET_ANSWER+35
                POS_TUNNEL_EQUALS_9_1[0] = ST_OFFSET_ANSWER+35
                POS_TUNNEL_EQUALS_9_2[0] = ST_OFFSET_ANSWER+35

            if 66000 < NEW_TIMER < 71000:
                TASK_1 = FONT.render(
                    f'{all_exercises[9][0]}+{all_exercises[9][1]}', 0, WHITE)
                POS_TASK_1 = TASK_1.get_rect()
                POS_TASK_1.center = (WIDTH//2, HEIGHT//100*8)
                WIN.blit(TASK_1, POS_TASK_1)

                move_tunnels()

                POS_TUNNEL_EQUALS_9_0[0] -= speed*acceleration
                POS_TUNNEL_EQUALS_9_1[0] -= speed*acceleration
                POS_TUNNEL_EQUALS_9_2[0] -= speed*acceleration

                if CAR_RIGHT-6 <= POS_TUNNEL_1_0[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_9_0 == False and ROAD_LANES == 0 and COLLISION == False:
                    COLLISION = True
                    lives -= 1
                    car_hits()
                    equals_reset_9()
                elif CAR_RIGHT-6 <= POS_TUNNEL_1_0[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_9_0 == True and ROAD_LANES == 0 and COLLISION == False:
                    COLLISION = True
                    gate_sound()
                    score += score_limit
                if CAR_RIGHT-6 <= POS_TUNNEL_1_1[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_9_1 == False and ROAD_LANES == 1 and COLLISION == False:
                    COLLISION = True
                    lives -= 1
                    car_hits()
                    equals_reset_9()
                elif CAR_RIGHT-6 <= POS_TUNNEL_1_1[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_9_1 == True and ROAD_LANES == 1 and COLLISION == False:
                    COLLISION = True
                    gate_sound()
                    score += score_limit
                if CAR_RIGHT-6 <= POS_TUNNEL_1_2[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_9_2 == False and ROAD_LANES == 2 and COLLISION == False:
                    COLLISION = True
                    lives -= 1
                    car_hits()
                    equals_reset_9()
                elif CAR_RIGHT-6 <= POS_TUNNEL_1_2[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_9_2 == True and ROAD_LANES == 2 and COLLISION == False:
                    COLLISION = True
                    gate_sound()
                    score += score_limit

                # print(f'{POS_TUNNEL_1_0[0]} {CAR_RIGHT} {score}')

            if 71000 < NEW_TIMER < 73000:
                COLLISION = False

                equals_reset_9()

                reset_tunnels()

            if 73000 < NEW_TIMER:
                if 73001 < NEW_TIMER < 73018:
                    lvl_complete_sound()
                WIN_CONDITION = True
                WIN.blit(MAIN_MENU_BACK, POS_BACK)
                GAME_OVER = FONT.render(f'ПОБЕДА!', 0, WHITE)
                POS_GAME_OVER = GAME_OVER.get_rect(center=(WIDTH//2, HEIGHT//2-100))
                GAME_OVER_SCORE = FONT.render(f'ВАШ СЧЕТ: {score}', 0, WHITE)
                POS_GAME_OVER_SCORE = GAME_OVER_SCORE.get_rect(center=(WIDTH//2, HEIGHT//2))
                GAME_OVER_PRESS_ESC = FONT_SCORE.render(f'След уровень: ENTER', 0, WHITE)
                POS_GAME_OVER_PRESS_ESC = GAME_OVER_PRESS_ESC.get_rect(center=(WIDTH//2, HEIGHT//100*70))
                WIN.blit(GAME_OVER, POS_GAME_OVER)
                WIN.blit(GAME_OVER_SCORE, POS_GAME_OVER_SCORE)
                WIN.blit(GAME_OVER_PRESS_ESC, POS_GAME_OVER_PRESS_ESC)

        if lives != 0:
            SCORE_0 = FONT_SCORE.render(f'{score}', 0, WHITE)
            POS_SCORE_0 = SCORE_0.get_rect(
                center=(WIDTH//100*92, HEIGHT//100*99+30))
            WIN.blit(SCORE_0, POS_SCORE_0)
        # FPS_DEBUG
        #    FPS_DRAW_0 = FONT_FPS.render(f'NEW_TIMER: {NEW_TIMER}', 0, WHITE)
        #    POS_FPS_DRAW_0 = FPS_DRAW_0.get_rect(center=(164, 746))
        #    WIN.blit(FPS_DRAW_0, POS_FPS_DRAW_0)
        #    FPS_DRAW_1 = FONT_FPS.render(f'current_time: {current_time}', 0, WHITE)
        #    POS_FPS_DRAW_1 = FPS_DRAW_1.get_rect(center=(150, 760))
        #    WIN.blit(FPS_DRAW_1, POS_FPS_DRAW_1)
        else:
            if GAME_OVER_SOUND_FLAG == False:
                game_over_sound()
                GAME_OVER_SOUND_FLAG = True
            WIN.blit(MAIN_MENU_BACK, POS_BACK)
            GAME_OVER = FONT.render(f'GAME OVER', 0, WHITE)
            POS_GAME_OVER = GAME_OVER.get_rect(center=(WIDTH//2, HEIGHT//2-100))
            GAME_OVER_SCORE = FONT.render(f'ВАШ СЧЕТ: {score}', 0, WHITE)
            POS_GAME_OVER_SCORE = GAME_OVER_SCORE.get_rect(center=(WIDTH//2, HEIGHT//2))
            GAME_OVER_PRESS_ESC = FONT_SCORE.render(f'МЕНЮ: ESC', 0, WHITE)
            POS_GAME_OVER_PRESS_ESC = GAME_OVER_PRESS_ESC.get_rect(center=(WIDTH//2, HEIGHT//100*70))
            WIN.blit(GAME_OVER, POS_GAME_OVER)
            WIN.blit(GAME_OVER_SCORE, POS_GAME_OVER_SCORE)
            WIN.blit(GAME_OVER_PRESS_ESC, POS_GAME_OVER_PRESS_ESC)

        if game_is_on:
            pygame.display.flip()
            current_time = pygame.time.get_ticks()
            NEW_TIMER += 17
            pygame.mixer.music.unpause()
        else:
            current_time = current_time
            NEW_TIMER = NEW_TIMER
            pygame.mixer.music.pause() 

        clock.tick(FPS)
        
        


def lvl2():

    lvl2_music()

    BG = pygame.image.load('img/lvl2/sunset.png')
    POS_BG = BG.get_rect(center=(WIDTH//2, HEIGHT//2))

    MOUNTAINS = pygame.image.load('img/lvl2/sunset.png').convert_alpha()
    POS_MOUNTAINS = MOUNTAINS.get_rect(center=(WIDTH//2, HEIGHT//2))

    ROAD = pygame.image.load('img/lvl2/road.png').convert_alpha()

    CAR = pygame.image.load('img/lvl2/car.png').convert_alpha()
    CAR_WIDTH = CAR.get_width()
    POS_CAR = CAR.get_rect()
    POS_CAR.center = WIDTH//100*20, HEIGHT//100*65
    CAR_RIGHT = POS_CAR[0]+CAR_WIDTH

    CAR_W = pygame.image.load('img/lvl2/car_w.png').convert_alpha()
    CAR_W_WIDTH = CAR_W.get_width()
    POS_CAR_W = CAR_W.get_rect()
    POS_CAR_W.center = WIDTH//100*20, HEIGHT//100*65
    CAR_W_RIGHT = POS_CAR_W[0]+CAR_W_WIDTH

    CAR_2 = pygame.image.load('img/lvl2/car_crashed_1.png').convert_alpha()
    CAR_2_WIDTH = CAR_2.get_width()
    POS_CAR_2 = CAR_2.get_rect()
    POS_CAR_2.center = WIDTH//100*20, HEIGHT//100*65
    CAR_2_RIGHT = POS_CAR_2[0]+CAR_2_WIDTH

    CAR_2_W = pygame.image.load('img/lvl2/car_crashed_1_w.png').convert_alpha()
    CAR_2_W_WIDTH = CAR_2_W.get_width()
    POS_CAR_2_W = CAR_2_W.get_rect()
    POS_CAR_2_W.center = WIDTH//100*20, HEIGHT//100*65
    CAR_2_W_RIGHT = POS_CAR_2_W[0]+CAR_2_W_WIDTH

    CAR_3 = pygame.image.load('img/lvl2/car_crashed_2.png').convert_alpha()
    CAR_3_WIDTH = CAR_3.get_width()
    POS_CAR_3 = CAR_3.get_rect()
    POS_CAR_3.center = WIDTH//100*20, HEIGHT//100*65
    CAR_3_RIGHT = POS_CAR_3[0]+CAR_3_WIDTH

    CAR_3_W = pygame.image.load('img/lvl2/car_crashed_2_w.png').convert_alpha()
    CAR_3_W_WIDTH = CAR_3_W.get_width()
    POS_CAR_3_W = CAR_3_W.get_rect()
    POS_CAR_3_W.center = WIDTH//100*20, HEIGHT//100*65
    CAR_3_W_RIGHT = POS_CAR_3_W[0]+CAR_3_W_WIDTH

    CAR_4 = pygame.image.load('img/lvl2/car_crashed_3.png').convert_alpha()
    CAR_4_WIDTH = CAR_4.get_width()
    POS_CAR_4 = CAR_4.get_rect()
    POS_CAR_4.center = WIDTH//100*20, HEIGHT//100*65
    CAR_4_RIGHT = POS_CAR_4[0]+CAR_4_WIDTH

    TASK = pygame.image.load('img/lvl2/task.png').convert_alpha()
    POS_TASK = TASK.get_rect(center=(WIDTH//2, HEIGHT//100*8))
    SCORE = pygame.image.load('img/lvl2/score.png').convert_alpha()
    POS_SCORE = SCORE.get_rect(center=(WIDTH//100*92, HEIGHT//100*99+30))
    PAUSE = pygame.image.load('img/lvl2/pause.png').convert_alpha()
    POS_PAUSE = PAUSE.get_rect(center=(WIDTH//100*92, HEIGHT//100*6))

    ST_OFFSET_TUNNEL_0 = WIDTH+100
    ST_OFFSET_TUNNEL_1 = WIDTH+98+100
    ST_OFFSET_ANSWER = WIDTH+180

    TUNNEL_0 = pygame.image.load('img/lvl2/tunnel_0.png').convert_alpha()
    POS_TUNNEL_0_0 = TUNNEL_0.get_rect()
    POS_TUNNEL_0_0.center = ST_OFFSET_TUNNEL_0, HEIGHT//100*52
    POS_TUNNEL_0_1 = TUNNEL_0.get_rect()
    POS_TUNNEL_0_1.center = ST_OFFSET_TUNNEL_0, HEIGHT//100*72
    POS_TUNNEL_0_2 = TUNNEL_0.get_rect()
    POS_TUNNEL_0_2.center = ST_OFFSET_TUNNEL_0, HEIGHT//100*95

    TUNNEL_1 = pygame.image.load('img/lvl2/tunnel_1.png').convert_alpha()
    POS_TUNNEL_1_0 = TUNNEL_1.get_rect()
    POS_TUNNEL_1_0.center = ST_OFFSET_TUNNEL_1, HEIGHT//100*52
    POS_TUNNEL_1_1 = TUNNEL_1.get_rect()
    POS_TUNNEL_1_1.center = ST_OFFSET_TUNNEL_1, HEIGHT//100*72
    POS_TUNNEL_1_2 = TUNNEL_1.get_rect()
    POS_TUNNEL_1_2.center = ST_OFFSET_TUNNEL_1, HEIGHT//100*95

    run_lvl = True
    clock = pygame.time.Clock()
    i = 0
    exercises = 10
    FPS = 60
    NEW_TIMER = 0
    ROAD_LANES = 1
    lives = 3
    score = 0
    score_limit = 1
    COLLISION = False
    COLLISION_PAUSE = 1000
    game_is_on = True
    current_time = 0
    speed = 8
    acceleration = 1.0
    GAME_OVER_SOUND_FLAG = False
    CAR_HIT_SOUND_FLAG = False
    CAR_HIT_2_SOUND_FLAG = False
    WIN_CONDITION = False
    pressed = pygame.key.get_pressed()

    all_exercises, all_answers, all_answer_flag, all_answer_flags_last = [], [], [], []

    for exercise in range(10):
        first_sum = random.randint(50, 98)
        second_sum = random.randint(1, 49)

        sum_true = first_sum - second_sum

        if sum_true > 89:
            sum_fake_1 = sum_true + random.randint(-10, 1)
            sum_fake_2 = sum_true + random.randint(-10, 1)
        elif sum_true < 11:
            sum_fake_1 = sum_true + random.randint(1, 10)
            sum_fake_2 = sum_true + random.randint(1, 10)
        else:
            sum_fake_1 = sum_true + random.randint(-10, 10)
            sum_fake_2 = sum_true + random.randint(-10, 10)
            
        if sum_true == sum_fake_1 or sum_true == sum_fake_2 or sum_fake_1 == sum_fake_2:
            # print(f'{sum_true} {sum_fake_1} {sum_fake_2}')

            if sum_true == sum_fake_1:
                sum_fake_1 += 1
            if sum_true == sum_fake_2:
                sum_fake_2 += 2
            if sum_fake_1 == sum_fake_2:
                sum_fake_1 += 1
                sum_fake_2 -= 2
            
            # print(f'{sum_true} {sum_fake_1} {sum_fake_2}')
        
        # if sum_true == sum_fake_1 or sum_true
        all_exercises.append([first_sum, second_sum, sum_true, sum_fake_1, sum_fake_2])
        all_answers.append([sum_true, sum_fake_1, sum_fake_2])


    print(all_exercises)
    # print(all_answers)

    for all_answer in all_answers:
        new_answers = all_answer
        random.shuffle(new_answers)

    # print(all_answers)

    jj = 0

    for all_answer in all_answers:
        for a_a in all_answer:
            kk = math.floor(jj/3)
            jj += 1
            if a_a == all_exercises[kk][2]:
                all_answer_flag.append(True)
            else:
                all_answer_flag.append(False)
            # print(f'{kk} {a_a} {all_exercises[kk][2]}')
    # print(all_answer_flag)

    TUNNEL_EQUALS_0_0 = FONT.render(f'{all_answers[0][0]}', 0, WHITE)
    POS_TUNNEL_EQUALS_0_0 = TUNNEL_EQUALS_0_0.get_rect()
    POS_TUNNEL_EQUALS_0_0.center = ST_OFFSET_ANSWER, HEIGHT//100*52
    TUNNEL_LOGIC_0_0 = all_answer_flag[0]

    TUNNEL_EQUALS_0_1 = FONT.render(f'{all_answers[0][1]}', 0, WHITE)
    POS_TUNNEL_EQUALS_0_1 = TUNNEL_EQUALS_0_1.get_rect()
    POS_TUNNEL_EQUALS_0_1.center = ST_OFFSET_ANSWER, HEIGHT//100*72
    TUNNEL_LOGIC_0_1 = all_answer_flag[1]

    TUNNEL_EQUALS_0_2 = FONT.render(f'{all_answers[0][2]}', 0, WHITE)
    POS_TUNNEL_EQUALS_0_2 = TUNNEL_EQUALS_0_2.get_rect()
    POS_TUNNEL_EQUALS_0_2.center = ST_OFFSET_ANSWER, HEIGHT//100*92
    TUNNEL_LOGIC_0_2 = all_answer_flag[2]

    TUNNEL_EQUALS_1_0 = FONT.render(f'{all_answers[1][0]}', 0, WHITE)
    POS_TUNNEL_EQUALS_1_0 = TUNNEL_EQUALS_1_0.get_rect()
    POS_TUNNEL_EQUALS_1_0.center = ST_OFFSET_ANSWER, HEIGHT//100*52
    TUNNEL_LOGIC_1_0 = all_answer_flag[3]

    TUNNEL_EQUALS_1_1 = FONT.render(f'{all_answers[1][1]}', 0, WHITE)
    POS_TUNNEL_EQUALS_1_1 = TUNNEL_EQUALS_1_1.get_rect()
    POS_TUNNEL_EQUALS_1_1.center = ST_OFFSET_ANSWER, HEIGHT//100*72
    TUNNEL_LOGIC_1_1 = all_answer_flag[4]

    TUNNEL_EQUALS_1_2 = FONT.render(f'{all_answers[1][2]}', 0, WHITE)
    POS_TUNNEL_EQUALS_1_2 = TUNNEL_EQUALS_1_2.get_rect()
    POS_TUNNEL_EQUALS_1_2.center = ST_OFFSET_ANSWER, HEIGHT//100*92
    TUNNEL_LOGIC_1_2 = all_answer_flag[5]

    TUNNEL_EQUALS_2_0 = FONT.render(f'{all_answers[2][0]}', 0, WHITE)
    POS_TUNNEL_EQUALS_2_0 = TUNNEL_EQUALS_2_0.get_rect()
    POS_TUNNEL_EQUALS_2_0.center = ST_OFFSET_ANSWER, HEIGHT//100*52
    TUNNEL_LOGIC_2_0 = all_answer_flag[6]

    TUNNEL_EQUALS_2_1 = FONT.render(f'{all_answers[2][1]}', 0, WHITE)
    POS_TUNNEL_EQUALS_2_1 = TUNNEL_EQUALS_2_1.get_rect()
    POS_TUNNEL_EQUALS_2_1.center = ST_OFFSET_ANSWER, HEIGHT//100*72
    TUNNEL_LOGIC_2_1 = all_answer_flag[7]

    TUNNEL_EQUALS_2_2 = FONT.render(f'{all_answers[2][2]}', 0, WHITE)
    POS_TUNNEL_EQUALS_2_2 = TUNNEL_EQUALS_2_2.get_rect()
    POS_TUNNEL_EQUALS_2_2.center = ST_OFFSET_ANSWER, HEIGHT//100*92
    TUNNEL_LOGIC_2_2 = all_answer_flag[8]

    TUNNEL_EQUALS_3_0 = FONT.render(f'{all_answers[3][0]}', 0, WHITE)
    POS_TUNNEL_EQUALS_3_0 = TUNNEL_EQUALS_3_0.get_rect()
    POS_TUNNEL_EQUALS_3_0.center = ST_OFFSET_ANSWER, HEIGHT//100*52
    TUNNEL_LOGIC_3_0 = all_answer_flag[9]

    TUNNEL_EQUALS_3_1 = FONT.render(f'{all_answers[3][1]}', 0, WHITE)
    POS_TUNNEL_EQUALS_3_1 = TUNNEL_EQUALS_3_1.get_rect()
    POS_TUNNEL_EQUALS_3_1.center = ST_OFFSET_ANSWER, HEIGHT//100*72
    TUNNEL_LOGIC_3_1 = all_answer_flag[10]

    TUNNEL_EQUALS_3_2 = FONT.render(f'{all_answers[3][2]}', 0, WHITE)
    POS_TUNNEL_EQUALS_3_2 = TUNNEL_EQUALS_3_2.get_rect()
    POS_TUNNEL_EQUALS_3_2.center = ST_OFFSET_ANSWER, HEIGHT//100*92
    TUNNEL_LOGIC_3_2 = all_answer_flag[11]

    TUNNEL_EQUALS_4_0 = FONT.render(f'{all_answers[4][0]}', 0, WHITE)
    POS_TUNNEL_EQUALS_4_0 = TUNNEL_EQUALS_4_0.get_rect()
    POS_TUNNEL_EQUALS_4_0.center = ST_OFFSET_ANSWER, HEIGHT//100*52
    TUNNEL_LOGIC_4_0 = all_answer_flag[12]

    TUNNEL_EQUALS_4_1 = FONT.render(f'{all_answers[4][1]}', 0, WHITE)
    POS_TUNNEL_EQUALS_4_1 = TUNNEL_EQUALS_4_1.get_rect()
    POS_TUNNEL_EQUALS_4_1.center = ST_OFFSET_ANSWER, HEIGHT//100*72
    TUNNEL_LOGIC_4_1 = all_answer_flag[13]

    TUNNEL_EQUALS_4_2 = FONT.render(f'{all_answers[4][2]}', 0, WHITE)
    POS_TUNNEL_EQUALS_4_2 = TUNNEL_EQUALS_4_2.get_rect()
    POS_TUNNEL_EQUALS_4_2.center = ST_OFFSET_ANSWER, HEIGHT//100*92
    TUNNEL_LOGIC_4_2 = all_answer_flag[14]

    TUNNEL_EQUALS_5_0 = FONT.render(f'{all_answers[5][0]}', 0, WHITE)
    POS_TUNNEL_EQUALS_5_0 = TUNNEL_EQUALS_5_0.get_rect()
    POS_TUNNEL_EQUALS_5_0.center = ST_OFFSET_ANSWER, HEIGHT//100*52
    TUNNEL_LOGIC_5_0 = all_answer_flag[15]

    TUNNEL_EQUALS_5_1 = FONT.render(f'{all_answers[5][1]}', 0, WHITE)
    POS_TUNNEL_EQUALS_5_1 = TUNNEL_EQUALS_5_1.get_rect()
    POS_TUNNEL_EQUALS_5_1.center = ST_OFFSET_ANSWER, HEIGHT//100*72
    TUNNEL_LOGIC_5_1 = all_answer_flag[16]

    TUNNEL_EQUALS_5_2 = FONT.render(f'{all_answers[5][2]}', 0, WHITE)
    POS_TUNNEL_EQUALS_5_2 = TUNNEL_EQUALS_5_2.get_rect()
    POS_TUNNEL_EQUALS_5_2.center = ST_OFFSET_ANSWER, HEIGHT//100*92
    TUNNEL_LOGIC_5_2 = all_answer_flag[17]

    TUNNEL_EQUALS_6_0 = FONT.render(f'{all_answers[6][0]}', 0, WHITE)
    POS_TUNNEL_EQUALS_6_0 = TUNNEL_EQUALS_6_0.get_rect()
    POS_TUNNEL_EQUALS_6_0.center = ST_OFFSET_ANSWER, HEIGHT//100*52
    TUNNEL_LOGIC_6_0 = all_answer_flag[18]

    TUNNEL_EQUALS_6_1 = FONT.render(f'{all_answers[6][1]}', 0, WHITE)
    POS_TUNNEL_EQUALS_6_1 = TUNNEL_EQUALS_6_1.get_rect()
    POS_TUNNEL_EQUALS_6_1.center = ST_OFFSET_ANSWER, HEIGHT//100*72
    TUNNEL_LOGIC_6_1 = all_answer_flag[19]

    TUNNEL_EQUALS_6_2 = FONT.render(f'{all_answers[6][2]}', 0, WHITE)
    POS_TUNNEL_EQUALS_6_2 = TUNNEL_EQUALS_6_2.get_rect()
    POS_TUNNEL_EQUALS_6_2.center = ST_OFFSET_ANSWER, HEIGHT//100*92
    TUNNEL_LOGIC_6_2 = all_answer_flag[20]

    TUNNEL_EQUALS_7_0 = FONT.render(f'{all_answers[7][0]}', 0, WHITE)
    POS_TUNNEL_EQUALS_7_0 = TUNNEL_EQUALS_7_0.get_rect()
    POS_TUNNEL_EQUALS_7_0.center = ST_OFFSET_ANSWER, HEIGHT//100*52
    TUNNEL_LOGIC_7_0 = all_answer_flag[21]

    TUNNEL_EQUALS_7_1 = FONT.render(f'{all_answers[7][1]}', 0, WHITE)
    POS_TUNNEL_EQUALS_7_1 = TUNNEL_EQUALS_7_1.get_rect()
    POS_TUNNEL_EQUALS_7_1.center = ST_OFFSET_ANSWER, HEIGHT//100*72
    TUNNEL_LOGIC_7_1 = all_answer_flag[22]

    TUNNEL_EQUALS_7_2 = FONT.render(f'{all_answers[7][2]}', 0, WHITE)
    POS_TUNNEL_EQUALS_7_2 = TUNNEL_EQUALS_7_2.get_rect()
    POS_TUNNEL_EQUALS_7_2.center = ST_OFFSET_ANSWER, HEIGHT//100*92
    TUNNEL_LOGIC_7_2 = all_answer_flag[23]

    TUNNEL_EQUALS_8_0 = FONT.render(f'{all_answers[8][0]}', 0, WHITE)
    POS_TUNNEL_EQUALS_8_0 = TUNNEL_EQUALS_8_0.get_rect()
    POS_TUNNEL_EQUALS_8_0.center = ST_OFFSET_ANSWER, HEIGHT//100*52
    TUNNEL_LOGIC_8_0 = all_answer_flag[24]

    TUNNEL_EQUALS_8_1 = FONT.render(f'{all_answers[8][1]}', 0, WHITE)
    POS_TUNNEL_EQUALS_8_1 = TUNNEL_EQUALS_8_1.get_rect()
    POS_TUNNEL_EQUALS_8_1.center = ST_OFFSET_ANSWER, HEIGHT//100*72
    TUNNEL_LOGIC_8_1 = all_answer_flag[25]

    TUNNEL_EQUALS_8_2 = FONT.render(f'{all_answers[8][2]}', 0, WHITE)
    POS_TUNNEL_EQUALS_8_2 = TUNNEL_EQUALS_8_2.get_rect()
    POS_TUNNEL_EQUALS_8_2.center = ST_OFFSET_ANSWER, HEIGHT//100*92
    TUNNEL_LOGIC_8_2 = all_answer_flag[26]

    TUNNEL_EQUALS_9_0 = FONT.render(f'{all_answers[9][0]}', 0, WHITE)
    POS_TUNNEL_EQUALS_9_0 = TUNNEL_EQUALS_9_0.get_rect()
    POS_TUNNEL_EQUALS_9_0.center = ST_OFFSET_ANSWER, HEIGHT//100*52
    TUNNEL_LOGIC_9_0 = all_answer_flag[27]

    TUNNEL_EQUALS_9_1 = FONT.render(f'{all_answers[9][1]}', 0, WHITE)
    POS_TUNNEL_EQUALS_9_1 = TUNNEL_EQUALS_9_1.get_rect()
    POS_TUNNEL_EQUALS_9_1.center = ST_OFFSET_ANSWER, HEIGHT//100*72
    TUNNEL_LOGIC_9_1 = all_answer_flag[28]

    TUNNEL_EQUALS_9_2 = FONT.render(f'{all_answers[9][2]}', 0, WHITE)
    POS_TUNNEL_EQUALS_9_2 = TUNNEL_EQUALS_9_2.get_rect()
    POS_TUNNEL_EQUALS_9_2.center = ST_OFFSET_ANSWER, HEIGHT//100*92
    TUNNEL_LOGIC_9_2 = all_answer_flag[29]

    def draw_all():
        if lives != 0:
            WIN.blit(BG, POS_BG)
            WIN.blit(MOUNTAINS, POS_MOUNTAINS)
            WIN.blit(ROAD, (i, 0))
            WIN.blit(ROAD, (WIDTH+i, 0))
            # WIN.blit(ROAD, POS_ROAD)
            WIN.blit(TASK, POS_TASK)

            # WIN.blit(HEART, POS_HEART_0)
            # WIN.blit(HEART, POS_HEART_1)
            # WIN.blit(HEART, POS_HEART_2)

            

            WIN.blit(TUNNEL_0, POS_TUNNEL_0_0)
            WIN.blit(TUNNEL_0, POS_TUNNEL_0_1)
            WIN.blit(TUNNEL_0, POS_TUNNEL_0_2)

        ostatok = current_time // 250 % 2

        if lives == 3 and ostatok == 0:
            WIN.blit(CAR, POS_CAR)
        elif lives == 3 and ostatok != 0:
            WIN.blit(CAR_W, (POS_CAR_W[0], POS_CAR_W[1]+2))
        if lives == 2 and ostatok == 0:
            WIN.blit(CAR_2, POS_CAR_2)
        elif lives == 2 and ostatok != 0:
            WIN.blit(CAR_2_W, (POS_CAR_2_W[0], POS_CAR_2_W[1]+2))
        if lives == 1 and ostatok == 0:
            WIN.blit(CAR_3, POS_CAR_3)
        elif lives == 1 and ostatok != 0:
            WIN.blit(CAR_3_W, (POS_CAR_3_W[0], POS_CAR_3_W[1]+2))
        if lives == 0:
            WIN.blit(CAR_4, POS_CAR_4)

        if lives != 0:
            WIN.blit(TUNNEL_1, POS_TUNNEL_1_0)
            WIN.blit(TUNNEL_1, POS_TUNNEL_1_1)
            WIN.blit(TUNNEL_1, POS_TUNNEL_1_2)

            WIN.blit(TUNNEL_EQUALS_0_0, POS_TUNNEL_EQUALS_0_0)
            WIN.blit(TUNNEL_EQUALS_0_1, POS_TUNNEL_EQUALS_0_1)
            WIN.blit(TUNNEL_EQUALS_0_2, POS_TUNNEL_EQUALS_0_2)

            WIN.blit(TUNNEL_EQUALS_1_0, POS_TUNNEL_EQUALS_1_0)
            WIN.blit(TUNNEL_EQUALS_1_1, POS_TUNNEL_EQUALS_1_1)
            WIN.blit(TUNNEL_EQUALS_1_2, POS_TUNNEL_EQUALS_1_2)

            WIN.blit(TUNNEL_EQUALS_2_0, POS_TUNNEL_EQUALS_2_0)
            WIN.blit(TUNNEL_EQUALS_2_1, POS_TUNNEL_EQUALS_2_1)
            WIN.blit(TUNNEL_EQUALS_2_2, POS_TUNNEL_EQUALS_2_2)

            WIN.blit(TUNNEL_EQUALS_3_0, POS_TUNNEL_EQUALS_3_0)
            WIN.blit(TUNNEL_EQUALS_3_1, POS_TUNNEL_EQUALS_3_1)
            WIN.blit(TUNNEL_EQUALS_3_2, POS_TUNNEL_EQUALS_3_2)

            WIN.blit(TUNNEL_EQUALS_4_0, POS_TUNNEL_EQUALS_4_0)
            WIN.blit(TUNNEL_EQUALS_4_1, POS_TUNNEL_EQUALS_4_1)
            WIN.blit(TUNNEL_EQUALS_4_2, POS_TUNNEL_EQUALS_4_2)

            WIN.blit(TUNNEL_EQUALS_5_0, POS_TUNNEL_EQUALS_5_0)
            WIN.blit(TUNNEL_EQUALS_5_1, POS_TUNNEL_EQUALS_5_1)
            WIN.blit(TUNNEL_EQUALS_5_2, POS_TUNNEL_EQUALS_5_2)

            WIN.blit(TUNNEL_EQUALS_6_0, POS_TUNNEL_EQUALS_6_0)
            WIN.blit(TUNNEL_EQUALS_6_1, POS_TUNNEL_EQUALS_6_1)
            WIN.blit(TUNNEL_EQUALS_6_2, POS_TUNNEL_EQUALS_6_2)

            WIN.blit(TUNNEL_EQUALS_7_0, POS_TUNNEL_EQUALS_7_0)
            WIN.blit(TUNNEL_EQUALS_7_1, POS_TUNNEL_EQUALS_7_1)
            WIN.blit(TUNNEL_EQUALS_7_2, POS_TUNNEL_EQUALS_7_2)

            WIN.blit(TUNNEL_EQUALS_8_0, POS_TUNNEL_EQUALS_8_0)
            WIN.blit(TUNNEL_EQUALS_8_1, POS_TUNNEL_EQUALS_8_1)
            WIN.blit(TUNNEL_EQUALS_8_2, POS_TUNNEL_EQUALS_8_2)

            WIN.blit(TUNNEL_EQUALS_9_0, POS_TUNNEL_EQUALS_9_0)
            WIN.blit(TUNNEL_EQUALS_9_1, POS_TUNNEL_EQUALS_9_1)
            WIN.blit(TUNNEL_EQUALS_9_2, POS_TUNNEL_EQUALS_9_2)
        
        WIN.blit(SCORE, POS_SCORE)
        WIN.blit(PAUSE, POS_PAUSE)

    while run_lvl:

        if game_is_on:
            current_time = pygame.time.get_ticks()
            NEW_TIMER += 17
        else:
            current_time = 0
            NEW_TIMER = 0

        def reset_tunnels():
            POS_TUNNEL_0_0[0] = ST_OFFSET_TUNNEL_0+33
            POS_TUNNEL_0_1[0] = ST_OFFSET_TUNNEL_0+33
            POS_TUNNEL_0_2[0] = ST_OFFSET_TUNNEL_0+33

            POS_TUNNEL_1_0[0] = ST_OFFSET_TUNNEL_1
            POS_TUNNEL_1_1[0] = ST_OFFSET_TUNNEL_1
            POS_TUNNEL_1_2[0] = ST_OFFSET_TUNNEL_1

        def move_tunnels():
            POS_TUNNEL_0_0[0] -= speed*acceleration
            POS_TUNNEL_0_1[0] -= speed*acceleration
            POS_TUNNEL_0_2[0] -= speed*acceleration

            POS_TUNNEL_1_0[0] -= speed*acceleration
            POS_TUNNEL_1_1[0] -= speed*acceleration
            POS_TUNNEL_1_2[0] -= speed*acceleration

        def equals_reset_0():
            POS_TUNNEL_EQUALS_0_0[0] = -WIDTH
            POS_TUNNEL_EQUALS_0_1[0] = -WIDTH
            POS_TUNNEL_EQUALS_0_2[0] = -WIDTH

        def equals_reset_1():
            POS_TUNNEL_EQUALS_1_0[0] = -WIDTH
            POS_TUNNEL_EQUALS_1_1[0] = -WIDTH
            POS_TUNNEL_EQUALS_1_2[0] = -WIDTH

        def equals_reset_2():
            POS_TUNNEL_EQUALS_2_0[0] = -WIDTH
            POS_TUNNEL_EQUALS_2_1[0] = -WIDTH
            POS_TUNNEL_EQUALS_2_2[0] = -WIDTH

        def equals_reset_3():
            POS_TUNNEL_EQUALS_3_0[0] = -WIDTH
            POS_TUNNEL_EQUALS_3_1[0] = -WIDTH
            POS_TUNNEL_EQUALS_3_2[0] = -WIDTH

        def equals_reset_4():
            POS_TUNNEL_EQUALS_4_0[0] = -WIDTH
            POS_TUNNEL_EQUALS_4_1[0] = -WIDTH
            POS_TUNNEL_EQUALS_4_2[0] = -WIDTH

        def equals_reset_5():
            POS_TUNNEL_EQUALS_5_0[0] = -WIDTH
            POS_TUNNEL_EQUALS_5_1[0] = -WIDTH
            POS_TUNNEL_EQUALS_5_2[0] = -WIDTH

        def equals_reset_6():
            POS_TUNNEL_EQUALS_6_0[0] = -WIDTH
            POS_TUNNEL_EQUALS_6_1[0] = -WIDTH
            POS_TUNNEL_EQUALS_6_2[0] = -WIDTH

        def equals_reset_7():
            POS_TUNNEL_EQUALS_7_0[0] = -WIDTH
            POS_TUNNEL_EQUALS_7_1[0] = -WIDTH
            POS_TUNNEL_EQUALS_7_2[0] = -WIDTH

        def equals_reset_8():
            POS_TUNNEL_EQUALS_8_0[0] = -WIDTH
            POS_TUNNEL_EQUALS_8_1[0] = -WIDTH
            POS_TUNNEL_EQUALS_8_2[0] = -WIDTH

        def equals_reset_9():
            POS_TUNNEL_EQUALS_9_0[0] = -WIDTH
            POS_TUNNEL_EQUALS_9_1[0] = -WIDTH
            POS_TUNNEL_EQUALS_9_2[0] = -WIDTH

        def car_hits():
            if lives == 2:
                car_hit_sound()
            elif lives == 1:
                car_hit_sound_2()
            if lives > 0:
                pygame.time.wait(COLLISION_PAUSE)
        # print(f'{current_time} {NEW_TIMER}')

        draw_all()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.mixer.music.stop()
                menu_selected_sound()
                run_lvl = False
                NEW_TIMER = 0
                main_menu_music()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    ROAD_LANES += 1
                if event.key == pygame.K_UP:
                    ROAD_LANES -= 1
                if event.key == pygame.K_0:
                    game_is_on = True
                    lives = 3
                    # current_time = pygame.time.get_ticks()
                if event.key == pygame.K_9:
                    game_is_on = False
                    NEW_TIMER = 0

            if (event.type == pygame.KEYDOWN and event.key == K_RIGHT) or (event.type == pygame.KEYUP and event.key == K_LEFT):
                acceleration += 0.5
            if (event.type == pygame.KEYDOWN and event.key == K_LEFT) or (event.type == pygame.KEYUP and event.key == K_RIGHT):
                acceleration -= 0.5
            if event.type == pygame.KEYDOWN and event.key == K_RETURN and WIN_CONDITION:
                run_lvl = False
                lvl3()

        if lives == 3:
            WIN.blit(HEART, POS_HEART)
            WIN.blit(HEART, (POS_HEART[0]+60, POS_HEART[1]))
            WIN.blit(HEART, (POS_HEART[0]+120, POS_HEART[1]))
        elif lives == 2:
            WIN.blit(HEART, POS_HEART)
            WIN.blit(HEART, (POS_HEART[0]+60, POS_HEART[1]))
        elif lives == 1:
            WIN.blit(HEART, POS_HEART)

        if i <= -WIDTH:
            WIN.blit(ROAD, (i+WIDTH, 0))
            i = 0
        i -= speed*acceleration

        if ROAD_LANES == 0:
            POS_CAR[1] = HEIGHT//100*43
            POS_CAR_W[1] = HEIGHT//100*43
            POS_CAR_2[1] = HEIGHT//100*43
            POS_CAR_2_W[1] = HEIGHT//100*43
            POS_CAR_3[1] = HEIGHT//100*43
            POS_CAR_3_W[1] = HEIGHT//100*43
            POS_CAR_4[1] = HEIGHT//100*43
            # print(ROAD_LANES)
        elif ROAD_LANES == 1:
            POS_CAR[1] = HEIGHT//100*63
            POS_CAR_W[1] = HEIGHT//100*63
            POS_CAR_2[1] = HEIGHT//100*63
            POS_CAR_2_W[1] = HEIGHT//100*63
            POS_CAR_3[1] = HEIGHT//100*63
            POS_CAR_3_W[1] = HEIGHT//100*63
            POS_CAR_4[1] = HEIGHT//100*63
            # print(ROAD_LANES)
        elif ROAD_LANES == 2:
            POS_CAR[1] = HEIGHT//100*83
            POS_CAR_W[1] = HEIGHT//100*83
            POS_CAR_2[1] = HEIGHT//100*83
            POS_CAR_2_W[1] = HEIGHT//100*83
            POS_CAR_3[1] = HEIGHT//100*83
            POS_CAR_3_W[1] = HEIGHT//100*83
            POS_CAR_4[1] = HEIGHT//100*83
            # print(ROAD_LANES)
        elif ROAD_LANES > 2:
            ROAD_LANES = 2
        elif ROAD_LANES < 0:
            ROAD_LANES = 0

        if lives != 0:
            if 0 < NEW_TIMER < 3000:
                COLLISION = False

                equals_reset_0()

                reset_tunnels()

                POS_TUNNEL_EQUALS_0_0[0] = ST_OFFSET_ANSWER+35
                POS_TUNNEL_EQUALS_0_1[0] = ST_OFFSET_ANSWER+35
                POS_TUNNEL_EQUALS_0_2[0] = ST_OFFSET_ANSWER+35

            if 3000 < NEW_TIMER < 8000:
                TASK_1 = FONT.render(
                    f'{all_exercises[0][0]}-{all_exercises[0][1]}', 0, WHITE)
                POS_TASK_1 = TASK_1.get_rect()
                POS_TASK_1.center = (WIDTH//2, HEIGHT//100*8)
                WIN.blit(TASK_1, POS_TASK_1)

                move_tunnels()

                POS_TUNNEL_EQUALS_0_0[0] -= speed*acceleration
                POS_TUNNEL_EQUALS_0_1[0] -= speed*acceleration
                POS_TUNNEL_EQUALS_0_2[0] -= speed*acceleration

                if CAR_RIGHT-6 <= POS_TUNNEL_1_0[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_0_0 == False and ROAD_LANES == 0 and COLLISION == False:
                    COLLISION = True
                    lives -= 1
                    car_hits()
                    equals_reset_0()
                elif CAR_RIGHT-6 <= POS_TUNNEL_1_0[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_0_0 == True and ROAD_LANES == 0 and COLLISION == False:
                    COLLISION = True
                    gate_sound()
                    score += score_limit
                if CAR_RIGHT-6 <= POS_TUNNEL_1_1[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_0_1 == False and ROAD_LANES == 1 and COLLISION == False:
                    COLLISION = True
                    lives -= 1
                    car_hits()
                    equals_reset_0()
                elif CAR_RIGHT-6 <= POS_TUNNEL_1_1[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_0_1 == True and ROAD_LANES == 1 and COLLISION == False:
                    COLLISION = True
                    gate_sound()
                    score += score_limit
                if CAR_RIGHT-6 <= POS_TUNNEL_1_2[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_0_2 == False and ROAD_LANES == 2 and COLLISION == False:
                    COLLISION = True
                    lives -= 1
                    car_hits()
                    equals_reset_0()
                elif CAR_RIGHT-6 <= POS_TUNNEL_1_2[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_0_2 == True and ROAD_LANES == 2 and COLLISION == False:
                    COLLISION = True
                    gate_sound()
                    score += score_limit

                # print(f'{POS_TUNNEL_1_0[0]} {CAR_RIGHT} {score}')

            if 8000 < NEW_TIMER < 10000:
                COLLISION = False

                equals_reset_0()

                reset_tunnels()

                POS_TUNNEL_EQUALS_1_0[0] = ST_OFFSET_ANSWER+35
                POS_TUNNEL_EQUALS_1_1[0] = ST_OFFSET_ANSWER+35
                POS_TUNNEL_EQUALS_1_2[0] = ST_OFFSET_ANSWER+35

            if 10000 < NEW_TIMER < 15000:
                TASK_1 = FONT.render(
                    f'{all_exercises[1][0]}-{all_exercises[1][1]}', 0, WHITE)
                POS_TASK_1 = TASK_1.get_rect()
                POS_TASK_1.center = (WIDTH//2, HEIGHT//100*8)
                WIN.blit(TASK_1, POS_TASK_1)

                move_tunnels()

                POS_TUNNEL_EQUALS_1_0[0] -= speed*acceleration
                POS_TUNNEL_EQUALS_1_1[0] -= speed*acceleration
                POS_TUNNEL_EQUALS_1_2[0] -= speed*acceleration

                if CAR_RIGHT-6 <= POS_TUNNEL_1_0[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_1_0 == False and ROAD_LANES == 0 and COLLISION == False:
                    COLLISION = True
                    lives -= 1
                    car_hits()
                    equals_reset_1()
                elif CAR_RIGHT-6 <= POS_TUNNEL_1_0[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_1_0 == True and ROAD_LANES == 0 and COLLISION == False:
                    COLLISION = True
                    gate_sound()
                    score += score_limit
                if CAR_RIGHT-6 <= POS_TUNNEL_1_1[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_1_1 == False and ROAD_LANES == 1 and COLLISION == False:
                    COLLISION = True
                    lives -= 1
                    car_hits()
                    equals_reset_1()
                elif CAR_RIGHT-6 <= POS_TUNNEL_1_1[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_1_1 == True and ROAD_LANES == 1 and COLLISION == False:
                    COLLISION = True
                    gate_sound()
                    score += score_limit
                if CAR_RIGHT-6 <= POS_TUNNEL_1_2[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_1_2 == False and ROAD_LANES == 2 and COLLISION == False:
                    COLLISION = True
                    lives -= 1
                    car_hits()
                    equals_reset_1()
                elif CAR_RIGHT-6 <= POS_TUNNEL_1_2[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_1_2 == True and ROAD_LANES == 2 and COLLISION == False:
                    COLLISION = True
                    gate_sound()
                    score += score_limit

                # print(f'{POS_TUNNEL_1_0[0]} {CAR_RIGHT} {score}')

            if 15000 < NEW_TIMER < 17000:
                COLLISION = False

                equals_reset_1()

                reset_tunnels()

                POS_TUNNEL_EQUALS_2_0[0] = ST_OFFSET_ANSWER+35
                POS_TUNNEL_EQUALS_2_1[0] = ST_OFFSET_ANSWER+35
                POS_TUNNEL_EQUALS_2_2[0] = ST_OFFSET_ANSWER+35

            if 17000 < NEW_TIMER < 22000:
                TASK_1 = FONT.render(
                    f'{all_exercises[2][0]}-{all_exercises[2][1]}', 0, WHITE)
                POS_TASK_1 = TASK_1.get_rect()
                POS_TASK_1.center = (WIDTH//2, HEIGHT//100*8)
                WIN.blit(TASK_1, POS_TASK_1)

                move_tunnels()

                POS_TUNNEL_EQUALS_2_0[0] -= speed*acceleration
                POS_TUNNEL_EQUALS_2_1[0] -= speed*acceleration
                POS_TUNNEL_EQUALS_2_2[0] -= speed*acceleration

                if CAR_RIGHT-6 <= POS_TUNNEL_1_0[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_2_0 == False and ROAD_LANES == 0 and COLLISION == False:
                    COLLISION = True
                    lives -= 1
                    car_hits()
                    equals_reset_2()
                elif CAR_RIGHT-6 <= POS_TUNNEL_1_0[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_2_0 == True and ROAD_LANES == 0 and COLLISION == False:
                    COLLISION = True
                    gate_sound()
                    score += score_limit
                if CAR_RIGHT-6 <= POS_TUNNEL_1_1[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_2_1 == False and ROAD_LANES == 1 and COLLISION == False:
                    COLLISION = True
                    lives -= 1
                    car_hits()
                    equals_reset_2()
                elif CAR_RIGHT-6 <= POS_TUNNEL_1_1[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_2_1 == True and ROAD_LANES == 1 and COLLISION == False:
                    COLLISION = True
                    gate_sound()
                    score += score_limit
                if CAR_RIGHT-6 <= POS_TUNNEL_1_2[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_2_2 == False and ROAD_LANES == 2 and COLLISION == False:
                    COLLISION = True
                    lives -= 1
                    car_hits()
                    equals_reset_2()
                elif CAR_RIGHT-6 <= POS_TUNNEL_1_2[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_2_2 == True and ROAD_LANES == 2 and COLLISION == False:
                    COLLISION = True
                    gate_sound()
                    score += score_limit

                # print(f'{POS_TUNNEL_1_0[0]} {CAR_RIGHT} {score}')

            if 22000 < NEW_TIMER < 24000:
                COLLISION = False

                equals_reset_2()

                reset_tunnels()

                POS_TUNNEL_EQUALS_3_0[0] = ST_OFFSET_ANSWER+35
                POS_TUNNEL_EQUALS_3_1[0] = ST_OFFSET_ANSWER+35
                POS_TUNNEL_EQUALS_3_2[0] = ST_OFFSET_ANSWER+35

            if 24000 < NEW_TIMER < 29000:
                TASK_1 = FONT.render(
                    f'{all_exercises[3][0]}-{all_exercises[3][1]}', 0, WHITE)
                POS_TASK_1 = TASK_1.get_rect()
                POS_TASK_1.center = (WIDTH//2, HEIGHT//100*8)
                WIN.blit(TASK_1, POS_TASK_1)

                move_tunnels()

                POS_TUNNEL_EQUALS_3_0[0] -= speed*acceleration
                POS_TUNNEL_EQUALS_3_1[0] -= speed*acceleration
                POS_TUNNEL_EQUALS_3_2[0] -= speed*acceleration

                if CAR_RIGHT-6 <= POS_TUNNEL_1_0[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_3_0 == False and ROAD_LANES == 0 and COLLISION == False:
                    COLLISION = True
                    lives -= 1
                    car_hits()
                    equals_reset_3()
                elif CAR_RIGHT-6 <= POS_TUNNEL_1_0[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_3_0 == True and ROAD_LANES == 0 and COLLISION == False:
                    COLLISION = True
                    gate_sound()
                    score += score_limit
                if CAR_RIGHT-6 <= POS_TUNNEL_1_1[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_3_1 == False and ROAD_LANES == 1 and COLLISION == False:
                    COLLISION = True
                    lives -= 1
                    car_hits()
                    equals_reset_3()
                elif CAR_RIGHT-6 <= POS_TUNNEL_1_1[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_3_1 == True and ROAD_LANES == 1 and COLLISION == False:
                    COLLISION = True
                    gate_sound()
                    score += score_limit
                if CAR_RIGHT-6 <= POS_TUNNEL_1_2[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_3_2 == False and ROAD_LANES == 2 and COLLISION == False:
                    COLLISION = True
                    lives -= 1
                    car_hits()
                    equals_reset_3()
                elif CAR_RIGHT-6 <= POS_TUNNEL_1_2[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_3_2 == True and ROAD_LANES == 2 and COLLISION == False:
                    COLLISION = True
                    gate_sound()
                    score += score_limit

                # print(f'{POS_TUNNEL_1_0[0]} {CAR_RIGHT} {score}')

            if 29000 < NEW_TIMER < 31000:
                COLLISION = False

                equals_reset_3()

                reset_tunnels()

                POS_TUNNEL_EQUALS_4_0[0] = ST_OFFSET_ANSWER+35
                POS_TUNNEL_EQUALS_4_1[0] = ST_OFFSET_ANSWER+35
                POS_TUNNEL_EQUALS_4_2[0] = ST_OFFSET_ANSWER+35

            if 31000 < NEW_TIMER < 36000:
                TASK_1 = FONT.render(
                    f'{all_exercises[4][0]}-{all_exercises[4][1]}', 0, WHITE)
                POS_TASK_1 = TASK_1.get_rect()
                POS_TASK_1.center = (WIDTH//2, HEIGHT//100*8)
                WIN.blit(TASK_1, POS_TASK_1)

                move_tunnels()

                POS_TUNNEL_EQUALS_4_0[0] -= speed*acceleration
                POS_TUNNEL_EQUALS_4_1[0] -= speed*acceleration
                POS_TUNNEL_EQUALS_4_2[0] -= speed*acceleration

                if CAR_RIGHT-6 <= POS_TUNNEL_1_0[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_4_0 == False and ROAD_LANES == 0 and COLLISION == False:
                    COLLISION = True
                    lives -= 1
                    car_hits()
                    equals_reset_4()
                elif CAR_RIGHT-6 <= POS_TUNNEL_1_0[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_4_0 == True and ROAD_LANES == 0 and COLLISION == False:
                    COLLISION = True
                    gate_sound()
                    score += score_limit
                if CAR_RIGHT-6 <= POS_TUNNEL_1_1[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_4_1 == False and ROAD_LANES == 1 and COLLISION == False:
                    COLLISION = True
                    lives -= 1
                    car_hits()
                    equals_reset_4()
                elif CAR_RIGHT-6 <= POS_TUNNEL_1_1[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_4_1 == True and ROAD_LANES == 1 and COLLISION == False:
                    COLLISION = True
                    gate_sound()
                    score += score_limit
                if CAR_RIGHT-6 <= POS_TUNNEL_1_2[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_4_2 == False and ROAD_LANES == 2 and COLLISION == False:
                    COLLISION = True
                    lives -= 1
                    car_hits()
                    equals_reset_4()
                elif CAR_RIGHT-6 <= POS_TUNNEL_1_2[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_4_2 == True and ROAD_LANES == 2 and COLLISION == False:
                    COLLISION = True
                    gate_sound()
                    score += score_limit

                # print(f'{POS_TUNNEL_1_0[0]} {CAR_RIGHT} {score}')

            if 36000 < NEW_TIMER < 38000:
                COLLISION = False

                equals_reset_4()

                reset_tunnels()

                POS_TUNNEL_EQUALS_5_0[0] = ST_OFFSET_ANSWER+35
                POS_TUNNEL_EQUALS_5_1[0] = ST_OFFSET_ANSWER+35
                POS_TUNNEL_EQUALS_5_2[0] = ST_OFFSET_ANSWER+35

            if 38000 < NEW_TIMER < 43000:
                TASK_1 = FONT.render(
                    f'{all_exercises[5][0]}-{all_exercises[5][1]}', 0, WHITE)
                POS_TASK_1 = TASK_1.get_rect()
                POS_TASK_1.center = (WIDTH//2, HEIGHT//100*8)
                WIN.blit(TASK_1, POS_TASK_1)

                move_tunnels()

                POS_TUNNEL_EQUALS_5_0[0] -= speed*acceleration
                POS_TUNNEL_EQUALS_5_1[0] -= speed*acceleration
                POS_TUNNEL_EQUALS_5_2[0] -= speed*acceleration

                if CAR_RIGHT-6 <= POS_TUNNEL_1_0[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_5_0 == False and ROAD_LANES == 0 and COLLISION == False:
                    COLLISION = True
                    lives -= 1
                    car_hits()
                    equals_reset_5()
                elif CAR_RIGHT-6 <= POS_TUNNEL_1_0[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_5_0 == True and ROAD_LANES == 0 and COLLISION == False:
                    COLLISION = True
                    gate_sound()
                    score += score_limit
                if CAR_RIGHT-6 <= POS_TUNNEL_1_1[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_5_1 == False and ROAD_LANES == 1 and COLLISION == False:
                    COLLISION = True
                    lives -= 1
                    car_hits()
                    equals_reset_5()
                elif CAR_RIGHT-6 <= POS_TUNNEL_1_1[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_5_1 == True and ROAD_LANES == 1 and COLLISION == False:
                    COLLISION = True
                    gate_sound()
                    score += score_limit
                if CAR_RIGHT-6 <= POS_TUNNEL_1_2[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_5_2 == False and ROAD_LANES == 2 and COLLISION == False:
                    COLLISION = True
                    lives -= 1
                    car_hits()
                    equals_reset_5()
                elif CAR_RIGHT-6 <= POS_TUNNEL_1_2[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_5_2 == True and ROAD_LANES == 2 and COLLISION == False:
                    COLLISION = True
                    gate_sound()
                    score += score_limit

                # print(f'{POS_TUNNEL_1_0[0]} {CAR_RIGHT} {score}')

            if 43000 < NEW_TIMER < 45000:
                COLLISION = False

                equals_reset_5()

                reset_tunnels()

                POS_TUNNEL_EQUALS_6_0[0] = ST_OFFSET_ANSWER+35
                POS_TUNNEL_EQUALS_6_1[0] = ST_OFFSET_ANSWER+35
                POS_TUNNEL_EQUALS_6_2[0] = ST_OFFSET_ANSWER+35

            if 45000 < NEW_TIMER < 50000:
                TASK_1 = FONT.render(
                    f'{all_exercises[6][0]}-{all_exercises[6][1]}', 0, WHITE)
                POS_TASK_1 = TASK_1.get_rect()
                POS_TASK_1.center = (WIDTH//2, HEIGHT//100*8)
                WIN.blit(TASK_1, POS_TASK_1)

                move_tunnels()

                POS_TUNNEL_EQUALS_6_0[0] -= speed*acceleration
                POS_TUNNEL_EQUALS_6_1[0] -= speed*acceleration
                POS_TUNNEL_EQUALS_6_2[0] -= speed*acceleration

                if CAR_RIGHT-6 <= POS_TUNNEL_1_0[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_6_0 == False and ROAD_LANES == 0 and COLLISION == False:
                    COLLISION = True
                    lives -= 1
                    car_hits()
                    equals_reset_6()
                elif CAR_RIGHT-6 <= POS_TUNNEL_1_0[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_6_0 == True and ROAD_LANES == 0 and COLLISION == False:
                    COLLISION = True
                    gate_sound()
                    score += score_limit
                if CAR_RIGHT-6 <= POS_TUNNEL_1_1[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_6_1 == False and ROAD_LANES == 1 and COLLISION == False:
                    COLLISION = True
                    lives -= 1
                    car_hits()
                    equals_reset_6()
                elif CAR_RIGHT-6 <= POS_TUNNEL_1_1[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_6_1 == True and ROAD_LANES == 1 and COLLISION == False:
                    COLLISION = True
                    gate_sound()
                    score += score_limit
                if CAR_RIGHT-6 <= POS_TUNNEL_1_2[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_6_2 == False and ROAD_LANES == 2 and COLLISION == False:
                    COLLISION = True
                    lives -= 1
                    car_hits()
                    equals_reset_6()
                elif CAR_RIGHT-6 <= POS_TUNNEL_1_2[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_6_2 == True and ROAD_LANES == 2 and COLLISION == False:
                    COLLISION = True
                    gate_sound()
                    score += score_limit

                # print(f'{POS_TUNNEL_1_0[0]} {CAR_RIGHT} {score}')

            if 50000 < NEW_TIMER < 52000:
                COLLISION = False

                equals_reset_6()

                reset_tunnels()

                POS_TUNNEL_EQUALS_7_0[0] = ST_OFFSET_ANSWER+35
                POS_TUNNEL_EQUALS_7_1[0] = ST_OFFSET_ANSWER+35
                POS_TUNNEL_EQUALS_7_2[0] = ST_OFFSET_ANSWER+35

            if 52000 < NEW_TIMER < 57000:
                TASK_1 = FONT.render(
                    f'{all_exercises[7][0]}-{all_exercises[7][1]}', 0, WHITE)
                POS_TASK_1 = TASK_1.get_rect()
                POS_TASK_1.center = (WIDTH//2, HEIGHT//100*8)
                WIN.blit(TASK_1, POS_TASK_1)

                move_tunnels()

                POS_TUNNEL_EQUALS_7_0[0] -= speed*acceleration
                POS_TUNNEL_EQUALS_7_1[0] -= speed*acceleration
                POS_TUNNEL_EQUALS_7_2[0] -= speed*acceleration

                if CAR_RIGHT-6 <= POS_TUNNEL_1_0[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_7_0 == False and ROAD_LANES == 0 and COLLISION == False:
                    COLLISION = True
                    lives -= 1
                    car_hits()
                    equals_reset_7()
                elif CAR_RIGHT-6 <= POS_TUNNEL_1_0[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_7_0 == True and ROAD_LANES == 0 and COLLISION == False:
                    COLLISION = True
                    gate_sound()
                    score += score_limit
                if CAR_RIGHT-6 <= POS_TUNNEL_1_1[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_7_1 == False and ROAD_LANES == 1 and COLLISION == False:
                    COLLISION = True
                    lives -= 1
                    car_hits()
                    equals_reset_7()
                elif CAR_RIGHT-6 <= POS_TUNNEL_1_1[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_7_1 == True and ROAD_LANES == 1 and COLLISION == False:
                    COLLISION = True
                    gate_sound()
                    score += score_limit
                if CAR_RIGHT-6 <= POS_TUNNEL_1_2[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_7_2 == False and ROAD_LANES == 2 and COLLISION == False:
                    COLLISION = True
                    lives -= 1
                    car_hits()
                    equals_reset_7()
                elif CAR_RIGHT-6 <= POS_TUNNEL_1_2[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_7_2 == True and ROAD_LANES == 2 and COLLISION == False:
                    COLLISION = True
                    gate_sound()
                    score += score_limit

                # print(f'{POS_TUNNEL_1_0[0]} {CAR_RIGHT} {score}')

            if 57000 < NEW_TIMER < 59000:
                COLLISION = False

                equals_reset_7()

                reset_tunnels()

                POS_TUNNEL_EQUALS_8_0[0] = ST_OFFSET_ANSWER+35
                POS_TUNNEL_EQUALS_8_1[0] = ST_OFFSET_ANSWER+35
                POS_TUNNEL_EQUALS_8_2[0] = ST_OFFSET_ANSWER+35

            if 59000 < NEW_TIMER < 64000:
                TASK_1 = FONT.render(
                    f'{all_exercises[8][0]}-{all_exercises[8][1]}', 0, WHITE)
                POS_TASK_1 = TASK_1.get_rect()
                POS_TASK_1.center = (WIDTH//2, HEIGHT//100*8)
                WIN.blit(TASK_1, POS_TASK_1)

                move_tunnels()

                POS_TUNNEL_EQUALS_8_0[0] -= speed*acceleration
                POS_TUNNEL_EQUALS_8_1[0] -= speed*acceleration
                POS_TUNNEL_EQUALS_8_2[0] -= speed*acceleration

                if CAR_RIGHT-6 <= POS_TUNNEL_1_0[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_8_0 == False and ROAD_LANES == 0 and COLLISION == False:
                    COLLISION = True
                    lives -= 1
                    car_hits()
                    equals_reset_8()
                elif CAR_RIGHT-6 <= POS_TUNNEL_1_0[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_8_0 == True and ROAD_LANES == 0 and COLLISION == False:
                    COLLISION = True
                    gate_sound()
                    score += score_limit
                if CAR_RIGHT-6 <= POS_TUNNEL_1_1[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_8_1 == False and ROAD_LANES == 1 and COLLISION == False:
                    COLLISION = True
                    lives -= 1
                    car_hits()
                    equals_reset_8()
                elif CAR_RIGHT-6 <= POS_TUNNEL_1_1[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_8_1 == True and ROAD_LANES == 1 and COLLISION == False:
                    COLLISION = True
                    gate_sound()
                    score += score_limit
                if CAR_RIGHT-6 <= POS_TUNNEL_1_2[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_8_2 == False and ROAD_LANES == 2 and COLLISION == False:
                    COLLISION = True
                    lives -= 1
                    car_hits()
                    equals_reset_8()
                elif CAR_RIGHT-6 <= POS_TUNNEL_1_2[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_8_2 == True and ROAD_LANES == 2 and COLLISION == False:
                    COLLISION = True
                    gate_sound()
                    score += score_limit

                # print(f'{POS_TUNNEL_1_0[0]} {CAR_RIGHT} {score}')

            if 64000 < NEW_TIMER < 66000:
                COLLISION = False

                equals_reset_8()

                reset_tunnels()

                POS_TUNNEL_EQUALS_9_0[0] = ST_OFFSET_ANSWER+35
                POS_TUNNEL_EQUALS_9_1[0] = ST_OFFSET_ANSWER+35
                POS_TUNNEL_EQUALS_9_2[0] = ST_OFFSET_ANSWER+35

            if 66000 < NEW_TIMER < 71000:
                TASK_1 = FONT.render(
                    f'{all_exercises[9][0]}-{all_exercises[9][1]}', 0, WHITE)
                POS_TASK_1 = TASK_1.get_rect()
                POS_TASK_1.center = (WIDTH//2, HEIGHT//100*8)
                WIN.blit(TASK_1, POS_TASK_1)

                move_tunnels()

                POS_TUNNEL_EQUALS_9_0[0] -= speed*acceleration
                POS_TUNNEL_EQUALS_9_1[0] -= speed*acceleration
                POS_TUNNEL_EQUALS_9_2[0] -= speed*acceleration

                if CAR_RIGHT-6 <= POS_TUNNEL_1_0[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_9_0 == False and ROAD_LANES == 0 and COLLISION == False:
                    COLLISION = True
                    lives -= 1
                    car_hits()
                    equals_reset_9()
                elif CAR_RIGHT-6 <= POS_TUNNEL_1_0[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_9_0 == True and ROAD_LANES == 0 and COLLISION == False:
                    COLLISION = True
                    gate_sound()
                    score += score_limit
                if CAR_RIGHT-6 <= POS_TUNNEL_1_1[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_9_1 == False and ROAD_LANES == 1 and COLLISION == False:
                    COLLISION = True
                    lives -= 1
                    car_hits()
                    equals_reset_9()
                elif CAR_RIGHT-6 <= POS_TUNNEL_1_1[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_9_1 == True and ROAD_LANES == 1 and COLLISION == False:
                    COLLISION = True
                    gate_sound()
                    score += score_limit
                if CAR_RIGHT-6 <= POS_TUNNEL_1_2[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_9_2 == False and ROAD_LANES == 2 and COLLISION == False:
                    COLLISION = True
                    lives -= 1
                    car_hits()
                    equals_reset_9()
                elif CAR_RIGHT-6 <= POS_TUNNEL_1_2[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_9_2 == True and ROAD_LANES == 2 and COLLISION == False:
                    COLLISION = True
                    gate_sound()
                    score += score_limit

                # print(f'{POS_TUNNEL_1_0[0]} {CAR_RIGHT} {score}')

            if 71000 < NEW_TIMER < 73000:
                COLLISION = False

                equals_reset_9()

                reset_tunnels()

            if 73000 < NEW_TIMER:
                if 73001 < NEW_TIMER < 73018:
                    lvl_complete_sound()
                WIN_CONDITION = True
                WIN.blit(MAIN_MENU_BACK, POS_BACK)
                GAME_OVER = FONT.render(f'ПОБЕДА!', 0, WHITE)
                POS_GAME_OVER = GAME_OVER.get_rect(center=(WIDTH//2, HEIGHT//2-100))
                GAME_OVER_SCORE = FONT.render(f'ВАШ СЧЕТ: {score}', 0, WHITE)
                POS_GAME_OVER_SCORE = GAME_OVER_SCORE.get_rect(center=(WIDTH//2, HEIGHT//2))
                GAME_OVER_PRESS_ESC = FONT_SCORE.render(f'След уровень: ENTER', 0, WHITE)
                POS_GAME_OVER_PRESS_ESC = GAME_OVER_PRESS_ESC.get_rect(center=(WIDTH//2, HEIGHT//100*70))
                WIN.blit(GAME_OVER, POS_GAME_OVER)
                WIN.blit(GAME_OVER_SCORE, POS_GAME_OVER_SCORE)
                WIN.blit(GAME_OVER_PRESS_ESC, POS_GAME_OVER_PRESS_ESC)

        if lives != 0:
            SCORE_0 = FONT_SCORE.render(f'{score}', 0, WHITE)
            POS_SCORE_0 = SCORE_0.get_rect(
                center=(WIDTH//100*92, HEIGHT//100*99+30))
            WIN.blit(SCORE_0, POS_SCORE_0)
        else:
            if GAME_OVER_SOUND_FLAG == False:
                game_over_sound()
                GAME_OVER_SOUND_FLAG = True
            WIN.blit(MAIN_MENU_BACK, POS_BACK)
            GAME_OVER = FONT.render(f'GAME OVER', 0, WHITE)
            POS_GAME_OVER = GAME_OVER.get_rect(center=(WIDTH//2, HEIGHT//2-100))
            GAME_OVER.set_alpha(100)
            GAME_OVER_SCORE = FONT.render(f'ВАШ СЧЕТ: {score}', 0, WHITE)
            POS_GAME_OVER_SCORE = GAME_OVER_SCORE.get_rect(center=(WIDTH//2, HEIGHT//2))
            GAME_OVER_PRESS_ESC = FONT_SCORE.render(f'МЕНЮ: ESC', 0, WHITE)
            POS_GAME_OVER_PRESS_ESC = GAME_OVER_PRESS_ESC.get_rect(center=(WIDTH//2, HEIGHT//100*70))
            WIN.blit(GAME_OVER, POS_GAME_OVER)
            WIN.blit(GAME_OVER_SCORE, POS_GAME_OVER_SCORE)
            WIN.blit(GAME_OVER_PRESS_ESC, POS_GAME_OVER_PRESS_ESC)

        if game_is_on:
            pygame.display.flip()
        else:
            NEW_TIMER = 0

        clock.tick(FPS)




def lvl3():

    lvl3_music()

    BG = pygame.image.load('img/lvl3/sunset.png')
    POS_BG = BG.get_rect(center=(WIDTH//2, HEIGHT//2))

    ROAD = pygame.image.load('img/lvl3/road.png').convert_alpha()

    CAR = pygame.image.load('img/lvl3/car.png').convert_alpha()
    CAR_WIDTH = CAR.get_width()
    POS_CAR = CAR.get_rect()
    POS_CAR.center = WIDTH//100*20, HEIGHT//100*65
    CAR_RIGHT = POS_CAR[0]+CAR_WIDTH

    CAR_W = pygame.image.load('img/lvl3/car_w.png').convert_alpha()
    CAR_W_WIDTH = CAR_W.get_width()
    POS_CAR_W = CAR_W.get_rect()
    POS_CAR_W.center = WIDTH//100*20, HEIGHT//100*65
    CAR_W_RIGHT = POS_CAR_W[0]+CAR_W_WIDTH

    CAR_2 = pygame.image.load('img/lvl3/car_crashed_1.png').convert_alpha()
    CAR_2_WIDTH = CAR_2.get_width()
    POS_CAR_2 = CAR_2.get_rect()
    POS_CAR_2.center = WIDTH//100*20, HEIGHT//100*65
    CAR_2_RIGHT = POS_CAR_2[0]+CAR_2_WIDTH

    CAR_2_W = pygame.image.load('img/lvl3/car_crashed_1_w.png').convert_alpha()
    CAR_2_W_WIDTH = CAR_2_W.get_width()
    POS_CAR_2_W = CAR_2_W.get_rect()
    POS_CAR_2_W.center = WIDTH//100*20, HEIGHT//100*65
    CAR_2_W_RIGHT = POS_CAR_2_W[0]+CAR_2_W_WIDTH

    CAR_3 = pygame.image.load('img/lvl3/car_crashed_2.png').convert_alpha()
    CAR_3_WIDTH = CAR_3.get_width()
    POS_CAR_3 = CAR_3.get_rect()
    POS_CAR_3.center = WIDTH//100*20, HEIGHT//100*65
    CAR_3_RIGHT = POS_CAR_3[0]+CAR_3_WIDTH

    CAR_3_W = pygame.image.load('img/lvl3/car_crashed_2_w.png').convert_alpha()
    CAR_3_W_WIDTH = CAR_3_W.get_width()
    POS_CAR_3_W = CAR_3_W.get_rect()
    POS_CAR_3_W.center = WIDTH//100*20, HEIGHT//100*65
    CAR_3_W_RIGHT = POS_CAR_3_W[0]+CAR_3_W_WIDTH

    CAR_4 = pygame.image.load('img/lvl3/car_crashed_3.png').convert_alpha()
    CAR_4_WIDTH = CAR_4.get_width()
    POS_CAR_4 = CAR_4.get_rect()
    POS_CAR_4.center = WIDTH//100*20, HEIGHT//100*65
    CAR_4_RIGHT = POS_CAR_4[0]+CAR_4_WIDTH

    TASK = pygame.image.load('img/lvl3/task.png').convert_alpha()
    POS_TASK = TASK.get_rect(center=(WIDTH//2, HEIGHT//100*8))
    SCORE = pygame.image.load('img/lvl3/score.png').convert_alpha()
    POS_SCORE = SCORE.get_rect(center=(WIDTH//100*92, HEIGHT//100*99+30))
    PAUSE = pygame.image.load('img/lvl3/pause.png').convert_alpha()
    POS_PAUSE = PAUSE.get_rect(center=(WIDTH//100*92, HEIGHT//100*6))

    ST_OFFSET_TUNNEL_0 = WIDTH+100
    ST_OFFSET_TUNNEL_1 = WIDTH+98+100
    ST_OFFSET_ANSWER = WIDTH+180

    TUNNEL_0 = pygame.image.load('img/lvl3/tunnel_0.png').convert_alpha()
    POS_TUNNEL_0_0 = TUNNEL_0.get_rect()
    POS_TUNNEL_0_0.center = ST_OFFSET_TUNNEL_0, HEIGHT//100*46
    POS_TUNNEL_0_1 = TUNNEL_0.get_rect()
    POS_TUNNEL_0_1.center = ST_OFFSET_TUNNEL_0, HEIGHT//100*66
    POS_TUNNEL_0_2 = TUNNEL_0.get_rect()
    POS_TUNNEL_0_2.center = ST_OFFSET_TUNNEL_0, HEIGHT//100*86

    TUNNEL_1 = pygame.image.load('img/lvl3/tunnel_1.png').convert_alpha()
    POS_TUNNEL_1_0 = TUNNEL_1.get_rect()
    POS_TUNNEL_1_0.center = ST_OFFSET_TUNNEL_1, HEIGHT//100*46
    POS_TUNNEL_1_1 = TUNNEL_1.get_rect()
    POS_TUNNEL_1_1.center = ST_OFFSET_TUNNEL_1, HEIGHT//100*66
    POS_TUNNEL_1_2 = TUNNEL_1.get_rect()
    POS_TUNNEL_1_2.center = ST_OFFSET_TUNNEL_1, HEIGHT//100*86

    run_lvl = True
    clock = pygame.time.Clock()
    i = 0
    exercises = 10
    FPS = 60
    NEW_TIMER = 0
    ROAD_LANES = 1
    lives = 3
    score = 0
    score_limit = 1
    COLLISION = False
    COLLISION_PAUSE = 1000
    game_is_on = True
    current_time = 0
    speed = 8
    acceleration = 1.0
    GAME_OVER_SOUND_FLAG = False
    CAR_HIT_SOUND_FLAG = False
    CAR_HIT_2_SOUND_FLAG = False
    WIN_CONDITION = False
    pressed = pygame.key.get_pressed()

    all_exercises, all_answers, all_answer_flag, all_answer_flags_last = [], [], [], []

    for exercise in range(10):
        first_sum = random.randint(1, 9)
        second_sum = random.randint(1, 9)

        sum_true = first_sum * second_sum

        if sum_true > 89:
            sum_fake_1 = sum_true + random.randint(-10, 1)
            sum_fake_2 = sum_true + random.randint(-10, 1)
        elif sum_true < 11:
            sum_fake_1 = sum_true + random.randint(1, 10)
            sum_fake_2 = sum_true + random.randint(1, 10)
        else:
            sum_fake_1 = sum_true + random.randint(-10, 10)
            sum_fake_2 = sum_true + random.randint(-10, 10)

        if sum_true == sum_fake_1 or sum_true == sum_fake_2 or sum_fake_1 == sum_fake_2:
            # print(f'{sum_true} {sum_fake_1} {sum_fake_2}')

            if sum_true == sum_fake_1:
                sum_fake_1 += 1
            if sum_true == sum_fake_2:
                sum_fake_2 += 2
            if sum_fake_1 == sum_fake_2:
                sum_fake_1 += 1
                sum_fake_2 -= 2

            # print(f'{sum_true} {sum_fake_1} {sum_fake_2}')

        # if sum_true == sum_fake_1 or sum_true
        all_exercises.append(
            [first_sum, second_sum, sum_true, sum_fake_1, sum_fake_2])
        all_answers.append([sum_true, sum_fake_1, sum_fake_2])

    print(all_exercises)
    # print(all_answers)

    for all_answer in all_answers:
        new_answers = all_answer
        random.shuffle(new_answers)

    # print(all_answers)

    jj = 0

    for all_answer in all_answers:
        for a_a in all_answer:
            kk = math.floor(jj/3)
            jj += 1
            if a_a == all_exercises[kk][2]:
                all_answer_flag.append(True)
            else:
                all_answer_flag.append(False)
            # print(f'{kk} {a_a} {all_exercises[kk][2]}')
    # print(all_answer_flag)

    TUNNEL_EQUALS_0_0 = FONT.render(f'{all_answers[0][0]}', 0, WHITE)
    POS_TUNNEL_EQUALS_0_0 = TUNNEL_EQUALS_0_0.get_rect()
    POS_TUNNEL_EQUALS_0_0.center = ST_OFFSET_ANSWER, HEIGHT//100*46
    TUNNEL_LOGIC_0_0 = all_answer_flag[0]

    TUNNEL_EQUALS_0_1 = FONT.render(f'{all_answers[0][1]}', 0, WHITE)
    POS_TUNNEL_EQUALS_0_1 = TUNNEL_EQUALS_0_1.get_rect()
    POS_TUNNEL_EQUALS_0_1.center = ST_OFFSET_ANSWER, HEIGHT//100*66
    TUNNEL_LOGIC_0_1 = all_answer_flag[1]

    TUNNEL_EQUALS_0_2 = FONT.render(f'{all_answers[0][2]}', 0, WHITE)
    POS_TUNNEL_EQUALS_0_2 = TUNNEL_EQUALS_0_2.get_rect()
    POS_TUNNEL_EQUALS_0_2.center = ST_OFFSET_ANSWER, HEIGHT//100*86
    TUNNEL_LOGIC_0_2 = all_answer_flag[2]

    TUNNEL_EQUALS_1_0 = FONT.render(f'{all_answers[1][0]}', 0, WHITE)
    POS_TUNNEL_EQUALS_1_0 = TUNNEL_EQUALS_1_0.get_rect()
    POS_TUNNEL_EQUALS_1_0.center = ST_OFFSET_ANSWER, HEIGHT//100*46
    TUNNEL_LOGIC_1_0 = all_answer_flag[3]

    TUNNEL_EQUALS_1_1 = FONT.render(f'{all_answers[1][1]}', 0, WHITE)
    POS_TUNNEL_EQUALS_1_1 = TUNNEL_EQUALS_1_1.get_rect()
    POS_TUNNEL_EQUALS_1_1.center = ST_OFFSET_ANSWER, HEIGHT//100*66
    TUNNEL_LOGIC_1_1 = all_answer_flag[4]

    TUNNEL_EQUALS_1_2 = FONT.render(f'{all_answers[1][2]}', 0, WHITE)
    POS_TUNNEL_EQUALS_1_2 = TUNNEL_EQUALS_1_2.get_rect()
    POS_TUNNEL_EQUALS_1_2.center = ST_OFFSET_ANSWER, HEIGHT//100*86
    TUNNEL_LOGIC_1_2 = all_answer_flag[5]

    TUNNEL_EQUALS_2_0 = FONT.render(f'{all_answers[2][0]}', 0, WHITE)
    POS_TUNNEL_EQUALS_2_0 = TUNNEL_EQUALS_2_0.get_rect()
    POS_TUNNEL_EQUALS_2_0.center = ST_OFFSET_ANSWER, HEIGHT//100*46
    TUNNEL_LOGIC_2_0 = all_answer_flag[6]

    TUNNEL_EQUALS_2_1 = FONT.render(f'{all_answers[2][1]}', 0, WHITE)
    POS_TUNNEL_EQUALS_2_1 = TUNNEL_EQUALS_2_1.get_rect()
    POS_TUNNEL_EQUALS_2_1.center = ST_OFFSET_ANSWER, HEIGHT//100*66
    TUNNEL_LOGIC_2_1 = all_answer_flag[7]

    TUNNEL_EQUALS_2_2 = FONT.render(f'{all_answers[2][2]}', 0, WHITE)
    POS_TUNNEL_EQUALS_2_2 = TUNNEL_EQUALS_2_2.get_rect()
    POS_TUNNEL_EQUALS_2_2.center = ST_OFFSET_ANSWER, HEIGHT//100*86
    TUNNEL_LOGIC_2_2 = all_answer_flag[8]

    TUNNEL_EQUALS_3_0 = FONT.render(f'{all_answers[3][0]}', 0, WHITE)
    POS_TUNNEL_EQUALS_3_0 = TUNNEL_EQUALS_3_0.get_rect()
    POS_TUNNEL_EQUALS_3_0.center = ST_OFFSET_ANSWER, HEIGHT//100*46
    TUNNEL_LOGIC_3_0 = all_answer_flag[9]

    TUNNEL_EQUALS_3_1 = FONT.render(f'{all_answers[3][1]}', 0, WHITE)
    POS_TUNNEL_EQUALS_3_1 = TUNNEL_EQUALS_3_1.get_rect()
    POS_TUNNEL_EQUALS_3_1.center = ST_OFFSET_ANSWER, HEIGHT//100*66
    TUNNEL_LOGIC_3_1 = all_answer_flag[10]

    TUNNEL_EQUALS_3_2 = FONT.render(f'{all_answers[3][2]}', 0, WHITE)
    POS_TUNNEL_EQUALS_3_2 = TUNNEL_EQUALS_3_2.get_rect()
    POS_TUNNEL_EQUALS_3_2.center = ST_OFFSET_ANSWER, HEIGHT//100*86
    TUNNEL_LOGIC_3_2 = all_answer_flag[11]

    TUNNEL_EQUALS_4_0 = FONT.render(f'{all_answers[4][0]}', 0, WHITE)
    POS_TUNNEL_EQUALS_4_0 = TUNNEL_EQUALS_4_0.get_rect()
    POS_TUNNEL_EQUALS_4_0.center = ST_OFFSET_ANSWER, HEIGHT//100*46
    TUNNEL_LOGIC_4_0 = all_answer_flag[12]

    TUNNEL_EQUALS_4_1 = FONT.render(f'{all_answers[4][1]}', 0, WHITE)
    POS_TUNNEL_EQUALS_4_1 = TUNNEL_EQUALS_4_1.get_rect()
    POS_TUNNEL_EQUALS_4_1.center = ST_OFFSET_ANSWER, HEIGHT//100*66
    TUNNEL_LOGIC_4_1 = all_answer_flag[13]

    TUNNEL_EQUALS_4_2 = FONT.render(f'{all_answers[4][2]}', 0, WHITE)
    POS_TUNNEL_EQUALS_4_2 = TUNNEL_EQUALS_4_2.get_rect()
    POS_TUNNEL_EQUALS_4_2.center = ST_OFFSET_ANSWER, HEIGHT//100*86
    TUNNEL_LOGIC_4_2 = all_answer_flag[14]

    TUNNEL_EQUALS_5_0 = FONT.render(f'{all_answers[5][0]}', 0, WHITE)
    POS_TUNNEL_EQUALS_5_0 = TUNNEL_EQUALS_5_0.get_rect()
    POS_TUNNEL_EQUALS_5_0.center = ST_OFFSET_ANSWER, HEIGHT//100*46
    TUNNEL_LOGIC_5_0 = all_answer_flag[15]

    TUNNEL_EQUALS_5_1 = FONT.render(f'{all_answers[5][1]}', 0, WHITE)
    POS_TUNNEL_EQUALS_5_1 = TUNNEL_EQUALS_5_1.get_rect()
    POS_TUNNEL_EQUALS_5_1.center = ST_OFFSET_ANSWER, HEIGHT//100*66
    TUNNEL_LOGIC_5_1 = all_answer_flag[16]

    TUNNEL_EQUALS_5_2 = FONT.render(f'{all_answers[5][2]}', 0, WHITE)
    POS_TUNNEL_EQUALS_5_2 = TUNNEL_EQUALS_5_2.get_rect()
    POS_TUNNEL_EQUALS_5_2.center = ST_OFFSET_ANSWER, HEIGHT//100*86
    TUNNEL_LOGIC_5_2 = all_answer_flag[17]

    TUNNEL_EQUALS_6_0 = FONT.render(f'{all_answers[6][0]}', 0, WHITE)
    POS_TUNNEL_EQUALS_6_0 = TUNNEL_EQUALS_6_0.get_rect()
    POS_TUNNEL_EQUALS_6_0.center = ST_OFFSET_ANSWER, HEIGHT//100*46
    TUNNEL_LOGIC_6_0 = all_answer_flag[18]

    TUNNEL_EQUALS_6_1 = FONT.render(f'{all_answers[6][1]}', 0, WHITE)
    POS_TUNNEL_EQUALS_6_1 = TUNNEL_EQUALS_6_1.get_rect()
    POS_TUNNEL_EQUALS_6_1.center = ST_OFFSET_ANSWER, HEIGHT//100*66
    TUNNEL_LOGIC_6_1 = all_answer_flag[19]

    TUNNEL_EQUALS_6_2 = FONT.render(f'{all_answers[6][2]}', 0, WHITE)
    POS_TUNNEL_EQUALS_6_2 = TUNNEL_EQUALS_6_2.get_rect()
    POS_TUNNEL_EQUALS_6_2.center = ST_OFFSET_ANSWER, HEIGHT//100*86
    TUNNEL_LOGIC_6_2 = all_answer_flag[20]

    TUNNEL_EQUALS_7_0 = FONT.render(f'{all_answers[7][0]}', 0, WHITE)
    POS_TUNNEL_EQUALS_7_0 = TUNNEL_EQUALS_7_0.get_rect()
    POS_TUNNEL_EQUALS_7_0.center = ST_OFFSET_ANSWER, HEIGHT//100*46
    TUNNEL_LOGIC_7_0 = all_answer_flag[21]

    TUNNEL_EQUALS_7_1 = FONT.render(f'{all_answers[7][1]}', 0, WHITE)
    POS_TUNNEL_EQUALS_7_1 = TUNNEL_EQUALS_7_1.get_rect()
    POS_TUNNEL_EQUALS_7_1.center = ST_OFFSET_ANSWER, HEIGHT//100*66
    TUNNEL_LOGIC_7_1 = all_answer_flag[22]

    TUNNEL_EQUALS_7_2 = FONT.render(f'{all_answers[7][2]}', 0, WHITE)
    POS_TUNNEL_EQUALS_7_2 = TUNNEL_EQUALS_7_2.get_rect()
    POS_TUNNEL_EQUALS_7_2.center = ST_OFFSET_ANSWER, HEIGHT//100*86
    TUNNEL_LOGIC_7_2 = all_answer_flag[23]

    TUNNEL_EQUALS_8_0 = FONT.render(f'{all_answers[8][0]}', 0, WHITE)
    POS_TUNNEL_EQUALS_8_0 = TUNNEL_EQUALS_8_0.get_rect()
    POS_TUNNEL_EQUALS_8_0.center = ST_OFFSET_ANSWER, HEIGHT//100*46
    TUNNEL_LOGIC_8_0 = all_answer_flag[24]

    TUNNEL_EQUALS_8_1 = FONT.render(f'{all_answers[8][1]}', 0, WHITE)
    POS_TUNNEL_EQUALS_8_1 = TUNNEL_EQUALS_8_1.get_rect()
    POS_TUNNEL_EQUALS_8_1.center = ST_OFFSET_ANSWER, HEIGHT//100*66
    TUNNEL_LOGIC_8_1 = all_answer_flag[25]

    TUNNEL_EQUALS_8_2 = FONT.render(f'{all_answers[8][2]}', 0, WHITE)
    POS_TUNNEL_EQUALS_8_2 = TUNNEL_EQUALS_8_2.get_rect()
    POS_TUNNEL_EQUALS_8_2.center = ST_OFFSET_ANSWER, HEIGHT//100*86
    TUNNEL_LOGIC_8_2 = all_answer_flag[26]

    TUNNEL_EQUALS_9_0 = FONT.render(f'{all_answers[9][0]}', 0, WHITE)
    POS_TUNNEL_EQUALS_9_0 = TUNNEL_EQUALS_9_0.get_rect()
    POS_TUNNEL_EQUALS_9_0.center = ST_OFFSET_ANSWER, HEIGHT//100*46
    TUNNEL_LOGIC_9_0 = all_answer_flag[27]

    TUNNEL_EQUALS_9_1 = FONT.render(f'{all_answers[9][1]}', 0, WHITE)
    POS_TUNNEL_EQUALS_9_1 = TUNNEL_EQUALS_9_1.get_rect()
    POS_TUNNEL_EQUALS_9_1.center = ST_OFFSET_ANSWER, HEIGHT//100*66
    TUNNEL_LOGIC_9_1 = all_answer_flag[28]

    TUNNEL_EQUALS_9_2 = FONT.render(f'{all_answers[9][2]}', 0, WHITE)
    POS_TUNNEL_EQUALS_9_2 = TUNNEL_EQUALS_9_2.get_rect()
    POS_TUNNEL_EQUALS_9_2.center = ST_OFFSET_ANSWER, HEIGHT//100*86
    TUNNEL_LOGIC_9_2 = all_answer_flag[29]

    def draw_all():
        if lives != 0:
            WIN.blit(BG, POS_BG)
            WIN.blit(ROAD, (i, 0))
            WIN.blit(ROAD, (WIDTH+i, 0))
            # WIN.blit(ROAD, POS_ROAD)
            WIN.blit(TASK, POS_TASK)

            # WIN.blit(HEART, POS_HEART_0)
            # WIN.blit(HEART, POS_HEART_1)
            # WIN.blit(HEART, POS_HEART_2)

            WIN.blit(TUNNEL_0, POS_TUNNEL_0_0)
            WIN.blit(TUNNEL_0, POS_TUNNEL_0_1)
            WIN.blit(TUNNEL_0, POS_TUNNEL_0_2)

        ostatok = current_time // 250 % 2

        if lives == 3 and ostatok == 0:
            WIN.blit(CAR, POS_CAR)
        elif lives == 3 and ostatok != 0:
            WIN.blit(CAR_W, (POS_CAR_W[0], POS_CAR_W[1]+2))
        if lives == 2 and ostatok == 0:
            WIN.blit(CAR_2, POS_CAR_2)
        elif lives == 2 and ostatok != 0:
            WIN.blit(CAR_2_W, (POS_CAR_2_W[0], POS_CAR_2_W[1]+2))
        if lives == 1 and ostatok == 0:
            WIN.blit(CAR_3, POS_CAR_3)
        elif lives == 1 and ostatok != 0:
            WIN.blit(CAR_3_W, (POS_CAR_3_W[0], POS_CAR_3_W[1]+2))
        if lives == 0:
            WIN.blit(CAR_4, POS_CAR_4)

        if lives != 0:
            WIN.blit(TUNNEL_1, POS_TUNNEL_1_0)
            WIN.blit(TUNNEL_1, POS_TUNNEL_1_1)
            WIN.blit(TUNNEL_1, POS_TUNNEL_1_2)

            WIN.blit(TUNNEL_EQUALS_0_0, POS_TUNNEL_EQUALS_0_0)
            WIN.blit(TUNNEL_EQUALS_0_1, POS_TUNNEL_EQUALS_0_1)
            WIN.blit(TUNNEL_EQUALS_0_2, POS_TUNNEL_EQUALS_0_2)

            WIN.blit(TUNNEL_EQUALS_1_0, POS_TUNNEL_EQUALS_1_0)
            WIN.blit(TUNNEL_EQUALS_1_1, POS_TUNNEL_EQUALS_1_1)
            WIN.blit(TUNNEL_EQUALS_1_2, POS_TUNNEL_EQUALS_1_2)

            WIN.blit(TUNNEL_EQUALS_2_0, POS_TUNNEL_EQUALS_2_0)
            WIN.blit(TUNNEL_EQUALS_2_1, POS_TUNNEL_EQUALS_2_1)
            WIN.blit(TUNNEL_EQUALS_2_2, POS_TUNNEL_EQUALS_2_2)

            WIN.blit(TUNNEL_EQUALS_3_0, POS_TUNNEL_EQUALS_3_0)
            WIN.blit(TUNNEL_EQUALS_3_1, POS_TUNNEL_EQUALS_3_1)
            WIN.blit(TUNNEL_EQUALS_3_2, POS_TUNNEL_EQUALS_3_2)

            WIN.blit(TUNNEL_EQUALS_4_0, POS_TUNNEL_EQUALS_4_0)
            WIN.blit(TUNNEL_EQUALS_4_1, POS_TUNNEL_EQUALS_4_1)
            WIN.blit(TUNNEL_EQUALS_4_2, POS_TUNNEL_EQUALS_4_2)

            WIN.blit(TUNNEL_EQUALS_5_0, POS_TUNNEL_EQUALS_5_0)
            WIN.blit(TUNNEL_EQUALS_5_1, POS_TUNNEL_EQUALS_5_1)
            WIN.blit(TUNNEL_EQUALS_5_2, POS_TUNNEL_EQUALS_5_2)

            WIN.blit(TUNNEL_EQUALS_6_0, POS_TUNNEL_EQUALS_6_0)
            WIN.blit(TUNNEL_EQUALS_6_1, POS_TUNNEL_EQUALS_6_1)
            WIN.blit(TUNNEL_EQUALS_6_2, POS_TUNNEL_EQUALS_6_2)

            WIN.blit(TUNNEL_EQUALS_7_0, POS_TUNNEL_EQUALS_7_0)
            WIN.blit(TUNNEL_EQUALS_7_1, POS_TUNNEL_EQUALS_7_1)
            WIN.blit(TUNNEL_EQUALS_7_2, POS_TUNNEL_EQUALS_7_2)

            WIN.blit(TUNNEL_EQUALS_8_0, POS_TUNNEL_EQUALS_8_0)
            WIN.blit(TUNNEL_EQUALS_8_1, POS_TUNNEL_EQUALS_8_1)
            WIN.blit(TUNNEL_EQUALS_8_2, POS_TUNNEL_EQUALS_8_2)

            WIN.blit(TUNNEL_EQUALS_9_0, POS_TUNNEL_EQUALS_9_0)
            WIN.blit(TUNNEL_EQUALS_9_1, POS_TUNNEL_EQUALS_9_1)
            WIN.blit(TUNNEL_EQUALS_9_2, POS_TUNNEL_EQUALS_9_2)

        WIN.blit(SCORE, POS_SCORE)
        WIN.blit(PAUSE, POS_PAUSE)

    while run_lvl:

        if game_is_on:
            current_time = pygame.time.get_ticks()
            NEW_TIMER += 17
        else:
            current_time = 0
            NEW_TIMER = 0

        def reset_tunnels():
            POS_TUNNEL_0_0[0] = ST_OFFSET_TUNNEL_0+33
            POS_TUNNEL_0_1[0] = ST_OFFSET_TUNNEL_0+33
            POS_TUNNEL_0_2[0] = ST_OFFSET_TUNNEL_0+33

            POS_TUNNEL_1_0[0] = ST_OFFSET_TUNNEL_1
            POS_TUNNEL_1_1[0] = ST_OFFSET_TUNNEL_1
            POS_TUNNEL_1_2[0] = ST_OFFSET_TUNNEL_1

        def move_tunnels():
            POS_TUNNEL_0_0[0] -= speed*acceleration
            POS_TUNNEL_0_1[0] -= speed*acceleration
            POS_TUNNEL_0_2[0] -= speed*acceleration

            POS_TUNNEL_1_0[0] -= speed*acceleration
            POS_TUNNEL_1_1[0] -= speed*acceleration
            POS_TUNNEL_1_2[0] -= speed*acceleration

        def equals_reset_0():
            POS_TUNNEL_EQUALS_0_0[0] = -WIDTH
            POS_TUNNEL_EQUALS_0_1[0] = -WIDTH
            POS_TUNNEL_EQUALS_0_2[0] = -WIDTH

        def equals_reset_1():
            POS_TUNNEL_EQUALS_1_0[0] = -WIDTH
            POS_TUNNEL_EQUALS_1_1[0] = -WIDTH
            POS_TUNNEL_EQUALS_1_2[0] = -WIDTH

        def equals_reset_2():
            POS_TUNNEL_EQUALS_2_0[0] = -WIDTH
            POS_TUNNEL_EQUALS_2_1[0] = -WIDTH
            POS_TUNNEL_EQUALS_2_2[0] = -WIDTH

        def equals_reset_3():
            POS_TUNNEL_EQUALS_3_0[0] = -WIDTH
            POS_TUNNEL_EQUALS_3_1[0] = -WIDTH
            POS_TUNNEL_EQUALS_3_2[0] = -WIDTH

        def equals_reset_4():
            POS_TUNNEL_EQUALS_4_0[0] = -WIDTH
            POS_TUNNEL_EQUALS_4_1[0] = -WIDTH
            POS_TUNNEL_EQUALS_4_2[0] = -WIDTH

        def equals_reset_5():
            POS_TUNNEL_EQUALS_5_0[0] = -WIDTH
            POS_TUNNEL_EQUALS_5_1[0] = -WIDTH
            POS_TUNNEL_EQUALS_5_2[0] = -WIDTH

        def equals_reset_6():
            POS_TUNNEL_EQUALS_6_0[0] = -WIDTH
            POS_TUNNEL_EQUALS_6_1[0] = -WIDTH
            POS_TUNNEL_EQUALS_6_2[0] = -WIDTH

        def equals_reset_7():
            POS_TUNNEL_EQUALS_7_0[0] = -WIDTH
            POS_TUNNEL_EQUALS_7_1[0] = -WIDTH
            POS_TUNNEL_EQUALS_7_2[0] = -WIDTH

        def equals_reset_8():
            POS_TUNNEL_EQUALS_8_0[0] = -WIDTH
            POS_TUNNEL_EQUALS_8_1[0] = -WIDTH
            POS_TUNNEL_EQUALS_8_2[0] = -WIDTH

        def equals_reset_9():
            POS_TUNNEL_EQUALS_9_0[0] = -WIDTH
            POS_TUNNEL_EQUALS_9_1[0] = -WIDTH
            POS_TUNNEL_EQUALS_9_2[0] = -WIDTH

        def car_hits():
            if lives == 2:
                car_hit_sound()
            elif lives == 1:
                car_hit_sound_2()
            if lives > 0:
                pygame.time.wait(COLLISION_PAUSE)
        # print(f'{current_time} {NEW_TIMER}')

        draw_all()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.mixer.music.stop()
                menu_selected_sound()
                run_lvl = False
                NEW_TIMER = 0
                main_menu_music()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    ROAD_LANES += 1
                if event.key == pygame.K_UP:
                    ROAD_LANES -= 1
                if event.key == pygame.K_0:
                    game_is_on = True
                    lives = 3
                    # current_time = pygame.time.get_ticks()
                if event.key == pygame.K_9:
                    game_is_on = False
                    NEW_TIMER = 0

            if (event.type == pygame.KEYDOWN and event.key == K_RIGHT) or (event.type == pygame.KEYUP and event.key == K_LEFT):
                acceleration += 0.5
            if (event.type == pygame.KEYDOWN and event.key == K_LEFT) or (event.type == pygame.KEYUP and event.key == K_RIGHT):
                acceleration -= 0.5
            if event.type == pygame.KEYDOWN and event.key == K_RETURN and WIN_CONDITION:
                run_lvl = False
                lvl4()

        if lives == 3:
            WIN.blit(HEART, POS_HEART)
            WIN.blit(HEART, (POS_HEART[0]+60, POS_HEART[1]))
            WIN.blit(HEART, (POS_HEART[0]+120, POS_HEART[1]))
        elif lives == 2:
            WIN.blit(HEART, POS_HEART)
            WIN.blit(HEART, (POS_HEART[0]+60, POS_HEART[1]))
        elif lives == 1:
            WIN.blit(HEART, POS_HEART)

        if i <= -WIDTH:
            WIN.blit(ROAD, (i+WIDTH, 0))
            i = 0
        i -= speed*acceleration

        if ROAD_LANES == 0:
            POS_CAR[1] = HEIGHT//100*37
            POS_CAR_W[1] = HEIGHT//100*37
            POS_CAR_2[1] = HEIGHT//100*37
            POS_CAR_2_W[1] = HEIGHT//100*37
            POS_CAR_3[1] = HEIGHT//100*37
            POS_CAR_3_W[1] = HEIGHT//100*37
            POS_CAR_4[1] = HEIGHT//100*37
            # print(ROAD_LANES)
        elif ROAD_LANES == 1:
            POS_CAR[1] = HEIGHT//100*57
            POS_CAR_W[1] = HEIGHT//100*57
            POS_CAR_2[1] = HEIGHT//100*57
            POS_CAR_2_W[1] = HEIGHT//100*57
            POS_CAR_3[1] = HEIGHT//100*57
            POS_CAR_3_W[1] = HEIGHT//100*57
            POS_CAR_4[1] = HEIGHT//100*57
            # print(ROAD_LANES)
        elif ROAD_LANES == 2:
            POS_CAR[1] = HEIGHT//100*77
            POS_CAR_W[1] = HEIGHT//100*77
            POS_CAR_2[1] = HEIGHT//100*77
            POS_CAR_2_W[1] = HEIGHT//100*77
            POS_CAR_3[1] = HEIGHT//100*77
            POS_CAR_3_W[1] = HEIGHT//100*77
            POS_CAR_4[1] = HEIGHT//100*77
            # print(ROAD_LANES)
        elif ROAD_LANES > 2:
            ROAD_LANES = 2
        elif ROAD_LANES < 0:
            ROAD_LANES = 0

        if lives != 0:
            if 0 < NEW_TIMER < 3000:
                COLLISION = False

                equals_reset_0()

                reset_tunnels()

                POS_TUNNEL_EQUALS_0_0[0] = ST_OFFSET_ANSWER+35
                POS_TUNNEL_EQUALS_0_1[0] = ST_OFFSET_ANSWER+35
                POS_TUNNEL_EQUALS_0_2[0] = ST_OFFSET_ANSWER+35

            if 3000 < NEW_TIMER < 8000:
                TASK_1 = FONT.render(
                    f'{all_exercises[0][0]}x{all_exercises[0][1]}', 0, WHITE)
                POS_TASK_1 = TASK_1.get_rect()
                POS_TASK_1.center = (WIDTH//2, HEIGHT//100*8)
                WIN.blit(TASK_1, POS_TASK_1)

                move_tunnels()

                POS_TUNNEL_EQUALS_0_0[0] -= speed*acceleration
                POS_TUNNEL_EQUALS_0_1[0] -= speed*acceleration
                POS_TUNNEL_EQUALS_0_2[0] -= speed*acceleration

                if CAR_RIGHT-6 <= POS_TUNNEL_1_0[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_0_0 == False and ROAD_LANES == 0 and COLLISION == False:
                    COLLISION = True
                    lives -= 1
                    car_hits()
                    equals_reset_0()
                elif CAR_RIGHT-6 <= POS_TUNNEL_1_0[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_0_0 == True and ROAD_LANES == 0 and COLLISION == False:
                    COLLISION = True
                    gate_sound()
                    score += score_limit
                if CAR_RIGHT-6 <= POS_TUNNEL_1_1[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_0_1 == False and ROAD_LANES == 1 and COLLISION == False:
                    COLLISION = True
                    lives -= 1
                    car_hits()
                    equals_reset_0()
                elif CAR_RIGHT-6 <= POS_TUNNEL_1_1[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_0_1 == True and ROAD_LANES == 1 and COLLISION == False:
                    COLLISION = True
                    gate_sound()
                    score += score_limit
                if CAR_RIGHT-6 <= POS_TUNNEL_1_2[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_0_2 == False and ROAD_LANES == 2 and COLLISION == False:
                    COLLISION = True
                    lives -= 1
                    car_hits()
                    equals_reset_0()
                elif CAR_RIGHT-6 <= POS_TUNNEL_1_2[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_0_2 == True and ROAD_LANES == 2 and COLLISION == False:
                    COLLISION = True
                    gate_sound()
                    score += score_limit

                # print(f'{POS_TUNNEL_1_0[0]} {CAR_RIGHT} {score}')

            if 8000 < NEW_TIMER < 10000:
                COLLISION = False

                equals_reset_0()

                reset_tunnels()

                POS_TUNNEL_EQUALS_1_0[0] = ST_OFFSET_ANSWER+35
                POS_TUNNEL_EQUALS_1_1[0] = ST_OFFSET_ANSWER+35
                POS_TUNNEL_EQUALS_1_2[0] = ST_OFFSET_ANSWER+35

            if 10000 < NEW_TIMER < 15000:
                TASK_1 = FONT.render(
                    f'{all_exercises[1][0]}x{all_exercises[1][1]}', 0, WHITE)
                POS_TASK_1 = TASK_1.get_rect()
                POS_TASK_1.center = (WIDTH//2, HEIGHT//100*8)
                WIN.blit(TASK_1, POS_TASK_1)

                move_tunnels()

                POS_TUNNEL_EQUALS_1_0[0] -= speed*acceleration
                POS_TUNNEL_EQUALS_1_1[0] -= speed*acceleration
                POS_TUNNEL_EQUALS_1_2[0] -= speed*acceleration

                if CAR_RIGHT-6 <= POS_TUNNEL_1_0[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_1_0 == False and ROAD_LANES == 0 and COLLISION == False:
                    COLLISION = True
                    lives -= 1
                    car_hits()
                    equals_reset_1()
                elif CAR_RIGHT-6 <= POS_TUNNEL_1_0[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_1_0 == True and ROAD_LANES == 0 and COLLISION == False:
                    COLLISION = True
                    gate_sound()
                    score += score_limit
                if CAR_RIGHT-6 <= POS_TUNNEL_1_1[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_1_1 == False and ROAD_LANES == 1 and COLLISION == False:
                    COLLISION = True
                    lives -= 1
                    car_hits()
                    equals_reset_1()
                elif CAR_RIGHT-6 <= POS_TUNNEL_1_1[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_1_1 == True and ROAD_LANES == 1 and COLLISION == False:
                    COLLISION = True
                    gate_sound()
                    score += score_limit
                if CAR_RIGHT-6 <= POS_TUNNEL_1_2[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_1_2 == False and ROAD_LANES == 2 and COLLISION == False:
                    COLLISION = True
                    lives -= 1
                    car_hits()
                    equals_reset_1()
                elif CAR_RIGHT-6 <= POS_TUNNEL_1_2[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_1_2 == True and ROAD_LANES == 2 and COLLISION == False:
                    COLLISION = True
                    gate_sound()
                    score += score_limit

                # print(f'{POS_TUNNEL_1_0[0]} {CAR_RIGHT} {score}')

            if 15000 < NEW_TIMER < 17000:
                COLLISION = False

                equals_reset_1()

                reset_tunnels()

                POS_TUNNEL_EQUALS_2_0[0] = ST_OFFSET_ANSWER+35
                POS_TUNNEL_EQUALS_2_1[0] = ST_OFFSET_ANSWER+35
                POS_TUNNEL_EQUALS_2_2[0] = ST_OFFSET_ANSWER+35

            if 17000 < NEW_TIMER < 22000:
                TASK_1 = FONT.render(
                    f'{all_exercises[2][0]}x{all_exercises[2][1]}', 0, WHITE)
                POS_TASK_1 = TASK_1.get_rect()
                POS_TASK_1.center = (WIDTH//2, HEIGHT//100*8)
                WIN.blit(TASK_1, POS_TASK_1)

                move_tunnels()

                POS_TUNNEL_EQUALS_2_0[0] -= speed*acceleration
                POS_TUNNEL_EQUALS_2_1[0] -= speed*acceleration
                POS_TUNNEL_EQUALS_2_2[0] -= speed*acceleration

                if CAR_RIGHT-6 <= POS_TUNNEL_1_0[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_2_0 == False and ROAD_LANES == 0 and COLLISION == False:
                    COLLISION = True
                    lives -= 1
                    car_hits()
                    equals_reset_2()
                elif CAR_RIGHT-6 <= POS_TUNNEL_1_0[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_2_0 == True and ROAD_LANES == 0 and COLLISION == False:
                    COLLISION = True
                    gate_sound()
                    score += score_limit
                if CAR_RIGHT-6 <= POS_TUNNEL_1_1[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_2_1 == False and ROAD_LANES == 1 and COLLISION == False:
                    COLLISION = True
                    lives -= 1
                    car_hits()
                    equals_reset_2()
                elif CAR_RIGHT-6 <= POS_TUNNEL_1_1[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_2_1 == True and ROAD_LANES == 1 and COLLISION == False:
                    COLLISION = True
                    gate_sound()
                    score += score_limit
                if CAR_RIGHT-6 <= POS_TUNNEL_1_2[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_2_2 == False and ROAD_LANES == 2 and COLLISION == False:
                    COLLISION = True
                    lives -= 1
                    car_hits()
                    equals_reset_2()
                elif CAR_RIGHT-6 <= POS_TUNNEL_1_2[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_2_2 == True and ROAD_LANES == 2 and COLLISION == False:
                    COLLISION = True
                    gate_sound()
                    score += score_limit

                # print(f'{POS_TUNNEL_1_0[0]} {CAR_RIGHT} {score}')

            if 22000 < NEW_TIMER < 24000:
                COLLISION = False

                equals_reset_2()

                reset_tunnels()

                POS_TUNNEL_EQUALS_3_0[0] = ST_OFFSET_ANSWER+35
                POS_TUNNEL_EQUALS_3_1[0] = ST_OFFSET_ANSWER+35
                POS_TUNNEL_EQUALS_3_2[0] = ST_OFFSET_ANSWER+35

            if 24000 < NEW_TIMER < 29000:
                TASK_1 = FONT.render(
                    f'{all_exercises[3][0]}x{all_exercises[3][1]}', 0, WHITE)
                POS_TASK_1 = TASK_1.get_rect()
                POS_TASK_1.center = (WIDTH//2, HEIGHT//100*8)
                WIN.blit(TASK_1, POS_TASK_1)

                move_tunnels()

                POS_TUNNEL_EQUALS_3_0[0] -= speed*acceleration
                POS_TUNNEL_EQUALS_3_1[0] -= speed*acceleration
                POS_TUNNEL_EQUALS_3_2[0] -= speed*acceleration

                if CAR_RIGHT-6 <= POS_TUNNEL_1_0[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_3_0 == False and ROAD_LANES == 0 and COLLISION == False:
                    COLLISION = True
                    lives -= 1
                    car_hits()
                    equals_reset_3()
                elif CAR_RIGHT-6 <= POS_TUNNEL_1_0[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_3_0 == True and ROAD_LANES == 0 and COLLISION == False:
                    COLLISION = True
                    gate_sound()
                    score += score_limit
                if CAR_RIGHT-6 <= POS_TUNNEL_1_1[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_3_1 == False and ROAD_LANES == 1 and COLLISION == False:
                    COLLISION = True
                    lives -= 1
                    car_hits()
                    equals_reset_3()
                elif CAR_RIGHT-6 <= POS_TUNNEL_1_1[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_3_1 == True and ROAD_LANES == 1 and COLLISION == False:
                    COLLISION = True
                    gate_sound()
                    score += score_limit
                if CAR_RIGHT-6 <= POS_TUNNEL_1_2[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_3_2 == False and ROAD_LANES == 2 and COLLISION == False:
                    COLLISION = True
                    lives -= 1
                    car_hits()
                    equals_reset_3()
                elif CAR_RIGHT-6 <= POS_TUNNEL_1_2[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_3_2 == True and ROAD_LANES == 2 and COLLISION == False:
                    COLLISION = True
                    gate_sound()
                    score += score_limit

                # print(f'{POS_TUNNEL_1_0[0]} {CAR_RIGHT} {score}')

            if 29000 < NEW_TIMER < 31000:
                COLLISION = False

                equals_reset_3()

                reset_tunnels()

                POS_TUNNEL_EQUALS_4_0[0] = ST_OFFSET_ANSWER+35
                POS_TUNNEL_EQUALS_4_1[0] = ST_OFFSET_ANSWER+35
                POS_TUNNEL_EQUALS_4_2[0] = ST_OFFSET_ANSWER+35

            if 31000 < NEW_TIMER < 36000:
                TASK_1 = FONT.render(
                    f'{all_exercises[4][0]}x{all_exercises[4][1]}', 0, WHITE)
                POS_TASK_1 = TASK_1.get_rect()
                POS_TASK_1.center = (WIDTH//2, HEIGHT//100*8)
                WIN.blit(TASK_1, POS_TASK_1)

                move_tunnels()

                POS_TUNNEL_EQUALS_4_0[0] -= speed*acceleration
                POS_TUNNEL_EQUALS_4_1[0] -= speed*acceleration
                POS_TUNNEL_EQUALS_4_2[0] -= speed*acceleration

                if CAR_RIGHT-6 <= POS_TUNNEL_1_0[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_4_0 == False and ROAD_LANES == 0 and COLLISION == False:
                    COLLISION = True
                    lives -= 1
                    car_hits()
                    equals_reset_4()
                elif CAR_RIGHT-6 <= POS_TUNNEL_1_0[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_4_0 == True and ROAD_LANES == 0 and COLLISION == False:
                    COLLISION = True
                    gate_sound()
                    score += score_limit
                if CAR_RIGHT-6 <= POS_TUNNEL_1_1[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_4_1 == False and ROAD_LANES == 1 and COLLISION == False:
                    COLLISION = True
                    lives -= 1
                    car_hits()
                    equals_reset_4()
                elif CAR_RIGHT-6 <= POS_TUNNEL_1_1[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_4_1 == True and ROAD_LANES == 1 and COLLISION == False:
                    COLLISION = True
                    gate_sound()
                    score += score_limit
                if CAR_RIGHT-6 <= POS_TUNNEL_1_2[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_4_2 == False and ROAD_LANES == 2 and COLLISION == False:
                    COLLISION = True
                    lives -= 1
                    car_hits()
                    equals_reset_4()
                elif CAR_RIGHT-6 <= POS_TUNNEL_1_2[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_4_2 == True and ROAD_LANES == 2 and COLLISION == False:
                    COLLISION = True
                    gate_sound()
                    score += score_limit

                # print(f'{POS_TUNNEL_1_0[0]} {CAR_RIGHT} {score}')

            if 36000 < NEW_TIMER < 38000:
                COLLISION = False

                equals_reset_4()

                reset_tunnels()

                POS_TUNNEL_EQUALS_5_0[0] = ST_OFFSET_ANSWER+35
                POS_TUNNEL_EQUALS_5_1[0] = ST_OFFSET_ANSWER+35
                POS_TUNNEL_EQUALS_5_2[0] = ST_OFFSET_ANSWER+35

            if 38000 < NEW_TIMER < 43000:
                TASK_1 = FONT.render(
                    f'{all_exercises[5][0]}x{all_exercises[5][1]}', 0, WHITE)
                POS_TASK_1 = TASK_1.get_rect()
                POS_TASK_1.center = (WIDTH//2, HEIGHT//100*8)
                WIN.blit(TASK_1, POS_TASK_1)

                move_tunnels()

                POS_TUNNEL_EQUALS_5_0[0] -= speed*acceleration
                POS_TUNNEL_EQUALS_5_1[0] -= speed*acceleration
                POS_TUNNEL_EQUALS_5_2[0] -= speed*acceleration

                if CAR_RIGHT-6 <= POS_TUNNEL_1_0[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_5_0 == False and ROAD_LANES == 0 and COLLISION == False:
                    COLLISION = True
                    lives -= 1
                    car_hits()
                    equals_reset_5()
                elif CAR_RIGHT-6 <= POS_TUNNEL_1_0[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_5_0 == True and ROAD_LANES == 0 and COLLISION == False:
                    COLLISION = True
                    gate_sound()
                    score += score_limit
                if CAR_RIGHT-6 <= POS_TUNNEL_1_1[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_5_1 == False and ROAD_LANES == 1 and COLLISION == False:
                    COLLISION = True
                    lives -= 1
                    car_hits()
                    equals_reset_5()
                elif CAR_RIGHT-6 <= POS_TUNNEL_1_1[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_5_1 == True and ROAD_LANES == 1 and COLLISION == False:
                    COLLISION = True
                    gate_sound()
                    score += score_limit
                if CAR_RIGHT-6 <= POS_TUNNEL_1_2[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_5_2 == False and ROAD_LANES == 2 and COLLISION == False:
                    COLLISION = True
                    lives -= 1
                    car_hits()
                    equals_reset_5()
                elif CAR_RIGHT-6 <= POS_TUNNEL_1_2[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_5_2 == True and ROAD_LANES == 2 and COLLISION == False:
                    COLLISION = True
                    gate_sound()
                    score += score_limit

                # print(f'{POS_TUNNEL_1_0[0]} {CAR_RIGHT} {score}')

            if 43000 < NEW_TIMER < 45000:
                COLLISION = False

                equals_reset_5()

                reset_tunnels()

                POS_TUNNEL_EQUALS_6_0[0] = ST_OFFSET_ANSWER+35
                POS_TUNNEL_EQUALS_6_1[0] = ST_OFFSET_ANSWER+35
                POS_TUNNEL_EQUALS_6_2[0] = ST_OFFSET_ANSWER+35

            if 45000 < NEW_TIMER < 50000:
                TASK_1 = FONT.render(
                    f'{all_exercises[6][0]}x{all_exercises[6][1]}', 0, WHITE)
                POS_TASK_1 = TASK_1.get_rect()
                POS_TASK_1.center = (WIDTH//2, HEIGHT//100*8)
                WIN.blit(TASK_1, POS_TASK_1)

                move_tunnels()

                POS_TUNNEL_EQUALS_6_0[0] -= speed*acceleration
                POS_TUNNEL_EQUALS_6_1[0] -= speed*acceleration
                POS_TUNNEL_EQUALS_6_2[0] -= speed*acceleration

                if CAR_RIGHT-6 <= POS_TUNNEL_1_0[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_6_0 == False and ROAD_LANES == 0 and COLLISION == False:
                    COLLISION = True
                    lives -= 1
                    car_hits()
                    equals_reset_6()
                elif CAR_RIGHT-6 <= POS_TUNNEL_1_0[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_6_0 == True and ROAD_LANES == 0 and COLLISION == False:
                    COLLISION = True
                    gate_sound()
                    score += score_limit
                if CAR_RIGHT-6 <= POS_TUNNEL_1_1[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_6_1 == False and ROAD_LANES == 1 and COLLISION == False:
                    COLLISION = True
                    lives -= 1
                    car_hits()
                    equals_reset_6()
                elif CAR_RIGHT-6 <= POS_TUNNEL_1_1[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_6_1 == True and ROAD_LANES == 1 and COLLISION == False:
                    COLLISION = True
                    gate_sound()
                    score += score_limit
                if CAR_RIGHT-6 <= POS_TUNNEL_1_2[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_6_2 == False and ROAD_LANES == 2 and COLLISION == False:
                    COLLISION = True
                    lives -= 1
                    car_hits()
                    equals_reset_6()
                elif CAR_RIGHT-6 <= POS_TUNNEL_1_2[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_6_2 == True and ROAD_LANES == 2 and COLLISION == False:
                    COLLISION = True
                    gate_sound()
                    score += score_limit

                # print(f'{POS_TUNNEL_1_0[0]} {CAR_RIGHT} {score}')

            if 50000 < NEW_TIMER < 52000:
                COLLISION = False

                equals_reset_6()

                reset_tunnels()

                POS_TUNNEL_EQUALS_7_0[0] = ST_OFFSET_ANSWER+35
                POS_TUNNEL_EQUALS_7_1[0] = ST_OFFSET_ANSWER+35
                POS_TUNNEL_EQUALS_7_2[0] = ST_OFFSET_ANSWER+35

            if 52000 < NEW_TIMER < 57000:
                TASK_1 = FONT.render(
                    f'{all_exercises[7][0]}x{all_exercises[7][1]}', 0, WHITE)
                POS_TASK_1 = TASK_1.get_rect()
                POS_TASK_1.center = (WIDTH//2, HEIGHT//100*8)
                WIN.blit(TASK_1, POS_TASK_1)

                move_tunnels()

                POS_TUNNEL_EQUALS_7_0[0] -= speed*acceleration
                POS_TUNNEL_EQUALS_7_1[0] -= speed*acceleration
                POS_TUNNEL_EQUALS_7_2[0] -= speed*acceleration

                if CAR_RIGHT-6 <= POS_TUNNEL_1_0[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_7_0 == False and ROAD_LANES == 0 and COLLISION == False:
                    COLLISION = True
                    lives -= 1
                    car_hits()
                    equals_reset_7()
                elif CAR_RIGHT-6 <= POS_TUNNEL_1_0[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_7_0 == True and ROAD_LANES == 0 and COLLISION == False:
                    COLLISION = True
                    gate_sound()
                    score += score_limit
                if CAR_RIGHT-6 <= POS_TUNNEL_1_1[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_7_1 == False and ROAD_LANES == 1 and COLLISION == False:
                    COLLISION = True
                    lives -= 1
                    car_hits()
                    equals_reset_7()
                elif CAR_RIGHT-6 <= POS_TUNNEL_1_1[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_7_1 == True and ROAD_LANES == 1 and COLLISION == False:
                    COLLISION = True
                    gate_sound()
                    score += score_limit
                if CAR_RIGHT-6 <= POS_TUNNEL_1_2[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_7_2 == False and ROAD_LANES == 2 and COLLISION == False:
                    COLLISION = True
                    lives -= 1
                    car_hits()
                    equals_reset_7()
                elif CAR_RIGHT-6 <= POS_TUNNEL_1_2[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_7_2 == True and ROAD_LANES == 2 and COLLISION == False:
                    COLLISION = True
                    gate_sound()
                    score += score_limit

                # print(f'{POS_TUNNEL_1_0[0]} {CAR_RIGHT} {score}')

            if 57000 < NEW_TIMER < 59000:
                COLLISION = False

                equals_reset_7()

                reset_tunnels()

                POS_TUNNEL_EQUALS_8_0[0] = ST_OFFSET_ANSWER+35
                POS_TUNNEL_EQUALS_8_1[0] = ST_OFFSET_ANSWER+35
                POS_TUNNEL_EQUALS_8_2[0] = ST_OFFSET_ANSWER+35

            if 59000 < NEW_TIMER < 64000:
                TASK_1 = FONT.render(
                    f'{all_exercises[8][0]}x{all_exercises[8][1]}', 0, WHITE)
                POS_TASK_1 = TASK_1.get_rect()
                POS_TASK_1.center = (WIDTH//2, HEIGHT//100*8)
                WIN.blit(TASK_1, POS_TASK_1)

                move_tunnels()

                POS_TUNNEL_EQUALS_8_0[0] -= speed*acceleration
                POS_TUNNEL_EQUALS_8_1[0] -= speed*acceleration
                POS_TUNNEL_EQUALS_8_2[0] -= speed*acceleration

                if CAR_RIGHT-6 <= POS_TUNNEL_1_0[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_8_0 == False and ROAD_LANES == 0 and COLLISION == False:
                    COLLISION = True
                    lives -= 1
                    car_hits()
                    equals_reset_8()
                elif CAR_RIGHT-6 <= POS_TUNNEL_1_0[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_8_0 == True and ROAD_LANES == 0 and COLLISION == False:
                    COLLISION = True
                    gate_sound()
                    score += score_limit
                if CAR_RIGHT-6 <= POS_TUNNEL_1_1[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_8_1 == False and ROAD_LANES == 1 and COLLISION == False:
                    COLLISION = True
                    lives -= 1
                    car_hits()
                    equals_reset_8()
                elif CAR_RIGHT-6 <= POS_TUNNEL_1_1[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_8_1 == True and ROAD_LANES == 1 and COLLISION == False:
                    COLLISION = True
                    gate_sound()
                    score += score_limit
                if CAR_RIGHT-6 <= POS_TUNNEL_1_2[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_8_2 == False and ROAD_LANES == 2 and COLLISION == False:
                    COLLISION = True
                    lives -= 1
                    car_hits()
                    equals_reset_8()
                elif CAR_RIGHT-6 <= POS_TUNNEL_1_2[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_8_2 == True and ROAD_LANES == 2 and COLLISION == False:
                    COLLISION = True
                    gate_sound()
                    score += score_limit

                # print(f'{POS_TUNNEL_1_0[0]} {CAR_RIGHT} {score}')

            if 64000 < NEW_TIMER < 66000:
                COLLISION = False

                equals_reset_8()

                reset_tunnels()

                POS_TUNNEL_EQUALS_9_0[0] = ST_OFFSET_ANSWER+35
                POS_TUNNEL_EQUALS_9_1[0] = ST_OFFSET_ANSWER+35
                POS_TUNNEL_EQUALS_9_2[0] = ST_OFFSET_ANSWER+35

            if 66000 < NEW_TIMER < 71000:
                TASK_1 = FONT.render(
                    f'{all_exercises[9][0]}x{all_exercises[9][1]}', 0, WHITE)
                POS_TASK_1 = TASK_1.get_rect()
                POS_TASK_1.center = (WIDTH//2, HEIGHT//100*8)
                WIN.blit(TASK_1, POS_TASK_1)

                move_tunnels()

                POS_TUNNEL_EQUALS_9_0[0] -= speed*acceleration
                POS_TUNNEL_EQUALS_9_1[0] -= speed*acceleration
                POS_TUNNEL_EQUALS_9_2[0] -= speed*acceleration

                if CAR_RIGHT-6 <= POS_TUNNEL_1_0[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_9_0 == False and ROAD_LANES == 0 and COLLISION == False:
                    COLLISION = True
                    lives -= 1
                    car_hits()
                    equals_reset_9()
                elif CAR_RIGHT-6 <= POS_TUNNEL_1_0[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_9_0 == True and ROAD_LANES == 0 and COLLISION == False:
                    COLLISION = True
                    gate_sound()
                    score += score_limit
                if CAR_RIGHT-6 <= POS_TUNNEL_1_1[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_9_1 == False and ROAD_LANES == 1 and COLLISION == False:
                    COLLISION = True
                    lives -= 1
                    car_hits()
                    equals_reset_9()
                elif CAR_RIGHT-6 <= POS_TUNNEL_1_1[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_9_1 == True and ROAD_LANES == 1 and COLLISION == False:
                    COLLISION = True
                    gate_sound()
                    score += score_limit
                if CAR_RIGHT-6 <= POS_TUNNEL_1_2[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_9_2 == False and ROAD_LANES == 2 and COLLISION == False:
                    COLLISION = True
                    lives -= 1
                    car_hits()
                    equals_reset_9()
                elif CAR_RIGHT-6 <= POS_TUNNEL_1_2[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_9_2 == True and ROAD_LANES == 2 and COLLISION == False:
                    COLLISION = True
                    gate_sound()
                    score += score_limit

                # print(f'{POS_TUNNEL_1_0[0]} {CAR_RIGHT} {score}')

            if 71000 < NEW_TIMER < 73000:
                COLLISION = False

                equals_reset_9()

                reset_tunnels()

            if 73000 < NEW_TIMER:
                if 73001 < NEW_TIMER < 73018:
                    lvl_complete_sound()
                WIN_CONDITION = True
                WIN.blit(MAIN_MENU_BACK, POS_BACK)
                GAME_OVER = FONT.render(f'ПОБЕДА!', 0, WHITE)
                POS_GAME_OVER = GAME_OVER.get_rect(
                    center=(WIDTH//2, HEIGHT//2-100))
                GAME_OVER_SCORE = FONT.render(f'ВАШ СЧЕТ: {score}', 0, WHITE)
                POS_GAME_OVER_SCORE = GAME_OVER_SCORE.get_rect(
                    center=(WIDTH//2, HEIGHT//2))
                GAME_OVER_PRESS_ESC = FONT_SCORE.render(
                    f'След уровень: ENTER', 0, WHITE)
                POS_GAME_OVER_PRESS_ESC = GAME_OVER_PRESS_ESC.get_rect(
                    center=(WIDTH//2, HEIGHT//100*70))
                WIN.blit(GAME_OVER, POS_GAME_OVER)
                WIN.blit(GAME_OVER_SCORE, POS_GAME_OVER_SCORE)
                WIN.blit(GAME_OVER_PRESS_ESC, POS_GAME_OVER_PRESS_ESC)

        if lives != 0:
            SCORE_0 = FONT_SCORE.render(f'{score}', 0, WHITE)
            POS_SCORE_0 = SCORE_0.get_rect(
                center=(WIDTH//100*92, HEIGHT//100*99+30))
            WIN.blit(SCORE_0, POS_SCORE_0)
        else:
            if GAME_OVER_SOUND_FLAG == False:
                game_over_sound()
                GAME_OVER_SOUND_FLAG = True
            WIN.blit(MAIN_MENU_BACK, POS_BACK)
            GAME_OVER = FONT.render(f'GAME OVER', 0, WHITE)
            POS_GAME_OVER = GAME_OVER.get_rect(center=(WIDTH//2, HEIGHT//2-100))
            GAME_OVER.set_alpha(100)
            GAME_OVER_SCORE = FONT.render(f'ВАШ СЧЕТ: {score}', 0, WHITE)
            POS_GAME_OVER_SCORE = GAME_OVER_SCORE.get_rect(center=(WIDTH//2, HEIGHT//2))
            GAME_OVER_PRESS_ESC = FONT_SCORE.render(f'МЕНЮ: ESC', 0, WHITE)
            POS_GAME_OVER_PRESS_ESC = GAME_OVER_PRESS_ESC.get_rect(center=(WIDTH//2, HEIGHT//100*70))
            WIN.blit(GAME_OVER, POS_GAME_OVER)
            WIN.blit(GAME_OVER_SCORE, POS_GAME_OVER_SCORE)
            WIN.blit(GAME_OVER_PRESS_ESC, POS_GAME_OVER_PRESS_ESC)

        if game_is_on:
            pygame.display.flip()
        else:
            NEW_TIMER = 0

        clock.tick(FPS)




def lvl4():

    lvl4_music()

    BG = pygame.image.load('img/lvl4/sunset.png')
    POS_BG = BG.get_rect(center=(WIDTH//2, HEIGHT//2))

    ROAD = pygame.image.load('img/lvl4/road.png').convert_alpha()

    CAR = pygame.image.load('img/lvl4/car.png').convert_alpha()
    CAR_WIDTH = CAR.get_width()
    POS_CAR = CAR.get_rect()
    POS_CAR.center = WIDTH//100*20, HEIGHT//100*57
    CAR_RIGHT = POS_CAR[0]+CAR_WIDTH

    CAR_W = pygame.image.load('img/lvl4/car_w.png').convert_alpha()
    CAR_W_WIDTH = CAR_W.get_width()
    POS_CAR_W = CAR_W.get_rect()
    POS_CAR_W.center = WIDTH//100*20, HEIGHT//100*57
    CAR_W_RIGHT = POS_CAR_W[0]+CAR_W_WIDTH

    CAR_2 = pygame.image.load('img/lvl4/car_crashed_1.png').convert_alpha()
    CAR_2_WIDTH = CAR_2.get_width()
    POS_CAR_2 = CAR_2.get_rect()
    POS_CAR_2.center = WIDTH//100*20, HEIGHT//100*57
    CAR_2_RIGHT = POS_CAR_2[0]+CAR_2_WIDTH

    CAR_2_W = pygame.image.load('img/lvl4/car_crashed_1_w.png').convert_alpha()
    CAR_2_W_WIDTH = CAR_2_W.get_width()
    POS_CAR_2_W = CAR_2_W.get_rect()
    POS_CAR_2_W.center = WIDTH//100*20, HEIGHT//100*57
    CAR_2_W_RIGHT = POS_CAR_2_W[0]+CAR_2_W_WIDTH

    CAR_3 = pygame.image.load('img/lvl4/car_crashed_2.png').convert_alpha()
    CAR_3_WIDTH = CAR_3.get_width()
    POS_CAR_3 = CAR_3.get_rect()
    POS_CAR_3.center = WIDTH//100*20, HEIGHT//100*57
    CAR_3_RIGHT = POS_CAR_3[0]+CAR_3_WIDTH

    CAR_3_W = pygame.image.load('img/lvl4/car_crashed_2_w.png').convert_alpha()
    CAR_3_W_WIDTH = CAR_3_W.get_width()
    POS_CAR_3_W = CAR_3_W.get_rect()
    POS_CAR_3_W.center = WIDTH//100*20, HEIGHT//100*57
    CAR_3_W_RIGHT = POS_CAR_3_W[0]+CAR_3_W_WIDTH

    CAR_4 = pygame.image.load('img/lvl4/car_crashed_3.png').convert_alpha()
    CAR_4_WIDTH = CAR_4.get_width()
    POS_CAR_4 = CAR_4.get_rect()
    POS_CAR_4.center = WIDTH//100*20, HEIGHT//100*57
    CAR_4_RIGHT = POS_CAR_4[0]+CAR_4_WIDTH

    TASK = pygame.image.load('img/lvl4/task.png').convert_alpha()
    POS_TASK = TASK.get_rect(center=(WIDTH//2, HEIGHT//100*8))
    SCORE = pygame.image.load('img/lvl4/score.png').convert_alpha()
    POS_SCORE = SCORE.get_rect(center=(WIDTH//100*92, HEIGHT//100*99+30))
    PAUSE = pygame.image.load('img/lvl4/pause.png').convert_alpha()
    POS_PAUSE = PAUSE.get_rect(center=(WIDTH//100*92, HEIGHT//100*6))

    ST_OFFSET_TUNNEL_0 = WIDTH+100
    ST_OFFSET_TUNNEL_1 = WIDTH+100+100
    ST_OFFSET_ANSWER = WIDTH+195

    TUNNEL_0 = pygame.image.load('img/lvl4/tunnel_0.png').convert_alpha()
    POS_TUNNEL_0_0 = TUNNEL_0.get_rect()
    POS_TUNNEL_0_0.center = ST_OFFSET_TUNNEL_0, HEIGHT//100*46
    POS_TUNNEL_0_1 = TUNNEL_0.get_rect()
    POS_TUNNEL_0_1.center = ST_OFFSET_TUNNEL_0, HEIGHT//100*66
    POS_TUNNEL_0_2 = TUNNEL_0.get_rect()
    POS_TUNNEL_0_2.center = ST_OFFSET_TUNNEL_0, HEIGHT//100*86

    TUNNEL_1 = pygame.image.load('img/lvl4/tunnel_1.png').convert_alpha()
    POS_TUNNEL_1_0 = TUNNEL_1.get_rect()
    POS_TUNNEL_1_0.center = ST_OFFSET_TUNNEL_1, HEIGHT//100*46
    POS_TUNNEL_1_1 = TUNNEL_1.get_rect()
    POS_TUNNEL_1_1.center = ST_OFFSET_TUNNEL_1, HEIGHT//100*66
    POS_TUNNEL_1_2 = TUNNEL_1.get_rect()
    POS_TUNNEL_1_2.center = ST_OFFSET_TUNNEL_1, HEIGHT//100*86

    run_lvl = True
    clock = pygame.time.Clock()
    i = 0
    exercises = 10
    FPS = 60
    NEW_TIMER = 0
    ROAD_LANES = 1
    lives = 3
    score = 0
    score_limit = 1
    COLLISION = False
    COLLISION_PAUSE = 1000
    game_is_on = True
    current_time = 0
    speed = 8
    acceleration = 1.0
    GAME_OVER_SOUND_FLAG = False
    CAR_HIT_SOUND_FLAG = False
    CAR_HIT_2_SOUND_FLAG = False
    WIN_CONDITION = False
    pressed = pygame.key.get_pressed()

    all_exercises, all_answers, all_answer_flag, all_answer_flags_last = [], [], [], []

    for exercise in range(10):
        first_sum_prep = random.randint(1, 9)
        second_sum_prep = random.randint(1, 9)
        sum_prep = first_sum_prep * second_sum_prep
        
        first_sum = sum_prep
        second_sum = second_sum_prep

        sum_true = int(first_sum/second_sum)

        if sum_true > 89:
            sum_fake_1 = sum_true + random.randint(-10, 1)
            sum_fake_2 = sum_true + random.randint(-10, 1)
        elif sum_true < 11:
            sum_fake_1 = sum_true + random.randint(1, 10)
            sum_fake_2 = sum_true + random.randint(1, 10)
        else:
            sum_fake_1 = sum_true + random.randint(-10, 10)
            sum_fake_2 = sum_true + random.randint(-10, 10)

        if sum_true == sum_fake_1 or sum_true == sum_fake_2 or sum_fake_1 == sum_fake_2:
            # print(f'{sum_true} {sum_fake_1} {sum_fake_2}')

            if sum_true == sum_fake_1:
                sum_fake_1 += 1
            if sum_true == sum_fake_2:
                sum_fake_2 += 2
            if sum_fake_1 == sum_fake_2:
                sum_fake_1 += 1
                sum_fake_2 -= 2

            # print(f'{sum_true} {sum_fake_1} {sum_fake_2}')

        # if sum_true == sum_fake_1 or sum_true
        all_exercises.append(
            [first_sum, second_sum, sum_true, sum_fake_1, sum_fake_2])
        all_answers.append([sum_true, sum_fake_1, sum_fake_2])

    print(all_exercises)
    # print(all_answers)

    for all_answer in all_answers:
        new_answers = all_answer
        random.shuffle(new_answers)

    # print(all_answers)

    jj = 0

    for all_answer in all_answers:
        for a_a in all_answer:
            kk = math.floor(jj/3)
            jj += 1
            if a_a == all_exercises[kk][2]:
                all_answer_flag.append(True)
            else:
                all_answer_flag.append(False)
            # print(f'{kk} {a_a} {all_exercises[kk][2]}')
    # print(all_answer_flag)

    TUNNEL_EQUALS_0_0 = FONT.render(f'{all_answers[0][0]}', 0, WHITE)
    POS_TUNNEL_EQUALS_0_0 = TUNNEL_EQUALS_0_0.get_rect()
    POS_TUNNEL_EQUALS_0_0.center = ST_OFFSET_ANSWER, HEIGHT//100*46
    TUNNEL_LOGIC_0_0 = all_answer_flag[0]

    TUNNEL_EQUALS_0_1 = FONT.render(f'{all_answers[0][1]}', 0, WHITE)
    POS_TUNNEL_EQUALS_0_1 = TUNNEL_EQUALS_0_1.get_rect()
    POS_TUNNEL_EQUALS_0_1.center = ST_OFFSET_ANSWER, HEIGHT//100*66
    TUNNEL_LOGIC_0_1 = all_answer_flag[1]

    TUNNEL_EQUALS_0_2 = FONT.render(f'{all_answers[0][2]}', 0, WHITE)
    POS_TUNNEL_EQUALS_0_2 = TUNNEL_EQUALS_0_2.get_rect()
    POS_TUNNEL_EQUALS_0_2.center = ST_OFFSET_ANSWER, HEIGHT//100*86
    TUNNEL_LOGIC_0_2 = all_answer_flag[2]

    TUNNEL_EQUALS_1_0 = FONT.render(f'{all_answers[1][0]}', 0, WHITE)
    POS_TUNNEL_EQUALS_1_0 = TUNNEL_EQUALS_1_0.get_rect()
    POS_TUNNEL_EQUALS_1_0.center = ST_OFFSET_ANSWER, HEIGHT//100*46
    TUNNEL_LOGIC_1_0 = all_answer_flag[3]

    TUNNEL_EQUALS_1_1 = FONT.render(f'{all_answers[1][1]}', 0, WHITE)
    POS_TUNNEL_EQUALS_1_1 = TUNNEL_EQUALS_1_1.get_rect()
    POS_TUNNEL_EQUALS_1_1.center = ST_OFFSET_ANSWER, HEIGHT//100*66
    TUNNEL_LOGIC_1_1 = all_answer_flag[4]

    TUNNEL_EQUALS_1_2 = FONT.render(f'{all_answers[1][2]}', 0, WHITE)
    POS_TUNNEL_EQUALS_1_2 = TUNNEL_EQUALS_1_2.get_rect()
    POS_TUNNEL_EQUALS_1_2.center = ST_OFFSET_ANSWER, HEIGHT//100*86
    TUNNEL_LOGIC_1_2 = all_answer_flag[5]

    TUNNEL_EQUALS_2_0 = FONT.render(f'{all_answers[2][0]}', 0, WHITE)
    POS_TUNNEL_EQUALS_2_0 = TUNNEL_EQUALS_2_0.get_rect()
    POS_TUNNEL_EQUALS_2_0.center = ST_OFFSET_ANSWER, HEIGHT//100*46
    TUNNEL_LOGIC_2_0 = all_answer_flag[6]

    TUNNEL_EQUALS_2_1 = FONT.render(f'{all_answers[2][1]}', 0, WHITE)
    POS_TUNNEL_EQUALS_2_1 = TUNNEL_EQUALS_2_1.get_rect()
    POS_TUNNEL_EQUALS_2_1.center = ST_OFFSET_ANSWER, HEIGHT//100*66
    TUNNEL_LOGIC_2_1 = all_answer_flag[7]

    TUNNEL_EQUALS_2_2 = FONT.render(f'{all_answers[2][2]}', 0, WHITE)
    POS_TUNNEL_EQUALS_2_2 = TUNNEL_EQUALS_2_2.get_rect()
    POS_TUNNEL_EQUALS_2_2.center = ST_OFFSET_ANSWER, HEIGHT//100*86
    TUNNEL_LOGIC_2_2 = all_answer_flag[8]

    TUNNEL_EQUALS_3_0 = FONT.render(f'{all_answers[3][0]}', 0, WHITE)
    POS_TUNNEL_EQUALS_3_0 = TUNNEL_EQUALS_3_0.get_rect()
    POS_TUNNEL_EQUALS_3_0.center = ST_OFFSET_ANSWER, HEIGHT//100*46
    TUNNEL_LOGIC_3_0 = all_answer_flag[9]

    TUNNEL_EQUALS_3_1 = FONT.render(f'{all_answers[3][1]}', 0, WHITE)
    POS_TUNNEL_EQUALS_3_1 = TUNNEL_EQUALS_3_1.get_rect()
    POS_TUNNEL_EQUALS_3_1.center = ST_OFFSET_ANSWER, HEIGHT//100*66
    TUNNEL_LOGIC_3_1 = all_answer_flag[10]

    TUNNEL_EQUALS_3_2 = FONT.render(f'{all_answers[3][2]}', 0, WHITE)
    POS_TUNNEL_EQUALS_3_2 = TUNNEL_EQUALS_3_2.get_rect()
    POS_TUNNEL_EQUALS_3_2.center = ST_OFFSET_ANSWER, HEIGHT//100*86
    TUNNEL_LOGIC_3_2 = all_answer_flag[11]

    TUNNEL_EQUALS_4_0 = FONT.render(f'{all_answers[4][0]}', 0, WHITE)
    POS_TUNNEL_EQUALS_4_0 = TUNNEL_EQUALS_4_0.get_rect()
    POS_TUNNEL_EQUALS_4_0.center = ST_OFFSET_ANSWER, HEIGHT//100*46
    TUNNEL_LOGIC_4_0 = all_answer_flag[12]

    TUNNEL_EQUALS_4_1 = FONT.render(f'{all_answers[4][1]}', 0, WHITE)
    POS_TUNNEL_EQUALS_4_1 = TUNNEL_EQUALS_4_1.get_rect()
    POS_TUNNEL_EQUALS_4_1.center = ST_OFFSET_ANSWER, HEIGHT//100*66
    TUNNEL_LOGIC_4_1 = all_answer_flag[13]

    TUNNEL_EQUALS_4_2 = FONT.render(f'{all_answers[4][2]}', 0, WHITE)
    POS_TUNNEL_EQUALS_4_2 = TUNNEL_EQUALS_4_2.get_rect()
    POS_TUNNEL_EQUALS_4_2.center = ST_OFFSET_ANSWER, HEIGHT//100*86
    TUNNEL_LOGIC_4_2 = all_answer_flag[14]

    TUNNEL_EQUALS_5_0 = FONT.render(f'{all_answers[5][0]}', 0, WHITE)
    POS_TUNNEL_EQUALS_5_0 = TUNNEL_EQUALS_5_0.get_rect()
    POS_TUNNEL_EQUALS_5_0.center = ST_OFFSET_ANSWER, HEIGHT//100*46
    TUNNEL_LOGIC_5_0 = all_answer_flag[15]

    TUNNEL_EQUALS_5_1 = FONT.render(f'{all_answers[5][1]}', 0, WHITE)
    POS_TUNNEL_EQUALS_5_1 = TUNNEL_EQUALS_5_1.get_rect()
    POS_TUNNEL_EQUALS_5_1.center = ST_OFFSET_ANSWER, HEIGHT//100*66
    TUNNEL_LOGIC_5_1 = all_answer_flag[16]

    TUNNEL_EQUALS_5_2 = FONT.render(f'{all_answers[5][2]}', 0, WHITE)
    POS_TUNNEL_EQUALS_5_2 = TUNNEL_EQUALS_5_2.get_rect()
    POS_TUNNEL_EQUALS_5_2.center = ST_OFFSET_ANSWER, HEIGHT//100*86
    TUNNEL_LOGIC_5_2 = all_answer_flag[17]

    TUNNEL_EQUALS_6_0 = FONT.render(f'{all_answers[6][0]}', 0, WHITE)
    POS_TUNNEL_EQUALS_6_0 = TUNNEL_EQUALS_6_0.get_rect()
    POS_TUNNEL_EQUALS_6_0.center = ST_OFFSET_ANSWER, HEIGHT//100*46
    TUNNEL_LOGIC_6_0 = all_answer_flag[18]

    TUNNEL_EQUALS_6_1 = FONT.render(f'{all_answers[6][1]}', 0, WHITE)
    POS_TUNNEL_EQUALS_6_1 = TUNNEL_EQUALS_6_1.get_rect()
    POS_TUNNEL_EQUALS_6_1.center = ST_OFFSET_ANSWER, HEIGHT//100*66
    TUNNEL_LOGIC_6_1 = all_answer_flag[19]

    TUNNEL_EQUALS_6_2 = FONT.render(f'{all_answers[6][2]}', 0, WHITE)
    POS_TUNNEL_EQUALS_6_2 = TUNNEL_EQUALS_6_2.get_rect()
    POS_TUNNEL_EQUALS_6_2.center = ST_OFFSET_ANSWER, HEIGHT//100*86
    TUNNEL_LOGIC_6_2 = all_answer_flag[20]

    TUNNEL_EQUALS_7_0 = FONT.render(f'{all_answers[7][0]}', 0, WHITE)
    POS_TUNNEL_EQUALS_7_0 = TUNNEL_EQUALS_7_0.get_rect()
    POS_TUNNEL_EQUALS_7_0.center = ST_OFFSET_ANSWER, HEIGHT//100*46
    TUNNEL_LOGIC_7_0 = all_answer_flag[21]

    TUNNEL_EQUALS_7_1 = FONT.render(f'{all_answers[7][1]}', 0, WHITE)
    POS_TUNNEL_EQUALS_7_1 = TUNNEL_EQUALS_7_1.get_rect()
    POS_TUNNEL_EQUALS_7_1.center = ST_OFFSET_ANSWER, HEIGHT//100*66
    TUNNEL_LOGIC_7_1 = all_answer_flag[22]

    TUNNEL_EQUALS_7_2 = FONT.render(f'{all_answers[7][2]}', 0, WHITE)
    POS_TUNNEL_EQUALS_7_2 = TUNNEL_EQUALS_7_2.get_rect()
    POS_TUNNEL_EQUALS_7_2.center = ST_OFFSET_ANSWER, HEIGHT//100*86
    TUNNEL_LOGIC_7_2 = all_answer_flag[23]

    TUNNEL_EQUALS_8_0 = FONT.render(f'{all_answers[8][0]}', 0, WHITE)
    POS_TUNNEL_EQUALS_8_0 = TUNNEL_EQUALS_8_0.get_rect()
    POS_TUNNEL_EQUALS_8_0.center = ST_OFFSET_ANSWER, HEIGHT//100*46
    TUNNEL_LOGIC_8_0 = all_answer_flag[24]

    TUNNEL_EQUALS_8_1 = FONT.render(f'{all_answers[8][1]}', 0, WHITE)
    POS_TUNNEL_EQUALS_8_1 = TUNNEL_EQUALS_8_1.get_rect()
    POS_TUNNEL_EQUALS_8_1.center = ST_OFFSET_ANSWER, HEIGHT//100*66
    TUNNEL_LOGIC_8_1 = all_answer_flag[25]

    TUNNEL_EQUALS_8_2 = FONT.render(f'{all_answers[8][2]}', 0, WHITE)
    POS_TUNNEL_EQUALS_8_2 = TUNNEL_EQUALS_8_2.get_rect()
    POS_TUNNEL_EQUALS_8_2.center = ST_OFFSET_ANSWER, HEIGHT//100*86
    TUNNEL_LOGIC_8_2 = all_answer_flag[26]

    TUNNEL_EQUALS_9_0 = FONT.render(f'{all_answers[9][0]}', 0, WHITE)
    POS_TUNNEL_EQUALS_9_0 = TUNNEL_EQUALS_9_0.get_rect()
    POS_TUNNEL_EQUALS_9_0.center = ST_OFFSET_ANSWER, HEIGHT//100*46
    TUNNEL_LOGIC_9_0 = all_answer_flag[27]

    TUNNEL_EQUALS_9_1 = FONT.render(f'{all_answers[9][1]}', 0, WHITE)
    POS_TUNNEL_EQUALS_9_1 = TUNNEL_EQUALS_9_1.get_rect()
    POS_TUNNEL_EQUALS_9_1.center = ST_OFFSET_ANSWER, HEIGHT//100*66
    TUNNEL_LOGIC_9_1 = all_answer_flag[28]

    TUNNEL_EQUALS_9_2 = FONT.render(f'{all_answers[9][2]}', 0, WHITE)
    POS_TUNNEL_EQUALS_9_2 = TUNNEL_EQUALS_9_2.get_rect()
    POS_TUNNEL_EQUALS_9_2.center = ST_OFFSET_ANSWER, HEIGHT//100*86
    TUNNEL_LOGIC_9_2 = all_answer_flag[29]

    def draw_all():
        if lives != 0:
            WIN.blit(BG, POS_BG)
            WIN.blit(ROAD, (i, 0))
            WIN.blit(ROAD, (WIDTH+i, 0))
            # WIN.blit(ROAD, POS_ROAD)
            WIN.blit(TASK, POS_TASK)

            # WIN.blit(HEART, POS_HEART_0)
            # WIN.blit(HEART, POS_HEART_1)
            # WIN.blit(HEART, POS_HEART_2)

            WIN.blit(TUNNEL_0, POS_TUNNEL_0_0)
            WIN.blit(TUNNEL_0, POS_TUNNEL_0_1)
            WIN.blit(TUNNEL_0, POS_TUNNEL_0_2)

        ostatok = current_time // 250 % 2

        if lives == 3 and ostatok == 0:
            WIN.blit(CAR, POS_CAR)
        elif lives == 3 and ostatok != 0:
            WIN.blit(CAR_W, (POS_CAR_W[0], POS_CAR_W[1]+2))
        if lives == 2 and ostatok == 0:
            WIN.blit(CAR_2, POS_CAR_2)
        elif lives == 2 and ostatok != 0:
            WIN.blit(CAR_2_W, (POS_CAR_2_W[0], POS_CAR_2_W[1]+2))
        if lives == 1 and ostatok == 0:
            WIN.blit(CAR_3, POS_CAR_3)
        elif lives == 1 and ostatok != 0:
            WIN.blit(CAR_3_W, (POS_CAR_3_W[0], POS_CAR_3_W[1]+2))
        if lives == 0:
            WIN.blit(CAR_4, POS_CAR_4)

        if lives != 0:
            WIN.blit(TUNNEL_1, POS_TUNNEL_1_0)
            WIN.blit(TUNNEL_1, POS_TUNNEL_1_1)
            WIN.blit(TUNNEL_1, POS_TUNNEL_1_2)

            WIN.blit(TUNNEL_EQUALS_0_0, POS_TUNNEL_EQUALS_0_0)
            WIN.blit(TUNNEL_EQUALS_0_1, POS_TUNNEL_EQUALS_0_1)
            WIN.blit(TUNNEL_EQUALS_0_2, POS_TUNNEL_EQUALS_0_2)

            WIN.blit(TUNNEL_EQUALS_1_0, POS_TUNNEL_EQUALS_1_0)
            WIN.blit(TUNNEL_EQUALS_1_1, POS_TUNNEL_EQUALS_1_1)
            WIN.blit(TUNNEL_EQUALS_1_2, POS_TUNNEL_EQUALS_1_2)

            WIN.blit(TUNNEL_EQUALS_2_0, POS_TUNNEL_EQUALS_2_0)
            WIN.blit(TUNNEL_EQUALS_2_1, POS_TUNNEL_EQUALS_2_1)
            WIN.blit(TUNNEL_EQUALS_2_2, POS_TUNNEL_EQUALS_2_2)

            WIN.blit(TUNNEL_EQUALS_3_0, POS_TUNNEL_EQUALS_3_0)
            WIN.blit(TUNNEL_EQUALS_3_1, POS_TUNNEL_EQUALS_3_1)
            WIN.blit(TUNNEL_EQUALS_3_2, POS_TUNNEL_EQUALS_3_2)

            WIN.blit(TUNNEL_EQUALS_4_0, POS_TUNNEL_EQUALS_4_0)
            WIN.blit(TUNNEL_EQUALS_4_1, POS_TUNNEL_EQUALS_4_1)
            WIN.blit(TUNNEL_EQUALS_4_2, POS_TUNNEL_EQUALS_4_2)

            WIN.blit(TUNNEL_EQUALS_5_0, POS_TUNNEL_EQUALS_5_0)
            WIN.blit(TUNNEL_EQUALS_5_1, POS_TUNNEL_EQUALS_5_1)
            WIN.blit(TUNNEL_EQUALS_5_2, POS_TUNNEL_EQUALS_5_2)

            WIN.blit(TUNNEL_EQUALS_6_0, POS_TUNNEL_EQUALS_6_0)
            WIN.blit(TUNNEL_EQUALS_6_1, POS_TUNNEL_EQUALS_6_1)
            WIN.blit(TUNNEL_EQUALS_6_2, POS_TUNNEL_EQUALS_6_2)

            WIN.blit(TUNNEL_EQUALS_7_0, POS_TUNNEL_EQUALS_7_0)
            WIN.blit(TUNNEL_EQUALS_7_1, POS_TUNNEL_EQUALS_7_1)
            WIN.blit(TUNNEL_EQUALS_7_2, POS_TUNNEL_EQUALS_7_2)

            WIN.blit(TUNNEL_EQUALS_8_0, POS_TUNNEL_EQUALS_8_0)
            WIN.blit(TUNNEL_EQUALS_8_1, POS_TUNNEL_EQUALS_8_1)
            WIN.blit(TUNNEL_EQUALS_8_2, POS_TUNNEL_EQUALS_8_2)

            WIN.blit(TUNNEL_EQUALS_9_0, POS_TUNNEL_EQUALS_9_0)
            WIN.blit(TUNNEL_EQUALS_9_1, POS_TUNNEL_EQUALS_9_1)
            WIN.blit(TUNNEL_EQUALS_9_2, POS_TUNNEL_EQUALS_9_2)

        WIN.blit(SCORE, POS_SCORE)
        WIN.blit(PAUSE, POS_PAUSE)

    while run_lvl:

        if game_is_on:
            current_time = pygame.time.get_ticks()
            NEW_TIMER += 17
        else:
            current_time = 0
            NEW_TIMER = 0

        def reset_tunnels():
            POS_TUNNEL_0_0[0] = ST_OFFSET_TUNNEL_0+33
            POS_TUNNEL_0_1[0] = ST_OFFSET_TUNNEL_0+33
            POS_TUNNEL_0_2[0] = ST_OFFSET_TUNNEL_0+33

            POS_TUNNEL_1_0[0] = ST_OFFSET_TUNNEL_1
            POS_TUNNEL_1_1[0] = ST_OFFSET_TUNNEL_1
            POS_TUNNEL_1_2[0] = ST_OFFSET_TUNNEL_1

        def move_tunnels():
            POS_TUNNEL_0_0[0] -= speed*acceleration
            POS_TUNNEL_0_1[0] -= speed*acceleration
            POS_TUNNEL_0_2[0] -= speed*acceleration

            POS_TUNNEL_1_0[0] -= speed*acceleration
            POS_TUNNEL_1_1[0] -= speed*acceleration
            POS_TUNNEL_1_2[0] -= speed*acceleration

        def equals_reset_0():
            POS_TUNNEL_EQUALS_0_0[0] = -WIDTH
            POS_TUNNEL_EQUALS_0_1[0] = -WIDTH
            POS_TUNNEL_EQUALS_0_2[0] = -WIDTH

        def equals_reset_1():
            POS_TUNNEL_EQUALS_1_0[0] = -WIDTH
            POS_TUNNEL_EQUALS_1_1[0] = -WIDTH
            POS_TUNNEL_EQUALS_1_2[0] = -WIDTH

        def equals_reset_2():
            POS_TUNNEL_EQUALS_2_0[0] = -WIDTH
            POS_TUNNEL_EQUALS_2_1[0] = -WIDTH
            POS_TUNNEL_EQUALS_2_2[0] = -WIDTH

        def equals_reset_3():
            POS_TUNNEL_EQUALS_3_0[0] = -WIDTH
            POS_TUNNEL_EQUALS_3_1[0] = -WIDTH
            POS_TUNNEL_EQUALS_3_2[0] = -WIDTH

        def equals_reset_4():
            POS_TUNNEL_EQUALS_4_0[0] = -WIDTH
            POS_TUNNEL_EQUALS_4_1[0] = -WIDTH
            POS_TUNNEL_EQUALS_4_2[0] = -WIDTH

        def equals_reset_5():
            POS_TUNNEL_EQUALS_5_0[0] = -WIDTH
            POS_TUNNEL_EQUALS_5_1[0] = -WIDTH
            POS_TUNNEL_EQUALS_5_2[0] = -WIDTH

        def equals_reset_6():
            POS_TUNNEL_EQUALS_6_0[0] = -WIDTH
            POS_TUNNEL_EQUALS_6_1[0] = -WIDTH
            POS_TUNNEL_EQUALS_6_2[0] = -WIDTH

        def equals_reset_7():
            POS_TUNNEL_EQUALS_7_0[0] = -WIDTH
            POS_TUNNEL_EQUALS_7_1[0] = -WIDTH
            POS_TUNNEL_EQUALS_7_2[0] = -WIDTH

        def equals_reset_8():
            POS_TUNNEL_EQUALS_8_0[0] = -WIDTH
            POS_TUNNEL_EQUALS_8_1[0] = -WIDTH
            POS_TUNNEL_EQUALS_8_2[0] = -WIDTH

        def equals_reset_9():
            POS_TUNNEL_EQUALS_9_0[0] = -WIDTH
            POS_TUNNEL_EQUALS_9_1[0] = -WIDTH
            POS_TUNNEL_EQUALS_9_2[0] = -WIDTH

        def car_hits():
            if lives == 2:
                car_hit_sound()
            elif lives == 1:
                car_hit_sound_2()
            if lives > 0:
                pygame.time.wait(COLLISION_PAUSE)
        # print(f'{current_time} {NEW_TIMER}')

        draw_all()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE) or (event.type == pygame.KEYDOWN and event.key == K_RETURN and WIN_CONDITION):
                pygame.mixer.music.stop()
                menu_selected_sound()
                run_lvl = False
                NEW_TIMER = 0
                main_menu_music()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    ROAD_LANES += 1
                if event.key == pygame.K_UP:
                    ROAD_LANES -= 1
                if event.key == pygame.K_0:
                    game_is_on = True
                    lives = 3
                    # current_time = pygame.time.get_ticks()
                if event.key == pygame.K_9:
                    game_is_on = False
                    NEW_TIMER = 0

            if (event.type == pygame.KEYDOWN and event.key == K_RIGHT) or (event.type == pygame.KEYUP and event.key == K_LEFT):
                acceleration += 0.5
            if (event.type == pygame.KEYDOWN and event.key == K_LEFT) or (event.type == pygame.KEYUP and event.key == K_RIGHT):
                acceleration -= 0.5

        if lives == 3:
            WIN.blit(HEART, POS_HEART)
            WIN.blit(HEART, (POS_HEART[0]+60, POS_HEART[1]))
            WIN.blit(HEART, (POS_HEART[0]+120, POS_HEART[1]))
        elif lives == 2:
            WIN.blit(HEART, POS_HEART)
            WIN.blit(HEART, (POS_HEART[0]+60, POS_HEART[1]))
        elif lives == 1:
            WIN.blit(HEART, POS_HEART)

        if i <= -WIDTH:
            WIN.blit(ROAD, (i+WIDTH, 0))
            i = 0
        i -= speed*acceleration

        if ROAD_LANES == 0:
            POS_CAR[1] = HEIGHT//100*37
            POS_CAR_W[1] = HEIGHT//100*37
            POS_CAR_2[1] = HEIGHT//100*37
            POS_CAR_2_W[1] = HEIGHT//100*37
            POS_CAR_3[1] = HEIGHT//100*37
            POS_CAR_3_W[1] = HEIGHT//100*37
            POS_CAR_4[1] = HEIGHT//100*37
            # print(ROAD_LANES)
        elif ROAD_LANES == 1:
            POS_CAR[1] = HEIGHT//100*57
            POS_CAR_W[1] = HEIGHT//100*57
            POS_CAR_2[1] = HEIGHT//100*57
            POS_CAR_2_W[1] = HEIGHT//100*57
            POS_CAR_3[1] = HEIGHT//100*57
            POS_CAR_3_W[1] = HEIGHT//100*57
            POS_CAR_4[1] = HEIGHT//100*57
            # print(ROAD_LANES)
        elif ROAD_LANES == 2:
            POS_CAR[1] = HEIGHT//100*77
            POS_CAR_W[1] = HEIGHT//100*77
            POS_CAR_2[1] = HEIGHT//100*77
            POS_CAR_2_W[1] = HEIGHT//100*77
            POS_CAR_3[1] = HEIGHT//100*77
            POS_CAR_3_W[1] = HEIGHT//100*77
            POS_CAR_4[1] = HEIGHT//100*77
            # print(ROAD_LANES)
        elif ROAD_LANES > 2:
            ROAD_LANES = 2
        elif ROAD_LANES < 0:
            ROAD_LANES = 0

        if lives != 0:
            if 0 < NEW_TIMER < 3000:
                COLLISION = False

                equals_reset_0()

                reset_tunnels()

                POS_TUNNEL_EQUALS_0_0[0] = ST_OFFSET_ANSWER+35
                POS_TUNNEL_EQUALS_0_1[0] = ST_OFFSET_ANSWER+35
                POS_TUNNEL_EQUALS_0_2[0] = ST_OFFSET_ANSWER+35

            if 3000 < NEW_TIMER < 8000:
                TASK_1 = FONT.render(
                    f'{all_exercises[0][0]}:{all_exercises[0][1]}', 0, WHITE)
                POS_TASK_1 = TASK_1.get_rect()
                POS_TASK_1.center = (WIDTH//2, HEIGHT//100*8)
                WIN.blit(TASK_1, POS_TASK_1)

                move_tunnels()

                POS_TUNNEL_EQUALS_0_0[0] -= speed*acceleration
                POS_TUNNEL_EQUALS_0_1[0] -= speed*acceleration
                POS_TUNNEL_EQUALS_0_2[0] -= speed*acceleration

                if CAR_RIGHT-6 <= POS_TUNNEL_1_0[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_0_0 == False and ROAD_LANES == 0 and COLLISION == False:
                    COLLISION = True
                    lives -= 1
                    car_hits()
                    equals_reset_0()
                elif CAR_RIGHT-6 <= POS_TUNNEL_1_0[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_0_0 == True and ROAD_LANES == 0 and COLLISION == False:
                    COLLISION = True
                    gate_sound()
                    score += score_limit
                if CAR_RIGHT-6 <= POS_TUNNEL_1_1[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_0_1 == False and ROAD_LANES == 1 and COLLISION == False:
                    COLLISION = True
                    lives -= 1
                    car_hits()
                    equals_reset_0()
                elif CAR_RIGHT-6 <= POS_TUNNEL_1_1[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_0_1 == True and ROAD_LANES == 1 and COLLISION == False:
                    COLLISION = True
                    gate_sound()
                    score += score_limit
                if CAR_RIGHT-6 <= POS_TUNNEL_1_2[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_0_2 == False and ROAD_LANES == 2 and COLLISION == False:
                    COLLISION = True
                    lives -= 1
                    car_hits()
                    equals_reset_0()
                elif CAR_RIGHT-6 <= POS_TUNNEL_1_2[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_0_2 == True and ROAD_LANES == 2 and COLLISION == False:
                    COLLISION = True
                    gate_sound()
                    score += score_limit

                # print(f'{POS_TUNNEL_1_0[0]} {CAR_RIGHT} {score}')

            if 8000 < NEW_TIMER < 10000:
                COLLISION = False

                equals_reset_0()

                reset_tunnels()

                POS_TUNNEL_EQUALS_1_0[0] = ST_OFFSET_ANSWER+35
                POS_TUNNEL_EQUALS_1_1[0] = ST_OFFSET_ANSWER+35
                POS_TUNNEL_EQUALS_1_2[0] = ST_OFFSET_ANSWER+35

            if 10000 < NEW_TIMER < 15000:
                TASK_1 = FONT.render(
                    f'{all_exercises[1][0]}:{all_exercises[1][1]}', 0, WHITE)
                POS_TASK_1 = TASK_1.get_rect()
                POS_TASK_1.center = (WIDTH//2, HEIGHT//100*8)
                WIN.blit(TASK_1, POS_TASK_1)

                move_tunnels()

                POS_TUNNEL_EQUALS_1_0[0] -= speed*acceleration
                POS_TUNNEL_EQUALS_1_1[0] -= speed*acceleration
                POS_TUNNEL_EQUALS_1_2[0] -= speed*acceleration

                if CAR_RIGHT-6 <= POS_TUNNEL_1_0[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_1_0 == False and ROAD_LANES == 0 and COLLISION == False:
                    COLLISION = True
                    lives -= 1
                    car_hits()
                    equals_reset_1()
                elif CAR_RIGHT-6 <= POS_TUNNEL_1_0[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_1_0 == True and ROAD_LANES == 0 and COLLISION == False:
                    COLLISION = True
                    gate_sound()
                    score += score_limit
                if CAR_RIGHT-6 <= POS_TUNNEL_1_1[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_1_1 == False and ROAD_LANES == 1 and COLLISION == False:
                    COLLISION = True
                    lives -= 1
                    car_hits()
                    equals_reset_1()
                elif CAR_RIGHT-6 <= POS_TUNNEL_1_1[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_1_1 == True and ROAD_LANES == 1 and COLLISION == False:
                    COLLISION = True
                    gate_sound()
                    score += score_limit
                if CAR_RIGHT-6 <= POS_TUNNEL_1_2[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_1_2 == False and ROAD_LANES == 2 and COLLISION == False:
                    COLLISION = True
                    lives -= 1
                    car_hits()
                    equals_reset_1()
                elif CAR_RIGHT-6 <= POS_TUNNEL_1_2[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_1_2 == True and ROAD_LANES == 2 and COLLISION == False:
                    COLLISION = True
                    gate_sound()
                    score += score_limit

                # print(f'{POS_TUNNEL_1_0[0]} {CAR_RIGHT} {score}')

            if 15000 < NEW_TIMER < 17000:
                COLLISION = False

                equals_reset_1()

                reset_tunnels()

                POS_TUNNEL_EQUALS_2_0[0] = ST_OFFSET_ANSWER+35
                POS_TUNNEL_EQUALS_2_1[0] = ST_OFFSET_ANSWER+35
                POS_TUNNEL_EQUALS_2_2[0] = ST_OFFSET_ANSWER+35

            if 17000 < NEW_TIMER < 22000:
                TASK_1 = FONT.render(
                    f'{all_exercises[2][0]}:{all_exercises[2][1]}', 0, WHITE)
                POS_TASK_1 = TASK_1.get_rect()
                POS_TASK_1.center = (WIDTH//2, HEIGHT//100*8)
                WIN.blit(TASK_1, POS_TASK_1)

                move_tunnels()

                POS_TUNNEL_EQUALS_2_0[0] -= speed*acceleration
                POS_TUNNEL_EQUALS_2_1[0] -= speed*acceleration
                POS_TUNNEL_EQUALS_2_2[0] -= speed*acceleration

                if CAR_RIGHT-6 <= POS_TUNNEL_1_0[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_2_0 == False and ROAD_LANES == 0 and COLLISION == False:
                    COLLISION = True
                    lives -= 1
                    car_hits()
                    equals_reset_2()
                elif CAR_RIGHT-6 <= POS_TUNNEL_1_0[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_2_0 == True and ROAD_LANES == 0 and COLLISION == False:
                    COLLISION = True
                    gate_sound()
                    score += score_limit
                if CAR_RIGHT-6 <= POS_TUNNEL_1_1[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_2_1 == False and ROAD_LANES == 1 and COLLISION == False:
                    COLLISION = True
                    lives -= 1
                    car_hits()
                    equals_reset_2()
                elif CAR_RIGHT-6 <= POS_TUNNEL_1_1[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_2_1 == True and ROAD_LANES == 1 and COLLISION == False:
                    COLLISION = True
                    gate_sound()
                    score += score_limit
                if CAR_RIGHT-6 <= POS_TUNNEL_1_2[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_2_2 == False and ROAD_LANES == 2 and COLLISION == False:
                    COLLISION = True
                    lives -= 1
                    car_hits()
                    equals_reset_2()
                elif CAR_RIGHT-6 <= POS_TUNNEL_1_2[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_2_2 == True and ROAD_LANES == 2 and COLLISION == False:
                    COLLISION = True
                    gate_sound()
                    score += score_limit

                # print(f'{POS_TUNNEL_1_0[0]} {CAR_RIGHT} {score}')

            if 22000 < NEW_TIMER < 24000:
                COLLISION = False

                equals_reset_2()

                reset_tunnels()

                POS_TUNNEL_EQUALS_3_0[0] = ST_OFFSET_ANSWER+35
                POS_TUNNEL_EQUALS_3_1[0] = ST_OFFSET_ANSWER+35
                POS_TUNNEL_EQUALS_3_2[0] = ST_OFFSET_ANSWER+35

            if 24000 < NEW_TIMER < 29000:
                TASK_1 = FONT.render(
                    f'{all_exercises[3][0]}:{all_exercises[3][1]}', 0, WHITE)
                POS_TASK_1 = TASK_1.get_rect()
                POS_TASK_1.center = (WIDTH//2, HEIGHT//100*8)
                WIN.blit(TASK_1, POS_TASK_1)

                move_tunnels()

                POS_TUNNEL_EQUALS_3_0[0] -= speed*acceleration
                POS_TUNNEL_EQUALS_3_1[0] -= speed*acceleration
                POS_TUNNEL_EQUALS_3_2[0] -= speed*acceleration

                if CAR_RIGHT-6 <= POS_TUNNEL_1_0[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_3_0 == False and ROAD_LANES == 0 and COLLISION == False:
                    COLLISION = True
                    lives -= 1
                    car_hits()
                    equals_reset_3()
                elif CAR_RIGHT-6 <= POS_TUNNEL_1_0[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_3_0 == True and ROAD_LANES == 0 and COLLISION == False:
                    COLLISION = True
                    gate_sound()
                    score += score_limit
                if CAR_RIGHT-6 <= POS_TUNNEL_1_1[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_3_1 == False and ROAD_LANES == 1 and COLLISION == False:
                    COLLISION = True
                    lives -= 1
                    car_hits()
                    equals_reset_3()
                elif CAR_RIGHT-6 <= POS_TUNNEL_1_1[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_3_1 == True and ROAD_LANES == 1 and COLLISION == False:
                    COLLISION = True
                    gate_sound()
                    score += score_limit
                if CAR_RIGHT-6 <= POS_TUNNEL_1_2[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_3_2 == False and ROAD_LANES == 2 and COLLISION == False:
                    COLLISION = True
                    lives -= 1
                    car_hits()
                    equals_reset_3()
                elif CAR_RIGHT-6 <= POS_TUNNEL_1_2[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_3_2 == True and ROAD_LANES == 2 and COLLISION == False:
                    COLLISION = True
                    gate_sound()
                    score += score_limit

                # print(f'{POS_TUNNEL_1_0[0]} {CAR_RIGHT} {score}')

            if 29000 < NEW_TIMER < 31000:
                COLLISION = False

                equals_reset_3()

                reset_tunnels()

                POS_TUNNEL_EQUALS_4_0[0] = ST_OFFSET_ANSWER+35
                POS_TUNNEL_EQUALS_4_1[0] = ST_OFFSET_ANSWER+35
                POS_TUNNEL_EQUALS_4_2[0] = ST_OFFSET_ANSWER+35

            if 31000 < NEW_TIMER < 36000:
                TASK_1 = FONT.render(
                    f'{all_exercises[4][0]}:{all_exercises[4][1]}', 0, WHITE)
                POS_TASK_1 = TASK_1.get_rect()
                POS_TASK_1.center = (WIDTH//2, HEIGHT//100*8)
                WIN.blit(TASK_1, POS_TASK_1)

                move_tunnels()

                POS_TUNNEL_EQUALS_4_0[0] -= speed*acceleration
                POS_TUNNEL_EQUALS_4_1[0] -= speed*acceleration
                POS_TUNNEL_EQUALS_4_2[0] -= speed*acceleration

                if CAR_RIGHT-6 <= POS_TUNNEL_1_0[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_4_0 == False and ROAD_LANES == 0 and COLLISION == False:
                    COLLISION = True
                    lives -= 1
                    car_hits()
                    equals_reset_4()
                elif CAR_RIGHT-6 <= POS_TUNNEL_1_0[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_4_0 == True and ROAD_LANES == 0 and COLLISION == False:
                    COLLISION = True
                    gate_sound()
                    score += score_limit
                if CAR_RIGHT-6 <= POS_TUNNEL_1_1[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_4_1 == False and ROAD_LANES == 1 and COLLISION == False:
                    COLLISION = True
                    lives -= 1
                    car_hits()
                    equals_reset_4()
                elif CAR_RIGHT-6 <= POS_TUNNEL_1_1[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_4_1 == True and ROAD_LANES == 1 and COLLISION == False:
                    COLLISION = True
                    gate_sound()
                    score += score_limit
                if CAR_RIGHT-6 <= POS_TUNNEL_1_2[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_4_2 == False and ROAD_LANES == 2 and COLLISION == False:
                    COLLISION = True
                    lives -= 1
                    car_hits()
                    equals_reset_4()
                elif CAR_RIGHT-6 <= POS_TUNNEL_1_2[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_4_2 == True and ROAD_LANES == 2 and COLLISION == False:
                    COLLISION = True
                    gate_sound()
                    score += score_limit

                # print(f'{POS_TUNNEL_1_0[0]} {CAR_RIGHT} {score}')

            if 36000 < NEW_TIMER < 38000:
                COLLISION = False

                equals_reset_4()

                reset_tunnels()

                POS_TUNNEL_EQUALS_5_0[0] = ST_OFFSET_ANSWER+35
                POS_TUNNEL_EQUALS_5_1[0] = ST_OFFSET_ANSWER+35
                POS_TUNNEL_EQUALS_5_2[0] = ST_OFFSET_ANSWER+35

            if 38000 < NEW_TIMER < 43000:
                TASK_1 = FONT.render(
                    f'{all_exercises[5][0]}:{all_exercises[5][1]}', 0, WHITE)
                POS_TASK_1 = TASK_1.get_rect()
                POS_TASK_1.center = (WIDTH//2, HEIGHT//100*8)
                WIN.blit(TASK_1, POS_TASK_1)

                move_tunnels()

                POS_TUNNEL_EQUALS_5_0[0] -= speed*acceleration
                POS_TUNNEL_EQUALS_5_1[0] -= speed*acceleration
                POS_TUNNEL_EQUALS_5_2[0] -= speed*acceleration

                if CAR_RIGHT-6 <= POS_TUNNEL_1_0[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_5_0 == False and ROAD_LANES == 0 and COLLISION == False:
                    COLLISION = True
                    lives -= 1
                    car_hits()
                    equals_reset_5()
                elif CAR_RIGHT-6 <= POS_TUNNEL_1_0[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_5_0 == True and ROAD_LANES == 0 and COLLISION == False:
                    COLLISION = True
                    gate_sound()
                    score += score_limit
                if CAR_RIGHT-6 <= POS_TUNNEL_1_1[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_5_1 == False and ROAD_LANES == 1 and COLLISION == False:
                    COLLISION = True
                    lives -= 1
                    car_hits()
                    equals_reset_5()
                elif CAR_RIGHT-6 <= POS_TUNNEL_1_1[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_5_1 == True and ROAD_LANES == 1 and COLLISION == False:
                    COLLISION = True
                    gate_sound()
                    score += score_limit
                if CAR_RIGHT-6 <= POS_TUNNEL_1_2[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_5_2 == False and ROAD_LANES == 2 and COLLISION == False:
                    COLLISION = True
                    lives -= 1
                    car_hits()
                    equals_reset_5()
                elif CAR_RIGHT-6 <= POS_TUNNEL_1_2[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_5_2 == True and ROAD_LANES == 2 and COLLISION == False:
                    COLLISION = True
                    gate_sound()
                    score += score_limit

                # print(f'{POS_TUNNEL_1_0[0]} {CAR_RIGHT} {score}')

            if 43000 < NEW_TIMER < 45000:
                COLLISION = False

                equals_reset_5()

                reset_tunnels()

                POS_TUNNEL_EQUALS_6_0[0] = ST_OFFSET_ANSWER+35
                POS_TUNNEL_EQUALS_6_1[0] = ST_OFFSET_ANSWER+35
                POS_TUNNEL_EQUALS_6_2[0] = ST_OFFSET_ANSWER+35

            if 45000 < NEW_TIMER < 50000:
                TASK_1 = FONT.render(
                    f'{all_exercises[6][0]}:{all_exercises[6][1]}', 0, WHITE)
                POS_TASK_1 = TASK_1.get_rect()
                POS_TASK_1.center = (WIDTH//2, HEIGHT//100*8)
                WIN.blit(TASK_1, POS_TASK_1)

                move_tunnels()

                POS_TUNNEL_EQUALS_6_0[0] -= speed*acceleration
                POS_TUNNEL_EQUALS_6_1[0] -= speed*acceleration
                POS_TUNNEL_EQUALS_6_2[0] -= speed*acceleration

                if CAR_RIGHT-6 <= POS_TUNNEL_1_0[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_6_0 == False and ROAD_LANES == 0 and COLLISION == False:
                    COLLISION = True
                    lives -= 1
                    car_hits()
                    equals_reset_6()
                elif CAR_RIGHT-6 <= POS_TUNNEL_1_0[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_6_0 == True and ROAD_LANES == 0 and COLLISION == False:
                    COLLISION = True
                    gate_sound()
                    score += score_limit
                if CAR_RIGHT-6 <= POS_TUNNEL_1_1[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_6_1 == False and ROAD_LANES == 1 and COLLISION == False:
                    COLLISION = True
                    lives -= 1
                    car_hits()
                    equals_reset_6()
                elif CAR_RIGHT-6 <= POS_TUNNEL_1_1[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_6_1 == True and ROAD_LANES == 1 and COLLISION == False:
                    COLLISION = True
                    gate_sound()
                    score += score_limit
                if CAR_RIGHT-6 <= POS_TUNNEL_1_2[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_6_2 == False and ROAD_LANES == 2 and COLLISION == False:
                    COLLISION = True
                    lives -= 1
                    car_hits()
                    equals_reset_6()
                elif CAR_RIGHT-6 <= POS_TUNNEL_1_2[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_6_2 == True and ROAD_LANES == 2 and COLLISION == False:
                    COLLISION = True
                    gate_sound()
                    score += score_limit

                # print(f'{POS_TUNNEL_1_0[0]} {CAR_RIGHT} {score}')

            if 50000 < NEW_TIMER < 52000:
                COLLISION = False

                equals_reset_6()

                reset_tunnels()

                POS_TUNNEL_EQUALS_7_0[0] = ST_OFFSET_ANSWER+35
                POS_TUNNEL_EQUALS_7_1[0] = ST_OFFSET_ANSWER+35
                POS_TUNNEL_EQUALS_7_2[0] = ST_OFFSET_ANSWER+35

            if 52000 < NEW_TIMER < 57000:
                TASK_1 = FONT.render(
                    f'{all_exercises[7][0]}:{all_exercises[7][1]}', 0, WHITE)
                POS_TASK_1 = TASK_1.get_rect()
                POS_TASK_1.center = (WIDTH//2, HEIGHT//100*8)
                WIN.blit(TASK_1, POS_TASK_1)

                move_tunnels()

                POS_TUNNEL_EQUALS_7_0[0] -= speed*acceleration
                POS_TUNNEL_EQUALS_7_1[0] -= speed*acceleration
                POS_TUNNEL_EQUALS_7_2[0] -= speed*acceleration

                if CAR_RIGHT-6 <= POS_TUNNEL_1_0[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_7_0 == False and ROAD_LANES == 0 and COLLISION == False:
                    COLLISION = True
                    lives -= 1
                    car_hits()
                    equals_reset_7()
                elif CAR_RIGHT-6 <= POS_TUNNEL_1_0[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_7_0 == True and ROAD_LANES == 0 and COLLISION == False:
                    COLLISION = True
                    gate_sound()
                    score += score_limit
                if CAR_RIGHT-6 <= POS_TUNNEL_1_1[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_7_1 == False and ROAD_LANES == 1 and COLLISION == False:
                    COLLISION = True
                    lives -= 1
                    car_hits()
                    equals_reset_7()
                elif CAR_RIGHT-6 <= POS_TUNNEL_1_1[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_7_1 == True and ROAD_LANES == 1 and COLLISION == False:
                    COLLISION = True
                    gate_sound()
                    score += score_limit
                if CAR_RIGHT-6 <= POS_TUNNEL_1_2[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_7_2 == False and ROAD_LANES == 2 and COLLISION == False:
                    COLLISION = True
                    lives -= 1
                    car_hits()
                    equals_reset_7()
                elif CAR_RIGHT-6 <= POS_TUNNEL_1_2[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_7_2 == True and ROAD_LANES == 2 and COLLISION == False:
                    COLLISION = True
                    gate_sound()
                    score += score_limit

                # print(f'{POS_TUNNEL_1_0[0]} {CAR_RIGHT} {score}')

            if 57000 < NEW_TIMER < 59000:
                COLLISION = False

                equals_reset_7()

                reset_tunnels()

                POS_TUNNEL_EQUALS_8_0[0] = ST_OFFSET_ANSWER+35
                POS_TUNNEL_EQUALS_8_1[0] = ST_OFFSET_ANSWER+35
                POS_TUNNEL_EQUALS_8_2[0] = ST_OFFSET_ANSWER+35

            if 59000 < NEW_TIMER < 64000:
                TASK_1 = FONT.render(
                    f'{all_exercises[8][0]}:{all_exercises[8][1]}', 0, WHITE)
                POS_TASK_1 = TASK_1.get_rect()
                POS_TASK_1.center = (WIDTH//2, HEIGHT//100*8)
                WIN.blit(TASK_1, POS_TASK_1)

                move_tunnels()

                POS_TUNNEL_EQUALS_8_0[0] -= speed*acceleration
                POS_TUNNEL_EQUALS_8_1[0] -= speed*acceleration
                POS_TUNNEL_EQUALS_8_2[0] -= speed*acceleration

                if CAR_RIGHT-6 <= POS_TUNNEL_1_0[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_8_0 == False and ROAD_LANES == 0 and COLLISION == False:
                    COLLISION = True
                    lives -= 1
                    car_hits()
                    equals_reset_8()
                elif CAR_RIGHT-6 <= POS_TUNNEL_1_0[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_8_0 == True and ROAD_LANES == 0 and COLLISION == False:
                    COLLISION = True
                    gate_sound()
                    score += score_limit
                if CAR_RIGHT-6 <= POS_TUNNEL_1_1[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_8_1 == False and ROAD_LANES == 1 and COLLISION == False:
                    COLLISION = True
                    lives -= 1
                    car_hits()
                    equals_reset_8()
                elif CAR_RIGHT-6 <= POS_TUNNEL_1_1[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_8_1 == True and ROAD_LANES == 1 and COLLISION == False:
                    COLLISION = True
                    gate_sound()
                    score += score_limit
                if CAR_RIGHT-6 <= POS_TUNNEL_1_2[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_8_2 == False and ROAD_LANES == 2 and COLLISION == False:
                    COLLISION = True
                    lives -= 1
                    car_hits()
                    equals_reset_8()
                elif CAR_RIGHT-6 <= POS_TUNNEL_1_2[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_8_2 == True and ROAD_LANES == 2 and COLLISION == False:
                    COLLISION = True
                    gate_sound()
                    score += score_limit

                # print(f'{POS_TUNNEL_1_0[0]} {CAR_RIGHT} {score}')

            if 64000 < NEW_TIMER < 66000:
                COLLISION = False

                equals_reset_8()

                reset_tunnels()

                POS_TUNNEL_EQUALS_9_0[0] = ST_OFFSET_ANSWER+35
                POS_TUNNEL_EQUALS_9_1[0] = ST_OFFSET_ANSWER+35
                POS_TUNNEL_EQUALS_9_2[0] = ST_OFFSET_ANSWER+35

            if 66000 < NEW_TIMER < 71000:
                TASK_1 = FONT.render(
                    f'{all_exercises[9][0]}:{all_exercises[9][1]}', 0, WHITE)
                POS_TASK_1 = TASK_1.get_rect()
                POS_TASK_1.center = (WIDTH//2, HEIGHT//100*8)
                WIN.blit(TASK_1, POS_TASK_1)

                move_tunnels()

                POS_TUNNEL_EQUALS_9_0[0] -= speed*acceleration
                POS_TUNNEL_EQUALS_9_1[0] -= speed*acceleration
                POS_TUNNEL_EQUALS_9_2[0] -= speed*acceleration

                if CAR_RIGHT-6 <= POS_TUNNEL_1_0[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_9_0 == False and ROAD_LANES == 0 and COLLISION == False:
                    COLLISION = True
                    lives -= 1
                    car_hits()
                    equals_reset_9()
                elif CAR_RIGHT-6 <= POS_TUNNEL_1_0[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_9_0 == True and ROAD_LANES == 0 and COLLISION == False:
                    COLLISION = True
                    gate_sound()
                    score += score_limit
                if CAR_RIGHT-6 <= POS_TUNNEL_1_1[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_9_1 == False and ROAD_LANES == 1 and COLLISION == False:
                    COLLISION = True
                    lives -= 1
                    car_hits()
                    equals_reset_9()
                elif CAR_RIGHT-6 <= POS_TUNNEL_1_1[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_9_1 == True and ROAD_LANES == 1 and COLLISION == False:
                    COLLISION = True
                    gate_sound()
                    score += score_limit
                if CAR_RIGHT-6 <= POS_TUNNEL_1_2[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_9_2 == False and ROAD_LANES == 2 and COLLISION == False:
                    COLLISION = True
                    lives -= 1
                    car_hits()
                    equals_reset_9()
                elif CAR_RIGHT-6 <= POS_TUNNEL_1_2[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_9_2 == True and ROAD_LANES == 2 and COLLISION == False:
                    COLLISION = True
                    gate_sound()
                    score += score_limit

                # print(f'{POS_TUNNEL_1_0[0]} {CAR_RIGHT} {score}')

            if 71000 < NEW_TIMER < 73000:
                COLLISION = False

                equals_reset_9()

                reset_tunnels()

            if 73000 < NEW_TIMER:
                if 73001 < NEW_TIMER < 73018:
                    lvl_complete_sound()
                WIN_CONDITION = True
                WIN.blit(MAIN_MENU_BACK, POS_BACK)
                GAME_OVER = FONT.render(f'ПОБЕДА!', 0, WHITE)
                POS_GAME_OVER = GAME_OVER.get_rect(center=(WIDTH//2, HEIGHT//2-100))
                GAME_OVER_SCORE = FONT.render(f'ВАШ СЧЕТ: {score}', 0, WHITE)
                POS_GAME_OVER_SCORE = GAME_OVER_SCORE.get_rect(center=(WIDTH//2, HEIGHT//2))
                GAME_OVER_PRESS_ESC = FONT_SCORE.render(f'МЕНЮ: ENTER', 0, WHITE)
                POS_GAME_OVER_PRESS_ESC = GAME_OVER_PRESS_ESC.get_rect(center=(WIDTH//2, HEIGHT//100*70))
                WIN.blit(GAME_OVER, POS_GAME_OVER)
                WIN.blit(GAME_OVER_SCORE, POS_GAME_OVER_SCORE)
                WIN.blit(GAME_OVER_PRESS_ESC, POS_GAME_OVER_PRESS_ESC)

        if lives != 0:
            SCORE_0 = FONT_SCORE.render(f'{score}', 0, WHITE)
            POS_SCORE_0 = SCORE_0.get_rect(
                center=(WIDTH//100*92, HEIGHT//100*99+30))
            WIN.blit(SCORE_0, POS_SCORE_0)
        else:
            if GAME_OVER_SOUND_FLAG == False:
                game_over_sound()
                GAME_OVER_SOUND_FLAG = True
            WIN.blit(MAIN_MENU_BACK, POS_BACK)
            GAME_OVER = FONT.render(f'GAME OVER', 0, WHITE)
            POS_GAME_OVER = GAME_OVER.get_rect(center=(WIDTH//2, HEIGHT//2-100))
            GAME_OVER.set_alpha(100)
            GAME_OVER_SCORE = FONT.render(f'ВАШ СЧЕТ: {score}', 0, WHITE)
            POS_GAME_OVER_SCORE = GAME_OVER_SCORE.get_rect(center=(WIDTH//2, HEIGHT//2))
            GAME_OVER_PRESS_ESC = FONT_SCORE.render(f'МЕНЮ: ESC', 0, WHITE)
            POS_GAME_OVER_PRESS_ESC = GAME_OVER_PRESS_ESC.get_rect(center=(WIDTH//2, HEIGHT//100*70))
            WIN.blit(GAME_OVER, POS_GAME_OVER)
            WIN.blit(GAME_OVER_SCORE, POS_GAME_OVER_SCORE)
            WIN.blit(GAME_OVER_PRESS_ESC, POS_GAME_OVER_PRESS_ESC)

        if game_is_on:
            pygame.display.flip()
        else:
            NEW_TIMER = 0

        clock.tick(FPS)




















def draw_menu():
    WIN.fill(BLACK)
    MAIN_MENU_SPRITE.play()
    MAIN_MENU_SPRITE.blit(WIN, (0, (HEIGHT-582)/2))
    WIN.blit(MAIN_MENU_BACK, POS_BACK)
    if menu_main_page:
        WIN.blit(MAIN_MENU_START, POS_START)
        WIN.blit(MAIN_MENU_OPTIONS, POS_OPTIONS)
        WIN.blit(MAIN_MENU_EXIT, POS_EXIT)
    elif menu_lvl_choose_page:
        WIN.blit(MAIN_MENU_LVL_1, POS_MAIN_MENU_LVL_1)
        WIN.blit(MAIN_MENU_LVL_2, POS_MAIN_MENU_LVL_2)
        WIN.blit(MAIN_MENU_LVL_3, POS_MAIN_MENU_LVL_3)
        WIN.blit(MAIN_MENU_LVL_4, POS_MAIN_MENU_LVL_4)



run = True
counter = 0

if run:
    main_menu_music()
    
while run:

    draw_menu()

    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE and menu_main_page) or (counter == 2 and event.type == KEYDOWN and event.key == K_RETURN and menu_main_page):
            run = False
        if event.type == KEYDOWN and event.key == K_ESCAPE and menu_lvl_choose_page:
            menu_selected_sound()
            menu_lvl_choose_page = False
            menu_main_page = True
        if event.type == KEYDOWN:
            if event.key == K_DOWN :
                menu_select_sound()
                counter += 1
            if event.key == K_UP:
                menu_select_sound()
                counter -= 1

        if (counter == 0 and event.type == KEYDOWN and event.key == K_RETURN and menu_main_page) or (counter == 0 and event.type == KEYDOWN and event.key == K_RETURN and menu_lvl_choose_page):
            menu_selected_sound()
            lvl1()
        if counter == 1 and event.type == KEYDOWN and event.key == K_RETURN and menu_lvl_choose_page:
            menu_selected_sound()
            lvl2()
        if counter == 2 and event.type == KEYDOWN and event.key == K_RETURN and menu_lvl_choose_page:
            menu_selected_sound()
            lvl3()
        if counter == 3 and event.type == KEYDOWN and event.key == K_RETURN and menu_lvl_choose_page:
            menu_selected_sound()
            lvl4()
            
        if counter == 1 and event.type == KEYDOWN and event.key == K_RETURN:
            menu_selected_sound()
            menu_lvl_choose_page = True
            menu_main_page = False

    if counter == 0 and menu_main_page:
        pygame.draw.rect(WIN, WHITE, (WIDTH//2-RECT_X_1//2, HEIGHT//10*4-RECT_Y//2, RECT_X_1, RECT_Y), 7)
    elif counter == 1 and menu_main_page:
        pygame.draw.rect(WIN, WHITE, (WIDTH//2-RECT_X_2//2, HEIGHT//2-RECT_Y//2, RECT_X_2, RECT_Y), 7)
    elif counter == 2 and menu_main_page:
        pygame.draw.rect(WIN, WHITE, (WIDTH//2-RECT_X_3//2, HEIGHT//10*6-RECT_Y//2, RECT_X_3, RECT_Y), 7)
    elif counter > 2 and menu_main_page:
        counter = 0
    elif counter < 0 and menu_main_page:
        counter = 2

    if counter == 0 and menu_lvl_choose_page:
        pygame.draw.rect(WIN, WHITE, (WIDTH//2-RECT_X_1//2, HEIGHT//100*40-RECT_Y//2, RECT_X_1, RECT_Y), 7)
    elif counter == 1 and menu_lvl_choose_page:
        pygame.draw.rect(WIN, WHITE, (WIDTH//2-RECT_X_2//2, HEIGHT//100*50-RECT_Y//2, RECT_X_2, RECT_Y), 7)
    elif counter == 2 and menu_lvl_choose_page:
        pygame.draw.rect(WIN, WHITE, (WIDTH//2-RECT_X_3//2, HEIGHT//100*60-RECT_Y//2, RECT_X_3, RECT_Y), 7)
    elif counter == 3 and menu_lvl_choose_page:
        pygame.draw.rect(WIN, WHITE, (WIDTH//2-RECT_X_4//2, HEIGHT//100*70-RECT_Y//2, RECT_X_4, RECT_Y), 7)
    elif counter > 3 and menu_lvl_choose_page:
        counter = 0
    elif counter < 0 and menu_lvl_choose_page:
        counter = 3

    

    pygame.display.update()
