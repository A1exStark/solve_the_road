from hashlib import new
from numpy import append
import pygame
import random
from pygame.locals import *
from spritelist2 import *
from osts import *


pygame.display.set_caption('LVL1')
clock = pygame.time.Clock()
i = 0


all_exercises = []
all_answers = []
for exercise in range(10):
    first_sum = random.randint(0, 90)
    second_sum = random.randint(0, 100-first_sum-1)
    sum_true = first_sum + second_sum
    sum_fake_1 = sum_true + random.randint(-10, 10)
    sum_fake_2 = sum_true + random.randint(-10, 10)
    all_exercises.append([first_sum, second_sum, sum_true, sum_fake_1, sum_fake_2])
    all_answers.append([sum_true, sum_fake_1, sum_fake_2])

# print(all_exercises)
# print(all_answers)

for all_answer in all_answers:
    new_answers = all_answer
    random.shuffle(new_answers)

# print(all_answers)

TUNNEL_EQUALS_0_0 = FONT.render(f'{all_answers[0][0]}', 0, WHITE)
POS_TUNNEL_EQUALS_0_0 = TUNNEL_EQUALS_0_0.get_rect()
POS_TUNNEL_EQUALS_0_0.center = ST_OFFSET_ANSWER, HEIGHT//100*46

TUNNEL_EQUALS_0_1 = FONT.render(f'{all_answers[0][1]}', 0, WHITE)
POS_TUNNEL_EQUALS_0_1 = TUNNEL_EQUALS_0_1.get_rect()
POS_TUNNEL_EQUALS_0_1.center = ST_OFFSET_ANSWER, HEIGHT//100*66

TUNNEL_EQUALS_0_2 = FONT.render(f'{all_answers[0][2]}', 0, WHITE)
POS_TUNNEL_EQUALS_0_2 = TUNNEL_EQUALS_0_2.get_rect()
POS_TUNNEL_EQUALS_0_2.center = ST_OFFSET_ANSWER, HEIGHT//100*88

TUNNEL_EQUALS_1_0 = FONT.render(f'{all_answers[1][0]}', 0, WHITE)
POS_TUNNEL_EQUALS_1_0 = TUNNEL_EQUALS_1_0.get_rect()
POS_TUNNEL_EQUALS_1_0.center = ST_OFFSET_ANSWER, HEIGHT//100*46

TUNNEL_EQUALS_1_1 = FONT.render(f'{all_answers[1][1]}', 0, WHITE)
POS_TUNNEL_EQUALS_1_1 = TUNNEL_EQUALS_1_1.get_rect()
POS_TUNNEL_EQUALS_1_1.center = ST_OFFSET_ANSWER, HEIGHT//100*66

TUNNEL_EQUALS_1_2 = FONT.render(f'{all_answers[1][2]}', 0, WHITE)
POS_TUNNEL_EQUALS_1_2 = TUNNEL_EQUALS_1_2.get_rect()
POS_TUNNEL_EQUALS_1_2.center = ST_OFFSET_ANSWER, HEIGHT//100*88

TUNNEL_EQUALS_2_0 = FONT.render(f'{all_answers[1][0]}', 0, WHITE)
POS_TUNNEL_EQUALS_2_0 = TUNNEL_EQUALS_2_0.get_rect()
POS_TUNNEL_EQUALS_2_0.center = ST_OFFSET_ANSWER, HEIGHT//100*46

TUNNEL_EQUALS_2_1 = FONT.render(f'{all_answers[1][1]}', 0, WHITE)
POS_TUNNEL_EQUALS_2_1 = TUNNEL_EQUALS_2_1.get_rect()
POS_TUNNEL_EQUALS_2_1.center = ST_OFFSET_ANSWER, HEIGHT//100*66

TUNNEL_EQUALS_2_2 = FONT.render(f'{all_answers[1][2]}', 0, WHITE)
POS_TUNNEL_EQUALS_2_2 = TUNNEL_EQUALS_2_2.get_rect()
POS_TUNNEL_EQUALS_2_2.center = ST_OFFSET_ANSWER, HEIGHT//100*88

def draw_all():
    WIN.blit(BG, POS_BG)
    WIN.blit(MOUNTAINS, POS_MOUNTAINS)
    WIN.blit(FOREST, POS_FOREST)
    WIN.blit(ROAD, (i, 0))
    WIN.blit(ROAD, (WIDTH+i, 0))
    # WIN.blit(ROAD, POS_ROAD)
    WIN.blit(TASK, POS_TASK)
    
    WIN.blit(HEART, POS_HEART)
    WIN.blit(SCORE, POS_SCORE)
    WIN.blit(PAUSE, POS_PAUSE)

    WIN.blit(CAR, POS_CAR)

    WIN.blit(TUNNEL, POS_TUNNEL_0)
    WIN.blit(TUNNEL, POS_TUNNEL_1)
    WIN.blit(TUNNEL, POS_TUNNEL_2)

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

        POS_TUNNEL_0[0] -= speed*acceleration
        POS_TUNNEL_1[0] -= speed*acceleration
        POS_TUNNEL_2[0] -= speed*acceleration

        POS_TUNNEL_EQUALS_0_0[0] -= speed*acceleration
        POS_TUNNEL_EQUALS_0_1[0] -= speed*acceleration
        POS_TUNNEL_EQUALS_0_2[0] -= speed*acceleration
        
    if 8000 < current_time < 10000:
        POS_TUNNEL_0[0] = ST_OFFSET_TUNNEL
        POS_TUNNEL_1[0] = ST_OFFSET_TUNNEL
        POS_TUNNEL_2[0] = ST_OFFSET_TUNNEL
        POS_TUNNEL_EQUALS_1_0[0] = ST_OFFSET_ANSWER+70
        POS_TUNNEL_EQUALS_1_1[0] = ST_OFFSET_ANSWER+70
        POS_TUNNEL_EQUALS_1_2[0] = ST_OFFSET_ANSWER+70

    if 10000 < current_time < 15000:
        TASK_1 = FONT.render(f'{all_exercises[1][0]}+{all_exercises[1][1]}', 0, WHITE)
        POS_TASK_1 = TASK_1.get_rect(center=(WIDTH//2, HEIGHT//100*8))
        WIN.blit(TASK_1, POS_TASK_1)
            
        POS_TUNNEL_0[0] -= speed*acceleration
        POS_TUNNEL_1[0] -= speed*acceleration
        POS_TUNNEL_2[0] -= speed*acceleration

        POS_TUNNEL_EQUALS_1_0[0] -= speed*acceleration
        POS_TUNNEL_EQUALS_1_1[0] -= speed*acceleration
        POS_TUNNEL_EQUALS_1_2[0] -= speed*acceleration
    
    if 15000 < current_time < 17000:
        POS_TUNNEL_0[0] = ST_OFFSET_TUNNEL
        POS_TUNNEL_1[0] = ST_OFFSET_TUNNEL
        POS_TUNNEL_2[0] = ST_OFFSET_TUNNEL
        POS_TUNNEL_EQUALS_2_0[0] = ST_OFFSET_ANSWER+70
        POS_TUNNEL_EQUALS_2_1[0] = ST_OFFSET_ANSWER+70
        POS_TUNNEL_EQUALS_2_2[0] = ST_OFFSET_ANSWER+70

    if 17000 < current_time < 22000:
        TASK_1 = FONT.render(f'{all_exercises[2][0]}+{all_exercises[2][1]}', 0, WHITE)
        POS_TASK_1 = TASK_1.get_rect(center=(WIDTH//2, HEIGHT//100*8))
        WIN.blit(TASK_1, POS_TASK_1)

        POS_TUNNEL_0[0] -= speed*acceleration
        POS_TUNNEL_1[0] -= speed*acceleration
        POS_TUNNEL_2[0] -= speed*acceleration

        POS_TUNNEL_EQUALS_2_0[0] -= speed*acceleration
        POS_TUNNEL_EQUALS_2_1[0] -= speed*acceleration
        POS_TUNNEL_EQUALS_2_2[0] -= speed*acceleration

    if 22000 < current_time < 24000:
        POS_TUNNEL_0[0] = ST_OFFSET_TUNNEL
        POS_TUNNEL_1[0] = ST_OFFSET_TUNNEL
        POS_TUNNEL_2[0] = ST_OFFSET_TUNNEL
        

    
        
    

    # POS_ROAD[0] -= speed*acceleration
    # if POS_ROAD[0] < -WIDTH:
    #     POS_ROAD.center = WIDTH, HEIGHT//2
            
    pygame.display.update()
    clock.tick(60)

