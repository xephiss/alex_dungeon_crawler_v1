import pygame
import background_tiles
import map_layouts

floor_tiles = background_tiles.floor_tiles
collideable_tiles = background_tiles.collidable_tiles
aesthetic_tiles = background_tiles.aesthetic_tiles


class Levels:
    def __init__(self):
        self.level_number = 1

        self.level_one = {'map': map_layouts.level_one_map,
                          'collideable': map_layouts.level_one_collision,
                          'aesthetic': map_layouts.level_one_aesthetics}
        self.level_array = [self.level_one]

    # keytable = ('test', 'test2')
    # for i in keytable:
    #    print(tiles[i])

    def draw_map(self, screen):
        current_level = self.level_array[self.level_number - 1]
        collidable_array = current_level['map']
        row = 0
        column = 0
        for tile_iterate in collidable_array:
            screen.blit(floor_tiles[tile_iterate], (64 * row, 64 * column))
            if row != 9:
                row += 1
            else:
                row = 0
                column += 1

    def draw_collision(self, screen):
        current_level = self.level_array[self.level_number - 1]
        collidable_array = current_level['collideable']
        row = 0
        column = 0
        for tile_iterate in collidable_array:
            screen.blit(collideable_tiles[tile_iterate], (64 * row, 64 * column))
            if row != 9:
                row += 1
            else:
                row = 0
                column += 1

    def draw_aesthetic(self, screen):
        current_level = self.level_array[self.level_number - 1]
        collidable_array = current_level['aesthetic']
        row = 0
        column = 0
        for tile_iterate in collidable_array:
            screen.blit(aesthetic_tiles[tile_iterate], (64 * row, 64 * column))
            if row != 9:
                row += 1
            else:
                row = 0
                column += 1


    def draw(self, screen):
        self.draw_map(screen)
        self.draw_collision(screen)
        self.draw_aesthetic(screen)
