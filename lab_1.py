import numpy as np
import matplotlib.pyplot as plt


def poisson_process(lambd, steps):
    ksi = []
    beta = 1 / lambd

    ksi = np.random.exponential(beta, steps)
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
    plt.text(15, -0.25, "Done by YULIIA HETMAN", fontdict={'fontsize': 6})
    plt.show()


def main():
    lambd = 5
    steps = 21
    n = 0
    number_of_tries = 101
    counter = 0

    for i in range (1, number_of_tries):
        sums = poisson_process(lambd, steps) 
        print("\t|X(10)|\t|%2i|\t|%2.6f|" % (i, sums[10]))
        n = n + sums[10]
        if sums[3] == 3 * lambd and sums[10] == 9 * lambd:
            сounter = counter + 1

    arifm_mean = n / 100
    print("\n\t==> Average value of X(10) = %.6f" % (arifm_mean))
    print("\t==> for lambda equals %.2f :" % (lambd))
    print("\t==> Mean: EX(10) = %.2f" % (10 * pow(lambd, -1)))
    print("\t==> P{N(3) = 3 * lambda, N(10) = 9 * lambda, N(15) > 14 * lambda} = %.7f"
            % (counter / number_of_tries))
    t = np.arange(0, steps, 1)
    draw_graphic(t,sums)
    print("Done by YULIIA HETMAN")

main()
