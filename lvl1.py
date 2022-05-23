from hashlib import new
from numpy import append
import math
import pygame
import random
from pygame.locals import *
from spritelist2 import *
from osts import *


pygame.display.set_caption('LVL1')
clock = pygame.time.Clock()
i = 0
exercises = 10
lives = 3

all_exercises, all_answers, all_answer_flag, all_answer_flags_last = [], [], [], []

for exercise in range(10):
    first_sum = random.randint(0, 90)
    second_sum = random.randint(0, 100-first_sum-1)
    sum_true = first_sum + second_sum
    sum_fake_1 = sum_true + random.randint(-10, 10)
    sum_fake_2 = sum_true + random.randint(-10, 10)
    # if sum_true == sum_fake_1 or sum_true
    all_exercises.append([first_sum, second_sum, sum_true, sum_fake_1, sum_fake_2])
    all_answers.append([sum_true, sum_fake_1, sum_fake_2])

# print(all_exercises)
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

TUNNEL_EQUALS_2_0 = FONT.render(f'{all_answers[1][0]}', 0, WHITE)
POS_TUNNEL_EQUALS_2_0 = TUNNEL_EQUALS_2_0.get_rect()
POS_TUNNEL_EQUALS_2_0.center = ST_OFFSET_ANSWER, HEIGHT//100*46
TUNNEL_LOGIC_2_0 = all_answer_flag[6]

TUNNEL_EQUALS_2_1 = FONT.render(f'{all_answers[1][1]}', 0, WHITE)
POS_TUNNEL_EQUALS_2_1 = TUNNEL_EQUALS_2_1.get_rect()
POS_TUNNEL_EQUALS_2_1.center = ST_OFFSET_ANSWER, HEIGHT//100*66
TUNNEL_LOGIC_2_1 = all_answer_flag[7]

TUNNEL_EQUALS_2_2 = FONT.render(f'{all_answers[1][2]}', 0, WHITE)
POS_TUNNEL_EQUALS_2_2 = TUNNEL_EQUALS_2_2.get_rect()
POS_TUNNEL_EQUALS_2_2.center = ST_OFFSET_ANSWER, HEIGHT//100*88
TUNNEL_LOGIC_2_2 = all_answer_flag[8]

def draw_all():
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

    WIN.blit(CAR, POS_CAR)

    WIN.blit(TUNNEL_1, POS_TUNNEL_1_0)
    WIN.blit(TUNNEL_1, POS_TUNNEL_1_1)
    WIN.blit(TUNNEL_1, POS_TUNNEL_1_2)

    WIN.blit(TUNNEL_EQUALS_0_0, POS_TUNNEL_EQUALS_0_0)
    WIN.blit(TUNNEL_EQUALS_0_1, POS_TUNNEL_EQUALS_0_1)
    WIN.blit(TUNNEL_EQUALS_0_2, POS_TUNNEL_EQUALS_0_2)

    WIN.blit(TUNNEL_EQUALS_1_0, POS_TUNNEL_EQUALS_1_0)
    WIN.blit(TUNNEL_EQUALS_1_1, POS_TUNNEL_EQUALS_1_1)
    WIN.blit(TUNNEL_EQUALS_1_2, POS_TUNNEL_EQUALS_1_2)
    
    WIN.blit(TUNNEL_EQUALS_1_0, POS_TUNNEL_EQUALS_2_0)
    WIN.blit(TUNNEL_EQUALS_1_1, POS_TUNNEL_EQUALS_2_1)
    WIN.blit(TUNNEL_EQUALS_1_2, POS_TUNNEL_EQUALS_2_2)

run = True
ROAD_LANES = 1
lives = 3
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

        
    if 3000 < current_time < 8000:
        TASK_1 = FONT.render(f'{all_exercises[0][0]}+{all_exercises[0][1]}', 0, WHITE)
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

        
        
    if 8000 < current_time < 10000:
        POS_TUNNEL_0_0[0] = ST_OFFSET_TUNNEL_0+33
        POS_TUNNEL_0_1[0] = ST_OFFSET_TUNNEL_0+33
        POS_TUNNEL_0_2[0] = ST_OFFSET_TUNNEL_0+33

        POS_TUNNEL_1_0[0] = ST_OFFSET_TUNNEL_1
        POS_TUNNEL_1_1[0] = ST_OFFSET_TUNNEL_1
        POS_TUNNEL_1_2[0] = ST_OFFSET_TUNNEL_1

        POS_TUNNEL_EQUALS_1_0[0] = ST_OFFSET_ANSWER+35
        POS_TUNNEL_EQUALS_1_1[0] = ST_OFFSET_ANSWER+35
        POS_TUNNEL_EQUALS_1_2[0] = ST_OFFSET_ANSWER+35
        # pygame.time.wait(2000)

    if 10000 < current_time < 15000:
        TASK_1 = FONT.render(f'{all_exercises[1][0]}+{all_exercises[1][1]}', 0, WHITE)
        POS_TASK_1 = TASK_1.get_rect(center=(WIDTH//2, HEIGHT//100*8))
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
    
    if 15000 < current_time < 17000:
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
        TASK_1 = FONT.render(f'{all_exercises[2][0]}+{all_exercises[2][1]}', 0, WHITE)
        POS_TASK_1 = TASK_1.get_rect(center=(WIDTH//2, HEIGHT//100*8))
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

    if 22000 < current_time < 24000:
        POS_TUNNEL_0_0[0] = ST_OFFSET_TUNNEL_0+33
        POS_TUNNEL_0_1[0] = ST_OFFSET_TUNNEL_0+33
        POS_TUNNEL_0_2[0] = ST_OFFSET_TUNNEL_0+33

        POS_TUNNEL_1_0[0] = ST_OFFSET_TUNNEL_1
        POS_TUNNEL_1_1[0] = ST_OFFSET_TUNNEL_1
        POS_TUNNEL_1_2[0] = ST_OFFSET_TUNNEL_1
        

    
        
            
    pygame.display.update()
    clock.tick(60)

