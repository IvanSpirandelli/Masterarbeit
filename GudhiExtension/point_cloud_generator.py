import random
import numpy as np
import itertools as it

from GudhiExtension.alpha_complex_wrapper import alpha_complex_wrapper


def generate_n_gridpoints_of_dim_with_dilation(n, dim, dilation):
    points = set()
    while (len(points) < n):
        point = (random.randrange(0, dilation+1, 1) for i in range(dim))
        points.add(point)
    return [list(elem) for elem in points]

def generate_one_point(dim):
    return list(random.random() for _ in range(dim))

def generate_n_points(n, dim):
    points = set()
    while (len(points) < n):
        point = (random.random() for _ in range(dim))
        points.add(point)

    return [list(elem) for elem in points]



