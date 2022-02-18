import pygame

class EnemyBlueprint:
    def __init__(self, position_x, position_y):
        # Positional States
        self.position = pygame.math.Vector2(position_x + 10, position_y + 5)
        self.direction = False

        # Health Attributes
        self.hp = 100  # Should differ between enemies
        self.should_die = False
        self.hit_state = False
        self.hurt_time_accumulator = 0.0


        # Animation Attributes
        self.frames = []  # Initialises attribute as list type
        self.current_frame_index = 0
        self.frame_speed = 0.12     # Lower => Faster frame switching, as it is time to display each frame
        self.time_accumulator = 0.0

        # Attack attributes
        self.attack_time_accumulator = 0.0
        self.attack_speed = 2.0     # Lower => Faster attack

        self.active_projectiles = []
        self.reloading = False

        # Damage states for a white blit as an impact frame
        self.in_damage_state = False
        self.hit_damage_time = 0.2
        self.hit_damage_timer = 0.0

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
            if self.current_frame_index >= len(self.frames):    # Resets the loop
                self.current_frame_index = 0

            self.display_frame = self.frames[self.current_frame_index]

        # Health validation here, also so a death animation can be added
        if self.hp <= 0:
            self.should_die = True

        # Timer for the white impact frames
        if self.in_damage_state:
            self.hit_damage_timer += delta_time
            if self.hit_damage_timer > self.hit_damage_time:
                self.in_damage_state = False
                self.hit_damage_timer = 0.0

    def health_update(self, player_attacks_array, delta_time, player_weapon, player_damage_modifier):
        self.sprite_hitbox = self.display_frame.get_rect(topleft=(self.position.x, self.position.y))
        for player_attack in player_attacks_array:                  # Check collision with all projectile
            # Area collision testing using built-in pygame get_rect area
            if pygame.Rect.colliderect(self.sprite_hitbox, player_attack.hitbox):
                if not self.hit_state:
                    self.hp -= player_attack.weapon_damage * player_damage_modifier
                    self.hit_state = True
                    self.in_damage_state = True

            # Different weapon animations affects invulnerability time needed for enemy
            if player_weapon == 'fireball':
                if not pygame.Rect.colliderect(self.sprite_hitbox, player_attack.hitbox):
                    self.hurt_time_accumulator += delta_time
                    if self.hurt_time_accumulator > 0.7:
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


    # Debugging methods
    def hitbox(self, screen, player_attacks_array):
        rectangle = self.display_frame.get_rect(topleft=(self.position.x, self.position.y))
        pygame.draw.rect(screen, (200,100,100,20), rectangle)
        for player_attack in player_attacks_array:
            if pygame.Rect.colliderect(rectangle, player_attack.hitbox):
                print('Collided')