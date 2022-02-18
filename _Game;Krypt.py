import pygame
import pygame_gui

from main_menu_state import MainMenuState
from settings_state import SettingsState
from game_state import GameState


class GameApp:

    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Krypt')     # Window title
        self.window_surface = pygame.display.set_mode((640, 640))
        # Adds theme file after the (640, 640)
        self.ui_manager = pygame_gui.UIManager((640, 640), 'theme_1.json')
        self.clock = pygame.time.Clock()
        time_delta = self.clock.tick(60)/1000.0
        self.running = True

        self.states = {'main_menu': MainMenuState(self.window_surface, self.ui_manager),
                       'settings': SettingsState(self.window_surface, self.ui_manager),
                       }
        self.settings = self.states['settings'].settings_array  # Settings needs to load before game state does
        self.states['game'] = GameState(self.window_surface, time_delta, self.settings)
        self.active_state = self.states['main_menu']  # start the app in the main menu
        self.active_state.start()

    def run(self):
        while self.running:
            time_delta = self.clock.tick(60)/1000.0     # Around 60fps
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                # Call methods in other states
                self.ui_manager.process_events(event)
                self.active_state.handle_events(event)
            self.ui_manager.update(time_delta)
            self.active_state.update(time_delta)

            if self.active_state.transition_target is not None:     # Switch states
                if self.active_state.transition_target in self.states:
                    self.active_state.stop()
                    self.active_state = self.states[self.active_state.transition_target]
                    self.active_state.start()
                elif self.active_state.transition_target == 'quit':
                    self.running = False

            self.states['game'].settings = self.states['settings'].settings_array   # Passing settings through files

            pygame.display.update()


if __name__ == '__main__':
    app = GameApp()
    app.run()
