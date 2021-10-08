import pygame

tilesheet = pygame.image.load("Tiles/Dungeon_Tileset_Yellow tiles 32x32 16by20.png")
MULTIPLY = 2

tilesheet = pygame.transform.smoothscale(tilesheet, (512*MULTIPLY, 640*MULTIPLY))
base_coordinate = 32 * MULTIPLY


# Dictionary of tiling, starting top left to bottom right
# first digit represents what set of tiling, e.g floor, walls, pits
# second digit represents row height of the tile set
# third digit represents column number of the tile set

floor_tiles = {
    # 'test': 'hi',
    # 'test2': 'hi2',
    # Filler tile
    '000': tilesheet.subsurface(pygame.Rect(base_coordinate * 8, base_coordinate * 18, 32 * MULTIPLY, 32 * MULTIPLY)),
    # Floor tiles
    '001': tilesheet.subsurface(pygame.Rect(base_coordinate * 7, base_coordinate * 5, 32 * MULTIPLY, 32 * MULTIPLY)),
    '002': tilesheet.subsurface(pygame.Rect(base_coordinate * 8, base_coordinate * 5, 32 * MULTIPLY, 32 * MULTIPLY)),
    '003': tilesheet.subsurface(pygame.Rect(base_coordinate * 9, base_coordinate * 5, 32 * MULTIPLY, 32 * MULTIPLY)),
    '004': tilesheet.subsurface(pygame.Rect(base_coordinate * 10, base_coordinate * 5, 32 * MULTIPLY, 32 * MULTIPLY)),
    '005': tilesheet.subsurface(pygame.Rect(base_coordinate * 11, base_coordinate * 5, 32 * MULTIPLY, 32 * MULTIPLY)),
    '006': tilesheet.subsurface(pygame.Rect(base_coordinate * 12, base_coordinate * 5, 32 * MULTIPLY, 32 * MULTIPLY)),
    '007': tilesheet.subsurface(pygame.Rect(base_coordinate * 13, base_coordinate * 5, 32 * MULTIPLY, 32 * MULTIPLY)),
    '008': tilesheet.subsurface(pygame.Rect(base_coordinate * 14, base_coordinate * 5, 32 * MULTIPLY, 32 * MULTIPLY)),

    '011': tilesheet.subsurface(pygame.Rect(base_coordinate * 7, base_coordinate * 6, 32 * MULTIPLY, 32 * MULTIPLY)),
    '012': tilesheet.subsurface(pygame.Rect(base_coordinate * 8, base_coordinate * 6, 32 * MULTIPLY, 32 * MULTIPLY)),
    '013': tilesheet.subsurface(pygame.Rect(base_coordinate * 9, base_coordinate * 6, 32 * MULTIPLY, 32 * MULTIPLY)),
    '014': tilesheet.subsurface(pygame.Rect(base_coordinate * 10, base_coordinate * 6, 32 * MULTIPLY, 32 * MULTIPLY)),
    '015': tilesheet.subsurface(pygame.Rect(base_coordinate * 11, base_coordinate * 6, 32 * MULTIPLY, 32 * MULTIPLY)),
    '016': tilesheet.subsurface(pygame.Rect(base_coordinate * 12, base_coordinate * 6, 32 * MULTIPLY, 32 * MULTIPLY)),
    '017': tilesheet.subsurface(pygame.Rect(base_coordinate * 13, base_coordinate * 6, 32 * MULTIPLY, 32 * MULTIPLY)),
    '018': tilesheet.subsurface(pygame.Rect(base_coordinate * 14, base_coordinate * 6, 32 * MULTIPLY, 32 * MULTIPLY)),

}

collidable_tiles = {
    # Filler Tile
    '000': tilesheet.subsurface(pygame.Rect(base_coordinate * 8, base_coordinate * 18, 32 * MULTIPLY, 32 * MULTIPLY)),

    # Pillars
    '00': tilesheet.subsurface(pygame.Rect(base_coordinate * 0, base_coordinate * 13, 32 * MULTIPLY, 32 * MULTIPLY)),
    '01': tilesheet.subsurface(pygame.Rect(base_coordinate * 1, base_coordinate * 13, 32 * MULTIPLY, 32 * MULTIPLY)),
    '02': tilesheet.subsurface(pygame.Rect(base_coordinate * 2, base_coordinate * 13, 32 * MULTIPLY, 32 * MULTIPLY)),

    '10': tilesheet.subsurface(pygame.Rect(base_coordinate * 0, base_coordinate * 14, 32 * MULTIPLY, 32 * MULTIPLY)),
    '11': tilesheet.subsurface(pygame.Rect(base_coordinate * 1, base_coordinate * 14, 32 * MULTIPLY, 32 * MULTIPLY)),
    '12': tilesheet.subsurface(pygame.Rect(base_coordinate * 2, base_coordinate * 14, 32 * MULTIPLY, 32 * MULTIPLY)),

    # Inner Wall tiles
    '100': tilesheet.subsurface(pygame.Rect(base_coordinate * 3, base_coordinate * 0, 32 * MULTIPLY, 32 * MULTIPLY)),
    # 101, 102 are top wall, different aesthetic
    '101': tilesheet.subsurface(pygame.Rect(base_coordinate * 4, base_coordinate * 0, 32 * MULTIPLY, 32 * MULTIPLY)),
    '102': tilesheet.subsurface(pygame.Rect(base_coordinate * 1, base_coordinate * 2, 32 * MULTIPLY, 32 * MULTIPLY)),
    '103': tilesheet.subsurface(pygame.Rect(base_coordinate * 5, base_coordinate * 0, 32 * MULTIPLY, 32 * MULTIPLY)),

    # Left Corner, Top, Right Corner
    '110': tilesheet.subsurface(pygame.Rect(base_coordinate * 3, base_coordinate * 1, 32 * MULTIPLY, 32 * MULTIPLY)),
    '111': tilesheet.subsurface(pygame.Rect(base_coordinate * 4, base_coordinate * 1, 32 * MULTIPLY, 32 * MULTIPLY)),
    '112': tilesheet.subsurface(pygame.Rect(base_coordinate * 5, base_coordinate * 1, 32 * MULTIPLY, 32 * MULTIPLY)),

    # Left and Right walls
    '120': tilesheet.subsurface(pygame.Rect(base_coordinate * 2, base_coordinate * 1, 32 * MULTIPLY-1, 32 * MULTIPLY)),
    '121': tilesheet.subsurface(pygame.Rect(base_coordinate * 0, base_coordinate * 1, 32 * MULTIPLY, 32 * MULTIPLY)),

    # Left Corner, Bottom, Right Corner
    '130': tilesheet.subsurface(pygame.Rect(base_coordinate * 3, base_coordinate * 2, 32 * MULTIPLY, 32 * MULTIPLY)),
    '131': tilesheet.subsurface(pygame.Rect(base_coordinate * 4, base_coordinate * 2, 32 * MULTIPLY, 32 * MULTIPLY)),
    '132': tilesheet.subsurface(pygame.Rect(base_coordinate * 5, base_coordinate * 2, 32 * MULTIPLY, 32 * MULTIPLY)),

    # Bottom tiles
    '140': tilesheet.subsurface(pygame.Rect(base_coordinate * 3, base_coordinate * 3, 32 * MULTIPLY, 32 * MULTIPLY)),
    '141': tilesheet.subsurface(pygame.Rect(base_coordinate * 4, base_coordinate * 3, 32 * MULTIPLY, 32 * MULTIPLY)),
    '142': tilesheet.subsurface(pygame.Rect(base_coordinate * 5, base_coordinate * 3, 32 * MULTIPLY, 32 * MULTIPLY)),

    # Wall Passage tiles
    '300': tilesheet.subsurface(pygame.Rect(base_coordinate * 0, base_coordinate * 4, 32 * MULTIPLY, 32 * MULTIPLY)),
    '301': tilesheet.subsurface(pygame.Rect(base_coordinate * 1, base_coordinate * 4, 32 * MULTIPLY, 32 * MULTIPLY)),
    '302': tilesheet.subsurface(pygame.Rect(base_coordinate * 2, base_coordinate * 4, 32 * MULTIPLY, 32 * MULTIPLY)),
    '303': tilesheet.subsurface(pygame.Rect(base_coordinate * 3, base_coordinate * 4, 32 * MULTIPLY, 32 * MULTIPLY)),

    '310': tilesheet.subsurface(pygame.Rect(base_coordinate * 3, base_coordinate * 1, 32 * MULTIPLY, 32 * MULTIPLY)),
    '311': tilesheet.subsurface(pygame.Rect(base_coordinate * 1, base_coordinate * 5, 32 * MULTIPLY, 32 * MULTIPLY)),
    '312': tilesheet.subsurface(pygame.Rect(base_coordinate * 2, base_coordinate * 5, 32 * MULTIPLY, 32 * MULTIPLY)),
    '313': tilesheet.subsurface(pygame.Rect(base_coordinate * 5, base_coordinate * 1, 32 * MULTIPLY, 32 * MULTIPLY)),

    '320': tilesheet.subsurface(pygame.Rect(base_coordinate * 0, base_coordinate * 6, 32 * MULTIPLY, 32 * MULTIPLY)),
    '321': tilesheet.subsurface(pygame.Rect(base_coordinate * 1, base_coordinate * 6, 32 * MULTIPLY, 32 * MULTIPLY)),
    '322': tilesheet.subsurface(pygame.Rect(base_coordinate * 2, base_coordinate * 6, 32 * MULTIPLY, 32 * MULTIPLY)),
    '323': tilesheet.subsurface(pygame.Rect(base_coordinate * 3, base_coordinate * 6, 32 * MULTIPLY, 32 * MULTIPLY)),

    '330': tilesheet.subsurface(pygame.Rect(base_coordinate * 0, base_coordinate * 7, 32 * MULTIPLY, 32 * MULTIPLY)),
    '331': tilesheet.subsurface(pygame.Rect(base_coordinate * 1, base_coordinate * 7, 32 * MULTIPLY, 32 * MULTIPLY)),
    '332': tilesheet.subsurface(pygame.Rect(base_coordinate * 2, base_coordinate * 7, 32 * MULTIPLY, 32 * MULTIPLY)),
    '333': tilesheet.subsurface(pygame.Rect(base_coordinate * 3, base_coordinate * 7, 32 * MULTIPLY, 32 * MULTIPLY)),

    # Back Wall tiles
    '400': tilesheet.subsurface(pygame.Rect(base_coordinate * 7, base_coordinate * 0, 32 * MULTIPLY, 32 * MULTIPLY)),
    '401': tilesheet.subsurface(pygame.Rect(base_coordinate * 8, base_coordinate * 0, 32 * MULTIPLY, 32 * MULTIPLY)),
    '402': tilesheet.subsurface(pygame.Rect(base_coordinate * 9, base_coordinate * 0, 32 * MULTIPLY, 32 * MULTIPLY)),
    '403': tilesheet.subsurface(pygame.Rect(base_coordinate * 10, base_coordinate * 0, 32 * MULTIPLY, 32 * MULTIPLY)),
    '404': tilesheet.subsurface(pygame.Rect(base_coordinate * 11, base_coordinate * 0, 32 * MULTIPLY, 32 * MULTIPLY)),
    '405': tilesheet.subsurface(pygame.Rect(base_coordinate * 12, base_coordinate * 0, 32 * MULTIPLY, 32 * MULTIPLY)),
    '406': tilesheet.subsurface(pygame.Rect(base_coordinate * 13, base_coordinate * 0, 32 * MULTIPLY, 32 * MULTIPLY)),
    '407': tilesheet.subsurface(pygame.Rect(base_coordinate * 14, base_coordinate * 0, 32 * MULTIPLY, 32 * MULTIPLY)),
    '408': tilesheet.subsurface(pygame.Rect(base_coordinate * 9, base_coordinate * 2, 32 * MULTIPLY, 32 * MULTIPLY)),
    '409': tilesheet.subsurface(pygame.Rect(base_coordinate * 10, base_coordinate * 2, 32 * MULTIPLY, 32 * MULTIPLY)),

    '410': tilesheet.subsurface(pygame.Rect(base_coordinate * 7, base_coordinate * 1, 32 * MULTIPLY, 32 * MULTIPLY)),
    '411': tilesheet.subsurface(pygame.Rect(base_coordinate * 8, base_coordinate * 1, 32 * MULTIPLY, 32 * MULTIPLY)),
    '412': tilesheet.subsurface(pygame.Rect(base_coordinate * 9, base_coordinate * 1, 32 * MULTIPLY, 32 * MULTIPLY)),
    '413': tilesheet.subsurface(pygame.Rect(base_coordinate * 10, base_coordinate * 1, 32 * MULTIPLY, 32 * MULTIPLY)),
    '414': tilesheet.subsurface(pygame.Rect(base_coordinate * 11, base_coordinate * 1, 32 * MULTIPLY, 32 * MULTIPLY)),
    '415': tilesheet.subsurface(pygame.Rect(base_coordinate * 12, base_coordinate * 1, 32 * MULTIPLY, 32 * MULTIPLY)),
    '416': tilesheet.subsurface(pygame.Rect(base_coordinate * 13, base_coordinate * 1, 32 * MULTIPLY, 32 * MULTIPLY)),
    '417': tilesheet.subsurface(pygame.Rect(base_coordinate * 14, base_coordinate * 1, 32 * MULTIPLY, 32 * MULTIPLY)),
    '418': tilesheet.subsurface(pygame.Rect(base_coordinate * 9, base_coordinate * 3, 32 * MULTIPLY, 32 * MULTIPLY)),
    '419': tilesheet.subsurface(pygame.Rect(base_coordinate * 10, base_coordinate * 3, 32 * MULTIPLY, 32 * MULTIPLY)),

    # Pit tiles
    '500': tilesheet.subsurface(pygame.Rect(base_coordinate * 5, base_coordinate * 12, 32 * MULTIPLY, 32 * MULTIPLY)),
    '501': tilesheet.subsurface(pygame.Rect(base_coordinate * 6, base_coordinate * 8, 32 * MULTIPLY, 32 * MULTIPLY)),
    '502': tilesheet.subsurface(pygame.Rect(base_coordinate * 7, base_coordinate * 8, 32 * MULTIPLY, 32 * MULTIPLY)),
    '503': tilesheet.subsurface(pygame.Rect(base_coordinate * 8, base_coordinate * 8, 32 * MULTIPLY, 32 * MULTIPLY)),
    '504': tilesheet.subsurface(pygame.Rect(base_coordinate * 9, base_coordinate * 12, 32 * MULTIPLY, 32 * MULTIPLY)),

    '510': tilesheet.subsurface(pygame.Rect(base_coordinate * 5, base_coordinate * 13, 32 * MULTIPLY, 32 * MULTIPLY)),
    '511': tilesheet.subsurface(pygame.Rect(base_coordinate * 6, base_coordinate * 13, 32 * MULTIPLY, 32 * MULTIPLY)),
    '512': tilesheet.subsurface(pygame.Rect(base_coordinate * 7, base_coordinate * 13, 32 * MULTIPLY, 32 * MULTIPLY)),
    '513': tilesheet.subsurface(pygame.Rect(base_coordinate * 8, base_coordinate * 13, 32 * MULTIPLY, 32 * MULTIPLY)),
    '514': tilesheet.subsurface(pygame.Rect(base_coordinate * 9, base_coordinate * 13, 32 * MULTIPLY, 32 * MULTIPLY)),

    '520': tilesheet.subsurface(pygame.Rect(base_coordinate * 5, base_coordinate * 14, 32 * MULTIPLY, 32 * MULTIPLY)),
    '521': tilesheet.subsurface(pygame.Rect(base_coordinate * 6, base_coordinate * 14, 32 * MULTIPLY, 32 * MULTIPLY)),
    '522': tilesheet.subsurface(pygame.Rect(base_coordinate * 7, base_coordinate * 14, 32 * MULTIPLY, 32 * MULTIPLY)),
    '523': tilesheet.subsurface(pygame.Rect(base_coordinate * 8, base_coordinate * 14, 32 * MULTIPLY, 32 * MULTIPLY)),
    '524': tilesheet.subsurface(pygame.Rect(base_coordinate * 9, base_coordinate * 14, 32 * MULTIPLY, 32 * MULTIPLY)),

    '530': tilesheet.subsurface(pygame.Rect(base_coordinate * 5, base_coordinate * 11, 32 * MULTIPLY, 32 * MULTIPLY)),
    '531': tilesheet.subsurface(pygame.Rect(base_coordinate * 6, base_coordinate * 11, 32 * MULTIPLY, 32 * MULTIPLY)),
    '532': tilesheet.subsurface(pygame.Rect(base_coordinate * 7, base_coordinate * 11, 32 * MULTIPLY, 32 * MULTIPLY)),
    '533': tilesheet.subsurface(pygame.Rect(base_coordinate * 8, base_coordinate * 11, 32 * MULTIPLY, 32 * MULTIPLY)),
    '534': tilesheet.subsurface(pygame.Rect(base_coordinate * 9, base_coordinate * 11, 32 * MULTIPLY, 32 * MULTIPLY)),

    '540': tilesheet.subsurface(pygame.Rect(base_coordinate * 5, base_coordinate * 12, 32 * MULTIPLY, 32 * MULTIPLY)),
    '541': tilesheet.subsurface(pygame.Rect(base_coordinate * 6, base_coordinate * 12, 32 * MULTIPLY, 32 * MULTIPLY)),
    '542': tilesheet.subsurface(pygame.Rect(base_coordinate * 7, base_coordinate * 12, 32 * MULTIPLY, 32 * MULTIPLY)),
    '543': tilesheet.subsurface(pygame.Rect(base_coordinate * 8, base_coordinate * 12, 32 * MULTIPLY, 32 * MULTIPLY)),
    '544': tilesheet.subsurface(pygame.Rect(base_coordinate * 9, base_coordinate * 12, 32 * MULTIPLY, 32 * MULTIPLY))
}

aesthetic_tiles = {
    # Filler Tile
    '000': tilesheet.subsurface(pygame.Rect(base_coordinate * 8, base_coordinate * 18, 32 * MULTIPLY, 32 * MULTIPLY)),

    # Bones
    '0': tilesheet.subsurface(pygame.Rect(base_coordinate * 0, base_coordinate * 15, 32 * MULTIPLY, 32 * MULTIPLY)),
    '1': tilesheet.subsurface(pygame.Rect(base_coordinate * 1, base_coordinate * 15, 32 * MULTIPLY, 32 * MULTIPLY)),
    '2': tilesheet.subsurface(pygame.Rect(base_coordinate * 2, base_coordinate * 15, 32 * MULTIPLY, 32 * MULTIPLY)),

    # Stones
    '3': tilesheet.subsurface(pygame.Rect(base_coordinate * 2, base_coordinate * 16, 32 * MULTIPLY, 32 * MULTIPLY)),
    '4': tilesheet.subsurface(pygame.Rect(base_coordinate * 3, base_coordinate * 16, 32 * MULTIPLY, 32 * MULTIPLY)),
    '5': tilesheet.subsurface(pygame.Rect(base_coordinate * 2, base_coordinate * 17, 32 * MULTIPLY, 32 * MULTIPLY)),

    # Pillars
    '00': tilesheet.subsurface(pygame.Rect(base_coordinate * 0, base_coordinate * 13 + 1, 32 * MULTIPLY, 32 * MULTIPLY)),
    '01': tilesheet.subsurface(pygame.Rect(base_coordinate * 1, base_coordinate * 13 + 1, 32 * MULTIPLY, 32 * MULTIPLY)),
    '02': tilesheet.subsurface(pygame.Rect(base_coordinate * 2, base_coordinate * 13 + 1, 32 * MULTIPLY, 32 * MULTIPLY)),

    '10': tilesheet.subsurface(pygame.Rect(base_coordinate * 0, base_coordinate * 14, 32 * MULTIPLY, 32 * MULTIPLY)),
    '11': tilesheet.subsurface(pygame.Rect(base_coordinate * 1, base_coordinate * 14, 32 * MULTIPLY, 32 * MULTIPLY)),
    '12': tilesheet.subsurface(pygame.Rect(base_coordinate * 2, base_coordinate * 14, 32 * MULTIPLY, 32 * MULTIPLY)),
}

