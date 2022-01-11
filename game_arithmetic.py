from game_map import current_tile_size
import random
def pythagoras_length(horizontal, vertical):
    length = (horizontal**2 + vertical**2)**0.5
    return length


def displacement_vector(destination, source):
    displacement = destination - source
    return displacement


def unit_vector(vector, length):
    unit = vector/length
    return unit


def map_collision_v1(position, map_positions_array):
    for map_positions in map_positions_array:
        if (position.x < map_positions[0] + current_tile_size and map_positions[0] < int(position.x) + 6 and
                position.y < map_positions[1] + current_tile_size and map_positions[1] < int(position.y) + 6):
            return True


# returns a random value. The higher the number, the rarer the occurrence.
# Will be used to spawn a random max number of enemies, hence larger numbers is rarer
def random_max_enemy():
    random_value = random.randint(0, 100)
    if random_value == 100:
        return 20   # ~1%
    elif random_value > 97:
        return 10   # ~2%
    elif random_value > 85:
        return 7    # ~12%
    elif random_value > 75:
        return 6    # ~10%
    elif random_value > 50:
        return 5    # ~25%
    elif random_value > 20:
        return 4    # ~30%
    else:
        return 3    # ~20%
