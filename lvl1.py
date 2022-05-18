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
k = [2, 3, 4]

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

print(all_exercises)
print(all_answers)

for all_answer in all_answers:
    new_answers = all_answer
    random.shuffle(new_answers)

print(all_answers)

# print(all_exercises[0][k[0]], all_exercises[0][k[1]], all_exercises[0][k[2]])
TUNNEL_EQUALS_0 = FONT.render(f'{all_answers[0][0]}', 0, WHITE)
POS_TUNNEL_EQUALS_0 = TUNNEL_EQUALS_0.get_rect()
POS_TUNNEL_EQUALS_0.center = WIDTH//100*129, HEIGHT//100*46

TUNNEL_EQUALS_1 = FONT.render(f'{all_answers[0][1]}', 0, WHITE)
POS_TUNNEL_EQUALS_1 = TUNNEL_EQUALS_1.get_rect()
POS_TUNNEL_EQUALS_1.center = WIDTH//100*124, HEIGHT//100*66

TUNNEL_EQUALS_2 = FONT.render(f'{all_answers[0][2]}', 0, WHITE)
POS_TUNNEL_EQUALS_2 = TUNNEL_EQUALS_2.get_rect()
POS_TUNNEL_EQUALS_2.center = WIDTH//100*128, HEIGHT//100*88


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

    WIN.blit(TUNNEL, POS_TUNNEL_0)
    WIN.blit(TUNNEL, POS_TUNNEL_1)
    WIN.blit(TUNNEL, POS_TUNNEL_2)

    WIN.blit(TUNNEL_EQUALS_0, POS_TUNNEL_EQUALS_0)
    WIN.blit(TUNNEL_EQUALS_1, POS_TUNNEL_EQUALS_1)
    WIN.blit(TUNNEL_EQUALS_2, POS_TUNNEL_EQUALS_2)

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

        
    if 3000 < current_time < 8000:
        TASK_1 = FONT.render(f'{all_exercises[0][0]}+{all_exercises[0][1]}', 0, WHITE)
        POS_TASK_1 = TASK_1.get_rect()
        POS_TASK_1.center = (WIDTH//2, HEIGHT//100*8)
        WIN.blit(TASK_1, POS_TASK_1)

        POS_TUNNEL_0[0] -= speed*acceleration
        POS_TUNNEL_1[0] -= speed*acceleration
        POS_TUNNEL_2[0] -= speed*acceleration

        POS_TUNNEL_EQUALS_0[0] -= speed*acceleration
        POS_TUNNEL_EQUALS_1[0] -= speed*acceleration
        POS_TUNNEL_EQUALS_2[0] -= speed*acceleration
        
    if 8000 < current_time < 10000:
        POS_TUNNEL_0[0] = WIDTH//100*127
        POS_TUNNEL_1[0] = WIDTH//100*122
        POS_TUNNEL_2[0] = WIDTH//100*126

    if 10000 < current_time < 15000:
        TASK_1 = FONT.render(f'{all_exercises[1][0]}+{all_exercises[1][1]}', 0, WHITE)
        POS_TASK_1 = TASK_1.get_rect(center=(WIDTH//2, HEIGHT//100*8))
        WIN.blit(TASK_1, POS_TASK_1)
            
        POS_TUNNEL_0[0] -= speed*acceleration
        POS_TUNNEL_1[0] -= speed*acceleration
        POS_TUNNEL_2[0] -= speed*acceleration

    if i <= -WIDTH:
        WIN.blit(ROAD, (i+WIDTH, 0))
        i = 0
    i -= speed*acceleration


    if ROAD_LANES == 0:
        WIN.blit(CAR, POS_CAR_0)
        # print(ROAD_LANES)
    elif ROAD_LANES == 1:
        WIN.blit(CAR, POS_CAR_1)
        # print(ROAD_LANES)
    elif ROAD_LANES == 2:
        WIN.blit(CAR, POS_CAR_2)
        # print(ROAD_LANES)
    elif ROAD_LANES > 2:
        ROAD_LANES = 2
    elif ROAD_LANES < 0:
        ROAD_LANES = 0
        
    

    # POS_ROAD[0] -= speed*acceleration
    # if POS_ROAD[0] < -WIDTH:
    #     POS_ROAD.center = WIDTH, HEIGHT//2
            
    pygame.display.update()
    clock.tick(60)

