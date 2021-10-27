import pygame
import random
import melee_enemy_sprite
from enemy_blueprint_parent import EnemyBlueprint
from game_arithmetic import *


class MeleeEnemy(EnemyBlueprint):
    def __init__(self, position_x, position_y):
        super().__init__(position_x, position_y)        # Inherits all attributes from Parent
        self.current_enemy_type = 'melee'
        self.speed = 1.5
        self.hp = 70

        # To pick a random melee enemy
        random_enemy = random.randint(0, 1)
        possible_enemies = ['slime', 'slime']
        self.current_enemy = possible_enemies[random_enemy]

        size_multiplier = 1.0           # Validation to make sure there is a float
        if self.current_enemy == 'slime':
            initial_frames = melee_enemy_sprite.slime_animation_frames
            size_multiplier = 0.7

        # Changes sprite size
        self.size_x = int(32 * size_multiplier)
        self.size_y = int(36 * size_multiplier)
        for i in initial_frames:
            # For future size changes of sprite
            new_frame = pygame.transform.smoothscale(i, (self.size_x, self.size_y))
            self.frames.append(new_frame)
        self.display_frame = self.frames[self.current_frame_index]
        self.sprite_hitbox = self.display_frame.get_rect(topleft=(self.position.x, self.position.y))

        # White impact frame
        self.white_hit_surf = pygame.surface.Surface((self.size_x, self.size_y))
        self.white_hit_surf.fill(pygame.Color('#FFFFFF'))

    def draw(self, screen):
        frame = self.frames[self.current_frame_index].copy()
        if self.direction == True:      # Face left or right
            frame = pygame.transform.flip(frame, True, False)

        # Uses built-in function to add an rgb colour over the drawn entity
        if self.in_damage_state:        # Flashes white when hit
            frame.blit(self.white_hit_surf, (0, 0), special_flags=pygame.BLEND_RGB_ADD)

        # General draw instruction
        screen.blit(frame, (int(self.position.x), int(self.position.y)))

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
                # Melee not implemented yet
                pass

    def attack(self, screen, delta_time, collidablexy):
        pass

    def move(self, player_pos, player_hitbox, other_hitbox, number_divide):
        if (not self.reloading and
                not pygame.Rect.colliderect(self.sprite_hitbox, player_hitbox) and
                not (pygame.Rect.colliderect(self.sprite_hitbox, other_hitbox) and self.sprite_hitbox != other_hitbox)
        ):
            # Use functions to calculate distacne between points, and displacement vector
            length = pythagoras_length(self.position.x - player_pos.x, self.position.y - player_pos.y)
            displacement = displacement_vector(player_pos, self.position)
            unit = unit_vector(displacement, length)
            # Divide by number of entities as otherwise it moves 'n' times per cycle
            self.position += (unit * self.speed/abs(number_divide-0.2))
        # Check if overlapping any other enemy
        if pygame.Rect.colliderect(self.sprite_hitbox, other_hitbox) and self.sprite_hitbox != other_hitbox:
            self.position += pygame.math.Vector2(random.randint(-1, 1), random.randint(-1, 1))

