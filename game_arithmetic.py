from game_map import current_tile_size
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
