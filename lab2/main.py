from generators import binomial_int as binom, geom_int as geom, log_int as log, poisson_int as pois, uniform_int as uni
import characteristics

import plotter


def visualize_stats(rands, name: str):
    specs = characteristics.get_specs(randoms=rands, name=name, full=True)
    plotter.plot_polygon(specs, save=True, show=True)
    plotter.plot_steps(specs, save=True, show=True)


size = 10**4
rands = binom(10, 0.5, size=size)
visualize_stats(rands, name='Binomial')

for i in range(1, 4):
    rands = geom(0.5, size=size, algo=i)
    visualize_stats(rands, name='Geometric'+str(i))

for i in range(1, 3):
    rands = pois(10, size=size, algo=i)
    visualize_stats(rands, name='Poisson'+str(i))

rands = uni(11, 100, size=size)
visualize_stats(rands, name='Uniform')

rands = log(0.5, size=size)
visualize_stats(rands, name='Logarithmic')
