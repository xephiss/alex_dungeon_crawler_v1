import pygame

from pygame_gui.elements import UIButton
from pygame_gui import UI_BUTTON_PRESSED


class MainMenuState:
    def __init__(self, window_surface, ui_manager):
        self.time_accumulator = 0.0
        self.transition_target = None
        self.window_surface = window_surface
        self.ui_manager = ui_manager
        #self.title_font = pygame.font.Font(None, 64)
        # Receive styling for fonts
        self.title_font_front = self.ui_manager.get_theme().get_font(["title_screen_front"])
        self.title_font_back = self.ui_manager.get_theme().get_font(["title_screen_back"])

        self.background_surf = None
        self.title_text1 = None
        self.title_pos_rect1 = None
        self.title_text2 = None
        self.title_pos_rect2 = None

        self.start_game_button = None
        self.settings_button = None
        self.quit_button = None

    def start(self):
        self.transition_target = None
        self.background_surf = pygame.Surface((640, 640))
        self.background_surf.fill((200, 160, 100))

        self.title_text1 = self.title_font_front.render('Krypt', True, (200, 10, 50))
        self.title_pos_rect1 = self.title_text1.get_rect()
        self.title_pos_rect1.center = (321, 79)
        self.title_text2 = self.title_font_back.render('Krypt', True, (200, 120, 30))
        self.title_pos_rect2 = self.title_text2.get_rect()
        self.title_pos_rect2.center = (319, 80)

        self.start_game_button = UIButton(pygame.Rect((245, 210), (150, 30)),
                                          'Start Game',
                                          self.ui_manager)
        self.settings_button = UIButton(pygame.Rect((245, 260), (150, 30)),
                                        'Settings',
                                        self.ui_manager)
        self.quit_button = UIButton(pygame.Rect((245, 310), (150, 30)),
                                    'Quit',
                                    self.ui_manager)

    def stop(self):
        self.background_surf = None
        self.title_text1 = None
        self.title_pos_rect1 = None
        self.title_text2 = None
        self.title_pos_rect2 = None

        self.start_game_button.kill()
        self.start_game_button = None
        self.settings_button.kill()
        self.settings_button = None
        self.quit_button.kill()
        self.quit_button = None

    def handle_events(self, event):
        if event.type == pygame.USEREVENT and event.user_type == UI_BUTTON_PRESSED:
            if event.ui_element == self.start_game_button:
                self.transition_target = 'game'
            elif event.ui_element == self.settings_button:
                self.transition_target = 'settings'
            elif event.ui_element == self.quit_button:
                self.transition_target = 'quit'

    def update(self, time_delta):
        # clear the window to the background surface
        self.window_surface.blit(self.background_surf, (0, 0))
        # stick the title at the top layer
        self.window_surface.blit(self.title_text1, self.title_pos_rect1)
        self.window_surface.blit(self.title_text2, self.title_pos_rect2)

        self.ui_manager.draw_ui(self.window_surface)  # Draw the UI Bits

        # Animated Title
        self.time_accumulator += time_delta
        if self.time_accumulator > 7.0:
            self.title_text1 = self.title_font_front.render('Krypt', True, (100, 10, 10))
        if self.time_accumulator > 7.15:
            self.title_text1 = self.title_font_front.render('Krypt', True, (150, 10, 50))
            self.title_text2 = self.title_font_back.render('Krypt', True, (180, 100, 0))
        if self.time_accumulator > 7.20:
            self.title_text1 = self.title_font_front.render('Krypt', True, (200, 10, 50))
            self.title_text2 = self.title_font_back.render('Krypt', True, (200, 120, 30))

            self.time_accumulator = 0.0



