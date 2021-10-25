import pygame
import background_tiles
import levels_file.level_collection as level_collection     # Stores it as a variable
# Imports all the levels in another file, then import that file: level_collection


floor_tiles = background_tiles.floor_tiles
collidable_tiles = background_tiles.collidable_tiles
aesthetic_tiles = background_tiles.aesthetic_tiles

current_tile_size = 32 * background_tiles.MULTIPLY

class Levels:
    def __init__(self):
        self.mapped_level = False
        self.level_number = 2

        self.collidable = 'collidable'
        level_one = level_collection.level_one.level_one_dict
        level_two = level_collection.level_two.level_two_dict
        level_three = level_collection.level_three.level_three_dict
        level_four = level_collection.level_four.level_four_dict
        level_five = level_collection.level_five.level_five_dict
        level_six = level_collection.level_six.level_six_dict
        self.level_array = [level_one, level_two, level_three, level_four, level_five, level_six]

        # Collision algorithm
        '''self.collision_boxes = []'''
        self.collision_boxes_x = []
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

    def get_level(self):
        self.collision_boxes_x = []
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
    # keytable = ('test', 'test2')
    # for i in keytable:
    #    print(tiles[i])

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

    def draw_collision(self, screen):   # Draws tiles that are collided with, e.g the pillars
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

