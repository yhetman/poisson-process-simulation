#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
import math
import random

def brownDon(t, steps):
    Y= [0]
    T = t * steps
    root = np.sqrt(T)
    for i in range(T):
        Y.append(Y[-1] + np.random.normal(0, 1) * np.sqrt(i)/ root) # here we use the fact that random walk divided by square root of it's current number of steps converges to N(0,1)
    return Y
#    X = np.arange(0, t + steps, steps)                                               # so Yk/sigma*sqrt(n) = Yk*sqrt(k)/sigma*sqrt(n*k) = N(0,1)*sqrt(k)/sigma*sqrt(n)

def brownLevi(t, steps):
    Y= [0]
    T = steps * t
    for i in range(T):
        Y.append(Y[-1] + np.random.normal(0, i/T))
    return Y
#    X = np.arange(0, t + steps, steps)

def time_line(t, steps):
    steps = pow(steps, -1)
    X = np.arange(0, t + steps, steps)
    return X

def first_graphic(t, steps, X, Y):
    Y_1 = brownDon(t, steps)
    plt.plot(X, Y, c = 'red')
    plt.plot(X, Y_1, c = 'blue')
    plt.show()    
#    plt.xlabel('time')
#    plt.ylabel('W(t)')
#    plt.legend(['Donsker theorem', 'Levi simulation'], loc=2)
#    plt.suptitle('Brownian Motion', fontsize=25)

def second_graphic(t, steps): #check that plot lies within boundaries
    Y_1 = brownLevi(t, steps)
    X = time_line(t, steps)
    plt.plot(X, Y_1, c = 'green')
    Y_2 = [np.sqrt(2*k * np.log(np.log(k))) for k in X]
    Y_3 = [-np.sqrt(2*k * np.log(np.log(k))) for k in X]
    plt.plot(X, Y_2, c = 'blue')
    plt.plot(X, Y_3, c = 'blue') 
    plt.show()    
#   plt.xlabel('time')
#   plt.ylabel('W(t)')
#    plt.legend(['Levi simulation', 'Boundaries +- sqrt(2t*ln(ln(t))'], loc=2)
#    plt.suptitle('Law of the iterated logarithm ', fontsize=25)

def third_graphic(X, Y):
    a = 4
    b = 15
    Y_1 = [(a * x + b * y) for x, y in zip(X, Y)]
    plt.plot(X, Y_1, c = 'purple')  
    plt.show()    
#    plt.xlabel('time')
#    plt.ylabel('W(t)')
#    plt.suptitle('BM as a*t + b*W(t), a=' + str(a) + ' b=' + str(b), fontsize=25)

def main():
    steps = 1000 # how many steps we take per 1 unit of time. So for t=[0,1] we do this many iterations
    sig = 1
    Y = brownLevi(1, steps)
    X = time_line(1, steps)
    first_graphic(1, steps, X, Y)
    second_graphic(1000, steps)
    third_graphic(X, Y)

main()
