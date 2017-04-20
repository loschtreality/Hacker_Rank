from functools import reduce

def compute_sum(array):
    return reduce(lambda x,y: x + y, array)
