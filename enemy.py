# File no longer Used due to instantiation

import pygame
import random
import range_enemy_sprite
import melee_enemy_sprite
import projectile_sprite
import game_map
from pygame.locals import *
current_tile_size = game_map.current_tile_size

class Enemy:
    def __init__(self, position_x, position_y):
        # Positional States
        self.position = pygame.math.Vector2(position_x + 10, position_y + 5)
        self.direction = False

        # Health Attributes
        self.max_hp = 100       # Should differ between enemies
        self.hp = self.max_hp
        self.should_die = False
        self.hit_state = False
        self.hurt_time_accumulator = 0.0

        # Sprite Attributes
        size_multiplier = 1.0
        """!!!^^"""
        # For random spawning of which unit
        random_enemy = random.randint(0, 1)
        random_type = random.randint(0, 1)
        if random_type == 0:
            self.current_enemy_type = 'range'
        else:
            self.current_enemy_type = 'melee'

        # Projectile Dictionary holds name and corresponding sprite of enemy projectiles
        self.projectile_dict = {'skull': pygame.transform.smoothscale(range_enemy_sprite.spritesheet.subsurface(293, 327, 6, 6), (15, 15))}
        # Enemy Dictionary holds the Enemy name, nad it's corresponding projectile type
        self.enemy_dict = {'rangeDemon': self.projectile_dict['skull'],
                           'other': None}

        # Current_enemy_type will eventually be affected by random chance
        if self.current_enemy_type == 'range':
            possible_enemies = ['rangeDemon', 'rangeDemon']     # Second range enemy not yet implemented
        elif self.current_enemy_type == 'melee':
            possible_enemies = ['slime', 'slime']               # Second melee enemy not yet implemented

        self.current_enemy = possible_enemies[random_enemy]
        '''
        # will remove the number 2 later as currently only 'rangeDemon' exists
        # Will use: self.current_enemy = possible_enemies[random_enemy]
        if random_enemy == 0 or random_enemy == 1:
            self.current_enemy = "rangeDemon" 
            '''

        initial_frames = []
        if self.current_enemy_type == 'range':
            # Stores the related projectile sprite
            self.projectile = self.enemy_dict[self.current_enemy]
            if self.current_enemy == 'rangeDemon':
                initial_frames = range_enemy_sprite.demon_idle_frames
                size_multiplier = 1.4
        else:
            if self.current_enemy == 'slime':
                initial_frames = melee_enemy_sprite.slime_animation_frames
                size_multiplier = 0.7

        # Higher frame_speed means slower animation speed,
        # as it is the time taken for each frame to be displayed for.
        frame_speed = 0.12
        attack_speed = 2.0
        self.frames = []                    # Initialises attribute as list type

        # Changes sprite size
        self.size_x = int(32 * size_multiplier)
        self.size_y = int(36 * size_multiplier)
        for i in initial_frames:
            # For future size changes of sprite
            new_frame = pygame.transform.smoothscale(i, (self.size_x, self.size_y))
            self.frames.append(new_frame)

        self.current_frame_index = 0
        self.display_frame = self.frames[self.current_frame_index]
        self.frame_speed = frame_speed
        self.time_accumulator = random.randint(0, 110)/100

        self.attack_time_accumulator = 0.0
        self.attack_speed = attack_speed

        self.active_projectiles = []
        self.reloading = False

        # Damage states for a white blit as an impact frame
        self.in_damage_state = False
        self.hit_damage_time = 0.2
        self.hit_damage_timer = 0.0
        self.white_hit_surf = pygame.surface.Surface((self.size_x, self.size_y))
        self.white_hit_surf.fill(pygame.Color('#FFFFFF'))

    def draw(self, screen):
        frame = self.frames[self.current_frame_index].copy()
        if self.direction == True:      # Face left or right
            frame = pygame.transform.flip(frame, True, False)

        # Uses built-in function to add an rgb colour over the drawn entity
        if self.in_damage_state:        # Flashes white when hit
            frame.blit(self.white_hit_surf, (0, 0), special_flags=pygame.BLEND_RGB_ADD)

        if self.current_enemy == 'rangeDemon':
            if self.current_frame_index == 1 or self.current_frame_index == 2:
                # Because sprite is drawn from top left, and the frames are slightly different sizes,
                # the sprite's feet will appear to be moving up and down, when what the animation should look like
                # is the head bopping up and down. Hence '-2' for y-axis
                screen.blit(frame, (int(self.position.x),
                                    int(self.position.y - 2)))
            else:
                screen.blit(frame, (int(self.position.x),
                                    int(self.position.y)))

        else:       # General draw instruction
            screen.blit(frame, (int(self.position.x), int(self.position.y)))


    def update_player_pos(self, player_x):

        # Turn the enemy depending on player
        if player_x < self.position.x:
            self.direction = True
        else:
            self.direction = False

    def next_frame(self, delta_time):
        self.time_accumulator += delta_time
        # Calculates time spent per frame
        if self.time_accumulator > self.frame_speed:
            self.time_accumulator = 0.0
            self.current_frame_index += 1

            if self.current_frame_index >= len(self.frames):
                self.current_frame_index = 0

            self.display_frame = self.frames[self.current_frame_index]

        # Health validation here so a death animation can be added
        if self.hp <= 0:
            self.should_die = True

        # Timer for the white impact frames
        if self.in_damage_state:
            self.hit_damage_timer += delta_time
            if self.hit_damage_timer > self.hit_damage_time:
                self.in_damage_state = False
                self.hit_damage_timer = 0.0

    def check_attack(self, player_x, player_y, player_height, delta_time):
        # Prevents constant firing, by implementing a reload time
        if self.reloading == True:
            self.attack_time_accumulator += delta_time
            # Can make attack speed semi_random in the future
            if self.attack_time_accumulator > self.attack_speed:
                self.attack_time_accumulator = 0.0
                self.reloading = False

        if self.reloading == False:
            # If the player is left or right, with a bit of a view region so that it is not a single pixel line trigger
            if self.position.y - 2 < player_y + player_height/2 and player_y < self.position.y + self.size_y:
                if self.current_enemy_type == 'range':      # Ranged enemies spawn a projectile
                    self.active_projectiles.append(projectile_sprite.Projectile(self.projectile, self.position.x,
                                                                                (self.position.y + self.size_y/3),
                                                                                player_x, self.size_x/1.5))
                    self.reloading = True

                else:
                    # Melee not implemented yet
                    pass

    def attack(self, screen, delta_time, collidablexy):
        if self.current_enemy_type == 'range':
            for projectile in self.active_projectiles:
                projectile.general_updates(screen, delta_time)  # Draw, movement and rotation methods are in this
                #projectile.draw(screen)
                #projectile.update_movement(delta_time)
                #projectile.rotation(delta_time)

                for collidable_tile in collidablexy:
                    if (projectile.position.x < collidable_tile[0] + current_tile_size and collidable_tile[0] < int(projectile.position.x) + 6 and
                    projectile.position.y  < collidable_tile[1] + current_tile_size and collidable_tile[1] < int(projectile.position.y) + 6):
                        projectile.projectile_death()
                        # For future planning of delayed projectile death for death animation
                        if projectile.death == True:
                            self.active_projectiles.remove(projectile)

                if projectile.position.x < 0 or projectile.position.x > 640:
                    self.active_projectiles.remove(projectile)

    def health_update(self, player_attacks_array, delta_time, player_weapon):

        sprite_hitbox = self.display_frame.get_rect(topleft=(self.position.x, self.position.y))
        for player_attack in player_attacks_array:                  # Check collision with all projectile
            '''if (self.position.x < player_attack.position.x + player_attack.width and self.position.x + self.size_x > player_attack.position.x
            and self.position.y < player_attack.position.y + player_attack.height and self.position.y + self.size_y > player_attack.position.y):''' # Old code
            # Area collision testing using built-in pygame get_rect area
            if pygame.Rect.colliderect(sprite_hitbox, player_attack.hitbox):
                if not self.hit_state:
                    self.hp -= player_attack.weapon_damage
                    self.hit_state = True
                    self.in_damage_state = True

            # Different weapon animations affects invulnerability time needed for enemy
            if player_weapon == 'fireball':
                if not pygame.Rect.colliderect(sprite_hitbox, player_attack.hitbox):
                    self.hurt_time_accumulator += delta_time
                    if self.hurt_time_accumulator > 0.7:        # Can optimise this to call a variable instead of 0.7
                        self.hit_state = False
                        self.hurt_time_accumulator = 0

            elif player_weapon == 'sword':
                self.hurt_time_accumulator += delta_time
                if self.hurt_time_accumulator > 0.7:
                    self.hit_state = False
                    self.hurt_time_accumulator = 0

            elif player_weapon == 'flame':
                self.hurt_time_accumulator += delta_time
                if self.hurt_time_accumulator > 1.1:
                    self.hit_state = False
                    self.hurt_time_accumulator = 0

                # if not player_attack.hit_enemy:
                #     self.hp -= player_attack.weapon_damage
                #     player_attack.hit_enemy = True
    """Can take all this out and put in another file. Then reference a 'general update' method that holds all updates"""



# Debugging methods
    def hitbox(self, screen, player_attacks_array):
        rectangle = self.display_frame.get_rect(topleft=(self.position.x, self.position.y))
        pygame.draw.rect(screen, (200,100,100,20), rectangle)
        for player_attack in player_attacks_array:
            if pygame.Rect.colliderect(rectangle, player_attack.hitbox):
                print('Collided')

# USE INHERITANCE