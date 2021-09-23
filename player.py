import pygame
import red_knight_sprites
import game_map
from pygame.locals import *
current_tile_size = game_map.current_tile_size

'''class Scheme:   #The key controls for movement
    def __init__(self):
        self.move_forwards = K_w
        self.move_backwards = K_s
        self.move_right = K_d
        self.move_left = K_a'''


class Player:
    def __init__(self):

        # self.scheme = control_scheme
        # self.image_name = "frames/red_knight_run_f1.png"
        # self.sprite_image = pygame.image.load(self.image_name).convert_alpha()
        # The default stats for character attributes
        self.position = pygame.math.Vector2(320.0, 320.0)
        self.speed = 185.0

        self.max_health = 50
        self.health = self.max_health
        self.should_die = False

        self.move_accumulator = 0.0

        self.move_up = False
        self.move_down = False
        self.move_right = False
        self.move_left = False

        self.direction = False

        self.collision_mapped = False
        self.touched_state = False

        # Higher frame_speed means slower animation speed,
        # as it is the time taken for each frame to be displayed for.
        frame_speed = 0.1

        initial_frames = red_knight_sprites.running_frames
        self.frames = []                    # Will contain a list of image sprites in animated order

        SIZE_MULTIPLIER = 1
        self.size_x = int(32 * SIZE_MULTIPLIER)
        self.size_y = int(48 * SIZE_MULTIPLIER)
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




    def update_movement(self, time_delta, collision_x, collision_y):
        speed_delta = self.speed * time_delta
        #collision_boxes = collision
        # Stores the top left corner of all collidable tile regions
        array_of_collision_x = collision_x
        array_of_collision_y = collision_y
        length = len(array_of_collision_x)

        collide_y = False
        collide_x = False

        # All collision arithmetic determines the state of collision when the character is within the collidable regions
        # With some fine tuning (the +- 10 or 15) to centre the collisions


        if self.move_up:
            move_to_y = self.position.y - speed_delta
            for i in range(0, length):
                if (array_of_collision_y[i] + self.size_y < move_to_y + self.size_y - 10 <= current_tile_size + array_of_collision_y[i] and
                        array_of_collision_x[i] - 15 < self.position.x <= current_tile_size - 15 + array_of_collision_x[i]):
                    collide_y = True
            if collide_y == False:
                self.position.y = move_to_y


        if self.move_down:
            move_to_y = self.position.y + speed_delta

            for i in range (0, length):
                if array_of_collision_y[i] - current_tile_size/4.5 < move_to_y + self.size_y - 10 <= current_tile_size + array_of_collision_y[i] and\
                        array_of_collision_x[i] - 15 < self.position.x <= current_tile_size - 15 + array_of_collision_x[i]:
                    collide_y = True
            if collide_y == False:
                self.position.y = move_to_y


        if self.move_left:
            move_to_x = self.position.x - speed_delta
            for i in range (0, length):
                if array_of_collision_x[i] - 15 < move_to_x <= current_tile_size - 15 + array_of_collision_x[i] and \
                        array_of_collision_y[i] - current_tile_size/5 < self.position.y + self.size_y - 10 <= current_tile_size + array_of_collision_y[i]:
                    collide_x = True
            if collide_x == False:
                self.position.x = move_to_x


        if self.move_right:
            move_to_x = self.position.x + speed_delta
            for i in range (0, length):
                if array_of_collision_x[i] - 15 < move_to_x <= current_tile_size - 15 + array_of_collision_x[i] and \
                        array_of_collision_y[i] - current_tile_size/5 < self.position.y + self.size_y - 10 <= current_tile_size + array_of_collision_y[i]:
                    collide_x = True
            if collide_x == False:
                self.position.x = move_to_x

    def on_key_press(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == K_w:
                self.move_up = True
            if event.key == K_s:
                self.move_down = True
            if event.key == K_a:
                self.move_left = True
                self.direction = True
            if event.key == K_d:
                self.move_right = True
                self.direction = False

            if event.key == K_p:
                self.health = 0

    def on_key_release(self, event):
        if event.type == pygame.KEYUP:
            if event.key == K_w:
                self.move_up = False
            if event.key == K_s:
                self.move_down = False
            if event.key == K_a:
                self.move_left = False
            if event.key == K_d:
                self.move_right = False

    def next_frame(self, delta_time):
        self.time_accumulator += delta_time
        # finds the next frame in the animation sequence
        # time_accumulator compares the time spent on the current frame to determine how long to show the frame for
        if self.time_accumulator > self.frame_speed:
            self.time_accumulator = 0.0
            self.current_frame_index += 1

            if self.current_frame_index >= len(self.frames):
                self.current_frame_index = 0

            self.display_frame = self.frames[self.current_frame_index]


    def player_death_damage(self, enemy_pos_x, enemy_pos_y, enemy_width, enemy_height):
        if (self.position.x < enemy_pos_x + enemy_width and self.position.x + self.size_x > enemy_pos_x
                and self.position.y < enemy_pos_y + enemy_height and self.position.y + self.size_y > enemy_pos_y
           ):

            # prevents health from constantly decreasing whilst in enemy
            if not self.touched_state:
                self.health -= 10
                self.touched_state = True
        else:
            self.touched_state = False

        if self.health <= 0:
            self.should_die = True

'''class RespawnPlayer:
    def __init__(self, player):
        self.control_scheme = player.scheme'''

