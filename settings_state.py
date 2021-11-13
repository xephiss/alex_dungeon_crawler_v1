import pygame

from pygame_gui.elements import UIButton
from pygame_gui import UI_BUTTON_PRESSED


class SettingsState:
    def __init__(self, window_surface, ui_manager):
        self.transition_target = None
        self.window_surface = window_surface
        self.ui_manager = ui_manager
        self.title_font = self.ui_manager.get_theme().get_font(["title_screen_front"])

        self.background_surf = None
        self.title_text = None
        self.title_pos_rect = None

        self.back_button = None
        self.health_setting_button = None

    def start(self):
        self.transition_target = None
        self.background_surf = pygame.Surface((640, 640))
        self.background_surf.fill((190, 150, 90))
        self.title_text = self.title_font.render('Settings', True, (150, 30, 30))
        self.title_pos_rect = self.title_text.get_rect()
        self.title_pos_rect.center = (320, 50)

        # Buttons
        self.back_button = UIButton(pygame.Rect((400, 550), (200, 30)),
                                    'Back to menu', self.ui_manager)
        self.health_setting_button = UIButton(pygame.Rect((140, 180), (180, 30)),
                                              'Toggle Health%', self.ui_manager)

    def stop(self):
        self.background_surf = None
        self.title_text = None
        self.title_pos_rect = None

        self.back_button.kill()
        self.back_button = None

    def handle_events(self, event):
        if event.type == pygame.USEREVENT and event.user_type == UI_BUTTON_PRESSED:
            if event.ui_element == self.back_button:
                self.transition_target = 'main_menu'

    def update(self, time_delta):
        # clear the window to the background surface
        self.window_surface.blit(self.background_surf, (0, 0))
        # stick the title at the top
        self.window_surface.blit(self.title_text, self.title_pos_rect)

        self.ui_manager.draw_ui(self.window_surface)  # Draw the UI Bits
