from generators import exponential, normal, hi_square, student, uniform
import characteristics

import plotter


def visualize_stats(rands, name: str):
    specs = characteristics.get_specs(randoms=rands, name=name, full=True)
    plotter.plot_polygon(specs, save=True, show=True)
    plotter.plot_steps(specs, save=True, show=True)


size = 10**4

rands = uniform(0., 1., size=size)
visualize_stats(rands, name='Uniform')

for i in range(1, 3):
    rands = normal(size=size, algo=i)
    visualize_stats(rands, name='Normal'+str(i))

rands = exponential(1, size=size)
visualize_stats(rands, name='Exponential')

rands = hi_square(10, size=size)
visualize_stats(rands, name='Hi Square')

rands = student(10, size=size)
visualize_stats(rands, name='Student')
