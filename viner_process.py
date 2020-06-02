import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import math
import random

n = 1000 # how many steps we take per 1 unit of time. So for t=[0,1] we do this many iterations
sig = 1


def Brownian_Donsker(time):
    process = [0]
    bot = np.sqrt(time*n)
    for k in range(n*time):
        process.append(process[-1] + np.random.normal(0, 1)*np.sqrt(k)/bot) # here we use the fact that random walk divided by square root of it's current number of steps converges to N(0,1)
    x = np.arange(0, time+1/n, 1/n)                                               # so Yk/sigma*sqrt(n) = Yk*sqrt(k)/sigma*sqrt(n*k) = N(0,1)*sqrt(k)/sigma*sqrt(n)
    return process, x

def Brownian_Levi(time):
    process = [0]
    total_time = n*time
    for k in range(n*time):
        process.append(process[-1] + np.random.normal(0, k/total_time))
    x = np.arange(0, time+1/n, 1/n)
    return process, x


def plot_one():
    y1, x1 = Brownian_Donsker(1)
    y2, x2 = Brownian_Levi(1)
    sns.set()
    plt.plot(x1,y1, c='#7a0505')
    plt.plot(x2,y2, c='#1d6f72')
    plt.xlabel('time')
    plt.ylabel('W(t)')
    plt.legend(['Donsker theorem', 'Levi simulation'], loc=2)
    plt.suptitle('Brownian Motion', fontsize=25)
    plt.show()

def plot_two(): #check that plot lies within boundaries
    y, x = Brownian_Levi(1000)
    plt.plot(x,y, c='#7a0505')
    y1 = [np.sqrt(2*t * np.log(np.log(t))) for t in x]
    y2 = [-np.sqrt(2*t * np.log(np.log(t))) for t in x]
    sns.set()
    plt.plot(x,y1, c='#1d6f72')
    plt.plot(x,y2, c='#1d6f72') 
    plt.xlabel('time')
    plt.ylabel('W(t)')
    plt.legend(['Levi simulation', 'Boundaries +- sqrt(2t*ln(ln(t))'], loc=2)
    plt.suptitle('Law of the iterated logarithm ', fontsize=25)
    plt.show()    

def plot_three():
    y, x = Brownian_Levi(1)
    a = 4
    b = 15
    y1 = [(a*t + b*W) for t, W  in zip(x, y)]
    sns.set()
    plt.plot(x,y1, c='#1d6f72')  
    plt.xlabel('time')
    plt.ylabel('W(t)')
    plt.suptitle('BM as a*t + b*W(t), a=' + str(a) + ' b=' + str(b), fontsize=25)
    plt.show()    

plot_one()
plot_two()
plot_three()
