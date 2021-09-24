import pygame
from pygame.locals import *

import enemy
import enemy_spawn
import player
import game_map


class GameState:
    def __init__(self, window_surface, time_delta):
        self.transition_target = None
        self.window_surface = window_surface

        self.title_font = pygame.font.Font(None, 64)
        self.instructions_font = pygame.font.Font(None, 32)

        self.background_surf = None
        self.title_text = None
        self.title_pos_rect = None
        self.instructions_text = None
        self.instructions_text_pos_rect = None

        self.time_delta = time_delta


    def start(self):
        self.transition_target = None
        self.background_surf = pygame.Surface((640, 640))
        self.background_surf.fill((200, 150, 100))

        #self.title_text = self.title_font.render('The Game', True, (255, 255, 255))
        #self.title_pos_rect = self.title_text.get_rect()
        #self.title_pos_rect.center = (400, 50)

        #self.instructions_text = self.instructions_font.render('Press ESC to return to main menu',
                                                               #True, (255, 255, 255))

        #self.instructions_text_pos_rect = self.instructions_text.get_rect()
        #self.instructions_text_pos_rect.center = (400, 100)

        #Animation(knight_red, 16, 22, 0, 4, 0.1)

        self.players = [player.Player()]

        #self.player1 = player.Player()
        self.level = game_map.Levels()
        self.spawn_tiles = enemy_spawn.Spawn(self.level.level_array[self.level.level_number - 1])

        self.enemy_count = 0
        self.active_enemies = []
        #self.enemy1 = enemy.Enemy()

    def stop(self):
        self.background_surf = None
        self.title_text = None
        self.title_pos_rect = None
        self.instructions_text = None
        self.instructions_text_pos_rect = None

    def handle_events(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            self.transition_target = 'main_menu'

        for player in self.players:
            player.on_key_press(event)
            player.on_key_release(event)

    def update(self, time_delta):
        # clear the window to the background surface
        self.window_surface.blit(self.background_surf, (0, 0))
        # stick the title at the top
        # self.window_surface.blit(self.title_text, self.title_pos_rect)
        # stick the instructions below

        # self.window_surface.blit(self.instructions_text, self.instructions_text_pos_rect)
        #self.level.draw_map(self.window_surface)
        #self.level.draw_aesthetic(self.window_surface)
        #self.level.draw_collision(self.window_surface)
        self.level.draw(self.window_surface)

        collisions_x = self.level.collision_boxes_x
        collisions_y = self.level.collision_boxes_y

        if self.enemy_count < 2: ########################
            self.spawn_tiles.spawn()
            self.active_enemies.append(enemy.Enemy(self.spawn_tiles.spawn_x, self.spawn_tiles.spawn_y))
            self.enemy_count += 1


        for enemy_inst in self.active_enemies:
            enemy_inst.next_frame(time_delta)
            enemy_inst.draw(self.window_surface)

        for player in self.players:
            for enemy_inst in self.active_enemies:
                enemy_inst.update_player_pos(player.position.x)
                enemy_inst.check_attack(player.position.x, player.position.y, player.size_y ,time_delta)
                enemy_inst.attack(self.window_surface, time_delta)
            player.update_movement(time_delta, collisions_x, collisions_y)
            player.next_frame(time_delta)
            # !Can eventually do a 'for enemy in enemies.... when multiple instances'
            for enemy_inst in self.active_enemies:
                player.player_death_damage(enemy_inst.position.x, enemy_inst.position.y, enemy_inst.size_x, enemy_inst.size_y, enemy_inst.active_projectiles)
            player.draw(self.window_surface)
            player.draw_health(self.window_surface)

            if player.should_die == True:
                self.players.remove(player)



        self.level.draw_front_aesthetic(self.window_surface)

