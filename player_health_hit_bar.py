import pygame


# Independent file as it is an individually drawn entity, even though it relates to player
def draw_player_bar(self, screen):
    if self.health > self.max_health:       # Validates health again, in case of healing overflowing
        self.health = self.max_health
    # Changeable colour variable
    colour_hex = int(255 * self.health / self.max_health)
    if self.health > 20:  # Buffer colour for more time as red
        colour_hex -= 20

    # Health Bar: Coloured Health and Black Outline
    health_bar = pygame.Surface((44 * (self.health / self.max_health), 7))  # Width (proportional), Height
    health_bar.set_alpha(100)  # Sets transparency (alpha value)
    health_bar.fill((200, colour_hex, 0))  # Fills colour (RGB), Green changes with health proportion
    screen.blit(health_bar, (self.position.x - 6, self.position.y - 12))  # Position to draw

    hp_front_box = pygame.Rect(self.position.x - 8, self.position.y - 13, 47, 9)  # (pos x/y), width, height
    pygame.draw.rect(screen, (0, 0, 0), hp_front_box, 2)  # Parameters: Surface, colour, image, line thickness

    # Invulnerable Bar
    invulnerable_bar = pygame.Rect(35.5, 617, 114 * ((3 - self.hurt_time_accumulator) / 3.0), 3)  # Surface
    pygame.draw.rect(screen, (20, 150, 150), invulnerable_bar, 8)  # Colour and line thickness

    # invulnerable_front_box = pygame.Rect(32, 600, 100, 14)
    # pygame.draw.rect(screen, (0, 0, 0), invulnerable_front_box, 5)