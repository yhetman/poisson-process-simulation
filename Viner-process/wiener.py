#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
import math
import random

steps = 1000
sig = 1


def Donsker_process(t):
    Y = [0]
    #T = t * steps 
    root = np.sqrt(t*steps)
    for i in range(t*steps):
        Y.append(Y[-1] + np.random.normal(0, 1) * np.sqrt(i) / root)
    X = np.arange(0, t + 1 / steps, 1 / steps)
    return X, Y

def Levi_process(t):
    Y = [0]
    T = steps * t
    for i in range(t*steps):
        Y.append(Y[-1] + np.random.normal(0, i/T))
    X = np.arange(0, t + 1 / steps, 1 / steps)
    return X, Y

def main():
    a = 4
    b = 15
    
    figure = plt.figure(dpi = 50, figsize = [20, 15])
    
    ax_1 = figure.add_subplot(3, 2, 1)
    ax_2 = figure.add_subplot(3, 2, 4)
    ax_3 = figure.add_subplot(3, 2, 5)
    
    LX, Lprocess = Levi_process(1)
    DX1, Dprocess1 = Donsker_process(1)
    
    process = [(a * t + b * w) for t, w in zip(LX, Lprocess)]
    
    DX2, Dprocess2 = Donsker_process(1000)
    ax_2.plot(DX2, Dprocess2, c = 'black')
    Dp1 = [(np.sqrt(2 * x * np.log(np.log(x)))) for x in DX2]
    Dp2 = [(-np.sqrt(2 * x * np.log(np.log(x)))) for x in DX2]
    
    ax_1.plot(LX, Lprocess, c = 'blue')
    ax_1.plot(DX1, Dprocess1, c = 'green')
    ax_1.legend(['Levi process', 'Donsker simulation'], loc = 2)
    ax_1.set(title = 'Donsker and Levi processes')
   
    ax_2.plot(DX2, Dp1, c = 'red')
    ax_2.plot(DX2, Dp2, c = 'red')
    ax_2.legend(['Donsker process', 'Boundaries'], loc = 2)
    ax_2.set(title = 'Donsker simulation with checked boundries')
    
    ax_3.plot(LX, process, c = 'purple')
    ax_3.set(title = 'X(t) = a * t + b * W(t)')
    plt.tight_layout()
    #ax_1, ax_2, ax_3.xlabel('Time')
    #ax_1, ax_2, ax_3.ylabel('Wiener process')
    plt.show()


if __name__ == "__main__":
    main()
