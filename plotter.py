import matplotlib.pyplot as plt
import numpy as np


def plot_autocorrelation(correlation: list, show=True, save=False):
    plt.stem(correlation, linefmt='b-', markerfmt=' ', use_line_collection=True)
    plt.ylim(-1.0, 1.0)
    plt.xlabel('shift')
    plt.ylabel('autocorrelation')
    if show:
        plt.show()
    if save:
        plt.savefig('correlation.png')
    plt.clf()


def plot_polygon(polygon: np.array, borders: list, show=True, save=False):
    plt.stem(borders, polygon, linefmt='g--', markerfmt='b-', use_line_collection=True)
    plt.ylim(.0, 1.0)
    plt.xlabel('value')
    plt.ylabel('distribution density function')
    if show:
        plt.show()
    if save:
        plt.savefig('polygon.png')
    plt.clf()


def plot_steps(steps: np.array, borders: list, show=True, save=False):
    plt.stem(borders, steps, linefmt='g--', markerfmt='b-', use_line_collection=True)
    plt.ylim(.0, 1.0)
    plt.xlabel('value')
    plt.ylabel('distribution function')
    if show:
        plt.show()
    if save:
        plt.savefig('steps.png')
    plt.clf()
