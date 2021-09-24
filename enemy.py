import pygame
import random
import range_enemy_sprite
import projectile_sprite
import game_map
from pygame.locals import *
current_tile_size = game_map.current_tile_size

class Enemy:
    def __init__(self, position_x, position_y):
        self.position = pygame.math.Vector2(position_x, position_y)

        self.direction = False

        # For random spawning of which unit
        random_type = random.randint(1, 2)
        random_enemy = random.randint(1, 2)

        self.projectile_dict = {'skull': pygame.transform.smoothscale(range_enemy_sprite.spritesheet.subsurface(293, 327, 6, 6), (15, 15))}
        # Enemy Dictionary holds the Enemy name, nad it's corresponding projectile type
        self.enemy_dict = {'rangeDemon': self.projectile_dict['skull'],
                           'other': None}

        # Current_enemy_type will eventually be affected by random chance
        self.current_enemy_type = 'range'
        if self.current_enemy_type == 'range':
            possible_enemies = ['rangeDemon', 'other']

        # will remove the number 2 later as currently only 'rangeDemon' exists
        if random_enemy == 1 or random_enemy == 2:
            self.current_enemy = 'rangeDemon'

        self.projectile = self.enemy_dict[self.current_enemy]

        # Higher frame_speed means slower animation speed,
        # as it is the time taken for each frame to be displayed for.
        frame_speed = 0.12
        attack_speed = 2.0

        initial_frames = []
        if self.current_enemy == 'rangeDemon':
            initial_frames = range_enemy_sprite.demon_idle_frames
        self.frames = []                    # Initialises attribute as list type

        SIZE_MULTIPLIER = 1.4
        # Add a if demon here eventually
        self.size_x = int(32 * SIZE_MULTIPLIER)
        self.size_y = int(36 * SIZE_MULTIPLIER)
        for i in initial_frames:
            # For future size changes of sprite
            new_frame = pygame.transform.smoothscale(i, (self.size_x, self.size_y))
            self.frames.append(new_frame)

        self.current_frame_index = 0
        self.display_frame = self.frames[self.current_frame_index]
        self.frame_speed = frame_speed
        self.time_accumulator = 0.0

        self.attack_time_accumulator = 0.0
        self.attack_speed = attack_speed

        self.active_projectiles = []
        self.reloading = False



    def draw(self, screen):

        frame = self.frames[self.current_frame_index]
        if self.direction == True:
            frame = pygame.transform.flip(frame, True, False)

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

    def check_attack(self, player_x, player_y, player_height, delta_time):
        # Prevents constant firing, by implementing a reload time
        if self.reloading == True:
            self.attack_time_accumulator += delta_time
            # Can make attack speed semi_random
            if self.attack_time_accumulator > self.attack_speed:
                self.attack_time_accumulator = 0.0
                self.reloading = False

        if self.reloading == False:
            # If the player is left or right, with a bit of a view region so that it is not a single pixel line trigger
            if self.position.y - 2 < player_y + player_height/2 and player_y < self.position.y + self.size_y:
                if self.current_enemy_type == 'range':
                    self.active_projectiles.append(projectile_sprite.Projectile(self.projectile, self.position.x,
                                                                                (self.position.y + self.size_y/3),
                                                                                player_x, self.size_x/1.5))
                    self.reloading = True

                else:
                    # Melee not implemented yet
                    pass

    def attack(self, screen, delta_time):
        if self.current_enemy_type == 'range':
            for projectile in self.active_projectiles:
                projectile.draw(screen)
                projectile.update_movement(delta_time)
                projectile.rotation(delta_time)

                if projectile.position.x < 0 or projectile.position.x > 640:
                    self.active_projectiles.remove(projectile)

