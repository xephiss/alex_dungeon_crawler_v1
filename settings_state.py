import pygame
import pygame_gui

import settings_file

from pygame_gui.elements import UIButton, UIHorizontalSlider
from pygame_gui import UI_BUTTON_PRESSED

# Debug
from pygame.locals import *


class SettingsState:
    def __init__(self, window_surface, ui_manager):
        self.transition_target = None
        self.window_surface = window_surface
        self.ui_manager = ui_manager
        self.title_font = self.ui_manager.get_theme().get_font(["title_screen_front"])
        self.settings_font = self.ui_manager.get_theme().get_font(["settings_text"])

        self.background_surf = None
        self.title_text = None
        self.title_pos_rect = None
        self.health_text, self.movement_text, self.damage_text = None, None, None
        self.health_text_pos_rect, self.movement_text_pos_rect, self.damage_text_pos_rect = None, None, None
        self.preset_text_pos_rect = None

        # Initialises Button
        self.back_button = None
        self.health_setting_button = None
        self.movement_setting_button = None
        self.damage_setting_button = None
        self.preset_wasd_button = None
        self.preset_arrow_button = None

        self.health_setting_slider = None

        # Loads the settings and places it into a single array so that it can be called as a whole
        self.movement_preset = settings_file.preset
        self.health_modifier = settings_file.health_modifier
        self.movement_modifier = settings_file.movement_modifier
        self.damage_modifier = settings_file.damage_modifier
        self.settings_array = [self.movement_preset, self.health_modifier, self.movement_modifier, self.damage_modifier]

        if self.movement_preset == 'preset_wasd\n':     # Compares saved preset value
            self.preset_words_move = 'Movement: WASD'
            self.preset_words_attack = "Directional Attack: Arrow Keys"
        else:
            self.preset_words_move = 'Movement: Arrow Keys'
            self.preset_words_attack = 'Directional Attack: WASD'

    def start(self):
        self.transition_target = None
        self.background_surf = pygame.Surface((640, 640))
        self.background_surf.fill((190, 150, 90))
        # Text to draw
        self.title_text = self.title_font.render('Settings', True, (150, 30, 30))
        self.title_pos_rect = self.title_text.get_rect()
        self.title_pos_rect.center = (320, 50)

        # Health Settings
        self.health_text = self.settings_font.render(str(round(self.health_modifier * 100, 3)), True, (250, 100, 30))
        self.health_text_pos_rect = self.health_text.get_rect()
        self.health_text_pos_rect.center = (400, 255)

        # Movement Settings
        self.movement_text = self.settings_font.render(str(round(self.movement_modifier * 100, 3)), True,
                                                       (250, 100, 30))
        self.movement_text_pos_rect = self.movement_text.get_rect()
        self.movement_text_pos_rect.center = (400, 315)

        # Player Damage Settings
        self.damage_text = self.settings_font.render(str(round(self.damage_modifier * 100, 3)), True, (250, 100, 30))
        self.damage_text_pos_rect = self.damage_text.get_rect()
        self.damage_text_pos_rect.center = (400, 375)

        # Control Settings
        self.preset_text_move = self.settings_font.render(self.preset_words_move, True, (200, 60, 0))
        self.preset_text_move_pos_rect = self.preset_text_move.get_rect()
        self.preset_text_move_pos_rect.center = (320, 170)

        self.preset_text_attack = self.settings_font.render(self.preset_words_attack, True, (200, 60, 0))
        self.preset_text_attack_pos_rect = self.preset_text_attack.get_rect()
        self.preset_text_attack_pos_rect.center = (320, 200)

        # Buttons
        self.back_button = UIButton(pygame.Rect((400, 550), (200, 30)),  # (position), (dimensions), 'Text', format
                                    'Back to menu', self.ui_manager)
        self.health_setting_button = UIButton(pygame.Rect((140, 240), (200, 30)),
                                              'Toggle Health%', self.ui_manager)
        self.movement_setting_button = UIButton(pygame.Rect((140, 300), (200, 30)),
                                                'Toggle Movement%', self.ui_manager)
        self.damage_setting_button = UIButton(pygame.Rect((140, 360), (200, 30)),
                                              'Toggle Damage%', self.ui_manager)

        self.preset_wasd_button = UIButton(pygame.Rect((200, 130), (100, 25)),
                                              'Preset 1', self.ui_manager)
        self.preset_arrow_button = UIButton(pygame.Rect((340, 130), (100, 25)),
                                               'Preset 2', self.ui_manager)

        # Slider[(Position), (Dimensions), Default start value (variable), Range of valid values, Format]
        self.health_setting_slider = UIHorizontalSlider(pygame.Rect((140, 580), (300, 20)), self.health_modifier, (0.3, 2.0), self.ui_manager)


    def stop(self):
        # Stops all running processes
        self.background_surf = None
        self.title_text = None
        self.title_pos_rect = None
        self.health_text = None
        self.health_text_pos_rect = None

        self.back_button.kill()
        self.health_setting_button.kill()
        self.movement_setting_button.kill()
        self.damage_setting_button.kill()
        self.preset_wasd_button.kill()
        self.preset_arrow_button.kill()

        self.health_setting_slider.kill()

        self.health_setting_button = None
        self.back_button = None
        self.movement_setting_button = None
        self.damage_setting_button = None
        self.preset_wasd_button = None
        self.preset_arrow_button = None

        self.health_setting_slider = None

    def handle_events(self, event):
        if event.type == pygame.USEREVENT and event.user_type == UI_BUTTON_PRESSED:
            if event.ui_element == self.back_button:
                self.transition_target = 'main_menu'

            if event.ui_element == self.health_setting_button:
                self.health_modifier += 0.1
                if self.health_modifier > 2.1:
                    self.health_modifier = 0.3

            if event.ui_element == self.movement_setting_button:
                self.movement_modifier += 0.1
                if self.movement_modifier > 2.1:
                    self.movement_modifier = 0.5

            if event.ui_element == self.damage_setting_button:
                self.damage_modifier += 0.1
                if self.damage_modifier > 2.1:
                    self.damage_modifier = 0.3

            if event.ui_element == self.preset_wasd_button:
                self.movement_preset = 'preset_wasd\n'
                self.preset_words_move = 'Movement: WASD'
                self.preset_words_attack = "Directional Attack: Arrow Keys"

            if event.ui_element == self.preset_arrow_button:
                self.movement_preset = 'preset_arrow\n'
                self.preset_words_move = 'Movement: Arrow Keys'
                self.preset_words_attack = 'Directional Attack: WASD'
            # Re-saves the text to render so that it can be updated
            self.preset_text_move = self.settings_font.render(self.preset_words_move, True, (200, 60, 0))
            self.preset_text_attack = self.settings_font.render(self.preset_words_attack, True, (200, 60, 0))

            # Saving the data in settings
            settings_saved = open("settings_save.txt.", "w")
            settings_saved.write(str(self.movement_preset) + str(self.health_modifier)
                                 + "\n" + str(self.movement_modifier) + "\n" + str(self.damage_modifier) + "\n")
            settings_saved.close()
            # Update the rendering
            self.health_text = self.settings_font.render(str(round(self.health_modifier * 100, 3)), True,
                                                         (250, 100, 30))
            self.movement_text = self.settings_font.render(str(round(self.movement_modifier * 100, 3)), True,
                                                           (250, 100, 30))
            self.damage_text = self.settings_font.render(str(round(self.damage_modifier * 100, 3)), True,
                                                         (250, 100, 30))
            self.settings_array = [self.movement_preset, self.health_modifier, self.movement_modifier,
                                   self.damage_modifier]

            # Debugs
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_HORIZONTAL_SLIDER_MOVED:
                if event.ui_element == self.health_setting_slider:
                    print(event.value)


                    self.health_modifier_test = event.value
                    self.health_modifier = (self.health_modifier_test * 100 // 10) / 10 # // is integer division
                    print(self.health_modifier)



    def update(self, time_delta):
        # clear the window to the background surface
        self.window_surface.blit(self.background_surf, (0, 0))
        # Draw all the text boxes, may not have to always be updated
        self.window_surface.blit(self.title_text, self.title_pos_rect)
        self.window_surface.blit(self.health_text, self.health_text_pos_rect)
        self.window_surface.blit(self.movement_text, self.movement_text_pos_rect)
        self.window_surface.blit(self.damage_text, self.damage_text_pos_rect)
        self.window_surface.blit(self.preset_text_move, self.preset_text_move_pos_rect)
        self.window_surface.blit(self.preset_text_attack, self.preset_text_attack_pos_rect)

        self.ui_manager.draw_ui(self.window_surface)  # Draw the UI Bits

        # Saving as an array allows passing between states
        self.settings_array = [self.movement_preset, self.health_modifier, self.movement_modifier,
                               self.damage_modifier]

        #slider_value = round(self.sliderTest.get_current_value(), 3)
        #print(slider_value)
        value = self.health_setting_slider.get_current_value()
        #print(value)


