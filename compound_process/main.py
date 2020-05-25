#!/usr/bin/env python3

import graphic
import numpy as np

def count_probability(spnd, m):
    p = 0.0
    for i in spnd:
        if i >= 2000 * m:
            p += 1
    return (p / len(spnd))

def count_variance(spnd, mean):
    var = []
    for i in spnd:
        var.append((i - mean)**2)
    return (np.mean(var))

def monte_carlo(iterations, m):
    poisson = []
    spendings = []
    for _ in range(iterations):
        pois = [0]
        while pois[-1] <= m:
            pois.append(pois[-1] + np.random.exponential(0.04))
        length = len(pois)
        poisson.append(length - 1)
        spendings.append(sum(np.random.uniform(5, 95, length - 1)))
    sum_uni = np.cumsum(np.random.uniform(5, 95, length))
    #graphic.draw(sum_uni, pois)
    return spendings

def main(m):
    iterations = 10000
    spnd = monte_carlo(iterations, m)
    spnd_mean = np.mean(spnd)
    spnd_variance = count_variance(spnd, spnd_mean)
    spnd_stdev = np.sqrt(spnd_variance)
    probability = count_probability(spnd, m)
    print("<=======================> RESULTS <=======================>")
    print("<====== %d iterations were made" % iterations)
    print("<====== For m = %d" % m)
    print("<====== Mean equals : %f" % spnd_mean)
    print("<====== Variance equals : %f" % spnd_variance)
    print("<====== Standard deviation equals : %f" % spnd_stdev)
    print("<====== Probability that more than %d will be spent : %f" % (2000 * m, probability))

main(3)
