import pygame
import pygame_gui
import settings_file
from pygame_gui.elements import UIButton, UIHorizontalSlider
from pygame_gui import UI_BUTTON_PRESSED


class SettingsState:
    def __init__(self, window_surface, ui_manager):
        self.transition_target = None
        self.window_surface = window_surface
        self.ui_manager = ui_manager
        self.title_font = self.ui_manager.get_theme().get_font(["setting_title"])
        self.settings_font = self.ui_manager.get_theme().get_font(["settings_text"])

        self.background_surf = None
        self.title_text = None
        self.title_pos_rect = None
        self.health_text, self.movement_text, self.damage_text = None, None, None
        self.health_text_pos_rect, self.movement_text_pos_rect, self.damage_text_pos_rect = None, None, None
        self.preset_text_pos_rect = None

        # Initialises Button
        self.back_button, self.preset_text, self.preset_wasd_button, self.preset_arrow_button = None, None, None, None
        # Initialises Slider
        self.health_setting_slider, self.movement_setting_slider, self.damage_setting_slider = None, None, None
        # Initialises Text and Rectangles
        self.preset_text_move, self.preset_text_attack, self.extra_controls_text = None, None, None
        self.preset_text_move_pos_rect, self.preset_text_attack_pos_rect, self.extra_controls_pos = None, None, None

        # Loads the settings and places it into a single array so that it can be called as a whole
        self.movement_preset = settings_file.preset
        self.health_modifier = settings_file.health_modifier
        self.movement_modifier = settings_file.movement_modifier
        self.damage_modifier = settings_file.damage_modifier
        self.settings_array = [self.movement_preset, self.health_modifier, self.movement_modifier, self.damage_modifier]

        if self.movement_preset == 'preset_wasd\n':  # Compares saved preset value
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
        self.health_text = self.settings_font.render("Max Health: " + str(round(self.health_modifier * 100, 3)),
                                                     True, (210, 10, 60))
        self.health_text_pos_rect = self.health_text.get_rect()
        self.health_text_pos_rect.center = (320, 320)

        # Movement Settings
        self.movement_text = self.settings_font.render("Movement Speed: " + str(round(self.movement_modifier * 100, 3)),
                                                       True, (100, 10, 160))
        self.movement_text_pos_rect = self.movement_text.get_rect()
        self.movement_text_pos_rect.center = (320, 400)

        # Player Damage Settings
        self.damage_text = self.settings_font.render("Player Damage: " + str(round(self.damage_modifier * 100, 3)),
                                                     True, (200, 10, 10))
        self.damage_text_pos_rect = self.damage_text.get_rect()
        self.damage_text_pos_rect.center = (320, 480)

        # Control Settings
        self.preset_text = self.settings_font.render("Pick your control scheme:", True, (240, 40, 0))
        self.preset_text_pos_rect = self.preset_text.get_rect()
        self.preset_text_pos_rect.center = (285, 120)

        self.preset_text_move = self.settings_font.render(self.preset_words_move, True, (200, 60, 0))
        self.preset_text_move_pos_rect = self.preset_text_move.get_rect()
        self.preset_text_move_pos_rect.center = (320, 195)

        self.preset_text_attack = self.settings_font.render(self.preset_words_attack, True, (200, 60, 0))
        self.preset_text_attack_pos_rect = self.preset_text_attack.get_rect()
        self.preset_text_attack_pos_rect.center = (320, 225)

        self.extra_controls_text = self.settings_font.render("Change weapon buttons: 1 / 2 / 3", True, (198, 58, 6))
        self.extra_controls_pos = self.extra_controls_text.get_rect()
        self.extra_controls_pos.center = (320, 257)

        # Buttons
        self.back_button = UIButton(pygame.Rect((400, 570), (200, 30)),  # (position), (dimensions), 'Text', format
                                    'Back to menu', self.ui_manager)
        self.preset_wasd_button = UIButton(pygame.Rect((200, 145), (100, 25)),
                                           'Preset 1', self.ui_manager)
        self.preset_arrow_button = UIButton(pygame.Rect((340, 145), (100, 25)),
                                            'Preset 2', self.ui_manager)

        # Sliders
        # [(Position), (Dimensions), Default start value (variable), Range of valid values, Format]
        self.health_setting_slider = UIHorizontalSlider(pygame.Rect((170, 335), (300, 20)), self.health_modifier,
                                                        (0.3, 2.0), self.ui_manager)
        self.movement_setting_slider = UIHorizontalSlider(pygame.Rect((170, 425), (300, 20)), self.movement_modifier,
                                                          (0.3, 2.0), self.ui_manager)
        self.damage_setting_slider = UIHorizontalSlider(pygame.Rect((170, 495), (300, 20)), self.damage_modifier,
                                                        (0.3, 2.0), self.ui_manager)

    def stop(self):
        # Stops all running processes
        self.background_surf = None
        self.title_text = None
        self.title_pos_rect = None
        self.health_text = None
        self.health_text_pos_rect = None

        self.back_button.kill()
        self.preset_wasd_button.kill()
        self.preset_arrow_button.kill()

        self.back_button, self.preset_text, self.preset_wasd_button, self.preset_arrow_button = None, None, None, None

        self.health_setting_slider.kill()
        self.movement_setting_slider.kill()
        self.damage_setting_slider.kill()

        self.health_setting_slider, self.movement_setting_slider, self.damage_setting_slider = None, None, None

    def handle_events(self, event):
        if event.type == pygame.USEREVENT and event.user_type == UI_BUTTON_PRESSED:
            if event.ui_element == self.back_button:
                self.transition_target = 'main_menu'

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

        # Slider value update and saving
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_HORIZONTAL_SLIDER_MOVED:
                if event.ui_element == self.health_setting_slider:  # Health Setting
                    health_modifier_value = event.value
                    self.health_modifier = (health_modifier_value * 100 // 10) / 10  # rounds value to nearest 10

                if event.ui_element == self.movement_setting_slider:  # Movement Setting
                    movement_modifier_value = event.value
                    self.movement_modifier = (movement_modifier_value * 100 // 10) / 10

                if event.ui_element == self.damage_setting_slider:  # Damage Setting
                    damage_modifier_value = event.value
                    self.damage_modifier = (damage_modifier_value * 100 // 10) / 10

        # Saving the data in settings
        settings_saved = open("settings_save.txt.", "w")
        settings_saved.write(str(self.movement_preset) + str(self.health_modifier)
                             + "\n" + str(self.movement_modifier) + "\n" + str(self.damage_modifier) + "\n")
        settings_saved.close()
        # Update the rendering
        self.health_text = self.settings_font.render("Max Health: " + str(round(self.health_modifier * 100, 3)),
                                                     True, (200, 10, 60))
        self.movement_text = self.settings_font.render("Movement Speed: " + str(round(self.movement_modifier * 100, 3)),
                                                       True, (100, 10, 160))
        self.damage_text = self.settings_font.render("Player Damage: " + str(round(self.damage_modifier * 100, 3)),
                                                     True, (200, 10, 10))
        self.settings_array = [self.movement_preset, self.health_modifier, self.movement_modifier,
                               self.damage_modifier]

    def update(self, time_delta):
        # clear the window to the background surface
        self.window_surface.blit(self.background_surf, (0, 0))
        # Draw all the text boxes, may not have to always be updated
        self.window_surface.blit(self.title_text, self.title_pos_rect)      # Title
        self.window_surface.blit(self.health_text, self.health_text_pos_rect)       # Health Value
        self.window_surface.blit(self.movement_text, self.movement_text_pos_rect)   # Speed Value
        self.window_surface.blit(self.damage_text, self.damage_text_pos_rect)       # Damage Value
        # Control Presets
        self.window_surface.blit(self.preset_text, self.preset_text_pos_rect)
        self.window_surface.blit(self.preset_text_move, self.preset_text_move_pos_rect)
        self.window_surface.blit(self.preset_text_attack, self.preset_text_attack_pos_rect)
        self.window_surface.blit(self.extra_controls_text, self.extra_controls_pos)

        self.ui_manager.draw_ui(self.window_surface)  # Draw the UI Bits

        # Saving as an array allows passing between states
        self.settings_array = [self.movement_preset, self.health_modifier, self.movement_modifier,
                               self.damage_modifier]
