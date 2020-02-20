import numpy as np


def IRNUNI(ILOW: int, IUP: int, size=1):
    '''
    Returns int value IR,
    uniformly distributed in interval ILOW <= IR <= IUP

    If size is specified,
    returns array of IRs with size and same restrictions
    '''
    if size == 1:
        u = np.random.uniform()
    else:
        u = np.random.uniform(size=size)
    return int((IUP - ILOW + 1) * u + ILOW)


def IRNBIN():
    pass
