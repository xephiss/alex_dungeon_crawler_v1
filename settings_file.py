from pygame.locals import *

settings_saved = open('settings_save.txt', 'r')   # Opens a text file
preset = str(settings_saved.readline()) # Reads and saves the first line
health_modifier = float(str(settings_saved.readline())[0:3])
movement_modifier = float(settings_saved.readline())
damage_modifier = float(settings_saved.readline())
settings_saved.close()


# Function so that any changes in settings can be called as a function in player after setting changes
def preset_choice(self, preset_key):
    if preset_key == 'preset_wasd\n':
        self.move_key_up = K_w
        self.move_key_down = K_s
        self.move_key_left = K_a
        self.move_key_right = K_d

        self.attack_key_up = K_UP
        self.attack_key_down = K_DOWN
        self.attack_key_left = K_LEFT
        self.attack_key_right = K_RIGHT

    elif preset_key == 'preset_arrow\n':
        self.move_key_up = K_UP
        self.move_key_down = K_DOWN
        self.move_key_left = K_LEFT
        self.move_key_right = K_RIGHT

        self.attack_key_up = K_w
        self.attack_key_down = K_s
        self.attack_key_left = K_a
        self.attack_key_right = K_d
