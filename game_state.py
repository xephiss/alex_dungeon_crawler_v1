import pygame
from pygame.locals import *

import enemy
import enemy_spawn
import collision_file
import player
import game_map


class GameState:
    def __init__(self, window_surface, time_delta):
        self.transition_target = None
        self.window_surface = window_surface

        self.title_font = pygame.font.Font(None, 64)
        self.instructions_font = pygame.font.Font(None, 32)
        self.ui_font = pygame.font.Font(None, 20)

        self.background_surf = None
        self.title_text = None
        self.title_pos_rect = None
        self.instructions_text = None
        self.instructions_text_pos_rect = None
        self.ui_text = None
        self.ui_text_pos_rect = None

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

        self.ui_text = self.ui_font.render('Collision Invulnerability', True, (200, 200, 200))
        self.ui_text_pos_rect = self.ui_text.get_rect()
        self.ui_text_pos_rect.center = (105, 600)

        #Animation(knight_red, 16, 22, 0, 4, 0.1)

        self.players = [player.Player()]

        #self.player1 = player.Player()
        self.level = game_map.Levels()
        self.spawn_tiles = enemy_spawn.Spawn(self.level.level_array[self.level.level_number - 1])
        self.collision_class = collision_file.CollisionClass(self.level.level_array[self.level.level_number - 1])


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

        # Background and map tiles drawn before all game entities
        self.level.draw(self.window_surface)

        # Collision Codes
        collisions_x = self.level.collision_boxes_x
        collisions_y = self.level.collision_boxes_y
        if self.level.mapped_level == False:
            self.collision_class.collision_area(self.level.level_array[self.level.level_number - 1])
            self.collision_class.collision_area_projectile(self.level.level_array[self.level.level_number - 1])
            self.collidablexy = self.collision_class.collidable_positions
            self.collidablexy_projectile = self.collision_class.collidable_positions_projectile
            self.level.mapped_level = True

        # Spawn a number of enemies
        if self.enemy_count < 2:
            self.spawn_tiles.spawn()
            self.active_enemies.append(enemy.Enemy(self.spawn_tiles.spawn_x, self.spawn_tiles.spawn_y))
            self.enemy_count += 1

        # Update independent enemy methods
        for enemy_inst in self.active_enemies:
            enemy_inst.next_frame(time_delta)
            enemy_inst.draw(self.window_surface)
            if enemy_inst.should_die == True:
                self.active_enemies.remove(enemy_inst)

        # Update methods that depend on player
        for player in self.players:
            #for enemy_inst in self.active_enemies:

            player.update_movement(time_delta, collisions_x, collisions_y)
            player.next_frame(time_delta)
            player.player_attack_call(time_delta)
            player.player_attack_update(self.window_surface, time_delta, self.collidablexy_projectile)

            # Update enemy - player interactions
            for enemy_inst in self.active_enemies:
                enemy_inst.update_player_pos(player.position.x)
                enemy_inst.check_attack(player.position.x, player.position.y, player.size_y ,time_delta)
                enemy_inst.attack(self.window_surface, time_delta, self.collidablexy_projectile)

                player.player_death_damage(enemy_inst.position.x, enemy_inst.position.y, enemy_inst.size_x, enemy_inst.size_y, enemy_inst.active_projectiles, time_delta)
                enemy_inst.health_update(player.active_attacks)
                #enemy_inst.hitbox(self.window_surface, player.active_attacks)  # Debugging hitbox

            player.draw(self.window_surface)
            player.draw_player_bar(self.window_surface)

            if player.should_die == True:
                self.players.remove(player)

        # Front-ground aesthetic is drawn after all other game entities
        self.level.draw_front_aesthetic(self.window_surface)


        # UI Stuff
        self.window_surface.blit(self.ui_text, self.ui_text_pos_rect)
        invulnerable_front_box = pygame.Rect(32, 612, 120, 14)      # Pos x, y, width, height
        pygame.draw.rect(self.window_surface, (0, 0, 0), invulnerable_front_box, 5)     # Colour, image, line size





