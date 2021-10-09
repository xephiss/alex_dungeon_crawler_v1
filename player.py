import pygame

import player_projectile
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
        self.momentum = 0.0

        # health states
        self.max_health = 100
        self.health = self.max_health

        self.should_die = False
        self.touched_state = False
        self.hit_state = False
        self.hurt_time_accumulator = 0.0

        # movement states
        self.move_accumulator = 0.0

        self.move_up = False
        self.move_down = False
        self.move_right = False
        self.move_left = False

        # When direction is False, player faces right
        self.direction = False

        self.collision_mapped = False

        # attack states
        # Weapons: sword, fireball, flame
        self.current_weapon = 'fireball'
        self.attacked = False
        self.attack_accumulator = 0.0
        self.attack_delay = 1.0     # Can change in an attack method
        self.attack_up, self.attack_down, self.attack_left, self.attack_right = False, False, False, False
        self.active_attacks = []
        #self.weapon_damage = 30


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

            for i in range(0, length):
                if array_of_collision_y[i] - current_tile_size/4.5 < move_to_y + self.size_y - 10 <= current_tile_size + array_of_collision_y[i] and\
                        array_of_collision_x[i] - 15 < self.position.x <= current_tile_size - 15 + array_of_collision_x[i]:
                    collide_y = True
            if collide_y == False:
                self.position.y = move_to_y


        if self.move_left:
            move_to_x = self.position.x - speed_delta
            for i in range(0, length):
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

            if event.key == K_UP:
                self.attack_up = True
            if event.key == K_DOWN:
                self.attack_down = True
            if event.key == K_LEFT:
                self.attack_left = True
            if event.key == K_RIGHT:
                self.attack_right = True

            # Debugging and Testing
            if event.key == K_p:    # Death Key
                self.health = 0
            if event.key == K_o:    # Heal Key
                self.health += 20
            if event.key == K_1:    # Sword
                self.current_weapon = 'sword'
            if event.key == K_2:    # Flame
                self.current_weapon = 'flame'
            if event.key == K_3:    # Fireball
                self.current_weapon = 'fireball'


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

            if event.key == K_UP:
                self.attack_up = False
            if event.key == K_DOWN:
                self.attack_down = False
            if event.key == K_LEFT:
                self.attack_left = False
            if event.key == K_RIGHT:
                self.attack_right = False

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

    def draw_player_bar(self, screen):
        # Health Bar: Red Health and Black Outline
        health_bar = pygame.Surface((44 * (self.health / self.max_health), 7))     # Width, Height
        health_bar.set_alpha(100)           # Sets transparency (alpha value)
        health_bar.fill((200, 0, 0))        # Fills colour
        screen.blit(health_bar, (self.position.x - 6, self.position.y - 12))        # Position

        hp_front_box = pygame.Rect(self.position.x - 8, self.position.y - 13, 47, 9)       # (pos x/y), width, height
        pygame.draw.rect(screen, (0, 0, 0), hp_front_box, 2)     # Surface, colour, image, border-line thickness

        # Invulnerable Bar
        invulnerable_bar = pygame.Rect(35.5, 617, 114 * ((3 - self.hurt_time_accumulator) / 3.0), 3)
        pygame.draw.rect(screen, (20, 150, 150), invulnerable_bar, 8)

        #invulnerable_front_box = pygame.Rect(32, 600, 100, 14)
        #pygame.draw.rect(screen, (0, 0, 0), invulnerable_front_box, 5)


    def player_death_damage(self, enemy_pos_x, enemy_pos_y, enemy_width, enemy_height, projectile_array, delta_time):
        # Provides a contact only invulnerable duration
        invulnerable_time = 3.0
        if (self.position.x < enemy_pos_x + enemy_width and self.position.x + self.size_x > enemy_pos_x
                and self.position.y < enemy_pos_y + enemy_height and self.position.y + self.size_y > enemy_pos_y):

            # prevents health from constantly decreasing whilst in enemy
            if not self.touched_state:
                self.health -= 10
                self.touched_state = True
        if self.touched_state:
            self.hurt_time_accumulator += delta_time
            if self.hurt_time_accumulator > invulnerable_time:
                self.touched_state = False
                self.hurt_time_accumulator = 0.0

        if self.health > self.max_health:
            self.health = self.max_health
            # if self.touched_state:
            #     self.hurt_time_accumulator += delta_time
            #     if self.hurt_time_accumulator > invulnerable_time:
            #         self.touched_state = False
            #         self.hurt_time_accumulator = 0.0
            # if not self.touched_state:
            #     self.health -= 10
            #     self.touched_state = True


        if len(projectile_array) != 0:
            for projectile in projectile_array:
                if (projectile.position.x <= self.position.x + self.size_x and
                        self.position.x <= projectile.position.x + 15 and
                        projectile.position.y <= self.position.y + self.size_y and
                        self.position.y <= projectile.position.y + 15):
                    self.health -= 1

        if self.health <= 0:
            self.should_die = True

    def player_attack_call(self, delta_time):
        hp_percent = self.health/self.max_health

        # If the player is moving, then the projectile fired would be a small bit faster
        if self.move_up or self.move_down or self.move_left or self.move_right:
            momentum = 50
        else:
            momentum = 0

        # Will only be able to attack in the four cardinal directions
        if self.attacked == False:
            if self.attack_up == True:
                self.active_attacks.append(player_projectile.PlayerProjectile(self.current_weapon, 'up', hp_percent, self.position, momentum))
                self.attacked = True
            elif self.attack_down == True:
                self.active_attacks.append(player_projectile.PlayerProjectile(self.current_weapon, 'down', hp_percent, self.position, momentum))
                self.attacked = True
            elif self.attack_left == True:
                self.active_attacks.append(player_projectile.PlayerProjectile(self.current_weapon, 'left', hp_percent, self.position, momentum))
                self.attacked = True
            elif self.attack_right == True:
                self.active_attacks.append(player_projectile.PlayerProjectile(self.current_weapon, 'right', hp_percent, self.position, momentum))
                self.attacked = True

        # Timer so attacks have a pause
        if self.attacked == True:
            self.attack_accumulator += delta_time
            if self.attack_accumulator > self.attack_delay:
                self.attack_accumulator = 0
                self.attacked = False

    def player_attack_update(self, screen, delta_time, collision_proj):
        for attack in self.active_attacks:
            attack.hitbox(screen)           # Debugging hit box
            attack.draw(screen)
            attack.update(delta_time)
            attack.move(delta_time, self.position)
            self.attack_delay = attack.attack_delay

            if attack.weapon == 'fireball':   ## CHANGE this to weapon in the instance rather than current weapon
                for collidable_tile in collision_proj:
                    if (attack.position.x + 20 < collidable_tile[0] + current_tile_size and collidable_tile[0] < int(attack.position.x) + 17 and
                    attack.position.y < collidable_tile[1] + current_tile_size - 5 and collidable_tile[1] < int(attack.position.y)):
                        attack.death = True
                        # For future planning of delayed projectile death for death animation
            if attack.death == True:
                self.active_attacks.remove(attack)


