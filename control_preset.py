from pygame.locals import *


preset_saved = open('control_preset.py', 'r')
preset_number = preset_saved.readline()
preset_saved.close()

if preset_number == 0:
    move_key_up = K_w
    move_key_down = K_s
    move_key_left = K_a
    move_key_right = K_d

    attack_key_up = K_UP
    attack_key_down = K_DOWN
    attack_key_left = K_LEFT
    attack_key_right = K_RIGHT
