import pygame
import red_knight_sprites
from pygame.locals import *


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
        # elf.sprite_image = pygame.image.load(self.image_name).convert_alpha()
        # The default stats for character attributes
        self.position = pygame.math.Vector2(64.0, 64.0)
        self.speed = 300.0

        self.max_health = 1000
        self.health = self.max_health
        self.should_die = False

        self.move_accumulator = 0.0

        self.move_up = False
        self.move_down = False
        self.move_right = False
        self.move_left = False

        # Higher frame_speed means slower animation speed,
        # as it is the time taken for each frame to be displayed for.
        frame_speed = 0.05

        initial_frames = red_knight_sprites.running_frames
        self.frames = []                    # Will contain a list of image sprites in animated order

        size_multiplier = 1
        for i in initial_frames:
            # For future size changes of sprite
            new_frame = pygame.transform.smoothscale(i, (32*size_multiplier, 56*size_multiplier))
            self.frames.append(new_frame)

        self.current_frame_index = 0
        self.display_frame = self.frames[self.current_frame_index]
        self.frame_speed = frame_speed
        self.time_accumulator = 0.0

    def draw(self, screen):
        frame = self.frames[self.current_frame_index]
        screen.blit(frame, (int(self.position.x),
                            int(self.position.y)))

    def update_movement(self, time_delta):
        speed_delta = self.speed * time_delta
        if self.move_up:
            self.position.y -= speed_delta
        if self.move_down:
            self.position.y += speed_delta
        if self.move_left:
            self.position.x -= speed_delta
        if self.move_right:
            self.position.x += speed_delta

    def on_key_press(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == K_w:
                self.move_up = True
            if event.key == K_s:
                self.move_down = True
            if event.key == K_a:
                self.move_left = True
            if event.key == K_d:
                self.move_right = True

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
        if self.time_accumulator > self.frame_speed:
            self.time_accumulator = 0.0
            self.current_frame_index += 1

            if self.current_frame_index >= len(self.frames):
                self.current_frame_index = 0

            self.display_frame = self.frames[self.current_frame_index]


'''class RespawnPlayer:
    def __init__(self, player):
        self.control_scheme = player.scheme'''

# myInstance_1 = Animation(knight_red, 16*2, 50, 0, 4, 0.1)

# defaultScheme = Scheme() #Saving the control keys as this variable
# player = Player()d

# clock = pygame.time.Clock()
# running = True

'''while running:

    delta_time = clock.tick()/1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #myInstance_1.update(delta_time)

    screen.fill(BLUE)
    screen.blit(#myInstance_1,(#position_x,#position_y))

    pygame.display.flip()
pygame.quit()'''
