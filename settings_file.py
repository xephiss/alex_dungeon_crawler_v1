from pygame.locals import *

settings_saved = open('settings_save.txt', 'r')   # Opens a text file
preset = str(settings_saved.readline()) # Reads and saves the first line
health_modifier = float(str(settings_saved.readline())[0:3])
movement_modifier = float(settings_saved.readline())
damage_modifier = float(settings_saved.readline())
settings_saved.close()

if preset == 'preset_wasd\n':
    move_key_up = K_w
    move_key_down = K_s
    move_key_left = K_a
    move_key_right = K_d

    attack_key_up = K_UP
    attack_key_down = K_DOWN
    attack_key_left = K_LEFT
    attack_key_right = K_RIGHT

elif preset == 'preset_arrow\n':
    move_key_up = K_UP
    move_key_down = K_DOWN
    move_key_left = K_LEFT
    move_key_right = K_RIGHT

    attack_key_up = K_w
    attack_key_down = K_s
    attack_key_left = K_a
    attack_key_right = K_d
