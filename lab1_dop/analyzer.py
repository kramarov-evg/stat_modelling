import numpy as np

manual_mode = False


def calculate_coef(n: int, m: int) -> float:
    return 2**m / n


def get_nus(m: int, epsilons: np.array) -> np.array:
    nus = np.zeros(2**m, dtype=np.int8)
    for i in epsilons:
        nus[i] += 1
    return nus


def calculate_hi(n: int, m: int, epsilons: np.array) -> float:
    coef = calculate_coef(n=n, m=m)
    nus = get_nus(m=m, epsilons=epsilons)
    return ((nus - 1 / coef) ** 2).sum() * coef


if manual_mode:
    epsilons = np.array(list(map(lambda x: int(x), input('epsilons = ').strip().split())))
    n = int(input('n = ').strip())
    m = int(input('m = ').strip())
else:
    m = 1
    n = 10**4
    epsilons = np.random.randint(0, 2**m, size=n)
    print(np.unique(epsilons, return_counts=True))

print('Hi-square is', calculate_hi(n=n, m=m, epsilons=epsilons))
print('Level of freedom is', 2**m - 1)
