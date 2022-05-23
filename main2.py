import pygame
from pygame.locals import *
from spritelist_menu import *
from osts import *
from lvl1 import *


pygame.display.set_caption('Solve The Road')

MAIN_MENU_START = FONT.render('START', 0, WHITE)
MAIN_MENU_OPTIONS = FONT.render('УРОВЕНЬ', 0, WHITE)
MAIN_MENU_EXIT = FONT.render('ВЫХОД', 0, WHITE)

POS_START = MAIN_MENU_START.get_rect(center=(WIDTH//2, HEIGHT//10*4))
POS_OPTIONS = MAIN_MENU_OPTIONS.get_rect(center=(WIDTH//2, HEIGHT//10*5))
POS_EXIT = MAIN_MENU_EXIT.get_rect(center=(WIDTH//2, HEIGHT//10*6))

pygame.display.set_caption('LVL1')
clock = pygame.time.Clock()
i = 0
exercises = 10

all_exercises, all_answers, all_answer_flag, all_answer_flags_last = [], [], [], []

for exercise in range(10):
    first_sum = random.randint(0, 90)
    second_sum = random.randint(0, 100-first_sum-1)
    sum_true = first_sum + second_sum
    sum_fake_1 = sum_true + random.randint(-10, 10)
    sum_fake_2 = sum_true + random.randint(-10, 10)
    # if sum_true == sum_fake_1 or sum_true
    all_exercises.append(
        [first_sum, second_sum, sum_true, sum_fake_1, sum_fake_2])
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

    ostatok = current_time % 10

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
        POS_GAME_OVER_SCORE = GAME_OVER_SCORE.get_rect(
            center=(WIDTH//2, HEIGHT//2))
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



ROAD_LANES = 1
lives = 3
score = 0
score_limit = 1
COLLISION = False
COLLISION_PAUSE = 1000
pressed = pygame.key.get_pressed()

def lvl1():
    print()       

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
                run_1 = True
                run = False

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
