import pygame
import red_knight_sprites

# This file is currently not used, kept for debugging references

class Animation:

    def __init__(self, frame_speed):
        initial_frames = red_knight_sprites.running_frames
        self.frames = []

        for i in initial_frames:
            new_frame = pygame.transform.smoothscale(i, (32, 56))   # Makes all the sprites the same size dimensions
            self.frames.append(new_frame)                           # Adds to a list so that the animation can run
                                                                    # via list index position
        self.current_frame_index = 0
        self.display_frame = self.frames[self.current_frame_index]
        self.frame_speed = frame_speed                              # Allows frame duration rate to be adjusted per instance
        self.time_accumulator = 0.0

    # This method is the logic for determining how long spent on each frame, when to switch
    def update(self, time_passed):
        self.time_accumulator += time_passed

        if self.time_accumulator > self.frame_speed:
            self.time_accumulator = 0.0
            self.current_frame_index += 1

            if self.current_frame_index >= len(self.frames):
                self.current_frame_index = 0

            self.display_frame = self.frames[self.current_frame_index]
