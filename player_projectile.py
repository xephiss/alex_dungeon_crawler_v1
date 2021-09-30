import player_attack_sprites
import pygame


class PlayerProjectile:
    def __init__(self, weapon, direction, health, spawn_pos):
        self.time_accumulator = 0.0
        self.current_frame_index = 0
        self.animation_delay = 0
        self.position = pygame.math.Vector2(spawn_pos.x, spawn_pos.y)
        self.weapon = weapon
        self.direction = direction
        self.death = False
        self.current_projectile_array = None
        sword_direction_array = None

        if weapon == 'fireball':
            if direction == 'right':
                self.current_projectile_array = player_attack_sprites.fireball_array[0]
            if direction == 'left':
                self.current_projectile_array = player_attack_sprites.fireball_array[1]
            if direction == 'up':
                self.current_projectile_array = player_attack_sprites.fireball_array[2]
            if direction == 'down':
                self.current_projectile_array = player_attack_sprites.fireball_array[3]
            self.animation_delay = 0.05

        elif weapon == 'flame':
            # Make sure the correct flame direction sprite is being used through the 2d Array
            if direction == 'right':
                self.current_projectile_array = player_attack_sprites.flame_array[0][0]
            if direction == 'left':
                self.current_projectile_array = player_attack_sprites.flame_array[0][1]
            if direction == 'up':
                self.current_projectile_array = player_attack_sprites.flame_array[1][0]
            if direction == 'down':
                self.current_projectile_array = player_attack_sprites.flame_array[1][1]

            self.animation_delay = 0.15
        else:
            if direction == 'right':
                sword_direction_array = player_attack_sprites.sword_array[0]
            elif direction == 'left':
                sword_direction_array = player_attack_sprites.sword_array[1]
            elif direction == 'up':
                sword_direction_array = player_attack_sprites.sword_array[2]
            elif direction == 'down':
                sword_direction_array = player_attack_sprites.sword_array[3]

            # Different colour slash depending on percentage health : White -> Yellow -> Blue -> Purple
            if health > 0.75:
                self.current_projectile_array = sword_direction_array[2]
            elif health > 0.5:
                self.current_projectile_array = sword_direction_array[3]
            elif health > 0.25:
                self.current_projectile_array = sword_direction_array[0]
            elif health > 0.0:
                self.current_projectile_array = sword_direction_array[1]
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

    def move(self, delta_time):
        if self.weapon == 'fireball':
            speed_delta = 120 * delta_time
            if self.direction == 'up':
                self.position.y -= speed_delta
            elif self.direction == 'down':
                self.position.y += speed_delta
            elif self.direction == 'left':
                self.position.x -= speed_delta
            else:
                self.position.x += speed_delta


