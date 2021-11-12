import pygame


entities_sprite_sheet = pygame.image.load("frames/100_tiles_16x16pi.png")
ladder = entities_sprite_sheet.subsurface(pygame.Rect(9 * 16, 3 * 16, 16, 16))
SIZE_MULTI = 3
ladder = pygame.transform.smoothscale(ladder, (16 * SIZE_MULTI, 16 * SIZE_MULTI))

class Ladder:
    def __init__(self, x_position: float, y_position: float):
        # Ladder sprite fades in
        self.rect = pygame.Rect((x_position + 8, y_position + 8), (16 * SIZE_MULTI, 16 * SIZE_MULTI))
        self.image = ladder

        self.touched_by_player = False

    def on_collided(self):
        self.touched_by_player = True

    def draw(self, screen):
        screen.blit(self.image, self.rect)