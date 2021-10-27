import random
import range_enemy
import melee_enemy


# Stores both types of enemies under one class.
class EnemyInstance:
    def __init__(self, position_x, position_y):
        random_enemy_type = random.randint(0, 1)        # Pick a random chance for melee or range

        if random_enemy_type == 0:
            self.enemy_inst = range_enemy.RangeEnemy(position_x, position_y)
        else:
            self.enemy_inst = melee_enemy.MeleeEnemy(position_x, position_y)
