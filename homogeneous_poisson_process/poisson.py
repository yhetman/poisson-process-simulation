#!/usr/bin/env/ python3

import numpy as np
import matplotlib.pyplot as plt


def poisson_process(lambd, steps):
    ksi = []
    beta = 1 / lambd

    ksi = np.random.exponential(beta, steps)
    sums = np.cumsum(ksi)
    return sums

def draw_graphic(x_ax, y_ax):
    fig, ax = plt.subplots()
    fig.set(facecolor = 'pink')
    ax.set(facecolor = 'pink')
    plt.title('Poisson Process',
        fontdict={ 'fontsize': 21},
        y=1.03, color='navy') 
    plt.step(x_ax, y_ax, c='indigo')
    plt.text(15, -2, "Done by YULIIA HETMAN", fontdict={'fontsize': 6})
    plt.show()


def mean_counter(sums, t, n):
    for j, obj in enumerate(sums):
        if obj > 10:
            n.append(t[j - 1])
            break
    return n


def probability_counter(sums, t, lambd):
    k = 0
    for j, obj in enumerate(sums):
        if obj >= 3 and  t[j - 1] < 5:
            return 1
    return 0
            
    
def main():
    lambd = 2
    steps = 20
    n = []
    number_of_tries = 10000
    counter = 0

    t = np.arange(0, steps, 1)  
    for i in range (number_of_tries):
        sums = poisson_process(lambd, steps)
        counter += probability_counter(sums, t, lambd)
        n = mean_counter(sums, t, n)
    print("\n\t==> MEAN is %.6f" % (np.mean(n)))
    print("\t==> for lambda equals %.2f :" % (lambd))
    print("\t==> P{N(3) < 5} = %.6f " % (counter / number_of_tries))
    draw_graphic(sums, t)
    print("\t|| Done by YULIIA HETMAN :) ||")

main()
