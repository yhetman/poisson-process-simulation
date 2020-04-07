import random
import numpy as np
import matplotlib.pyplot as plt


def poisson_process(lambd, steps):
    ksi = []
    
    ksi = np.random.exponential(lambd, steps)
    sums = np.cumsum(ksi)
    return sums

def draw_graphic(x_ax,y_ax):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    fig.set(facecolor = 'pink')
    ax.set(facecolor = 'pink')
    plt.title('Poisson Process',
        fontdict={ 'fontsize': 21},
        y=1.03, color='navy') 
    ax.plot(x_ax, y_ax, linestyle = 'steps-post',
        c='indigo')
    plt.text(15, -5, "Done by YULIIA HETMAN", fontdict={'fontsize': 6})
    plt.show()


def main():
    lambd = 2
    steps = 21
    n = 0

    for i in range (1,101):
        sums = poisson_process(lambd, steps) 
        print("\t|X(10)|\t|%2i|\t|%2.6f|" % (i, sums[10]))
        n = n + sums[10]
    
    arifm_mean = n / 100
    print("\n\tAverage value of X(10) = %.6f\n" % (arifm_mean))
    t = np.arange(0, steps, 1)
    draw_graphic(t,sums)
    print("Done by YULIIA HETMAN")

main()
