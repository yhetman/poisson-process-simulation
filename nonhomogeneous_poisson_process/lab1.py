import numpy as np
import matplotlib.pyplot as plt

times = [[1, 4],
            [3, 7],
            [8, 12],
            [15, 19],
            [10, 20],
            [5, 22],
            [3, 24]]

def process_simulation():
    sums = [0]
    for time_l, t_point in times:
        while 1:
            new = np.random.exponential(1 / time_l)
            if sums[-1] + new <= t_point:
                sums.append(sums[-1] + new)
            else:
                sums.append(t_point)
                break
    return sums


def loop_searching(X, Y, m, arr):
    for i, j in enumerate(X):
        if j > m:
            arr.append(Y[i - 1])
            return arr


def search_and_count():
    res_m = []
    res_m3 = []
    m = 3
    for _ in range(1000):
        X = process_simulation()
        Y = range(len(X))
        res_m = loop_searching(X, Y, m, res_m)
        res_m3 = loop_searching(X, Y, m + 3, res_m3)
    return [res_m, res_m3]


def main():
    results = search_and_count()
    mean = []
    var = []
    covariance = 0
    X = process_simulation()
    Y = range(len(X))
    for result in results:
        mean.append(np.mean(result))
    for every in results[0]:
        var.append((every - mean[0])**2)
    variance = np.mean(var)
    for every in range(len(results[0])):
        covariance += ((results[0][every] - mean[0]) * (results[1][every] - mean[1]))
    covariance /= (len(results[0])-1)
    print("Results at point t = :")
    print("Mean equals:" + str(mean[0]))
    print("Variance equals:"+ str(variance))
    print("Covariance for (N(t),N(t + 3)) equals:"  + str(covariance))
    plt.step(X, Y, c='blue')
    plt.show()


main()
