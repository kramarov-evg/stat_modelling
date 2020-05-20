import numpy as np


def uniform(a: float, b: float, size=1):
    values = (b-a) * np.random.uniform(size=size) + a
    return values if size > 1 else values[0]


def normal(m=0., sigma=1., size=1, algo=1):
    funcs = [normal_central_limit_theorem, normal_box_miller]
    values = funcs[algo-1](size) * sigma + m
    return (values if size > 1 else values[0])


def normal_central_limit_theorem(size: int):
    values = np.random.uniform(size=size)
    for i in range(11):
        values += np.random.uniform(size=size)
    return values - 6.


def normal_box_miller(size: int):
    values1, values2 = np.random.uniform(size=size), np.random.uniform(size=size)
    sqrt = np.vectorize(np.math.sqrt)
    ln = np.vectorize(np.math.log)
    cos = np.vectorize(np.math.cos)
    return sqrt(-2 * ln(values2)) * cos(2 * values1 * np.math.pi)


def exponential(beta: float, size=1):
    ln = np.vectorize(np.math.log)
    values = np.random.uniform(size=size)
    values = -beta * ln(values)
    return values if size > 1 else values[0]


def hi_square(N: int, size=1):
    values = np.zeros(size)
    for i in range(N):
        values += normal(size=size) ** 2
    return values if size > 1 else values[0]


def student(N: int, size=1):
    sqrt = np.vectorize(np.math.sqrt)
    values = np.random.uniform(size=size)
    values = normal(size=size) / sqrt(hi_square(N) / N)
    return values if size > 1 else values[0]


if __name__ == "__main__":
    pass
