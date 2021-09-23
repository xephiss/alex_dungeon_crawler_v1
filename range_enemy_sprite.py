import pygame
spritesheet = pygame.image.load('frames/Spritesheet_dungeon.png')

demon_frame1_idle = spritesheet.subsurface(20, 369, 26, 31)
demon_frame2_idle = spritesheet.subsurface(52, 369, 26, 31)
demon_frame1_attack = spritesheet.subsurface(84, 369, 26, 31)
demon_frame2_attack = spritesheet.subsurface(115, 369, 26, 31)

# demon_frame1_attack is used during idle frames to create a more fluid animation

demon_idle_frames = [demon_frame1_idle,
                     demon_frame2_idle,
                     demon_frame1_attack,
                     demon_frame2_idle,
                     ]

demon_attack_frames = [demon_frame1_attack,
                       demon_frame2_attack
                       ]
