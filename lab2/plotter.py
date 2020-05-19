import matplotlib.pyplot as plt


def plot_polygon(specs: dict, show=True, save=False):
    plt.hist(specs['randoms'], bins=specs['values'])
    plt.xlabel('value')
    plt.ylabel('Descrete distribution density function')
    if show:
        plt.show()
    if save:
        plt.savefig('/home/egor/dev/python/stata/lab2/results/'+specs['method']+'_polygon.png')
    plt.clf()


def plot_steps(specs: dict, show=True, save=False):
    plt.hist(specs['randoms'], bins=specs['values'], cumulative=True)
    plt.xlabel('value')
    plt.ylabel('Descrete distribution function')
    if show:
        plt.show()
    if save:
        plt.savefig('/home/egor/dev/python/stata/lab2/results/'+specs['method']+'_steps.png')
    plt.clf()
