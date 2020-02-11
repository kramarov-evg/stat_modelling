import rand_utils as ru
import plotter

print('size \t\t    M \t\t    D')
for size in [10, 100, 1000, 10000]:
    rands = ru.get_rand_list(size)
    if size == 10000:
        specs = ru.get_specs(rands, full=True)
    else:
        specs = ru.get_specs(rands)
    print(size, '\t\t', round(specs['expected value'], 5), '\t', round(specs['dispersion'], 5))
plotter.plot_autocorrelation(specs['autocorrelation'], save=True)
