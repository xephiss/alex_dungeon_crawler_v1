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
fireballSIZE = 100 * fireballMULTI
fireball_width = 45 * fireballMULTI      # sprite tile dimension
fireball_height = 34 * fireballMULTI
fireballBUFFER1 = 30        # X-axis buffer
fireballBUFFER2 = 35        # Y-axis buffer

# Cardinal directions have individual lists
fireball_array_r = []
fireball_array_l = []
fireball_array_u = []
fireball_array_d = []

# Cuts each frame out of the spritesheet, fireballBUFFER removes the whitespace between frame region (100x100),
# and actual frame
for i in range(0, 62):
    fireball_row = (i // 8)
    fireball_column = (i % 8)
    fireball_array_r.append(fireball_sheet.subsurface(fireball_row * fireballSIZE + fireballBUFFER1,
                                                      fireball_column * fireballSIZE + fireballBUFFER2,
                                                      fireball_width,
                                                      fireball_height))

temp = fireball_array_r
for i in temp:
    fireball_array_l.append(pygame.transform.rotate(i, 180))
# temp now faces left
for i in temp:
    fireball_array_u.append(pygame.transform.rotate(i, 90))
# temp now faces up
for i in temp:
    fireball_array_d.append(pygame.transform.rotate(i, 270))
# Fireball array consists of right, left, up, down
fireball_array = [fireball_array_r, fireball_array_l, fireball_array_u, fireball_array_d]

# Creating array for flame projectiles
flameMULTI = 2
# Resizing sprite
h_flame_sheet = pygame.transform.smoothscale(h_flame_sheet, (int(96 * flameMULTI), int(16 * flameMULTI)))

# For left or right facing flame arrays
h_flame_array_r = []
h_flame_array_l = []
for i in range(0, 3):
    h_flame_array_r.append(h_flame_sheet.subsurface(i * 32 * flameMULTI, 0, 32 * flameMULTI, 16 * flameMULTI))
temp = h_flame_array_r  # Need a temporary holding as the pygame..rotate,uses the actual data rather than as a copy
for i in temp:
    h_flame_array_l.append(pygame.transform.rotate(i, 180))

# Resizing sprite
v_flame_sheet = pygame.transform.smoothscale(v_flame_sheet, (int(16 * flameMULTI), int(128 * flameMULTI)))
# For up and down facing flame arrays
v_flame_array_d = []
v_flame_array_u = []
for i in range(0, 4):
    v_flame_array_d.append(v_flame_sheet.subsurface(0, i * 32 * flameMULTI, 16 * flameMULTI, 32 * flameMULTI))
temp = v_flame_array_d
for i in temp:
    v_flame_array_u.append(pygame.transform.rotate(i, 180))

# Array will be [[right, left], [up, down]]
flame_array = [[h_flame_array_r, h_flame_array_l], [v_flame_array_u, v_flame_array_d]]

# Sword sprites
swordMULTI = 2
sword_slash_sheet = pygame.transform.smoothscale(sword_slash_sheet, (int(175 * swordMULTI), int(128 * swordMULTI)))
# Directional sprite arrays for sword slash
# temp will hold a single colour, single direction
temp_array_u, temp_array_r, temp_array_d, temp_array_l = [], [], [], []

#These hold single direction, all colours
sword_array_right, sword_array_left, sword_array_up, sword_array_down = [], [], [], []

# Sword slashes: Blue, Purple, White, Yellow
for colourset in range(0, 4):
    initial_temp_array = []
    # Single direction, all colours
    temp_array_u, temp_array_r, temp_array_d, temp_array_l = [], [], [], []
    for slashframe in range(0, 5):
        temp_frame = sword_slash_sheet.subsurface(35 * slashframe * swordMULTI, 32 * colourset * swordMULTI, 35 * swordMULTI, 32 * swordMULTI)
        initial_temp_array.append(temp_frame)

    # Rotations may make image to look inverted, so a transform.flip is used at times
    for i in initial_temp_array:
        temp_array_l.append(pygame.transform.flip(i, False, True))
    for i in initial_temp_array:
        temp_array_u.append(pygame.transform.rotate(i, -90))
    for i in initial_temp_array:
        temp_array_r.append(pygame.transform.flip(pygame.transform.rotate(i, 180), False, False))
    for i in initial_temp_array:
        temp_array_d.append(pygame.transform.rotate(i, 90))

    # Four cardinal directions
    # Four colour sets in the sword array
    sword_array_up.append(temp_array_u)
    sword_array_down.append(temp_array_d)
    sword_array_left.append(temp_array_l)
    sword_array_right.append(temp_array_r)
sword_array = [sword_array_right, sword_array_left, sword_array_up, sword_array_down]
# 3D Array: Direction -> Colour -> Frame

