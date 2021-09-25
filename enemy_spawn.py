import random
from game_map import current_tile_size

class Spawn:
    def __init__(self, level_dict):
        self.collidable_array = level_dict['collidable']
        self.invalid_tile = []

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

