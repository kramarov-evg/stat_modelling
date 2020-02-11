import numpy as np


def get_rand_list(size: int) -> np.array:
    return np.random.uniform(size=size)


def _get_expected_value(randoms: np.array, size: int) -> float:
    return sum(randoms) / size


def _get_dispersion(randoms: np.array, size: int, expected: float) -> float:
    return sum((randoms - expected)**2) / size


def _get_autocorrelation(randoms: np.array, size: int, expected: float, dispersion: float) -> list:
    denominator = dispersion * size
    autocorrelation = []
    for shift in range(size):
        numerator = 0.0
        cut_randoms = randoms[:size - shift]
        shifted_randoms = randoms[shift:]
        numerator = numerator + sum((cut_randoms - expected) * (shifted_randoms - expected))
        autocorrelation.append(numerator / denominator)
    return autocorrelation


def _get_polygon(randoms: np.array, size: int) -> np.array:
    min_val = min(randoms)
    max_val = max(randoms)
    step = (max_val - min_val) / 12
    rel_freqs = np.zeros(12)
    for val in randoms:
        rel_freqs[(val-min_val) // step] += 1
    rel_freqs = rel_freqs / size
    return rel_freqs


def _get_steps(polygon: np.array) -> np.array:
    steps = np.zeros(13)
    for i in range(len(polygon)-1):
        steps[1+i] = sum(polygon[:i+1])


def get_specs(randoms: np.ndarray, full=False) -> dict:
    size = len(randoms)
    expected_val = _get_expected_value(randoms, size)
    specs = {'expected value': expected_val}
    dispersion = _get_dispersion(randoms, size, expected_val)
    specs['dispersion'] = dispersion
    if full:
        autocorrelation = _get_autocorrelation(randoms, size, expected_val, dispersion)
        specs['autocorrelation'] = autocorrelation
        polygon = _get_polygon(randoms, size)
        specs['polygon'] = polygon
        steps = _get_steps(polygon)
        specs['steps'] = steps
    return specs


if __name__ == "__main__":
    rands = get_rand_list(10000)
    print(get_specs(rands)['expected value'])
