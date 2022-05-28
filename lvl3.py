from hashlib import new
from numpy import append
import math
import pygame
import random
from pygame.locals import *
from spritelist_3 import *
from osts import *


pygame.display.set_caption('LVL3')
clock = pygame.time.Clock()
i = 0
exercises = 10

all_exercises, all_answers, all_answer_flag, all_answer_flags_last = [], [], [], []

for exercise in range(10):
    first_sum = random.randint(1, 9)
    second_sum = random.randint(1, 9)

    sum_true = first_sum * second_sum

    if sum_true > 89:
        sum_fake_1 = sum_true + random.randint(-10, 0)
        sum_fake_2 = sum_true + random.randint(-10, 0)
    elif sum_true < 11:
        sum_fake_1 = sum_true + random.randint(0, 10)
        sum_fake_2 = sum_true + random.randint(0, 10)
    else:
        sum_fake_1 = sum_true + random.randint(-10, 10)
        sum_fake_2 = sum_true + random.randint(-10, 10)
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


        WIN.blit(SCORE, POS_SCORE)
        WIN.blit(PAUSE, POS_PAUSE)

        WIN.blit(TUNNEL_0, POS_TUNNEL_0_0)
        WIN.blit(TUNNEL_0, POS_TUNNEL_0_1)
        WIN.blit(TUNNEL_0, POS_TUNNEL_0_2)

    ostatok = current_time%10


    if lives == 3 and ostatok == 0:
        WIN.blit(CAR, POS_CAR)
    elif lives == 3 and ostatok != 0:
        WIN.blit(CAR, (POS_CAR[0], POS_CAR[1]+2))
    if lives == 2 and ostatok == 0:
        WIN.blit(CAR, POS_CAR)
    elif lives == 2 and ostatok != 0:
        WIN.blit(CAR, (POS_CAR[0], POS_CAR[1]+2))
    if lives == 1 and ostatok == 0:
        WIN.blit(CAR, POS_CAR)
    elif lives == 1 and ostatok != 0:
        WIN.blit(CAR, (POS_CAR[0], POS_CAR[1]+2))
    elif lives == 0:
        # WIN.blit(CAR_4, POS_CAR_4)
        WIN.blit(MAIN_MENU_BACK, POS_BACK)
        GAME_OVER = FONT.render(f'GAME OVER', 0, WHITE)
        POS_GAME_OVER = GAME_OVER.get_rect(center=(WIDTH//2, HEIGHT//2-100))
        GAME_OVER_SCORE = FONT.render(f'ВАШ СЧЕТ: {score}', 0, WHITE)
        POS_GAME_OVER_SCORE = GAME_OVER_SCORE.get_rect(center=(WIDTH//2, HEIGHT//2))
        WIN.blit(GAME_OVER, POS_GAME_OVER)
        WIN.blit(GAME_OVER_SCORE, POS_GAME_OVER_SCORE)
    
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

run = True
ROAD_LANES = 1
lives = 3
score = 0
score_limit = 1
COLLISION = False
COLLISION_PAUSE = 1000
pressed = pygame.key.get_pressed()
while run:
    current_time = pygame.time.get_ticks()

    draw_all()
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                ROAD_LANES += 1         
            if event.key == pygame.K_UP:
                ROAD_LANES -= 1
        
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
        POS_CAR[1] = HEIGHT//100*40
        # print(ROAD_LANES)
    elif ROAD_LANES == 1:
        POS_CAR[1] = HEIGHT//100*60
        # print(ROAD_LANES)
    elif ROAD_LANES == 2:
        POS_CAR[1] = HEIGHT//100*80
        # print(ROAD_LANES)
    elif ROAD_LANES > 2:
        ROAD_LANES = 2
    elif ROAD_LANES < 0:
        ROAD_LANES = 0

    if lives != 0:    
        if 3000 < current_time < 8000:
            TASK_1 = FONT.render(f'{all_exercises[0][0]}х{all_exercises[0][1]}', 0, WHITE)
            POS_TASK_1 = TASK_1.get_rect()
            POS_TASK_1.center = (WIDTH//2, HEIGHT//100*8)
            WIN.blit(TASK_1, POS_TASK_1)

            POS_TUNNEL_0_0[0] -= speed*acceleration
            POS_TUNNEL_0_1[0] -= speed*acceleration
            POS_TUNNEL_0_2[0] -= speed*acceleration

            POS_TUNNEL_1_0[0] -= speed*acceleration
            POS_TUNNEL_1_1[0] -= speed*acceleration
            POS_TUNNEL_1_2[0] -= speed*acceleration

            POS_TUNNEL_EQUALS_0_0[0] -= speed*acceleration
            POS_TUNNEL_EQUALS_0_1[0] -= speed*acceleration
            POS_TUNNEL_EQUALS_0_2[0] -= speed*acceleration

            if CAR_RIGHT-6 <= POS_TUNNEL_1_0[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_0_0 == False and ROAD_LANES == 0 and COLLISION == False:
                COLLISION = True
                pygame.time.wait(COLLISION_PAUSE)
                lives -= 1
            elif CAR_RIGHT-6 <= POS_TUNNEL_1_0[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_0_0 == True and ROAD_LANES == 0 and COLLISION == False:
                COLLISION = True
                score += score_limit
            if CAR_RIGHT-6 <= POS_TUNNEL_1_1[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_0_1 == False and ROAD_LANES == 1 and COLLISION == False:
                COLLISION = True
                pygame.time.wait(COLLISION_PAUSE)
                lives -= 1
            elif CAR_RIGHT-6 <= POS_TUNNEL_1_1[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_0_1 == True and ROAD_LANES == 1 and COLLISION == False:
                COLLISION = True
                score += score_limit
            if CAR_RIGHT-6 <= POS_TUNNEL_1_2[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_0_2 == False and ROAD_LANES == 2 and COLLISION == False:
                COLLISION = True
                pygame.time.wait(COLLISION_PAUSE)
                lives -= 1
            elif CAR_RIGHT-6 <= POS_TUNNEL_1_2[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_0_2 == True and ROAD_LANES == 2 and COLLISION == False:
                COLLISION = True
                score += score_limit

            # print(f'{POS_TUNNEL_1_0[0]} {CAR_RIGHT} {score}')

        if 8000 < current_time < 10000:
            COLLISION = False

            POS_TUNNEL_EQUALS_0_0[0] = -WIDTH
            POS_TUNNEL_EQUALS_0_1[0] = -WIDTH
            POS_TUNNEL_EQUALS_0_2[0] = -WIDTH

            POS_TUNNEL_0_0[0] = ST_OFFSET_TUNNEL_0+33
            POS_TUNNEL_0_1[0] = ST_OFFSET_TUNNEL_0+33
            POS_TUNNEL_0_2[0] = ST_OFFSET_TUNNEL_0+33

            POS_TUNNEL_1_0[0] = ST_OFFSET_TUNNEL_1
            POS_TUNNEL_1_1[0] = ST_OFFSET_TUNNEL_1
            POS_TUNNEL_1_2[0] = ST_OFFSET_TUNNEL_1

            POS_TUNNEL_EQUALS_1_0[0] = ST_OFFSET_ANSWER+35
            POS_TUNNEL_EQUALS_1_1[0] = ST_OFFSET_ANSWER+35
            POS_TUNNEL_EQUALS_1_2[0] = ST_OFFSET_ANSWER+35

        if 10000 < current_time < 15000:
            TASK_1 = FONT.render(f'{all_exercises[1][0]}х{all_exercises[1][1]}', 0, WHITE)
            POS_TASK_1 = TASK_1.get_rect()
            POS_TASK_1.center = (WIDTH//2, HEIGHT//100*8)
            WIN.blit(TASK_1, POS_TASK_1)

            POS_TUNNEL_0_0[0] -= speed*acceleration
            POS_TUNNEL_0_1[0] -= speed*acceleration
            POS_TUNNEL_0_2[0] -= speed*acceleration

            POS_TUNNEL_1_0[0] -= speed*acceleration
            POS_TUNNEL_1_1[0] -= speed*acceleration
            POS_TUNNEL_1_2[0] -= speed*acceleration

            POS_TUNNEL_EQUALS_1_0[0] -= speed*acceleration
            POS_TUNNEL_EQUALS_1_1[0] -= speed*acceleration
            POS_TUNNEL_EQUALS_1_2[0] -= speed*acceleration

            if CAR_RIGHT-6 <= POS_TUNNEL_1_0[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_1_0 == False and ROAD_LANES == 0 and COLLISION == False:
                COLLISION = True
                pygame.time.wait(COLLISION_PAUSE)
                lives -= 1
            elif CAR_RIGHT-6 <= POS_TUNNEL_1_0[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_1_0 == True and ROAD_LANES == 0 and COLLISION == False:
                COLLISION = True
                score += score_limit
            if CAR_RIGHT-6 <= POS_TUNNEL_1_1[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_1_1 == False and ROAD_LANES == 1 and COLLISION == False:
                COLLISION = True
                pygame.time.wait(COLLISION_PAUSE)
                lives -= 1
            elif CAR_RIGHT-6 <= POS_TUNNEL_1_1[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_1_1 == True and ROAD_LANES == 1 and COLLISION == False:
                COLLISION = True
                score += score_limit
            if CAR_RIGHT-6 <= POS_TUNNEL_1_2[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_1_2 == False and ROAD_LANES == 2 and COLLISION == False:
                COLLISION = True
                pygame.time.wait(COLLISION_PAUSE)
                lives -= 1
            elif CAR_RIGHT-6 <= POS_TUNNEL_1_2[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_1_2 == True and ROAD_LANES == 2 and COLLISION == False:
                COLLISION = True
                score += score_limit

            # print(f'{POS_TUNNEL_1_0[0]} {CAR_RIGHT} {score}')

        if 15000 < current_time < 17000:
            COLLISION = False

            POS_TUNNEL_EQUALS_1_0[0] = -WIDTH
            POS_TUNNEL_EQUALS_1_1[0] = -WIDTH
            POS_TUNNEL_EQUALS_1_2[0] = -WIDTH

            POS_TUNNEL_0_0[0] = ST_OFFSET_TUNNEL_0+33
            POS_TUNNEL_0_1[0] = ST_OFFSET_TUNNEL_0+33
            POS_TUNNEL_0_2[0] = ST_OFFSET_TUNNEL_0+33

            POS_TUNNEL_1_0[0] = ST_OFFSET_TUNNEL_1
            POS_TUNNEL_1_1[0] = ST_OFFSET_TUNNEL_1
            POS_TUNNEL_1_2[0] = ST_OFFSET_TUNNEL_1

            POS_TUNNEL_EQUALS_2_0[0] = ST_OFFSET_ANSWER+35
            POS_TUNNEL_EQUALS_2_1[0] = ST_OFFSET_ANSWER+35
            POS_TUNNEL_EQUALS_2_2[0] = ST_OFFSET_ANSWER+35

        if 17000 < current_time < 22000:
            TASK_1 = FONT.render(f'{all_exercises[2][0]}х{all_exercises[2][1]}', 0, WHITE)
            POS_TASK_1 = TASK_1.get_rect()
            POS_TASK_1.center = (WIDTH//2, HEIGHT//100*8)
            WIN.blit(TASK_1, POS_TASK_1)

            POS_TUNNEL_0_0[0] -= speed*acceleration
            POS_TUNNEL_0_1[0] -= speed*acceleration
            POS_TUNNEL_0_2[0] -= speed*acceleration

            POS_TUNNEL_1_0[0] -= speed*acceleration
            POS_TUNNEL_1_1[0] -= speed*acceleration
            POS_TUNNEL_1_2[0] -= speed*acceleration

            POS_TUNNEL_EQUALS_2_0[0] -= speed*acceleration
            POS_TUNNEL_EQUALS_2_1[0] -= speed*acceleration
            POS_TUNNEL_EQUALS_2_2[0] -= speed*acceleration

            if CAR_RIGHT-6 <= POS_TUNNEL_1_0[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_2_0 == False and ROAD_LANES == 0 and COLLISION == False:
                COLLISION = True
                pygame.time.wait(COLLISION_PAUSE)
                lives -= 1
            elif CAR_RIGHT-6 <= POS_TUNNEL_1_0[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_2_0 == True and ROAD_LANES == 0 and COLLISION == False:
                COLLISION = True
                score += score_limit
            if CAR_RIGHT-6 <= POS_TUNNEL_1_1[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_2_1 == False and ROAD_LANES == 1 and COLLISION == False:
                COLLISION = True
                pygame.time.wait(COLLISION_PAUSE)
                lives -= 1
            elif CAR_RIGHT-6 <= POS_TUNNEL_1_1[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_2_1 == True and ROAD_LANES == 1 and COLLISION == False:
                COLLISION = True
                score += score_limit
            if CAR_RIGHT-6 <= POS_TUNNEL_1_2[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_2_2 == False and ROAD_LANES == 2 and COLLISION == False:
                COLLISION = True
                pygame.time.wait(COLLISION_PAUSE)
                lives -= 1
            elif CAR_RIGHT-6 <= POS_TUNNEL_1_2[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_2_2 == True and ROAD_LANES == 2 and COLLISION == False:
                COLLISION = True
                score += score_limit

            # print(f'{POS_TUNNEL_1_0[0]} {CAR_RIGHT} {score}')

        if 22000 < current_time < 24000:
            COLLISION = False

            POS_TUNNEL_EQUALS_2_0[0] = -WIDTH
            POS_TUNNEL_EQUALS_2_1[0] = -WIDTH
            POS_TUNNEL_EQUALS_2_2[0] = -WIDTH

            POS_TUNNEL_0_0[0] = ST_OFFSET_TUNNEL_0+33
            POS_TUNNEL_0_1[0] = ST_OFFSET_TUNNEL_0+33
            POS_TUNNEL_0_2[0] = ST_OFFSET_TUNNEL_0+33

            POS_TUNNEL_1_0[0] = ST_OFFSET_TUNNEL_1
            POS_TUNNEL_1_1[0] = ST_OFFSET_TUNNEL_1
            POS_TUNNEL_1_2[0] = ST_OFFSET_TUNNEL_1

            POS_TUNNEL_EQUALS_3_0[0] = ST_OFFSET_ANSWER+35
            POS_TUNNEL_EQUALS_3_1[0] = ST_OFFSET_ANSWER+35
            POS_TUNNEL_EQUALS_3_2[0] = ST_OFFSET_ANSWER+35

        if 24000 < current_time < 29000:
            TASK_1 = FONT.render(f'{all_exercises[3][0]}х{all_exercises[3][1]}', 0, WHITE)
            POS_TASK_1 = TASK_1.get_rect()
            POS_TASK_1.center = (WIDTH//2, HEIGHT//100*8)
            WIN.blit(TASK_1, POS_TASK_1)

            POS_TUNNEL_0_0[0] -= speed*acceleration
            POS_TUNNEL_0_1[0] -= speed*acceleration
            POS_TUNNEL_0_2[0] -= speed*acceleration

            POS_TUNNEL_1_0[0] -= speed*acceleration
            POS_TUNNEL_1_1[0] -= speed*acceleration
            POS_TUNNEL_1_2[0] -= speed*acceleration

            POS_TUNNEL_EQUALS_3_0[0] -= speed*acceleration
            POS_TUNNEL_EQUALS_3_1[0] -= speed*acceleration
            POS_TUNNEL_EQUALS_3_2[0] -= speed*acceleration

            if CAR_RIGHT-6 <= POS_TUNNEL_1_0[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_3_0 == False and ROAD_LANES == 0 and COLLISION == False:
                COLLISION = True
                pygame.time.wait(COLLISION_PAUSE)
                lives -= 1
            elif CAR_RIGHT-6 <= POS_TUNNEL_1_0[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_3_0 == True and ROAD_LANES == 0 and COLLISION == False:
                COLLISION = True
                score += score_limit
            if CAR_RIGHT-6 <= POS_TUNNEL_1_1[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_3_1 == False and ROAD_LANES == 1 and COLLISION == False:
                COLLISION = True
                pygame.time.wait(COLLISION_PAUSE)
                lives -= 1
            elif CAR_RIGHT-6 <= POS_TUNNEL_1_1[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_3_1 == True and ROAD_LANES == 1 and COLLISION == False:
                COLLISION = True
                score += score_limit
            if CAR_RIGHT-6 <= POS_TUNNEL_1_2[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_3_2 == False and ROAD_LANES == 2 and COLLISION == False:
                COLLISION = True
                pygame.time.wait(COLLISION_PAUSE)
                lives -= 1
            elif CAR_RIGHT-6 <= POS_TUNNEL_1_2[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_3_2 == True and ROAD_LANES == 2 and COLLISION == False:
                COLLISION = True
                score += score_limit

            # print(f'{POS_TUNNEL_1_0[0]} {CAR_RIGHT} {score}')

        if 29000 < current_time < 31000:
            COLLISION = False

            POS_TUNNEL_EQUALS_3_0[0] = -WIDTH
            POS_TUNNEL_EQUALS_3_1[0] = -WIDTH
            POS_TUNNEL_EQUALS_3_2[0] = -WIDTH

            POS_TUNNEL_0_0[0] = ST_OFFSET_TUNNEL_0+33
            POS_TUNNEL_0_1[0] = ST_OFFSET_TUNNEL_0+33
            POS_TUNNEL_0_2[0] = ST_OFFSET_TUNNEL_0+33

            POS_TUNNEL_1_0[0] = ST_OFFSET_TUNNEL_1
            POS_TUNNEL_1_1[0] = ST_OFFSET_TUNNEL_1
            POS_TUNNEL_1_2[0] = ST_OFFSET_TUNNEL_1

            POS_TUNNEL_EQUALS_4_0[0] = ST_OFFSET_ANSWER+35
            POS_TUNNEL_EQUALS_4_1[0] = ST_OFFSET_ANSWER+35
            POS_TUNNEL_EQUALS_4_2[0] = ST_OFFSET_ANSWER+35

        if 31000 < current_time < 36000:
            TASK_1 = FONT.render(f'{all_exercises[4][0]}х{all_exercises[4][1]}', 0, WHITE)
            POS_TASK_1 = TASK_1.get_rect()
            POS_TASK_1.center = (WIDTH//2, HEIGHT//100*8)
            WIN.blit(TASK_1, POS_TASK_1)

            POS_TUNNEL_0_0[0] -= speed*acceleration
            POS_TUNNEL_0_1[0] -= speed*acceleration
            POS_TUNNEL_0_2[0] -= speed*acceleration

            POS_TUNNEL_1_0[0] -= speed*acceleration
            POS_TUNNEL_1_1[0] -= speed*acceleration
            POS_TUNNEL_1_2[0] -= speed*acceleration

            POS_TUNNEL_EQUALS_4_0[0] -= speed*acceleration
            POS_TUNNEL_EQUALS_4_1[0] -= speed*acceleration
            POS_TUNNEL_EQUALS_4_2[0] -= speed*acceleration

            if CAR_RIGHT-6 <= POS_TUNNEL_1_0[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_4_0 == False and ROAD_LANES == 0 and COLLISION == False:
                COLLISION = True
                pygame.time.wait(COLLISION_PAUSE)
                lives -= 1
            elif CAR_RIGHT-6 <= POS_TUNNEL_1_0[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_4_0 == True and ROAD_LANES == 0 and COLLISION == False:
                COLLISION = True
                score += score_limit
            if CAR_RIGHT-6 <= POS_TUNNEL_1_1[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_4_1 == False and ROAD_LANES == 1 and COLLISION == False:
                COLLISION = True
                pygame.time.wait(COLLISION_PAUSE)
                lives -= 1
            elif CAR_RIGHT-6 <= POS_TUNNEL_1_1[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_4_1 == True and ROAD_LANES == 1 and COLLISION == False:
                COLLISION = True
                score += score_limit
            if CAR_RIGHT-6 <= POS_TUNNEL_1_2[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_4_2 == False and ROAD_LANES == 2 and COLLISION == False:
                COLLISION = True
                pygame.time.wait(COLLISION_PAUSE)
                lives -= 1
            elif CAR_RIGHT-6 <= POS_TUNNEL_1_2[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_4_2 == True and ROAD_LANES == 2 and COLLISION == False:
                COLLISION = True
                score += score_limit

            # print(f'{POS_TUNNEL_1_0[0]} {CAR_RIGHT} {score}')

        if 36000 < current_time < 38000:
            COLLISION = False

            POS_TUNNEL_EQUALS_4_0[0] = -WIDTH
            POS_TUNNEL_EQUALS_4_1[0] = -WIDTH
            POS_TUNNEL_EQUALS_4_2[0] = -WIDTH

            POS_TUNNEL_0_0[0] = ST_OFFSET_TUNNEL_0+33
            POS_TUNNEL_0_1[0] = ST_OFFSET_TUNNEL_0+33
            POS_TUNNEL_0_2[0] = ST_OFFSET_TUNNEL_0+33

            POS_TUNNEL_1_0[0] = ST_OFFSET_TUNNEL_1
            POS_TUNNEL_1_1[0] = ST_OFFSET_TUNNEL_1
            POS_TUNNEL_1_2[0] = ST_OFFSET_TUNNEL_1

            POS_TUNNEL_EQUALS_5_0[0] = ST_OFFSET_ANSWER+35
            POS_TUNNEL_EQUALS_5_1[0] = ST_OFFSET_ANSWER+35
            POS_TUNNEL_EQUALS_5_2[0] = ST_OFFSET_ANSWER+35

        if 38000 < current_time < 43000:
            TASK_1 = FONT.render(f'{all_exercises[5][0]}х{all_exercises[5][1]}', 0, WHITE)
            POS_TASK_1 = TASK_1.get_rect()
            POS_TASK_1.center = (WIDTH//2, HEIGHT//100*8)
            WIN.blit(TASK_1, POS_TASK_1)

            POS_TUNNEL_0_0[0] -= speed*acceleration
            POS_TUNNEL_0_1[0] -= speed*acceleration
            POS_TUNNEL_0_2[0] -= speed*acceleration

            POS_TUNNEL_1_0[0] -= speed*acceleration
            POS_TUNNEL_1_1[0] -= speed*acceleration
            POS_TUNNEL_1_2[0] -= speed*acceleration

            POS_TUNNEL_EQUALS_5_0[0] -= speed*acceleration
            POS_TUNNEL_EQUALS_5_1[0] -= speed*acceleration
            POS_TUNNEL_EQUALS_5_2[0] -= speed*acceleration

            if CAR_RIGHT-6 <= POS_TUNNEL_1_0[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_5_0 == False and ROAD_LANES == 0 and COLLISION == False:
                COLLISION = True
                pygame.time.wait(COLLISION_PAUSE)
                lives -= 1
            elif CAR_RIGHT-6 <= POS_TUNNEL_1_0[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_5_0 == True and ROAD_LANES == 0 and COLLISION == False:
                COLLISION = True
                score += score_limit
            if CAR_RIGHT-6 <= POS_TUNNEL_1_1[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_5_1 == False and ROAD_LANES == 1 and COLLISION == False:
                COLLISION = True
                pygame.time.wait(COLLISION_PAUSE)
                lives -= 1
            elif CAR_RIGHT-6 <= POS_TUNNEL_1_1[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_5_1 == True and ROAD_LANES == 1 and COLLISION == False:
                COLLISION = True
                score += score_limit
            if CAR_RIGHT-6 <= POS_TUNNEL_1_2[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_5_2 == False and ROAD_LANES == 2 and COLLISION == False:
                COLLISION = True
                pygame.time.wait(COLLISION_PAUSE)
                lives -= 1
            elif CAR_RIGHT-6 <= POS_TUNNEL_1_2[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_5_2 == True and ROAD_LANES == 2 and COLLISION == False:
                COLLISION = True
                score += score_limit

            # print(f'{POS_TUNNEL_1_0[0]} {CAR_RIGHT} {score}')

        if 43000 < current_time < 45000:
            COLLISION = False

            POS_TUNNEL_EQUALS_5_0[0] = -WIDTH
            POS_TUNNEL_EQUALS_5_1[0] = -WIDTH
            POS_TUNNEL_EQUALS_5_2[0] = -WIDTH

            POS_TUNNEL_0_0[0] = ST_OFFSET_TUNNEL_0+33
            POS_TUNNEL_0_1[0] = ST_OFFSET_TUNNEL_0+33
            POS_TUNNEL_0_2[0] = ST_OFFSET_TUNNEL_0+33

            POS_TUNNEL_1_0[0] = ST_OFFSET_TUNNEL_1
            POS_TUNNEL_1_1[0] = ST_OFFSET_TUNNEL_1
            POS_TUNNEL_1_2[0] = ST_OFFSET_TUNNEL_1

            POS_TUNNEL_EQUALS_6_0[0] = ST_OFFSET_ANSWER+35
            POS_TUNNEL_EQUALS_6_1[0] = ST_OFFSET_ANSWER+35
            POS_TUNNEL_EQUALS_6_2[0] = ST_OFFSET_ANSWER+35

        if 45000 < current_time < 50000:
            TASK_1 = FONT.render(f'{all_exercises[6][0]}х{all_exercises[6][1]}', 0, WHITE)
            POS_TASK_1 = TASK_1.get_rect()
            POS_TASK_1.center = (WIDTH//2, HEIGHT//100*8)
            WIN.blit(TASK_1, POS_TASK_1)

            POS_TUNNEL_0_0[0] -= speed*acceleration
            POS_TUNNEL_0_1[0] -= speed*acceleration
            POS_TUNNEL_0_2[0] -= speed*acceleration

            POS_TUNNEL_1_0[0] -= speed*acceleration
            POS_TUNNEL_1_1[0] -= speed*acceleration
            POS_TUNNEL_1_2[0] -= speed*acceleration

            POS_TUNNEL_EQUALS_6_0[0] -= speed*acceleration
            POS_TUNNEL_EQUALS_6_1[0] -= speed*acceleration
            POS_TUNNEL_EQUALS_6_2[0] -= speed*acceleration

            if CAR_RIGHT-6 <= POS_TUNNEL_1_0[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_6_0 == False and ROAD_LANES == 0 and COLLISION == False:
                COLLISION = True
                pygame.time.wait(COLLISION_PAUSE)
                lives -= 1
            elif CAR_RIGHT-6 <= POS_TUNNEL_1_0[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_6_0 == True and ROAD_LANES == 0 and COLLISION == False:
                COLLISION = True
                score += score_limit
            if CAR_RIGHT-6 <= POS_TUNNEL_1_1[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_6_1 == False and ROAD_LANES == 1 and COLLISION == False:
                COLLISION = True
                pygame.time.wait(COLLISION_PAUSE)
                lives -= 1
            elif CAR_RIGHT-6 <= POS_TUNNEL_1_1[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_6_1 == True and ROAD_LANES == 1 and COLLISION == False:
                COLLISION = True
                score += score_limit
            if CAR_RIGHT-6 <= POS_TUNNEL_1_2[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_6_2 == False and ROAD_LANES == 2 and COLLISION == False:
                COLLISION = True
                pygame.time.wait(COLLISION_PAUSE)
                lives -= 1
            elif CAR_RIGHT-6 <= POS_TUNNEL_1_2[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_6_2 == True and ROAD_LANES == 2 and COLLISION == False:
                COLLISION = True
                score += score_limit

            # print(f'{POS_TUNNEL_1_0[0]} {CAR_RIGHT} {score}')

        if 50000 < current_time < 52000:
            COLLISION = False

            POS_TUNNEL_EQUALS_6_0[0] = -WIDTH
            POS_TUNNEL_EQUALS_6_1[0] = -WIDTH
            POS_TUNNEL_EQUALS_6_2[0] = -WIDTH

            POS_TUNNEL_0_0[0] = ST_OFFSET_TUNNEL_0+33
            POS_TUNNEL_0_1[0] = ST_OFFSET_TUNNEL_0+33
            POS_TUNNEL_0_2[0] = ST_OFFSET_TUNNEL_0+33

            POS_TUNNEL_1_0[0] = ST_OFFSET_TUNNEL_1
            POS_TUNNEL_1_1[0] = ST_OFFSET_TUNNEL_1
            POS_TUNNEL_1_2[0] = ST_OFFSET_TUNNEL_1

            POS_TUNNEL_EQUALS_7_0[0] = ST_OFFSET_ANSWER+35
            POS_TUNNEL_EQUALS_7_1[0] = ST_OFFSET_ANSWER+35
            POS_TUNNEL_EQUALS_7_2[0] = ST_OFFSET_ANSWER+35

        if 52000 < current_time < 57000:
            TASK_1 = FONT.render(f'{all_exercises[7][0]}х{all_exercises[7][1]}', 0, WHITE)
            POS_TASK_1 = TASK_1.get_rect()
            POS_TASK_1.center = (WIDTH//2, HEIGHT//100*8)
            WIN.blit(TASK_1, POS_TASK_1)

            POS_TUNNEL_0_0[0] -= speed*acceleration
            POS_TUNNEL_0_1[0] -= speed*acceleration
            POS_TUNNEL_0_2[0] -= speed*acceleration

            POS_TUNNEL_1_0[0] -= speed*acceleration
            POS_TUNNEL_1_1[0] -= speed*acceleration
            POS_TUNNEL_1_2[0] -= speed*acceleration

            POS_TUNNEL_EQUALS_7_0[0] -= speed*acceleration
            POS_TUNNEL_EQUALS_7_1[0] -= speed*acceleration
            POS_TUNNEL_EQUALS_7_2[0] -= speed*acceleration

            if CAR_RIGHT-6 <= POS_TUNNEL_1_0[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_7_0 == False and ROAD_LANES == 0 and COLLISION == False:
                COLLISION = True
                pygame.time.wait(COLLISION_PAUSE)
                lives -= 1
            elif CAR_RIGHT-6 <= POS_TUNNEL_1_0[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_7_0 == True and ROAD_LANES == 0 and COLLISION == False:
                COLLISION = True
                score += score_limit
            if CAR_RIGHT-6 <= POS_TUNNEL_1_1[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_7_1 == False and ROAD_LANES == 1 and COLLISION == False:
                COLLISION = True
                pygame.time.wait(COLLISION_PAUSE)
                lives -= 1
            elif CAR_RIGHT-6 <= POS_TUNNEL_1_1[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_7_1 == True and ROAD_LANES == 1 and COLLISION == False:
                COLLISION = True
                score += score_limit
            if CAR_RIGHT-6 <= POS_TUNNEL_1_2[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_7_2 == False and ROAD_LANES == 2 and COLLISION == False:
                COLLISION = True
                pygame.time.wait(COLLISION_PAUSE)
                lives -= 1
            elif CAR_RIGHT-6 <= POS_TUNNEL_1_2[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_7_2 == True and ROAD_LANES == 2 and COLLISION == False:
                COLLISION = True
                score += score_limit

            # print(f'{POS_TUNNEL_1_0[0]} {CAR_RIGHT} {score}')

        if 57000 < current_time < 59000:
            COLLISION = False

            POS_TUNNEL_EQUALS_7_0[0] = -WIDTH
            POS_TUNNEL_EQUALS_7_1[0] = -WIDTH
            POS_TUNNEL_EQUALS_7_2[0] = -WIDTH

            POS_TUNNEL_0_0[0] = ST_OFFSET_TUNNEL_0+33
            POS_TUNNEL_0_1[0] = ST_OFFSET_TUNNEL_0+33
            POS_TUNNEL_0_2[0] = ST_OFFSET_TUNNEL_0+33

            POS_TUNNEL_1_0[0] = ST_OFFSET_TUNNEL_1
            POS_TUNNEL_1_1[0] = ST_OFFSET_TUNNEL_1
            POS_TUNNEL_1_2[0] = ST_OFFSET_TUNNEL_1

            POS_TUNNEL_EQUALS_8_0[0] = ST_OFFSET_ANSWER+35
            POS_TUNNEL_EQUALS_8_1[0] = ST_OFFSET_ANSWER+35
            POS_TUNNEL_EQUALS_8_2[0] = ST_OFFSET_ANSWER+35

        if 59000 < current_time < 64000:
            TASK_1 = FONT.render(f'{all_exercises[8][0]}х{all_exercises[8][1]}', 0, WHITE)
            POS_TASK_1 = TASK_1.get_rect()
            POS_TASK_1.center = (WIDTH//2, HEIGHT//100*8)
            WIN.blit(TASK_1, POS_TASK_1)

            POS_TUNNEL_0_0[0] -= speed*acceleration
            POS_TUNNEL_0_1[0] -= speed*acceleration
            POS_TUNNEL_0_2[0] -= speed*acceleration

            POS_TUNNEL_1_0[0] -= speed*acceleration
            POS_TUNNEL_1_1[0] -= speed*acceleration
            POS_TUNNEL_1_2[0] -= speed*acceleration

            POS_TUNNEL_EQUALS_8_0[0] -= speed*acceleration
            POS_TUNNEL_EQUALS_8_1[0] -= speed*acceleration
            POS_TUNNEL_EQUALS_8_2[0] -= speed*acceleration

            if CAR_RIGHT-6 <= POS_TUNNEL_1_0[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_8_0 == False and ROAD_LANES == 0 and COLLISION == False:
                COLLISION = True
                pygame.time.wait(COLLISION_PAUSE)
                lives -= 1
            elif CAR_RIGHT-6 <= POS_TUNNEL_1_0[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_8_0 == True and ROAD_LANES == 0 and COLLISION == False:
                COLLISION = True
                score += score_limit
            if CAR_RIGHT-6 <= POS_TUNNEL_1_1[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_8_1 == False and ROAD_LANES == 1 and COLLISION == False:
                COLLISION = True
                pygame.time.wait(COLLISION_PAUSE)
                lives -= 1
            elif CAR_RIGHT-6 <= POS_TUNNEL_1_1[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_8_1 == True and ROAD_LANES == 1 and COLLISION == False:
                COLLISION = True
                score += score_limit
            if CAR_RIGHT-6 <= POS_TUNNEL_1_2[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_8_2 == False and ROAD_LANES == 2 and COLLISION == False:
                COLLISION = True
                pygame.time.wait(COLLISION_PAUSE)
                lives -= 1
            elif CAR_RIGHT-6 <= POS_TUNNEL_1_2[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_8_2 == True and ROAD_LANES == 2 and COLLISION == False:
                COLLISION = True
                score += score_limit

            # print(f'{POS_TUNNEL_1_0[0]} {CAR_RIGHT} {score}')

        if 64000 < current_time < 66000:
            COLLISION = False

            POS_TUNNEL_EQUALS_8_0[0] = -WIDTH
            POS_TUNNEL_EQUALS_8_1[0] = -WIDTH
            POS_TUNNEL_EQUALS_8_2[0] = -WIDTH

            POS_TUNNEL_0_0[0] = ST_OFFSET_TUNNEL_0+33
            POS_TUNNEL_0_1[0] = ST_OFFSET_TUNNEL_0+33
            POS_TUNNEL_0_2[0] = ST_OFFSET_TUNNEL_0+33

            POS_TUNNEL_1_0[0] = ST_OFFSET_TUNNEL_1
            POS_TUNNEL_1_1[0] = ST_OFFSET_TUNNEL_1
            POS_TUNNEL_1_2[0] = ST_OFFSET_TUNNEL_1

            POS_TUNNEL_EQUALS_9_0[0] = ST_OFFSET_ANSWER+35
            POS_TUNNEL_EQUALS_9_1[0] = ST_OFFSET_ANSWER+35
            POS_TUNNEL_EQUALS_9_2[0] = ST_OFFSET_ANSWER+35

        if 66000 < current_time < 71000:
            TASK_1 = FONT.render(f'{all_exercises[9][0]}х{all_exercises[9][1]}', 0, WHITE)
            POS_TASK_1 = TASK_1.get_rect()
            POS_TASK_1.center = (WIDTH//2, HEIGHT//100*8)
            WIN.blit(TASK_1, POS_TASK_1)

            POS_TUNNEL_0_0[0] -= speed*acceleration
            POS_TUNNEL_0_1[0] -= speed*acceleration
            POS_TUNNEL_0_2[0] -= speed*acceleration

            POS_TUNNEL_1_0[0] -= speed*acceleration
            POS_TUNNEL_1_1[0] -= speed*acceleration
            POS_TUNNEL_1_2[0] -= speed*acceleration

            POS_TUNNEL_EQUALS_9_0[0] -= speed*acceleration
            POS_TUNNEL_EQUALS_9_1[0] -= speed*acceleration
            POS_TUNNEL_EQUALS_9_2[0] -= speed*acceleration

            if CAR_RIGHT-6 <= POS_TUNNEL_1_0[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_9_0 == False and ROAD_LANES == 0 and COLLISION == False:
                COLLISION = True
                pygame.time.wait(COLLISION_PAUSE)
                lives -= 1
            elif CAR_RIGHT-6 <= POS_TUNNEL_1_0[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_9_0 == True and ROAD_LANES == 0 and COLLISION == False:
                COLLISION = True
                score += score_limit
            if CAR_RIGHT-6 <= POS_TUNNEL_1_1[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_9_1 == False and ROAD_LANES == 1 and COLLISION == False:
                COLLISION = True
                pygame.time.wait(COLLISION_PAUSE)
                lives -= 1
            elif CAR_RIGHT-6 <= POS_TUNNEL_1_1[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_9_1 == True and ROAD_LANES == 1 and COLLISION == False:
                COLLISION = True
                score += score_limit
            if CAR_RIGHT-6 <= POS_TUNNEL_1_2[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_9_2 == False and ROAD_LANES == 2 and COLLISION == False:
                COLLISION = True
                pygame.time.wait(COLLISION_PAUSE)
                lives -= 1
            elif CAR_RIGHT-6 <= POS_TUNNEL_1_2[0] <= CAR_RIGHT+6 and TUNNEL_LOGIC_9_2 == True and ROAD_LANES == 2 and COLLISION == False:
                COLLISION = True
                score += score_limit

            # print(f'{POS_TUNNEL_1_0[0]} {CAR_RIGHT} {score}')

        if 71000 < current_time < 73000:
            COLLISION = False

            POS_TUNNEL_EQUALS_9_0[0] = -WIDTH
            POS_TUNNEL_EQUALS_9_1[0] = -WIDTH
            POS_TUNNEL_EQUALS_9_2[0] = -WIDTH

            POS_TUNNEL_0_0[0] = ST_OFFSET_TUNNEL_0+33
            POS_TUNNEL_0_1[0] = ST_OFFSET_TUNNEL_0+33
            POS_TUNNEL_0_2[0] = ST_OFFSET_TUNNEL_0+33

            POS_TUNNEL_1_0[0] = ST_OFFSET_TUNNEL_1
            POS_TUNNEL_1_1[0] = ST_OFFSET_TUNNEL_1
            POS_TUNNEL_1_2[0] = ST_OFFSET_TUNNEL_1
        
        if 73000 < current_time:
            WIN.blit(MAIN_MENU_BACK, POS_BACK)
            GAME_OVER = FONT.render(f'ПОБЕДА!', 0, WHITE)
            POS_GAME_OVER = GAME_OVER.get_rect(center=(WIDTH//2, HEIGHT//2-100))
            GAME_OVER_SCORE = FONT.render(f'ВАШ СЧЕТ: {score}', 0, WHITE)
            POS_GAME_OVER_SCORE = GAME_OVER_SCORE.get_rect(center=(WIDTH//2, HEIGHT//2))
            WIN.blit(GAME_OVER, POS_GAME_OVER)
            WIN.blit(GAME_OVER_SCORE, POS_GAME_OVER_SCORE)


    if lives != 0:
        SCORE_0 = FONT_SCORE.render(f'{score}', 0, WHITE)
        POS_SCORE_0 = SCORE_0.get_rect(center=(WIDTH//100*92, HEIGHT//100*99+30))
        WIN.blit(SCORE_0, POS_SCORE_0)

    pygame.display.update()
    clock.tick(60)

