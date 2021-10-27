
def pythagoras_length(horizontal, vertical):
    length = (horizontal**2 + vertical**2)**0.5
    return length


def displacement_vector(destination, source):
    displacement = destination - source
    return displacement

def unit_vector(vector, length):
    unit = vector/length
    return unit
