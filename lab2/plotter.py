import matplotlib.pyplot as plt


def plot_polygon(specs: dict, show=True, save=False):
    plt.hist(specs['randoms'], bins=specs['values'])
    fig = plt.gcf()
    plt.xlabel('value')
    plt.ylabel('Descrete distribution density function')
    fig.set_size_inches(7, 4)
    if show:
        plt.show()
    if save:
        plt.savefig('/home/egor/dev/python/stata/lab2/results/'+specs['method']+'_polygon.png', dpi=300)
    plt.clf()


def plot_steps(specs: dict, show=True, save=False):
    plt.hist(specs['randoms'], bins=specs['values'], cumulative=True)
    fig = plt.gcf()
    plt.xlabel('value')
    plt.ylabel('Descrete distribution function')
    fig.set_size_inches(7, 4)
    if show:
        plt.show()
    if save:
        plt.savefig('/home/egor/dev/python/stata/lab2/results/'+specs['method']+'_steps.png', dpi=300)
    plt.clf()
