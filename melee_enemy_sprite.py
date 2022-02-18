import pygame
spritesheet = pygame.image.load('frames/Spritesheet_dungeon.png')

slime_frame1 = spritesheet.subsurface(368, 112, 16, 16)
slime_frame2 = spritesheet.subsurface(384, 112, 16, 16)
slime_frame3 = spritesheet.subsurface(400, 112, 16, 16)
slime_frame4 = spritesheet.subsurface(416, 112, 16, 16)

slime_animation_frames = [slime_frame1, slime_frame2, slime_frame3, slime_frame4]

# Would have been used as a third enemy
ogre_animation_frames = [
spritesheet.subsurface(22, 324, 20, 28),
spritesheet.subsurface(54, 324, 20, 28),
spritesheet.subsurface(85, 324, 22, 28),
spritesheet.subsurface(118, 324, 20, 28),
spritesheet.subsurface(150, 324, 20, 28),
spritesheet.subsurface(22, 324, 20, 28),

]
