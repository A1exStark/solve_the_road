import pygame

pygame.mixer.pre_init(44100, -32, 2, 2048)
pygame.font.init()



# pygame.mixer.music.load('ost/Nightcall.ogg')
# pygame.mixer.music.set_volume(0.1)
# pygame.mixer.music.play(loops=-1, start=0.0, fade_ms=300)

MAIN_MENU_SELECT_SONUD = pygame.mixer.Sound('ost/sfx_menu_select.wav')
MAIN_MENU_SELECT_SONUD.set_volume(0.1)
MAIN_MENU_SELECTED_SONUD = pygame.mixer.Sound('ost/sfx_menu_selected.wav')
MAIN_MENU_SELECTED_SONUD.set_volume(0.1)

LVL_START_SOUND = pygame.mixer.Sound('ost/lvl_start.wav')
LVL_START_SOUND.set_volume(0.3)
