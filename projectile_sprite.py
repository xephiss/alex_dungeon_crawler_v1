import pygame
spritesheet = pygame.image.load('frames/Spritesheet_dungeon.png')

# Projectile Class for Enemy Projectiles
class Projectile:
    def __init__(self, projectile_type, spawn_x, spawn_y, player_x, additional_x):
        self.death = False      # When True, delete the instance
        self.speed = 120.0      # Movement speed
        # Timer and animation attributes
        self.time_accumulator = 0.0
        self.spin_speed = 0.1   # Rate of spin speed
        self.current_frame_index = 0

        # Determines whether the projectile should fire left or right
        if player_x <= spawn_x:
            self.direction = 'left'
        else:
            self.direction = 'right'
            spawn_x += additional_x

        self.position = pygame.math.Vector2(spawn_x, spawn_y)   # Position to spawn
        self.projectile_image = projectile_type
        # For rotating the sprite
        projectile_frame1 = self.projectile_image
        projectile_frame2 = pygame.transform.rotate(self.projectile_image, 45)
        projectile_frame3 = pygame.transform.rotate(self.projectile_image, 90)
        projectile_frame4 = pygame.transform.rotate(self.projectile_image, 135)

        self.projectile_frames = [projectile_frame1, projectile_frame2, projectile_frame3, projectile_frame4]
        self.display_frame = self.projectile_frames[self.current_frame_index]

    # Aesthetic effect of rotating projectile.
    def rotation(self, delta_time):
        self.time_accumulator += delta_time
        # Calculates time spent per frame
        if self.time_accumulator > self.spin_speed:
            self.time_accumulator = 0.0
            self.current_frame_index += 1

            if self.current_frame_index >= len(self.projectile_frames):
                self.current_frame_index = 0
            self.display_frame = self.projectile_frames[self.current_frame_index]

    def draw(self, screen):
        screen.blit(self.display_frame, (self.position.x, self.position.y))

    # Movement of projectile dependent on where player is upon spawning intance
    def update_movement(self, delta_time):
        speed_delta = self.speed * delta_time
        if self.direction == 'left':
            self.position.x -= speed_delta
        elif self.direction == 'right':
            self.position.x += speed_delta

    def projectile_death(self):
        self.death = True

    def general_updates(self, screen, delta_time):
        self.draw(screen)
        self.update_movement(delta_time)
        self.rotation(delta_time)

# In enemy file, need a reload speed