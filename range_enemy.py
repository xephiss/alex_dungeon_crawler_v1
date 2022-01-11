import pygame
import random
import range_enemy_sprite
import projectile_sprite
from enemy_blueprint_parent import EnemyBlueprint
import game_map

current_tile_size = game_map.current_tile_size


class RangeEnemy(EnemyBlueprint):
    def __init__(self, position_x, position_y):
        super().__init__(position_x, position_y)  # Inherits all attributes from Parent
        self.current_enemy_type = 'range'

        # Projectile Dictionary holds name and corresponding sprite of enemy projectiles
        self.projectile_dict = {
            'skull': pygame.transform.smoothscale(range_enemy_sprite.spritesheet.subsurface(293, 327, 6, 6), (15, 15))}
        # Enemy Dictionary holds the Enemy name, nad it's corresponding projectile type
        self.enemy_dict = {'rangeDemon': self.projectile_dict['skull'],
                           'other': None}

        random_enemy = random.randint(0, 1)  # To pick a random range enemy
        possible_enemies = ['rangeDemon', 'rangeDemon']
        self.current_enemy = possible_enemies[random_enemy]

        # Stores the related projectile sprite
        self.projectile = self.enemy_dict[self.current_enemy]
        size_multiplier = 1.0  # Validation to make sure there is a float
        if self.current_enemy == 'rangeDemon':
            initial_frames = range_enemy_sprite.demon_idle_frames
            size_multiplier = 1.4

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
        if self.direction == True:  # Face left or right
            frame = pygame.transform.flip(frame, True, False)

        # Uses built-in function to add an rgb colour over the drawn entity
        if self.in_damage_state:  # Flashes white when hit
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

        else:  # General draw instruction
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
            if self.position.y - 2 < player_y + player_height / 2 and player_y < self.position.y + self.size_y:
                if self.current_enemy_type == 'range':  # Ranged enemies spawn a projectile
                    self.active_projectiles.append(projectile_sprite.Projectile(self.projectile, self.position.x,
                                                                                (self.position.y + self.size_y / 3),
                                                                                player_x, self.size_x / 1.5))
                    self.reloading = True

                else:
                    # Melee not implemented yet
                    pass

    def attack(self, screen, delta_time, collidablexy):
        if self.current_enemy_type == 'range':
            for projectile in self.active_projectiles:
                projectile.general_updates(screen, delta_time)  # Draw, movement and rotation methods are in this

                for collidable_tile in collidablexy:
                    if (projectile.position.x < collidable_tile[0] + current_tile_size and collidable_tile[0] < int(
                            projectile.position.x) + 6 and
                            projectile.position.y < collidable_tile[1] + current_tile_size and collidable_tile[1] < int(
                                projectile.position.y) + 6):
                        projectile.projectile_death()
                # For future planning of delayed projectile death for death animation
                if projectile.death == True:
                    self.active_projectiles.remove(projectile)

                if projectile.position.x < 0 or projectile.position.x > 640:
                    self.active_projectiles.remove(projectile)

    def move(self, player_pos, player_hitbox, other_hitbox, number_divide, collideablexy):
        pass
