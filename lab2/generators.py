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
    prob_values = np.array([np.random.uniform() for i in range(size)])
    values = np.zeros(size, dtype=np.int8)

    for i in range(size):
        value = 0
        p_cur = (1 - p)**N
        prob_values[i] -= p_cur
        while (prob_values[i] >= 0):
            p_cur *= (N - value) / (value + 1) * p / (1 - p)
            value += 1
            prob_values[i] -= p_cur
        values[i] = value

    return values if size > 1 else values[0]


def geom_int(p: float, size=1, algo=1):
    '''
    Returns int value IR,
    geometrically distributed in interval 1 <= IR

    If size is specified,
    returns array of IRs with given size and same restrictions
    '''
    funcs = [geom_int_accum, geom_int_naive, geom_int_accum_advanced]
    return (funcs[algo-1](p, size) if size > 1 else funcs[algo-1](p, size)[0])


def poisson_int(mu: float, size=1, algo=1):
    '''
    Returns int value IR,
    distributed according to poisson's law in interval 1 <= IR

    If size is specified,
    returns array of IRs with given size and same restrictions
    '''
    funcs = [poisson_int_accum, poisson_int_accum_advanced]
    return (funcs[algo-1](mu, size) if size > 1 else funcs[algo-1](mu, size)[0])


def log_int(p: float, size=1):
    '''
    Returns int value IR,
    distributed according to logarithmic law in interval 1 <= IR

    If size is specified,
    returns array of IRs with given size and same restrictions
    '''
    prob_values = np.array([np.random.uniform() for i in range(size)])
    values = np.zeros(size, dtype=np.int8)

    for i in range(size):
        value = 1
        p_cur = -1 / math.log(1-p) * p
        prob_values[i] -= p_cur
        while (prob_values[i] >= 0):
            p_cur *= value
            value += 1
            p_cur *= p / value
            prob_values[i] -= p_cur
        values[i] = value

    return values if size > 1 else values[0]


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


def poisson_int_accum(mu: float, size: int) -> np.ndarray:
    prob_values = np.array([np.random.uniform() for i in range(size)])
    values = np.zeros(size, dtype=np.int8)

    for i in range(size):
        p_cur = math.e ** (-mu)
        value = 0
        while (prob_values[i] >= 0):
            prob_values[i] -= p_cur
            p_cur *= mu/(value+1)
            value += 1
        values[i] = value - 1

    return values


def poisson_int_accum_advanced(mu: float, size: int) -> np.ndarray:
    limit = math.e ** (-mu)
    values = np.zeros(size, dtype=np.int8)

    for i in range(size):
        value = 0
        prod = 1
        while (prod >= limit):
            value += 1
            prod *= np.random.uniform()
        values[i] = value - 1

    return values


if __name__ == "__main__":
    print(uniform_int(0, 10, size=10))
    print(binomial_int(10, 0.5, size=10))
    print(geom_int(0.5, size=10, algo=1))
    print(geom_int(0.5, size=10, algo=2))
    print(geom_int(0.5, size=10, algo=3))
    print(poisson_int(10, size=10, algo=1))
    print(poisson_int(10, size=10, algo=2))
    print(log_int(0.5, size=10))
