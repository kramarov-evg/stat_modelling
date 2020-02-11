import numpy as np


def get_rand_list(size: int) -> np.ndarray:
    return np.random.uniform(size=size)


def _get_expected_value(randoms: np.ndarray, size: int) -> float:
    return sum(randoms) / size


def _get_dispersion(randoms: np.ndarray, size: int, expected: float) -> float:
    return sum((randoms - expected)**2) / size


def _get_autocorrelation(randoms: np.ndarray, size: int, expected: float, dispersion: float) -> list:
    denominator = dispersion * size
    autocorrelation = []
    for shift in range(size):
        numerator = 0.0
        cut_randoms = randoms[:size - shift]
        shifted_randoms = randoms[shift:]
        numerator = numerator + sum((cut_randoms - expected) * (shifted_randoms * expected))
        autocorrelation.append(numerator / denominator)
    return autocorrelation


def get_specs(randoms: np.ndarray) -> dict:
    size = len(randoms)
    expected_val = _get_expected_value(randoms, size)
    specs = {'expected value': expected_val}
    dispersion = _get_dispersion(randoms, size, expected_val)
    specs['dispersion'] = dispersion
    autocorrelation = _get_autocorrelation(randoms, size, expected_val, dispersion)
    specs['autocorrelation'] = autocorrelation
    return specs


if __name__ == "__main__":
    rands = get_rand_list(10000)
    print(get_specs(rands)['expected value'])
