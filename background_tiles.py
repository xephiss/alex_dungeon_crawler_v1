import pygame

tilesheet = pygame.image.load("Tiles/Dungeon_Tileset_Yellow tiles 32x32 16by20.png")

# Dictionary of tiling, starting top left to bottom right
# first digit represents what set of tiling, e.g floor, walls, pits
# second digit represents row height of the tile set
# third digit represents column number of the tile set

tiles = {
    # Floor tiles
    '000': tilesheet.subsurface(pygame.Rect(32 * 7, 32 * 5, 32, 32)),
    '001': tilesheet.subsurface(pygame.Rect(32 * 8, 32 * 5, 32, 32)),
    '002': tilesheet.subsurface(pygame.Rect(32 * 9, 32 * 5, 32, 32)),
    '003': tilesheet.subsurface(pygame.Rect(32 * 10, 32 * 5, 32, 32)),
    '004': tilesheet.subsurface(pygame.Rect(32 * 11, 32 * 5, 32, 32)),
    '005': tilesheet.subsurface(pygame.Rect(32 * 12, 32 * 5, 32, 32)),
    '006': tilesheet.subsurface(pygame.Rect(32 * 13, 32 * 5, 32, 32)),
    '007': tilesheet.subsurface(pygame.Rect(32 * 14, 32 * 5, 32, 32)),

    '010': tilesheet.subsurface(pygame.Rect(32 * 7, 32 * 6, 32, 32)),
    '011': tilesheet.subsurface(pygame.Rect(32 * 8, 32 * 6, 32, 32)),
    '012': tilesheet.subsurface(pygame.Rect(32 * 9, 32 * 6, 32, 32)),
    '013': tilesheet.subsurface(pygame.Rect(32 * 10, 32 * 6, 32, 32)),
    '014': tilesheet.subsurface(pygame.Rect(32 * 11, 32 * 6, 32, 32)),
    '015': tilesheet.subsurface(pygame.Rect(32 * 12, 32 * 6, 32, 32)),
    '016': tilesheet.subsurface(pygame.Rect(32 * 13, 32 * 6, 32, 32)),
    '017': tilesheet.subsurface(pygame.Rect(32 * 14, 32 * 6, 32, 32)),

    # Inner Wall tiles
    '100': tilesheet.subsurface(pygame.Rect(32 * 3, 32 * 0, 32, 32)),
    '101': tilesheet.subsurface(pygame.Rect(32 * 4, 32 * 0, 32, 32)),
    '102': tilesheet.subsurface(pygame.Rect(32 * 5, 32 * 0, 32, 32)),

    '110': tilesheet.subsurface(pygame.Rect(32 * 3, 32 * 1, 32, 32)),
    '111': tilesheet.subsurface(pygame.Rect(32 * 4, 32 * 1, 32, 32)),
    '112': tilesheet.subsurface(pygame.Rect(32 * 5, 32 * 1, 32, 32)),

    '120': tilesheet.subsurface(pygame.Rect(32 * 3, 32 * 2, 32, 32)),
    '121': tilesheet.subsurface(pygame.Rect(32 * 4, 32 * 2, 32, 32)),
    '122': tilesheet.subsurface(pygame.Rect(32 * 5, 32 * 2, 32, 32)),

    '130': tilesheet.subsurface(pygame.Rect(32 * 3, 32 * 3, 32, 32)),
    '131': tilesheet.subsurface(pygame.Rect(32 * 4, 32 * 3, 32, 32)),
    '132': tilesheet.subsurface(pygame.Rect(32 * 5, 32 * 3, 32, 32)),

    # Wall Passage tiles
    '300': tilesheet.subsurface(pygame.Rect(32 * 0, 32 * 4, 32, 32)),
    '301': tilesheet.subsurface(pygame.Rect(32 * 1, 32 * 4, 32, 32)),
    '302': tilesheet.subsurface(pygame.Rect(32 * 2, 32 * 4, 32, 32)),
    '303': tilesheet.subsurface(pygame.Rect(32 * 3, 32 * 4, 32, 32)),

    '310': tilesheet.subsurface(pygame.Rect(32 * 3, 32 * 1, 32, 32)),
    '311': tilesheet.subsurface(pygame.Rect(32 * 1, 32 * 5, 32, 32)),
    '312': tilesheet.subsurface(pygame.Rect(32 * 2, 32 * 5, 32, 32)),
    '313': tilesheet.subsurface(pygame.Rect(32 * 5, 32 * 1, 32, 32)),

    '320': tilesheet.subsurface(pygame.Rect(32 * 0, 32 * 6, 32, 32)),
    '321': tilesheet.subsurface(pygame.Rect(32 * 1, 32 * 6, 32, 32)),
    '322': tilesheet.subsurface(pygame.Rect(32 * 2, 32 * 6, 32, 32)),
    '323': tilesheet.subsurface(pygame.Rect(32 * 3, 32 * 6, 32, 32)),

    '330': tilesheet.subsurface(pygame.Rect(32 * 0, 32 * 7, 32, 32)),
    '331': tilesheet.subsurface(pygame.Rect(32 * 1, 32 * 7, 32, 32)),
    '332': tilesheet.subsurface(pygame.Rect(32 * 2, 32 * 7, 32, 32)),
    '333': tilesheet.subsurface(pygame.Rect(32 * 3, 32 * 7, 32, 32)),

    # Back Wall tiles
    '400': tilesheet.subsurface(pygame.Rect(32 * 7, 32 * 0, 32, 32)),
    '401': tilesheet.subsurface(pygame.Rect(32 * 8, 32 * 0, 32, 32)),
    '402': tilesheet.subsurface(pygame.Rect(32 * 9, 32 * 0, 32, 32)),
    '403': tilesheet.subsurface(pygame.Rect(32 * 10, 32 * 0, 32, 32)),
    '404': tilesheet.subsurface(pygame.Rect(32 * 11, 32 * 0, 32, 32)),
    '405': tilesheet.subsurface(pygame.Rect(32 * 12, 32 * 0, 32, 32)),
    '406': tilesheet.subsurface(pygame.Rect(32 * 13, 32 * 0, 32, 32)),
    '407': tilesheet.subsurface(pygame.Rect(32 * 14, 32 * 0, 32, 32)),
    '408': tilesheet.subsurface(pygame.Rect(32 * 9, 32 * 2, 32, 32)),
    '409': tilesheet.subsurface(pygame.Rect(32 * 10, 32 * 2, 32, 32)),

    '410': tilesheet.subsurface(pygame.Rect(32 * 7, 32 * 1, 32, 32)),
    '411': tilesheet.subsurface(pygame.Rect(32 * 8, 32 * 1, 32, 32)),
    '412': tilesheet.subsurface(pygame.Rect(32 * 9, 32 * 1, 32, 32)),
    '413': tilesheet.subsurface(pygame.Rect(32 * 10, 32 * 1, 32, 32)),
    '414': tilesheet.subsurface(pygame.Rect(32 * 11, 32 * 1, 32, 32)),
    '415': tilesheet.subsurface(pygame.Rect(32 * 12, 32 * 1, 32, 32)),
    '416': tilesheet.subsurface(pygame.Rect(32 * 13, 32 * 1, 32, 32)),
    '417': tilesheet.subsurface(pygame.Rect(32 * 14, 32 * 1, 32, 32)),
    '418': tilesheet.subsurface(pygame.Rect(32 * 9, 32 * 3, 32, 32)),
    '419': tilesheet.subsurface(pygame.Rect(32 * 10, 32 * 3, 32, 32)),

    # Pit tiles
    '500': tilesheet.subsurface(pygame.Rect(32 * 5, 32 * 12, 32, 32)),
    '501': tilesheet.subsurface(pygame.Rect(32 * 6, 32 * 8, 32, 32)),
    '502': tilesheet.subsurface(pygame.Rect(32 * 7, 32 * 8, 32, 32)),
    '503': tilesheet.subsurface(pygame.Rect(32 * 8, 32 * 8, 32, 32)),
    '504': tilesheet.subsurface(pygame.Rect(32 * 9, 32 * 12, 32, 32)),

    '510': tilesheet.subsurface(pygame.Rect(32 * 5, 32 * 13, 32, 32)),
    '511': tilesheet.subsurface(pygame.Rect(32 * 6, 32 * 13, 32, 32)),
    '512': tilesheet.subsurface(pygame.Rect(32 * 7, 32 * 13, 32, 32)),
    '513': tilesheet.subsurface(pygame.Rect(32 * 8, 32 * 13, 32, 32)),
    '514': tilesheet.subsurface(pygame.Rect(32 * 9, 32 * 13, 32, 32)),

    '520': tilesheet.subsurface(pygame.Rect(32 * 5, 32 * 14, 32, 32)),
    '521': tilesheet.subsurface(pygame.Rect(32 * 6, 32 * 14, 32, 32)),
    '522': tilesheet.subsurface(pygame.Rect(32 * 7, 32 * 14, 32, 32)),
    '523': tilesheet.subsurface(pygame.Rect(32 * 8, 32 * 14, 32, 32)),
    '524': tilesheet.subsurface(pygame.Rect(32 * 9, 32 * 14, 32, 32)),

    '530': tilesheet.subsurface(pygame.Rect(32 * 5, 32 * 11, 32, 32)),
    '531': tilesheet.subsurface(pygame.Rect(32 * 6, 32 * 11, 32, 32)),
    '532': tilesheet.subsurface(pygame.Rect(32 * 7, 32 * 11, 32, 32)),
    '533': tilesheet.subsurface(pygame.Rect(32 * 8, 32 * 11, 32, 32)),
    '534': tilesheet.subsurface(pygame.Rect(32 * 9, 32 * 11, 32, 32)),

    '540': tilesheet.subsurface(pygame.Rect(32 * 5, 32 * 12, 32, 32)),
    '541': tilesheet.subsurface(pygame.Rect(32 * 6, 32 * 12, 32, 32)),
    '542': tilesheet.subsurface(pygame.Rect(32 * 7, 32 * 12, 32, 32)),
    '543': tilesheet.subsurface(pygame.Rect(32 * 8, 32 * 12, 32, 32)),
    '544': tilesheet.subsurface(pygame.Rect(32 * 9, 32 * 12, 32, 32))
}

collidable_tiles = {
    # Pillars
    '00': tilesheet.subsurface(pygame.Rect(32 * 0, 32 * 13, 32, 32)),
    '01': tilesheet.subsurface(pygame.Rect(32 * 1, 32 * 13, 32, 32)),
    '02': tilesheet.subsurface(pygame.Rect(32 * 2, 32 * 13, 32, 32)),

    '10': tilesheet.subsurface(pygame.Rect(32 * 0, 32 * 14, 32, 32)),
    '11': tilesheet.subsurface(pygame.Rect(32 * 1, 32 * 14, 32, 32)),
    '12': tilesheet.subsurface(pygame.Rect(32 * 2, 32 * 14, 32, 32))
}

aesthetic_tiles = {
    # Bones
    '0': tilesheet.subsurface(pygame.Rect(32 * 0, 32 * 15, 32, 32)),
    '1': tilesheet.subsurface(pygame.Rect(32 * 1, 32 * 15, 32, 32)),
    '2': tilesheet.subsurface(pygame.Rect(32 * 2, 32 * 15, 32, 32)),

    # Stones
    '3': tilesheet.subsurface(pygame.Rect(32 * 2, 32 * 16, 32, 32)),
    '4': tilesheet.subsurface(pygame.Rect(32 * 3, 32 * 16, 32, 32)),
    '5': tilesheet.subsurface(pygame.Rect(32 * 2, 32 * 17, 32, 32))
}
