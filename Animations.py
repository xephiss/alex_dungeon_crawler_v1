import pygame

class Animation:

    def __init__(self, sprite_sheet, frame_width, frame_height, animation_row, num_frames, frame_speed):
        knight_red = pygame.image.load('spritesheet_red_knight.png').convert_alpha()
        knight_red = pygame.transform.smoothscale(knight_red, (128, 56))
        self.frames = []
        for frame_number in range(0,num_frames):
            self.frames.append(sprite_sheet.subsurface(pygame.Rect(frame_number*frame_width,
                                                                   animation_row*frame_height+6,
                                                                   frame_width, frame_height)))

        self.current_frame_index = 0
        self.display_frame = self.frames[self.current_frame_index]
        self.frame_speed = frame_speed
        self.time_accumulator = 0.0

    def update(self, time_passed):
        self.time_accumulator += time_passed

        if self.time_accumulator > self.frame_speed:
            self.time_accumulator = 0.0
            self.current_frame_index += 1

            if self.current_frame_index >= len(self.frames):
                self.current_frame_index = 0

            self.display_frame = self.frames[self.current_frame_index]