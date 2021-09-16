import pygame

frame1 = pygame.image.load('frames/red_knight_frames/red_knight_run_f1.png')
frame2 = pygame.image.load('frames/red_knight_frames/red_knight_run_f2.png')
frame3 = pygame.image.load('frames/red_knight_frames/red_knight_run_f3.png')
frame4 = pygame.image.load('frames/red_knight_frames/red_knight_run_f4.png')

running_frames = [frame1.subsurface(0, 8, 32, 48),
                  frame2.subsurface(0, 8, 32, 48),
                  frame3.subsurface(0, 8, 32, 48),
                  frame4.subsurface(0, 8, 32, 48)]

