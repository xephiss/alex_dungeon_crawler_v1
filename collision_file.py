from game_map import current_tile_size


class CollisionClass:
    def __init__(self, level_dict):
        self.collidable_array = level_dict['collidable']
        self.collidable_positions = []

    # For every tile which is not blank '000', there must be collision
    def collision_area(self, level_dict):
        self.collidable_array = level_dict['collidable']
        index = 0
        self.collidable_positions = []
        for iterable_tile in self.collidable_array:
            if iterable_tile != '000':
                x_temp = (index % 10) * current_tile_size
                y_temp = (index // 10) * current_tile_size
                self.collidable_positions.append([x_temp, y_temp])

            index += 1
            # Y-axis = (index // 10) * current_tile_size
            # X-axis = (index % 10) * current_tile_size

    # Projectiles will fly over pits. Tiles: '5XX'
    def collision_area_projectile(self, level_dict):
        self.collidable_array = level_dict['collidable']
        index = 0
        self.collidable_positions_projectile = []
        for iterable_tile in self.collidable_array:
            # Top and bottom tiles have different hit-boxes
            if iterable_tile == '111':
                x_temp = (index % 10) * current_tile_size
                y_temp = (index // 10) * current_tile_size - 20
                self.collidable_positions_projectile.append([x_temp, y_temp])

            elif iterable_tile == '131':
                x_temp = (index % 10) * current_tile_size
                y_temp = (index // 10) * current_tile_size + 20
                self.collidable_positions_projectile.append([x_temp, y_temp])

            elif iterable_tile != '000' and not (500 <= int(iterable_tile) <= 544):
                x_temp = (index % 10) * current_tile_size
                y_temp = (index // 10) * current_tile_size
                self.collidable_positions_projectile.append([x_temp, y_temp])



            index += 1
