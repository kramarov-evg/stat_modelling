import matplotlib.pyplot as plt


def plot_autocorrelation(correlation: list, show=True, save=False):
    plt.stem(correlation, linefmt='b-', markerfmt=' ', use_line_collection=True)
    if show:
        plt.show()
    if save:
        plt.savefig('correlation.png')
