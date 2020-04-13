import numpy as np
import matplotlib.pyplot as plt

#it is needed to be remade

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
    plt.text(15, -2, "Done by YULIIA HETMAN", fontdict={'fontsize': 6})
    plt.show()


def main():
    lambd = 2 
    steps = 40
    n = []
    number_of_tries = 100
    counter = 0

    t = np.arange(0, steps,1)
    for i in range (number_of_tries):
        sums = poisson_process(lambd, steps)
        for j, obj in enumerate(sums):
            if obj > 10:
                print("|%2.6f|\t|%d|" % (obj, j))
                n.append(t[j - 1])
       # if sums[3] == 3 * lambd and sums[10] == 9 * lambd and sums[15] > 14 * lambd:
        #    сounter = counter + 1

    print("\n\t==> Average value is %.6f" % (np.mean(n)))
    print("\t==> for lambda equals %.2f :" % (lambd))
    print("\t==> Mean: EX(10) = %.2f" % (10 * pow(lambd, -1)))
   # print("\t==> P{N(3) = 3 * lambda, N(10) = 9 * lambda, N(15) > 14 * lambda} = %.7f" % (counter / number_of_tries))
    draw_graphic(sums, t)
    print("\t|| Done by YULIIA HETMAN :) ||")

main()
