import pygame

import enemy_instance
import enemy_spawn
import collision_file
import player
import game_map
from game_arithmetic import random_max_enemy


class GameState:
    def __init__(self, window_surface, time_delta, settings):
        # UI attributes
        self.transition_target = None
        self.window_surface = window_surface

        self.title_font = pygame.font.Font(None, 64)
        self.instructions_font = pygame.font.Font(None, 32)
        self.ui_font = pygame.font.Font(None, 20)
        self.help_ui_font = pygame.font.Font(None, 15)

        self.background_surf = None
        self.title_text = None
        self.title_pos_rect = None
        self.instructions_text = None
        self.instructions_text_pos_rect = None
        self.ui_text, self.help_text = None, None
        self.ui_text_pos_rect, self.help_text_pos_rect = None, None

        self.time_delta = time_delta

        # Level attributes
        self.cleared_level = False
        self.touched_next_level = False
        self.max_enemy = random_max_enemy()

        # Receives the settings
        self.settings = settings

    def start(self):
        self.transition_target = None   # State to transfer to
        self.background_surf = pygame.Surface((640, 640))
        self.background_surf.fill((200, 150, 100))

        # Creating the User Interface text, and defining the position
        self.ui_text = self.ui_font.render('Collision Invulnerability', True, (200, 200, 200))
        self.ui_text_pos_rect = self.ui_text.get_rect()
        self.ui_text_pos_rect.center = (105, 600)

        self.help_text = self.help_ui_font.render('Press ESC to return to menu', True, (200, 190, 190))
        self.help_text_pos_rect = self.help_text.get_rect()
        self.help_text_pos_rect.topright = (608, 620)
        # Map, tiles, collision fetching
        self.level = game_map.Levels()
        self.spawn_tiles = enemy_spawn.Spawn(self.level.level_array[self.level.level_number - 1])
        self.collision_class = collision_file.CollisionClass(self.level.level_array[self.level.level_number - 1])
        # Player and enemy generation
        self.players = [player.Player(self.level.end_of_level_tiles, self.settings)]  # Creates player instance
        self.enemy_count = 0
        self.active_enemies = []
        self.max_enemy = random_max_enemy()

        # Debugging
        self.touched_next_level = True

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

        # # Debugging: level change
        # if event.type == pygame.KEYDOWN and event.key == pygame.K_0:
        #     self.level.level_number += 1
        #     self.level.level_number = self.level.level_number % len(self.level.level_array)     # Remainder
        #     # Loops the levels via button press
        #     if self.level.level_number == 0:
        #         self.level.level_number = len(self.level.level_array)
        #     if self.level.level_number > len(self.level.level_array):
        #         self.level.level_number = 1
        #
        #     # Resets and remaps collision
        #     self.level.get_level()
        #     self.spawn_tiles = enemy_spawn.Spawn(self.level.level_array[self.level.level_number - 1])
        #     self.collision_class = collision_file.CollisionClass(self.level.level_array[self.level.level_number - 1])
        #     self.level.mapped_level = False
        #     if len(self.active_enemies) < 4:    #Number of enemies
        #         self.enemy_count = 0
        # if event.type == pygame.KEYDOWN and event.key == pygame.K_6:
        #     print(self.players[0].position)

    def update(self, time_delta):
        # clear the window to the background surface
        self.window_surface.blit(self.background_surf, (0, 0))

        # Background and map tiles drawn before all game entities
        self.level.draw(self.window_surface)

        # Collision Codes
        collisions_x = self.level.collision_boxes_x
        collisions_y = self.level.collision_boxes_y
        if self.level.mapped_level == False:  # Maps collidable regions
            self.collision_class.collision_area(self.level.level_array[self.level.level_number - 1])
            self.collision_class.collision_area_projectile(self.level.level_array[self.level.level_number - 1])
            self.collidablexy = self.collision_class.collidable_positions
            self.collidablexy_projectile = self.collision_class.collidable_positions_projectile

            self.spawn_tiles.general_spawn()  # Maps general valid tile once
            self.level.mapped_level = True

        # Spawn a random number of enemies after reset
        if self.enemy_count < self.max_enemy:
            self.spawn_tiles.spawn()
            enemy_generated = enemy_instance.EnemyInstance(self.spawn_tiles.spawn_x, self.spawn_tiles.spawn_y)
            enemy_inst = enemy_generated.enemy_inst
            self.active_enemies.append(enemy_inst)
            self.enemy_count += 1
            self.cleared_level = False

        if len(self.active_enemies) == 0:  # Changes cleared level state when all enemies are dead
            self.cleared_level = True

        # Checking if level has been cleared, collision with end tile, and all enemies killed, then increment level
        if self.cleared_level is True and len(self.active_enemies) == 0:
            self.level.spawn_end_of_level_tile(self.spawn_tiles.general_spawn_x, self.spawn_tiles.general_spawn_y)

        has_touched_end_tile = False
        for end_tile in self.level.end_of_level_tiles:
            if end_tile.touched_by_player:
                has_touched_end_tile = True
        if has_touched_end_tile:  # Level only increments when collision is true
            self.level.level_number += 1
            if self.level.level_number >= self.level.max_levels:
                # Loops the levels for now so that there is no index error
                self.level.level_number = 1
            self.enemy_count = 0  # Resets the enemy count so enemies can be spawned on the next level
            self.max_enemy = random_max_enemy()

            # Resets and remaps collision
            self.level.get_level()
            self.spawn_tiles = enemy_spawn.Spawn(self.level.level_array[self.level.level_number - 1])
            self.collision_class = collision_file.CollisionClass(
                self.level.level_array[self.level.level_number - 1])  # Collision for projectiles
            self.level.mapped_level = False
            self.level.clear_end_of_level_tiles()  # Makes sure the ladder is cleared (may be redundant)

        # Update independent enemy methods
        enemy_hitboxes = []
        for enemy_inst in self.active_enemies:
            enemy_inst.next_frame(time_delta)
            enemy_inst.draw(self.window_surface)
            enemy_hitboxes.append(enemy_inst.sprite_hitbox)
            if enemy_inst.should_die == True:
                self.active_enemies.remove(enemy_inst)

        # Update methods that depend on player
        for player in self.players:
            # for enemy_inst in self.active_enemies:

            player.update_movement(time_delta, collisions_x, collisions_y)
            player.next_frame(time_delta)
            player.player_attack_call(time_delta)
            player.player_attack_update(self.window_surface, time_delta, self.collidablexy_projectile)

            # Update enemy - player interactions
            for enemy_inst in self.active_enemies:
                enemy_inst.update_player_pos(player.position.x)

                for hitbox in enemy_hitboxes:
                    enemy_inst.move(player.position, player.hitbox, hitbox, len(enemy_hitboxes), self.collidablexy)
                enemy_inst.check_attack(player.position.x, player.position.y, player.size_y, time_delta)
                enemy_inst.attack(self.window_surface, time_delta, self.collidablexy_projectile)

                player.player_death_damage(enemy_inst.position.x, enemy_inst.position.y, enemy_inst.size_x,
                                           enemy_inst.size_y, enemy_inst.active_projectiles, time_delta)
                enemy_inst.health_update(player.active_attacks, time_delta,
                                         player.current_weapon, self.settings[3])  # Settings[3] is damage percentage
                # enemy_inst.hitbox(self.window_surface, player.active_attacks)  # Debugging hitbox

            player.draw(self.window_surface)
            # player.draw_player_bar(self.window_surface)

            if player.should_die == True:
                self.players.remove(player)

            player.end_of_level_tiles = self.level.end_of_level_tiles

        # Front-ground aesthetic is drawn after all other game entities
        self.level.draw_front_aesthetic(self.window_surface)

        # UI Stuff
        self.window_surface.blit(self.ui_text, self.ui_text_pos_rect)  # Draw the text
        self.window_surface.blit(self.help_text, self.help_text_pos_rect)
        invulnerable_front_box = pygame.Rect(32, 612, 120, 14)  # Pos x, y, width, height
        pygame.draw.rect(self.window_surface, (0, 0, 0), invulnerable_front_box, 5)  # Colour, image, line size
