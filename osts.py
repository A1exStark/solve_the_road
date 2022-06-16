import pygame

pygame.mixer.pre_init(44100, -32, 2, 2048)
pygame.font.init()



# pygame.mixer.music.load('ost/Nightcall.ogg')
# pygame.mixer.music.set_volume(0.1)
# pygame.mixer.music.play(loops=-1, start=0.0, fade_ms=300)
MUTE = 0
MAIN_MENU_SELECT_SONUD = pygame.mixer.Sound('ost/sfx_menu_select.wav')
MAIN_MENU_SELECT_SONUD.set_volume(MUTE*0.1)
MAIN_MENU_SELECTED_SONUD = pygame.mixer.Sound('ost/sfx_menu_selected.wav')
MAIN_MENU_SELECTED_SONUD.set_volume(MUTE*0.1)

LVL_START_SOUND = pygame.mixer.Sound('ost/lvl_start.wav')
LVL_START_SOUND.set_volume(MUTE*0.5)

GATE_SOUND = pygame.mixer.Sound('ost/gate.wav')
GATE_SOUND.set_volume(MUTE*0.3)

CAR_HIT_SOUND = pygame.mixer.Sound('ost/car_hit.wav')
CAR_HIT_SOUND.set_volume(MUTE*0.3)

CAR_HIT_SOUND_2 = pygame.mixer.Sound('ost/car_hit_2.wav')
CAR_HIT_SOUND_2.set_volume(MUTE*0.5)


LVL_COMPLETE_SOUND = pygame.mixer.Sound('ost/lvl_complete.wav')
LVL_COMPLETE_SOUND.set_volume(MUTE*0.3)
GAME_OVER_SOUND = pygame.mixer.Sound('ost/game_over.wav')
GAME_OVER_SOUND.set_volume(MUTE*0.3)



