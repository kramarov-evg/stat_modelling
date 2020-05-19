import numpy as np


def _get_expected_value(randoms: np.array, size: int) -> float:
    return randoms.sum() / size


def _get_dispersion(randoms: np.array, size: int, expected: float) -> float:
    return ((randoms - expected)**2).sum() / size


def _get_polygon(randoms: np.array, size: int) -> tuple:
    return np.unique(randoms, return_counts=True)


def get_specs(name: str, randoms: np.ndarray, full=False) -> dict:
    size = len(randoms)
    expected_val = _get_expected_value(randoms, size)
    specs = {'expected value': expected_val}
    specs['randoms'] = randoms
    specs['method'] = name
    dispersion = _get_dispersion(randoms, size, expected_val)
    specs['dispersion'] = dispersion
    if full:
        values, counts = _get_polygon(randoms, size)
        specs['values'] = values
        specs['counts'] = counts
    return specs
