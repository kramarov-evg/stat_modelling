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
        return ((IUP - ILOW + 1) * u + ILOW).astype(int)


def binomial_int(N: int, p: float, size=1):
    '''
    Returns int value IR,
    binomially distributed in interval ILOW <= IR <= IUP

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


if __name__ == "__main__":
    print(uniform_int(0, 10, size=10))
    print(binomial_int(10, 0.5, size=10))
