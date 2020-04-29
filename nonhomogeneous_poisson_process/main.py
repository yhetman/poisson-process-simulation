import graphic
import numpy as np

t_periods = np.array([(1, 5),
                    (4, 6),
                    (7, 11),
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


def calc_properties():
    res_14 = []
    res_17 = []
    for _ in range(100):
        X = process_simulation()
        Y = range(len(X))
        res_14 = loop_searching(X, Y, 14, res_14)
        res_17 = loop_searching(X, Y, 17, res_17)
    mean = np.mean(res_14)
    var = np.mean([ pow(i - mean, 2) for i in res_14])
    mean2 = np.mean(res_17)
    summary = 0
    for i in range(len(res_14)): summary += ((res_14[i] - mean) * (res_17[i] - mean2))
    cov = summary/(len(res_14) - 1)
    graphic.draw(X, Y)
    return [mean, var, cov]


def main():
    #X = process_simulation()
    #Y = range(len(X))
    #graphic.draw(X, Y)
    properties = calc_properties()
    print('For t = 14: ')
    print('Mean is %.4f' % properties[0])
    print('Variance is %.4f ' % properties[1])
    print('Covariance for N(14) and N(17) is %.4f' % properties[2], '\n')

main()
