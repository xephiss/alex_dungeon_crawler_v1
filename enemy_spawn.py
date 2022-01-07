import random
from game_map import current_tile_size

class Spawn:
    def __init__(self, level_dict):
        self.collidable_array = level_dict['collidable']
        self.invalid_tile = []
        self.general_spawn_x = 0
        self.general_spawn_y = 0

    def spawn(self):
        valid = False
        random_spawn = random.randint(0, 99)
        while not valid:
            if self.collidable_array[random_spawn] == '000' and random_spawn not in self.invalid_tile:
                # The following two lines calculates the row and column index
                self.spawn_y = (random_spawn // 10) * current_tile_size
                self.spawn_x = (random_spawn % 10) * current_tile_size
                # Adds this tile to list to mark as taken
                self.invalid_tile.append(random_spawn)
                valid = True
            else:
                # Adds the collidable tile number to list to mark as invalid
                self.invalid_tile.append(random_spawn)
                random_spawn = random.randint(0, 99)

    def general_spawn(self):        # Spawning algorithm used for tiles which are always valid: Corner regions
        x = random.randint(1, 2)
        y = random.randint(1, 2)
        flip_x = random.randint(0, 1)   # Left or right corner
        flip_y = random.randint(0, 1)   # Top or bottom corner

        if flip_x == 0:     # Left
            self.general_spawn_x = x * current_tile_size
        elif flip_x == 1:   # Right
            self.general_spawn_x = (9 - x) * current_tile_size
        if flip_y == 0:     # Top
            self.general_spawn_y = (y + 1) * current_tile_size
        elif flip_y == 1:   # Bottom
            self.general_spawn_y = (9 - y) * current_tile_size




