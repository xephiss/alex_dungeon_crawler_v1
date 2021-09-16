import pygame
import random
import range_enemy_sprite
import game_map
from pygame.locals import *
current_tile_size = game_map.current_tile_size

class Enemy:
    def __init__(self):
        self.position = pygame.math.Vector2(400.0, 400.0)

        self.direction = False

        random_type = random.randint(1, 2)
        random_enemy = random.randint(1, 2)

        current_enemy_type = 'range'
        if current_enemy_type == 'range':
            possible_enemies = ['demon', 'other']

        # will remove the number 2 later
        if random_enemy == 1 or random_enemy == 2:
            self.current_enemy = 'demon'



        # Higher frame_speed means slower animation speed,
        # as it is the time taken for each frame to be displayed for.
        frame_speed = 0.12

        initial_frames = []
        if self.current_enemy == 'demon':
            initial_frames = range_enemy_sprite.demon_idle_frames
        self.frames = []                    # Will contain a list of image sprites in animated order

        SIZE_MULTIPLIER = 1.4
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



    def draw(self, screen):
        frame = self.frames[self.current_frame_index]
        if self.direction == True:
            frame = pygame.transform.flip(frame, True, False)
        screen.blit(frame, (int(self.position.x),
                            int(self.position.y)))

    def next_frame(self, delta_time):
        self.time_accumulator += delta_time
        # finds the next frame in the animation sequence
        if self.time_accumulator > self.frame_speed:
            self.time_accumulator = 0.0
            self.current_frame_index += 1

            if self.current_frame_index >= len(self.frames):
                self.current_frame_index = 0

            self.display_frame = self.frames[self.current_frame_index]