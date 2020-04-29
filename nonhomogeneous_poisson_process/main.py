import graphic
import numpy as np

t_periods = np.array([(1, 5),
                    (4, 6),
                    (7, 11),
                    (12, 16),
                    (14, 17),
                    (9, 19),
                    (4, 20),
                    (2, 23)])

def process_simulation():
    period_sum = [0]
    for start, end in t_periods:
        while True:
            new = np.random.exponential(1 / start)
            if period_sum[-1] + new <= end:
                period_sum.append(period_sum[-1] + new)
            else:
                period_sum.append(end)
                break
    return period_sum


def loop_searching(X, Y, numb, arr):
    for index, every in enumerate(X):
        if every > numb:
            arr.append(Y[index - 1])
            return arr


def search_and_count():
    res_14 = []
    res_17 = []
    for _ in np.arange(0,1000):
        X = process_simulation()
        Y = range(len(X))
        res_14 = loop_searching(X, Y, 14, res_14)
        res_17 = loop_searching(X, Y, 17, res_17)
    graphic.draw(X, Y)
    return [res_14, res_17]


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
    print('\t->Results at point t = 14: ')
    print('\t->Mean equals:\t|%.4f|\n' % mean[0])
    print('\t->Variance equals:\t|%.4f|\n' % count_variance(results[0], mean[0]))
    print('\t->Covariance for N(14) and N(17) equals: |%.4f|\n' % count_covariance(len(results[0]), results, mean))


main()
