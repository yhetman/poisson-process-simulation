#!/usr/bin/env python3

import math
import random
import numpy as np
import matplotlib.pyplot as plt

steps = 1000
step = pow(steps, -1)

def Donsker_process(T):
    Y = [0]
    root = np.sqrt(T)
    for i in range(T):
        Y.append(Y[-1] + np.random.normal(0, 1) * np.sqrt(i) / root)
    X = np.arange(0, T / steps + step, step)
    return X, Y


def Levi_process(T):
    Y = [0]
    for i in range(T):
        Y.append(Y[-1] + np.random.normal(0, i/T))
    X = np.arange(0, T / steps + step, step)
    return X, Y


def third_ex(X, Y):
    a = 9
    b = 19
    process = []
    for t, w in zip(X, Y):
        process.append(a * t + b * w)
    return process


def second_ex(X):
    bound_1 = []
    bound_2 = []
    for x in X:
        bound_1.append(np.sqrt(2 * x * np.log(np.log(x))))
        bound_2.append(-np.sqrt(2 * x * np.log(np.log(x)))) 
    return (bound_1, bound_2)


def main():
    figure = plt.figure(dpi = 50, figsize = [25, 15])
    ax_1 = figure.add_subplot(3, 1, 1)
    ax_2 = figure.add_subplot(3, 1, 2)
    ax_3 = figure.add_subplot(3, 1, 3)
    
    LX, Lprocess = Levi_process(steps)
    DX1, Dprocess1 = Donsker_process(steps)
    
    ax_1.plot(LX, Lprocess, c = 'blue')
    ax_1.plot(DX1, Dprocess1, c = 'green')
    ax_1.legend(['Levi process', 'Donsker simulation'], loc = 2)
    ax_1.set(title = 'Donsker and Levi processes')

    DX2, Dprocess2 = Donsker_process(1000 * steps)
    ax_2.plot(DX2, Dprocess2, c = 'black')
    for y in second_ex(DX2):
        ax_2.plot(DX2, y, c = 'red')
    ax_2.legend(['Donsker process', 'Boundaries'], loc = 2)
    ax_2.set(title = 'Donsker simulation with checked boundries')
    
    ax_3.plot(LX, third_ex(LX, Lprocess), c = 'purple')
    ax_3.set(title = 'X(t) = a * t + b * W(t)')
    for ax in (ax_1, ax_2, ax_3):
        ax.set_xlabel('Time')
        ax.set_ylabel('Wiener process')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
