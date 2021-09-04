import pygame

tilesheet = pygame.image.load("Tiles/Dungeon_Tileset_Yellow tiles 32x32 16by20.png")
size_multiplier = 2
tilesheet = pygame.transform.smoothscale(tilesheet, (512*size_multiplier, 640*size_multiplier))
tile_size = (32 * size_multiplier, 32 * size_multiplier)
base_coordinate = 32 * size_multiplier


# Dictionary of tiling, starting top left to bottom right
# first digit represents what set of tiling, e.g floor, walls, pits
# second digit represents row height of the tile set
# third digit represents column number of the tile set

tiles = {
    # Floor tiles
    '000': tilesheet.subsurface(pygame.Rect(base_coordinate * 7, base_coordinate * 5, tile_size)),
    '001': tilesheet.subsurface(pygame.Rect(base_coordinate * 8, base_coordinate * 5, tile_size)),
    '002': tilesheet.subsurface(pygame.Rect(base_coordinate * 9, base_coordinate * 5, tile_size)),
    '003': tilesheet.subsurface(pygame.Rect(base_coordinate * 10, base_coordinate * 5, tile_size)),
    '004': tilesheet.subsurface(pygame.Rect(base_coordinate * 11, base_coordinate * 5, tile_size)),
    '005': tilesheet.subsurface(pygame.Rect(base_coordinate * 12, base_coordinate * 5, tile_size)),
    '006': tilesheet.subsurface(pygame.Rect(base_coordinate * 13, base_coordinate * 5, tile_size)),
    '007': tilesheet.subsurface(pygame.Rect(base_coordinate * 14, base_coordinate * 5, tile_size)),

    '010': tilesheet.subsurface(pygame.Rect(base_coordinate * 7, base_coordinate * 6, tile_size)),
    '011': tilesheet.subsurface(pygame.Rect(base_coordinate * 8, base_coordinate * 6, tile_size)),
    '012': tilesheet.subsurface(pygame.Rect(base_coordinate * 9, base_coordinate * 6, tile_size)),
    '013': tilesheet.subsurface(pygame.Rect(base_coordinate * 10, base_coordinate * 6, tile_size)),
    '014': tilesheet.subsurface(pygame.Rect(base_coordinate * 11, base_coordinate * 6, tile_size)),
    '015': tilesheet.subsurface(pygame.Rect(base_coordinate * 12, base_coordinate * 6, tile_size)),
    '016': tilesheet.subsurface(pygame.Rect(base_coordinate * 13, base_coordinate * 6, tile_size)),
    '017': tilesheet.subsurface(pygame.Rect(base_coordinate * 14, base_coordinate * 6, tile_size)),

    # Inner Wall tiles
    '100': tilesheet.subsurface(pygame.Rect(base_coordinate * 3, base_coordinate * 0, tile_size)),
    '101': tilesheet.subsurface(pygame.Rect(base_coordinate * 4, base_coordinate * 0, tile_size)),
    '102': tilesheet.subsurface(pygame.Rect(base_coordinate * 5, base_coordinate * 0, tile_size)),

    '110': tilesheet.subsurface(pygame.Rect(base_coordinate * 3, base_coordinate * 1, tile_size)),
    '111': tilesheet.subsurface(pygame.Rect(base_coordinate * 4, base_coordinate * 1, tile_size)),
    '112': tilesheet.subsurface(pygame.Rect(base_coordinate * 5, base_coordinate * 1, tile_size)),

    '120': tilesheet.subsurface(pygame.Rect(base_coordinate * 3, base_coordinate * 2, tile_size)),
    '121': tilesheet.subsurface(pygame.Rect(base_coordinate * 4, base_coordinate * 2, tile_size)),
    '122': tilesheet.subsurface(pygame.Rect(base_coordinate * 5, base_coordinate * 2, tile_size)),

    '130': tilesheet.subsurface(pygame.Rect(base_coordinate * 3, base_coordinate * 3, tile_size)),
    '131': tilesheet.subsurface(pygame.Rect(base_coordinate * 4, base_coordinate * 3, tile_size)),
    '1base_coordinate': tilesheet.subsurface(pygame.Rect(base_coordinate * 5, base_coordinate * 3, tile_size)),

    # Wall Passage tiles
    '300': tilesheet.subsurface(pygame.Rect(base_coordinate * 0, base_coordinate * 4, tile_size)),
    '301': tilesheet.subsurface(pygame.Rect(base_coordinate * 1, base_coordinate * 4, tile_size)),
    '302': tilesheet.subsurface(pygame.Rect(base_coordinate * 2, base_coordinate * 4, tile_size)),
    '303': tilesheet.subsurface(pygame.Rect(base_coordinate * 3, base_coordinate * 4, tile_size)),

    '310': tilesheet.subsurface(pygame.Rect(base_coordinate * 3, base_coordinate * 1, tile_size)),
    '311': tilesheet.subsurface(pygame.Rect(base_coordinate * 1, base_coordinate * 5, tile_size)),
    '312': tilesheet.subsurface(pygame.Rect(base_coordinate * 2, base_coordinate * 5, tile_size)),
    '313': tilesheet.subsurface(pygame.Rect(base_coordinate * 5, base_coordinate * 1, tile_size)),

    '320': tilesheet.subsurface(pygame.Rect(base_coordinate * 0, base_coordinate * 6, tile_size)),
    '321': tilesheet.subsurface(pygame.Rect(base_coordinate * 1, base_coordinate * 6, tile_size)),
    '322': tilesheet.subsurface(pygame.Rect(base_coordinate * 2, base_coordinate * 6, tile_size)),
    '323': tilesheet.subsurface(pygame.Rect(base_coordinate * 3, base_coordinate * 6, tile_size)),

    '330': tilesheet.subsurface(pygame.Rect(base_coordinate * 0, base_coordinate * 7, tile_size)),
    '331': tilesheet.subsurface(pygame.Rect(base_coordinate * 1, base_coordinate * 7, tile_size)),
    '332': tilesheet.subsurface(pygame.Rect(base_coordinate * 2, base_coordinate * 7, tile_size)),
    '333': tilesheet.subsurface(pygame.Rect(base_coordinate * 3, base_coordinate * 7, tile_size)),

    # Back Wall tiles
    '400': tilesheet.subsurface(pygame.Rect(base_coordinate * 7, base_coordinate * 0, tile_size)),
    '401': tilesheet.subsurface(pygame.Rect(base_coordinate * 8, base_coordinate * 0, tile_size)),
    '402': tilesheet.subsurface(pygame.Rect(base_coordinate * 9, base_coordinate * 0, tile_size)),
    '403': tilesheet.subsurface(pygame.Rect(base_coordinate * 10, base_coordinate * 0, tile_size)),
    '404': tilesheet.subsurface(pygame.Rect(base_coordinate * 11, base_coordinate * 0, tile_size)),
    '405': tilesheet.subsurface(pygame.Rect(base_coordinate * 12, base_coordinate * 0, tile_size)),
    '406': tilesheet.subsurface(pygame.Rect(base_coordinate * 13, base_coordinate * 0, tile_size)),
    '407': tilesheet.subsurface(pygame.Rect(base_coordinate * 14, base_coordinate * 0, tile_size)),
    '408': tilesheet.subsurface(pygame.Rect(base_coordinate * 9, base_coordinate * 2, tile_size)),
    '409': tilesheet.subsurface(pygame.Rect(base_coordinate * 10, base_coordinate * 2, tile_size)),

    '410': tilesheet.subsurface(pygame.Rect(base_coordinate * 7, base_coordinate * 1, tile_size)),
    '411': tilesheet.subsurface(pygame.Rect(base_coordinate * 8, base_coordinate * 1, tile_size)),
    '412': tilesheet.subsurface(pygame.Rect(base_coordinate * 9, base_coordinate * 1, tile_size)),
    '413': tilesheet.subsurface(pygame.Rect(base_coordinate * 10, base_coordinate * 1, tile_size)),
    '414': tilesheet.subsurface(pygame.Rect(base_coordinate * 11, base_coordinate * 1, tile_size)),
    '415': tilesheet.subsurface(pygame.Rect(base_coordinate * 12, base_coordinate * 1, tile_size)),
    '416': tilesheet.subsurface(pygame.Rect(base_coordinate * 13, base_coordinate * 1, tile_size)),
    '417': tilesheet.subsurface(pygame.Rect(base_coordinate * 14, base_coordinate * 1, tile_size)),
    '418': tilesheet.subsurface(pygame.Rect(base_coordinate * 9, base_coordinate * 3, tile_size)),
    '419': tilesheet.subsurface(pygame.Rect(base_coordinate * 10, base_coordinate * 3, tile_size)),

    # Pit tiles
    '500': tilesheet.subsurface(pygame.Rect(base_coordinate * 5, base_coordinate * 12, tile_size)),
    '501': tilesheet.subsurface(pygame.Rect(base_coordinate * 6, base_coordinate * 8, tile_size)),
    '502': tilesheet.subsurface(pygame.Rect(base_coordinate * 7, base_coordinate * 8, tile_size)),
    '503': tilesheet.subsurface(pygame.Rect(base_coordinate * 8, base_coordinate * 8, tile_size)),
    '504': tilesheet.subsurface(pygame.Rect(base_coordinate * 9, base_coordinate * 12, tile_size)),

    '510': tilesheet.subsurface(pygame.Rect(base_coordinate * 5, base_coordinate * 13, tile_size)),
    '511': tilesheet.subsurface(pygame.Rect(base_coordinate * 6, base_coordinate * 13, tile_size)),
    '512': tilesheet.subsurface(pygame.Rect(base_coordinate * 7, base_coordinate * 13, tile_size)),
    '513': tilesheet.subsurface(pygame.Rect(base_coordinate * 8, base_coordinate * 13, tile_size)),
    '514': tilesheet.subsurface(pygame.Rect(base_coordinate * 9, base_coordinate * 13, tile_size)),

    '520': tilesheet.subsurface(pygame.Rect(base_coordinate * 5, base_coordinate * 14, tile_size)),
    '521': tilesheet.subsurface(pygame.Rect(base_coordinate * 6, base_coordinate * 14, tile_size)),
    '522': tilesheet.subsurface(pygame.Rect(base_coordinate * 7, base_coordinate * 14, tile_size)),
    '523': tilesheet.subsurface(pygame.Rect(base_coordinate * 8, base_coordinate * 14, tile_size)),
    '524': tilesheet.subsurface(pygame.Rect(base_coordinate * 9, base_coordinate * 14, tile_size)),

    '530': tilesheet.subsurface(pygame.Rect(base_coordinate * 5, base_coordinate * 11, tile_size)),
    '531': tilesheet.subsurface(pygame.Rect(base_coordinate * 6, base_coordinate * 11, tile_size)),
    '5base_coordinate': tilesheet.subsurface(pygame.Rect(base_coordinate * 7, base_coordinate * 11, tile_size)),
    '533': tilesheet.subsurface(pygame.Rect(base_coordinate * 8, base_coordinate * 11, tile_size)),
    '534': tilesheet.subsurface(pygame.Rect(base_coordinate * 9, base_coordinate * 11, tile_size)),

    '540': tilesheet.subsurface(pygame.Rect(base_coordinate * 5, base_coordinate * 12, tile_size)),
    '541': tilesheet.subsurface(pygame.Rect(base_coordinate * 6, base_coordinate * 12, tile_size)),
    '542': tilesheet.subsurface(pygame.Rect(base_coordinate * 7, base_coordinate * 12, tile_size)),
    '543': tilesheet.subsurface(pygame.Rect(base_coordinate * 8, base_coordinate * 12, tile_size)),
    '544': tilesheet.subsurface(pygame.Rect(base_coordinate * 9, base_coordinate * 12, tile_size))
}

collidable_tiles = {
    # Pillars
    '00': tilesheet.subsurface(pygame.Rect(base_coordinate * 0, base_coordinate * 13, tile_size)),
    '01': tilesheet.subsurface(pygame.Rect(base_coordinate * 1, base_coordinate * 13, tile_size)),
    '02': tilesheet.subsurface(pygame.Rect(base_coordinate * 2, base_coordinate * 13, tile_size)),

    '10': tilesheet.subsurface(pygame.Rect(base_coordinate * 0, base_coordinate * 14, tile_size)),
    '11': tilesheet.subsurface(pygame.Rect(base_coordinate * 1, base_coordinate * 14, tile_size)),
    '12': tilesheet.subsurface(pygame.Rect(base_coordinate * 2, base_coordinate * 14, tile_size))
}

aesthetic_tiles = {
    # Bones
    '0': tilesheet.subsurface(pygame.Rect(base_coordinate * 0, base_coordinate * 15, tile_size)),
    '1': tilesheet.subsurface(pygame.Rect(base_coordinate * 1, base_coordinate * 15, tile_size)),
    '2': tilesheet.subsurface(pygame.Rect(base_coordinate * 2, base_coordinate * 15, tile_size)),

    # Stones
    '3': tilesheet.subsurface(pygame.Rect(base_coordinate * 2, base_coordinate * 16, tile_size)),
    '4': tilesheet.subsurface(pygame.Rect(base_coordinate * 3, base_coordinate * 16, tile_size)),
    '5': tilesheet.subsurface(pygame.Rect(base_coordinate * 2, base_coordinate * 17, tile_size))
}
