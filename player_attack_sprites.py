import pygame
fireball_sheet = pygame.image.load("Attacks/fireball_sheet.png")
h_flame_sheet = pygame.image.load("Attacks/h_flame_sheet.png")
v_flame_sheet = pygame.image.load("Attacks/v_flame_sheet.png")
sword_slash_sheet = pygame.image.load("Attacks/sword_slashes.png")

fireball_array = []
flame_array = []
sword_array = []

# Creating the array for fireball projectile
# Size can be changed here
fireballMULTI = 1
fireballSHEET = 800 * fireballMULTI     # spritesheet dimensions
fireballSIZE = 100 * fireballMULTI      # sprite tile dimension
for i in range(0, 62):
    fireball_row = (i // 8)
    fireball_column = (i % 8)
    fireball_array.append(fireball_sheet.subsurface(fireball_row * fireballSIZE, fireball_column * fireballSIZE, fireballSIZE, fireballSIZE))

# Creating array for flame projectiles
flameMULTI = 2
h_flame_sheet = pygame.transform.smoothscale(h_flame_sheet, (int(96 * flameMULTI), int(16 * flameMULTI)))
h_flame_array = []
for i in range(0, 3):
    h_flame_array.append(h_flame_sheet.subsurface(i * 32 * flameMULTI, 0, 32 * flameMULTI, 16 * flameMULTI))

v_flame_sheet = pygame.transform.smoothscale(v_flame_sheet, (int(16 * flameMULTI), int(128 * flameMULTI)))
v_flame_array = []
for i in range(0, 4):
    v_flame_array.append(v_flame_sheet.subsurface(0, i * 32 * flameMULTI, 16 * flameMULTI, 32 * flameMULTI))


# Array will be [horizontal, vertical]
flame_array = [[h_flame_array], v_flame_array]

# Sword slashes: Blue, Purple, White, Yellow
for colourset in range(0, 4):
    temp_array = []
    for slashframe in range(0, 5):
        temp_frame = sword_slash_sheet.subsurface(35 * slashframe, 32 * colourset, 35, 32)
        # Making sure all frames face right
        temp_frame = pygame.transform.rotate(temp_frame, 90)
        temp_array.append(temp_frame)
    # Four colour sets in the sword array
    sword_array.append(temp_array)

# for i in range(0, 5):
#     sword_array[i] = pygame.transform.rotate(sword_array[i], 45)
