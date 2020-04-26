import matplotlib.pyplot as plt
import numpy as np
import math
import graphic as graph

n = 100
lambd = 3
steps = 30
counter = 0
coeff = 1 / n
array = []

t = np.arange(0, steps, coeff)
for _ in range(pow(n, 2)):
    x = np.cumsum(np.random.poisson(lambd * coeff, steps * n))
    array.append(x[n * 10])
    if x[3 * n] == 3 * lambd  and x[10 * n] == 9 * lambd:
        if x[15 * n] > 14 * lambd:
            counter += 1

print("\t==> Average value is |%.4f|" % (np.mean(array)))
print("\t==> for lambda equals |%.1f| :" % (lambd))
print("\t==> P{N(3) = 3 * lambda, N(10) = 9 * lambda, N(15) > 14 * lambda} = |%.4f|" % (counter / pow(n, 2)))
print("\t|| Done by YULIIA HETMAN :) ||")
graph.draw_graphic(t, x)
