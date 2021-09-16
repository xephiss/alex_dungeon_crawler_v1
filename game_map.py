import pygame
import background_tiles
import map_layouts

floor_tiles = background_tiles.floor_tiles
collideable_tiles = background_tiles.collidable_tiles
aesthetic_tiles = background_tiles.aesthetic_tiles

current_tile_size = 32 * background_tiles.MULTIPLY

class Levels:
    def __init__(self):
        self.collision_mapped = False
        self.level_number = 1

        self.level_one = {'map': map_layouts.level_one_map,
                          'collideable': map_layouts.level_one_collision,
                          'aestheticBack': map_layouts.level_one_back_aesthetics,
                          'aestheticFront': map_layouts.level_one_front_aesthetics
                          }
        self.level_array = [self.level_one]

        # Collision algorithm
        self.collision_boxes = []
        self.collision_boxes_x = []
        self.collision_boxes_y = []
        # Will hold all the 'xy' positions of top left of collisions
        current_level = self.level_array[self.level_number - 1]
        collidable_array = current_level['collideable']
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

    def draw_map(self, screen):
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

    def draw_collision(self, screen):
        current_level = self.level_array[self.level_number - 1]
        tile_array = current_level['collideable']
        row = 0
        column = 0
        for tile_iterate in tile_array:
            screen.blit(collideable_tiles[tile_iterate], (current_tile_size * row, current_tile_size * column))
            if row != 9:
                row += 1
            else:
                row = 0
                column += 1

    def draw_back_aesthetic(self, screen):
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

    def draw_front_aesthetic(self, screen):
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

    def draw(self, screen):
        self.draw_map(screen)
        self.draw_collision(screen)
        self.draw_back_aesthetic(screen)

