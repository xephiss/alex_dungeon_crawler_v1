import player_attack_sprites
import pygame


class PlayerProjectile:
    def __init__(self, weapon, direction, health, spawn_pos, player_momentum):
        self.momentum = player_momentum

        self.time_accumulator = 0.0
        self.current_frame_index = 0
        self.animation_delay = 0
        self.position = pygame.math.Vector2(spawn_pos.x, spawn_pos.y)
        self.change_position = pygame.math.Vector2(0, 0)
        self.weapon = weapon
        self.direction = direction
        self.death = False
        self.current_projectile_array = None
        sword_direction_array = None

        if weapon == 'fireball':
            if direction == 'right':
                self.current_projectile_array = player_attack_sprites.fireball_array[0]
                self.position.x += 28       # Fine tuning spawn position - x
                self.position.y += 9        # Fine tuning spawn position - y
            if direction == 'left':
                self.current_projectile_array = player_attack_sprites.fireball_array[1]
                self.position.x -= 32
                self.position.y += 16
            if direction == 'up':
                self.current_projectile_array = player_attack_sprites.fireball_array[2]
                self.position.x -= 2
                self.position.y -= 5
            if direction == 'down':
                self.current_projectile_array = player_attack_sprites.fireball_array[3]
                self.position.x += 5
                self.position.y += 25

            # Animation delay for fireball
            self.animation_delay = 0.05

        elif weapon == 'flame':
            # Make sure the correct flame direction sprite is being used through the 2d Array
            # [0][X] are the horizontal flames, [1][X] is are the vertical flames
            if direction == 'right':
                self.current_projectile_array = player_attack_sprites.flame_array[0][0]
                self.change_position.x = 30     # Fine tuning spawn position - x
                self.change_position.y = 13     # Fine tuning spawn position - y
            if direction == 'left':
                self.current_projectile_array = player_attack_sprites.flame_array[0][1]
                self.change_position.x = -60
                self.change_position.y = 14
            if direction == 'up':
                self.current_projectile_array = player_attack_sprites.flame_array[1][0]
                self.change_position.x = 0
                self.change_position.y = -35
            if direction == 'down':
                self.current_projectile_array = player_attack_sprites.flame_array[1][1]
                self.change_position.y = 32

            # This is needed to set the initial position when spawned
            self.position.x += self.change_position.x
            self.position.y += self.change_position.y

            # Animation speed for flame
            self.animation_delay = 0.15

        else:       # Swords
            if direction == 'right':
                sword_direction_array = player_attack_sprites.sword_array[0]
            elif direction == 'left':
                sword_direction_array = player_attack_sprites.sword_array[1]
                self.change_position.x = -50    # Fine tunes spawn position based of character axis

            elif direction == 'up':
                sword_direction_array = player_attack_sprites.sword_array[2]
                self.change_position.x = -15
                self.change_position.y -= 29

            elif direction == 'down':
                sword_direction_array = player_attack_sprites.sword_array[3]
                self.change_position.x = -20
                self.change_position.y = 15

            # This is needed to set the initial position when spawned
            self.position.x += self.change_position.x
            self.position.y += self.change_position.y

            # Different colour slash depending on percentage health : White -> Yellow -> Blue -> Purple
            if health > 0.75:
                self.current_projectile_array = sword_direction_array[2]
            elif health > 0.5:
                self.current_projectile_array = sword_direction_array[3]
            elif health > 0.25:
                self.current_projectile_array = sword_direction_array[0]
            elif health > 0.0:
                self.current_projectile_array = sword_direction_array[1]

            # Animation speed for sword
            self.animation_delay = 0.1

        self.number_frames = len(self.current_projectile_array)
        # Default direction is right, unless it is 'flame[1] (vertical)'
        # if direction == 'down':
        #     if weapon != 'flame':
        #         for i in range(0, self.number_frames):
        #             self.current_projectile_array[i] = pygame.transform.rotate(self.current_projectile_array[i], 90)
        #
        # if direction == 'up':
        #     if weapon == 'flame':
        #         for i in range(0, self.number_frames):
        #             self.current_projectile_array[i] = pygame.transform.rotate(self.current_projectile_array[i], 180)
        #     else:
        #         for i in range(0, self.number_frames):
        #             self.current_projectile_array[i] = pygame.transform.rotate(self.current_projectile_array[i], -90)
        # if direction == 'left':
        #     for i in range(0, self.number_frames):
        #         self.current_projectile_array[i] = pygame.transform.rotate(self.current_projectile_array[i], 180)

        self.display_frame = self.current_projectile_array[self.current_frame_index]

    def update(self, delta_time):
        if self.death == False:
            self.time_accumulator += delta_time
            if self.time_accumulator > self.animation_delay:
                self.current_frame_index += 1
                self.time_accumulator = 0.0

                # Only fireball weapon should cycle
                if self.current_frame_index >= self.number_frames:
                    if self.weapon == 'flame' or self.weapon == 'sword':
                        self.current_frame_index = 2
                        self.death = True
                    else:
                        self.current_frame_index = 0
                self.display_frame = self.current_projectile_array[self.current_frame_index]

    def draw(self, screen):
        screen.blit(self.display_frame, (self.position.x, self.position.y))

    def move(self, delta_time, player_pos):
        if self.weapon == 'fireball':
            base_speed = 200
            speed_delta = (base_speed + self.momentum) * delta_time
            if self.direction == 'up':
                self.position.y -= speed_delta
            elif self.direction == 'down':
                self.position.y += speed_delta
            elif self.direction == 'left':
                self.position.x -= speed_delta
            else:
                self.position.x += speed_delta

        else:
            # Flame and Sword follow player
            if self.weapon == 'sword':
                self.position.x = player_pos.x + self.change_position.x
                self.position.y = player_pos.y + self.change_position.y
            if self.weapon == 'flame':
                self.position.x = player_pos.x + self.change_position.x
                self.position.y = player_pos.y + self.change_position.y

