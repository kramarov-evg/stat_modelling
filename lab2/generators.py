import math
import numpy as np


def uniform_int(ILOW: int, IUP: int, size=1):
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
        return ((IUP - ILOW + 1) * u + ILOW).astype(np.int8)


def binomial_int(N: int, p: float, size=1):
    '''
    Returns int value IR,
    binomially distributed in interval 0 <= IR <= N

    If size is specified,
    returns array of IRs with given size and same restrictions
    '''
    prob_limits = np.zeros(N+1)
    prob_limits[0] = (1 - p)**N
    for i in range(1, N+1):
        prob_limits[i] = prob_limits[i-1] * ((N - i + 1) / (i)) * (p / (1 - p))

    prob_values = np.array([np.random.uniform() for i in range(size)])
    values = np.zeros(size, dtype=np.int8)

    for i in range(size):
        value = 0
        while (value < N and prob_values[i] >= 0):
            prob_values[i] -= prob_limits[value]
            value += 1
        values[i] = value

    return (values if size > 1 else values[0])


def geom_int(p: float, size=1, algo=1):
    '''
    Returns int value IR,
    geometrically distributed in interval 1 <= IR

    If size is specified,
    returns array of IRs with given size and same restrictions
    '''
    funcs = [geom_int_accum, geom_int_naive, geom_int_accum_advanced]
    return (funcs[algo-1](p, size) if size > 1 else funcs[algo-1](p, size)[0])


def geom_int_accum(p: float, size: int) -> np.ndarray:
    prob_values = np.array([np.random.uniform() for i in range(size)])
    values = np.zeros(size, dtype=np.int8)

    q = 1-p
    for i in range(size):
        p_cur = p
        value = 0
        while (prob_values[i] >= 0):
            prob_values[i] -= p_cur
            p_cur *= q
            value += 1
        values[i] = value

    return values


def geom_int_naive(p: float, size: int) -> np.ndarray:
    values = np.zeros(size, dtype=np.int8)

    for i in range(size):
        naive = p
        counter = 0
        while naive >= p:
            naive = np.random.uniform()
            counter += 1
        values[i] = counter

    return values


def geom_int_accum_advanced(p: float, size: int) -> np.array:
    values = np.array([np.random.uniform() for i in range(size)])
    r_vals = [math.log(i) / math.log(1 - p) for i in values]
    return np.array(r_vals).astype(np.int8) + 1


if __name__ == "__main__":
    print(uniform_int(0, 9, size=10))
    print(binomial_int(10, 0.5, size=10))
    print(geom_int(0.5, size=10, algo=1))
    print(geom_int(0.5, size=10, algo=2))
    print(geom_int(0.5, size=10, algo=3))
