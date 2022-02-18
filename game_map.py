import background_tiles
import levels_file.level_collection as level_collection     # Stores it as a variable
# Imports all the levels in another file, then import that file: level_collection
from level_entities import Ladder

floor_tiles = background_tiles.floor_tiles
collidable_tiles = background_tiles.collidable_tiles
aesthetic_tiles = background_tiles.aesthetic_tiles

current_tile_size = 32 * background_tiles.MULTIPLY

class Levels:
    def __init__(self):
        self.mapped_level = False       # Validation from game_state so that tiling can be checked at start
        self.level_number = 1

        # Calls the stored levels
        level_one = level_collection.level_one.level_one_dict
        level_two = level_collection.level_two.level_two_dict
        level_three = level_collection.level_three.level_three_dict
        level_four = level_collection.level_four.level_four_dict
        level_five = level_collection.level_five.level_five_dict
        level_six = level_collection.level_six.level_six_dict
        self.level_array = [level_one, level_two, level_three, level_four, level_five, level_six]
        self.max_levels = len(self.level_array)

        self.end_of_level_tiles = []

        # Collision algorithm
        self.collision_boxes_x = []
        self.collision_boxes_y = []

        current_level = self.level_array[self.level_number - 1]     # Current level index
        collidable_array = current_level['collidable']
        row = 0
        column = 0
        for tile_iterate in collidable_array:
            if tile_iterate != '000' and tile_iterate != '131':
                temp_x = row * current_tile_size               # Holds the current collidable tile positions
                temp_y = column * current_tile_size

                self.collision_boxes_x.append(temp_x)
                self.collision_boxes_y.append(temp_y)

            if row != 9:
                row += 1
            else:
                row = 0
                column += 1

    def get_level(self):
        self.clear_end_of_level_tiles()     # Makes sure end tile: ladder, is cleared away
        if self.level_number >= self.max_levels:    # Validation that level number is valid
            self.level_number = 1

        self.collision_boxes_x = []  # Holds collision coordinates of map-based collision (walls)
        self.collision_boxes_y = []

        current_level = self.level_array[self.level_number - 1]
        collidable_array = current_level['collidable']
        row = 0
        column = 0
        for tile_iterate in collidable_array:
            if tile_iterate != '000' and tile_iterate != '131':
                temp_x = row * current_tile_size               # Holds the current collidable tile positions
                temp_y = column * current_tile_size

                self.collision_boxes_x.append(temp_x)
                self.collision_boxes_y.append(temp_y)

            if row != 9:
                row += 1
            else:
                row = 0
                column += 1

    def draw_map(self, screen):     # Draws the background map tiles, e.g the floor
        current_level = self.level_array[self.level_number - 1]
        tile_array = current_level['map']                       # Stores the tile key layout for the map
        row = 0
        column = 0
        for tile_iterate in tile_array:
            screen.blit(floor_tiles[tile_iterate], (current_tile_size * row, current_tile_size * column))
            if row != 9:
                row += 1
            else:
                row = 0
                column += 1

    def draw_collision(self, screen):   # Draws tiles that are collided with, e.g the pillars that are not walls
        current_level = self.level_array[self.level_number - 1]
        tile_array = current_level['collidable']
        row = 0
        column = 0
        for tile_iterate in tile_array:
            screen.blit(collidable_tiles[tile_iterate], (current_tile_size * row, current_tile_size * column))
            if row != 9:
                row += 1
            else:
                row = 0
                column += 1

    def draw_back_aesthetic(self, screen):      # Draws tiles which are underneath the player
        current_level = self.level_array[self.level_number - 1]
        tile_array = current_level['aestheticBack']
        row = 0
        column = 0
        for tile_iterate in tile_array:
            screen.blit(aesthetic_tiles[tile_iterate], (current_tile_size * row, current_tile_size * column))
            if row != 9:
                row += 1
            else:
                row = 0
                column += 1

    def draw_front_aesthetic(self, screen):     # Draws tiles that are in front of the player
        current_level = self.level_array[self.level_number - 1]
        tile_array = current_level['aestheticFront']
        row = 0
        column = 0
        for tile_iterate in tile_array:
            screen.blit(aesthetic_tiles[tile_iterate], (current_tile_size * row, current_tile_size * column))
            if row != 9:
                row += 1
            else:
                row = 0
                column += 1

    def draw(self, screen):     # Single method to call all of the other methods
        self.draw_map(screen)
        self.draw_collision(screen)
        self.draw_back_aesthetic(screen)

        for tile in self.end_of_level_tiles:    # Adds in the ladder tile entity
            tile.draw(screen)

    def spawn_end_of_level_tile(self, x_position: float, y_position: float):
        self.end_of_level_tiles.append(Ladder(x_position, y_position))      # Creates the end tile

    def clear_end_of_level_tiles(self):
        self.end_of_level_tiles = []    # Method to clear the end tile

