import graphic
import numpy as np

t_periods = np.array([(1, 4),
                    (3, 7),
                    (8, 12),
                    (15, 19),
                    (10, 20),
                    (5, 22),
                    (3, 24)])

def process_simulation():
    period_sum = [0]
    for lambd, end in t_periods:
        while True:
            new = np.random.exponential(1 / lambd)
            if period_sum[-1] + new <= end:
                period_sum.append(period_sum[-1] + new)
            else:
                period_sum.append(end)
                break
    return period_sum


def loop_searching(X, Y, m, arr):
    for index, every in enumerate(X):
        if every > m:
            arr.append(Y[index - 1])
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
    graphic.draw(X, Y)
    return [res_m, res_m3]


def count_means(results):
    mean = []
    for result in results:
        mean.append(np.mean(result))
    return mean


def count_variance(array, mean):
    var = []
    for every in array:
        var.append(pow(every - mean, 2))
    return (np.mean(var))


def count_covariance(length, arrs, means):
    covariance = 0
    for every in range(length):
        covariance += ((arrs[0][every] - means[0]) * (arrs[1][every] - means[1]))
    return (covariance /(length - 1))


def main():
    results = search_and_count()
    mean = count_means(results)
    print('\n\t->Results at point t = 3:\n')
    print('\t->Mean equals:\t|%.4f|\n' % mean[0])
    print('\t->Variance equals: |%.4f|\n'
            % count_variance(results[0], mean[0]))
    print('\t->Covariance for (N(t),N(t + 3)) equals: |%.4f|\n'
            % count_covariance(len(results[0]), results, mean))


main()
