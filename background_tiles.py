import pygame

tilesheet = pygame.image.load("Tiles/Dungeon_Tileset_Yellow tiles 32x32 16by20.png")

# Dictionary of tiling, starting top left to bottom right
# 03,04,13,14 are large square
floor_tiles = {'00' : tilesheet.subsurface(pygame.Rect(32*7,32*5,32,32)),
               '01' : tilesheet.subsurface(pygame.Rect(32*8,32*5,32,32)),
               '02' : tilesheet.subsurface(pygame.Rect(32*9,32*5,32,32)),
               '03' : tilesheet.subsurface(pygame.Rect(32*10,32*5,32,32)),
               '04' : tilesheet.subsurface(pygame.Rect(32*11,32*5,32,32)),
               '05' : tilesheet.subsurface(pygame.Rect(32*12,32*5,32,32)),
               '06' : tilesheet.subsurface(pygame.Rect(32*13,32*5,32,32)),
               '07' : tilesheet.subsurface(pygame.Rect(32*14,32*5,32,32)),

               '10' : tilesheet.subsurface(pygame.Rect(32*7,32*6,32,32)),
               '11' : tilesheet.subsurface(pygame.Rect(32*8,32*6,32,32)),
               '12' : tilesheet.subsurface(pygame.Rect(32*9,32*6,32,32)),
               '13' : tilesheet.subsurface(pygame.Rect(32*10,32*6,32,32)),
               '14' : tilesheet.subsurface(pygame.Rect(32*11,32*6,32,32)),
               '15' : tilesheet.subsurface(pygame.Rect(32*12,32*6,32,32)),
               '16' : tilesheet.subsurface(pygame.Rect(32*13,32*6,32,32)),
               '17' : tilesheet.subsurface(pygame.Rect(32*14,32*6,32,32)),
               }

innerWall_tiles = {'00': tilesheet.subsurface(pygame.Rect(32*3,32*0,32,32)),
                   '01': tilesheet.subsurface(pygame.Rect(32*4,32*0,32,32)),
                   '02': tilesheet.subsurface(pygame.Rect(32*5,32*0,32,32)),

                   '10': tilesheet.subsurface(pygame.Rect(32*3,32*1,32,32)),
                   '11': tilesheet.subsurface(pygame.Rect(32*4,32*1,32,32)),
                   '12': tilesheet.subsurface(pygame.Rect(32*5,32*1,32,32)),

                   '20': tilesheet.subsurface(pygame.Rect(32*3,32*2,32,32)),
                   '21': tilesheet.subsurface(pygame.Rect(32*4,32*2,32,32)),
                   '22': tilesheet.subsurface(pygame.Rect(32*5,32*2,32,32)),

                   '30': tilesheet.subsurface(pygame.Rect(32*3,32*3,32,32)),
                   '31': tilesheet.subsurface(pygame.Rect(32*4,32*3,32,32)),
                   '32': tilesheet.subsurface(pygame.Rect(32*5,32*3,32,32)),
                   }

# Note that 10,13 are recurring of innerWall_tiles that fit in the space respectively
wallPassage_tiles ={'00': tilesheet.subsurface(pygame.Rect(32*0,32*4,32,32)),
                    '01': tilesheet.subsurface(pygame.Rect(32*1,32*4,32,32)),
                    '02': tilesheet.subsurface(pygame.Rect(32*2,32*4,32,32)),
                    '03': tilesheet.subsurface(pygame.Rect(32*3,32*4,32,32)),

                    '10': tilesheet.subsurface(pygame.Rect(32*3,32*1,32,32)),
                    '11': tilesheet.subsurface(pygame.Rect(32*1,32*5,32,32)),
                    '12': tilesheet.subsurface(pygame.Rect(32*2,32*5,32,32)),
                    '13': tilesheet.subsurface(pygame.Rect(32*5,32*1,32,32)),

                    '20': tilesheet.subsurface(pygame.Rect(32*0,32*6,32,32)),
                    '21': tilesheet.subsurface(pygame.Rect(32*1,32*6,32,32)),
                    '22': tilesheet.subsurface(pygame.Rect(32*2,32*6,32,32)),
                    '23': tilesheet.subsurface(pygame.Rect(32*3,32*6,32,32)),

                    '30': tilesheet.subsurface(pygame.Rect(32*0,32*7,32,32)),
                    '31': tilesheet.subsurface(pygame.Rect(32*1,32*7,32,32)),
                    '32': tilesheet.subsurface(pygame.Rect(32*2,32*7,32,32)),
                    '33': tilesheet.subsurface(pygame.Rect(32*3,32*7,32,32)),

                    }