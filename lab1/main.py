import rand_utils as ru
import plotter

print('size \t\t    M \t\t    D')
for size in [10, 100, 1000, 10000, 100000, 1000000]:
    rands = ru.get_rand_list(size)
    if size == 1000:
        specs = ru.get_specs(rands, full=True)
        plotter.plot_autocorrelation(specs['autocorrelation'], save=True, show=False)
        plotter.plot_polygon(specs['polygon'], specs['borders1'], save=True, show=False)
        plotter.plot_steps(specs['steps'], specs['borders2'], save=True, show=False)
    else:
        specs = ru.get_specs(rands)
    print(size, '\t\t', round(specs['expected value'], 5), '\t', round(specs['dispersion'], 5))
