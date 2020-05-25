import numpy as np
import math

from generators import normal

TEST_ALGO = 2  # Box-Miller
n = 10**5
categories_count = 10


limits = [-4., -1.2805, -0.841, -0.524, -0.253, 0., 0.253, 0.525, 0.841, 1.281, 4.]


av_sum = 0
counter = 0
for i in range(10**2):
    samples = normal(size=n, algo=2)
    n_is = []
    p_is = []
    for i in range(1, categories_count+1):
        n_is.append(np.count_nonzero((samples < limits[i]) & (samples >= limits[i-1])))
        p_is.append(0.5 * (math.erf(limits[i] / math.sqrt(2)) - math.erf(limits[i-1] / math.sqrt(2))))
    sum = 0.

    for n_i, p_i in zip(n_is, p_is):
        sum += (n_i - n * p_i)**2 / (n * p_i)
    counter += 1
    av_sum += sum
    print(counter, end='\r')
print('Hi-square is', av_sum/counter, f'for {n} samples')
