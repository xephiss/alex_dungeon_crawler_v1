import pygame
import settings_file

from pygame_gui.elements import UIButton
from pygame_gui import UI_BUTTON_PRESSED


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

        self.back_button = None
        self.health_setting_button = None
        self.movement_setting_button = None
        self.damage_setting_button = None

        self.movement_preset = settings_file.preset
        self.health_modifier = settings_file.health_modifier
        self.movement_modifier = settings_file.movement_modifier
        self.damage_modifier = settings_file.damage_modifier

    def start(self):
        self.transition_target = None
        self.background_surf = pygame.Surface((640, 640))
        self.background_surf.fill((190, 150, 90))
        # Text to draw
        self.title_text = self.title_font.render('Settings', True, (150, 30, 30))
        self.title_pos_rect = self.title_text.get_rect()
        self.title_pos_rect.center = (320, 50)

        self.health_text = self.settings_font.render(str(settings_file.health_modifier * 100), True, (250, 100, 30))
        self.health_text_pos_rect = self.health_text.get_rect()
        self.health_text_pos_rect.center = (400, 195)

        self.movement_text = self.settings_font.render(str(settings_file.movement_modifier * 100), True, (250, 100, 30))
        self.movement_text_pos_rect = self.movement_text.get_rect()
        self.movement_text_pos_rect.center = (400, 255)

        self.damage_text = self.settings_font.render(str(settings_file.damage_modifier * 100), True, (250, 100, 30))
        self.damage_text_pos_rect = self.damage_text.get_rect()
        self.damage_text_pos_rect.center = (400, 315)

        # Buttons
        self.back_button = UIButton(pygame.Rect((400, 550), (200, 30)),
                                    'Back to menu', self.ui_manager)
        self.health_setting_button = UIButton(pygame.Rect((140, 180), (200, 30)),
                                              'Toggle Health%', self.ui_manager)
        self.movement_setting_button = UIButton(pygame.Rect((140, 240), (200, 30)),
                                              'Toggle Movement%', self.ui_manager)
        self.damage_setting_button = UIButton(pygame.Rect((140, 300), (200, 30)),
                                              'Toggle Damage%', self.ui_manager)



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

        self.health_setting_button = None
        self.back_button = None
        self.movement_setting_button = None
        self.damage_setting_button = None

    def handle_events(self, event):
        if event.type == pygame.USEREVENT and event.user_type == UI_BUTTON_PRESSED:
            if event.ui_element == self.back_button:
                self.transition_target = 'main_menu'
            if event.ui_element == self.health_setting_button:
                self.health_modifier += 0.1
                if self.health_modifier > 2.0:
                    self.health_modifier = 0.3

            if event.ui_element == self.movement_setting_button:
                self.movement_modifier += 0.1
                if self.movement_modifier > 2.0:
                    self.movement_modifier = 0.5

            if event.ui_element == self.damage_setting_button:
                self.damage_modifier += 0.1
                if self.damage_modifier > 2.0:
                    self.damage_modifier = 0.3

            settings_saved = open("settings_save.txt.", "w")
            settings_saved.write(str(self.movement_preset) + str(self.health_modifier)
                                 + "\n" + str(self.movement_modifier) + "\n" + str(self.damage_modifier) + "\n")
            settings_saved.close()
            self.health_text = self.settings_font.render(str(round(self.health_modifier * 100, 3)), True,
                                                         (250, 100, 30))
            self.movement_text = self.settings_font.render(str(round(self.movement_modifier * 100, 3)), True,
                                                         (250, 100, 30))
            self.damage_text = self.settings_font.render(str(round(self.damage_modifier * 100, 3)), True,
                                                         (250, 100, 30))

    def update(self, time_delta):
        # clear the window to the background surface
        self.window_surface.blit(self.background_surf, (0, 0))
        # stick the title at the top
        self.window_surface.blit(self.title_text, self.title_pos_rect)
        self.window_surface.blit(self.health_text, self.health_text_pos_rect)
        self.window_surface.blit(self.movement_text, self.movement_text_pos_rect)
        self.window_surface.blit(self.damage_text, self.damage_text_pos_rect)

        self.ui_manager.draw_ui(self.window_surface)  # Draw the UI Bits
