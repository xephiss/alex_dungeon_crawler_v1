import pygame
import math
'''
BLUE= (50,50,225)
screen = pygame.display.set_mode((700,500))
pygame.display.set_caption('Sprite Animation')
background_color: BLUE'''
knight_red = pygame.image.load('spritesheet_red_knight.png').convert_alpha()
knight_red = pygame.transform.smoothscale(knight_red, (128, 56))

class Animation:

    def __init__(self, sprite_sheet, frame_width, frame_height, animation_row, num_frames, speed):
        self.frames = []
        for frame_number in range(0,num_frames):
            self.frames.append(sprite_sheet.subsurface(pygame.Rect(frame_number*frame_width,
                                                                   animation_row*frame_height+6,
                                                                   frame_width, frame_height)))

        self.current_frame_index = 0
        self.display_frame = self.frames[self.current_frame_index]
        self.speed = speed
        self.time_accumulator = 0.0

    def update(self, time_passed):
        self.time_accumulator += time_passed

        if self.time_accumulator > self.speed:
            self.time_accumulator = 0.0
            self.current_frame_index += 1

            if self.current_frame_index >= len(self.frames):
                self.current_frame_index = 0

            self.display_frame = self.frames[self.current_frame_index]

class Scheme:
    def __init__(self):
        self.move_forwards = K_w
        self.move_backwards = K_s
        self.move_right = K_d
        self.move_left = K_a

class Player:
    def __init__(self, start_pos, control_scheme):

        self.scheme = control_scheme
        self.image_name = "frames/red_knight_run_f1"
        self.sprite_image = pygame.image.load(self.image_name).convert_alpha()

        self.acceleration = 200.0
        self.speed = 0.0
        self.max_speed = 200.0
        self.max_reverse_speed = -125.0
        self.strafe_speed = 0.0
        self.max_strafe_speed = 200.0
        self.total_speed = 0.0
        self.rotate_speed = 0.5

        self.max_health = 1000
        self.health = self.max_health
        self.should_die = False

        self.move_accumulator = 0.0

        self.position = [10,10]

        self.move_forwards = False
        self.move_backwards = False
        self.move_right = False
        self.move_left = False


    def processing_events(self, event):
        if event.type == pygame.KEYDOWN:    #key pressed
            if event.key == self.scheme.move_forwards:
                self.move_forwards = True
            if event.key == self.scheme.move_backwards:
                self.move_backwards = True
            if event.key == self.scheme.move_right:
                self.move_right = True
            if event.key == self.scheme.move_left:
                self.move_left = True

        if event.type == pygame.KEYUP:  #key released
            if event.key == self.scheme.move_forwards:
                self.move_forwards = False
            if event.key == self.scheme.move_backwards:
                self.move_backwards = False
            if event.key == self.scheme.move_right:
                self.move_right = False
            if event.key == self.scheme.move_left:
                self.move_left = False


    def update_movement(self, time_delta):
        if self.health == 0:
            self.should_die = True

        if self.move_forwards or self.move_backwards or self.move_right or self.move_left:
            if self.move_forwards:
                self.speed += self.acceleration * time_delta
                if self.speed > self.max_speed:
                    self.speed = self.max_speed

            elif self.move_backwards:
                self.speed -= self.acceleration * time_delta
                if self.speed < self.max_reverse_speed:
                    self.speed = self.max_reverse_speed

            if self.move_right:
                self.strafe_speed -= self.acceleration * time_delta
                if abs(self.strafe_speed) > self.max_strafe_speed:
                    self.strafe_speed = -self.max_strafe_speed

            elif self.move_left:
                self.strafe_speed += self.acceleration * time_delta
                if abs(self.strafe_speed) > self.max_strafe_speed:
                    self.strafe_speed = self.max_strafe_speed

            self.total_speed = math.sqrt(self.strafe_speed **2 + self.speed **2)

            test_move_position = [0, 0]
            test_move_position[0] = self.position[0]
            test_move_position[1] = self.position[1]
            forward_y_movement = time_delta * self.speed
            forward_x_movement = time_delta * self.strafe_speed
            test_move_position[0] += forward_x_movement
            test_move_position[1] += forward_y_movement


class RespawnPlayer:
    def __init__(self, player):
        self.control_scheme = player.scheme







'''
myInstance_1 = Animation(knight_red, 16*2, 50, 0, 4, 0.1)

clock = pygame.time.Clock()
running = True

while running:

    time_in_seconds = clock.tick()/1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    myInstance_1.update(time_in_seconds)

    screen.fill(BLUE)
    screen.blit(myInstance_1.display_frame,(64,64))

    pygame.display.flip()
pygame.quit()
'''