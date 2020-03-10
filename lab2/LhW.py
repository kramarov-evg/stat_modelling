import numpy as np


def IRNUNI(ILOW: int, IUP: int, size=1):
    '''
    Returns int value IR,
    uniformly distributed in interval ILOW <= IR <= IUP

    If size is specified,
    returns array of IRs with given size and same restrictions
    '''
    if size == 1:
        u = np.random.uniform()
        return int((IUP - ILOW + 1) * u + ILOW)
    else:
        u = np.random.uniform(size=size)
        return u.astype(int)


def IRNBIN():
    pass
