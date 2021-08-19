import pygame
import math
from pygame.locals import *
'''
BLUE= (50,50,225)
screen = pygame.display.set_mode((700,500))
pygame.display.set_caption('Sprite Animation')
background_color: BLUE'''



#All this Animation stuff isn't  used yet


'''class Scheme:   #The key controls for movement
    def __init__(self):
        self.move_forwards = K_w
        self.move_backwards = K_s
        self.move_right = K_d
        self.move_left = K_a'''

class Player:
    def __init__(self, position_x, position_y):

        #self.scheme = control_scheme
        #self.image_name = "frames/red_knight_run_f1.png"
        #self.sprite_image = pygame.image.load(self.image_name).convert_alpha()
        #The default stats for character attributes
        self.position_x = position_x
        self.position_y = position_y
        self.speed = 200.0


        self.max_health = 1000
        self.health = self.max_health
        self.should_die = False

        self.move_accumulator = 0.0


        self.move_forwards = False
        self.move_backwards = False
        self.move_right = False
        self.move_left = False

    #def set_sprite(self, sprite_sheet, frame_width, frame_height, animation_row, num_frames, speed):

        frame_width = 16
        frame_height = 50
        animation_row = 0
        num_frames = 4
        speed = 20

        knight_red = pygame.image.load('spritesheet_red_knight.png')
        knight_red = pygame.transform.smoothscale(knight_red, (128, 56))
        self.frames = []
        for frame_number in range(0, num_frames):
            self.frames.append(knight_red.subsurface(pygame.Rect(frame_number * frame_width,
                                                                    animation_row * frame_height + 6,
                                                                    frame_width, frame_height)))

        self.current_frame_index = 0
        self.display_frame = self.frames[self.current_frame_index]
        self.speed = speed
        self.time_accumulator = 0.0



    def draw(self, screen):
        frame = self.frames[self.current_frame_index]
        screen.blit(frame, (self.position_x, self.position_y))




    def update_movement(self, delta_time):
        if self.move_forwards or self.move_backwards or self.move_left or self.move_right:
            if self.move_forwards:
                self.position_y += self.speed * delta_time
            if self.move_backwards:
                self.position_y -= self.speed * delta_time
            if self.move_left:
                self.position_x -= self.speed * delta_time
            if self.move_right:
                self.position_x += self.speed * delta_time

    def next_frame(self):
        # finds the next frame in the animation sequence
        self.current_frame_index = self.current_frame_index + 1
        if self.current_frame_index >= len(self.frames):
            self.current_frame_index = 0
        #self.position_x = self.position_x + (self.direction * 3)




'''class RespawnPlayer:
    def __init__(self, player):
        self.control_scheme = player.scheme'''








#myInstance_1 = Animation(knight_red, 16*2, 50, 0, 4, 0.1)


#defaultScheme = Scheme() #Saving the control keys as this variable
player = Player(64,64)

clock = pygame.time.Clock()
running = True

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
