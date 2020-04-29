import graphic
import numpy as np

t_periods = np.array([(1, 5),
                    (4, 6),
                    (7, 11),
                    (14, 17),
                    (9, 19),
                    (4, 20),
                    (2, 23)])

#def certain_period(prev_sum, period):
#    while True:
#        new  = np.random.exponential(1 / period[0])
#   if prev_sum[-1] + new <= period[1]:  
#            prev_sum.append(prev_sum[-1] + new )
#        else:
#            prev_sum.append(period[1])
#            return prev_sum

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
            #t_sum = simulate_period(t_sum, period)
    return period_sum

def calc_properties():
    samples = []
    samples2 = []
    for _ in range(100):
        X = process_simulation()
        Y = range(len(X))
    
        for i, item in enumerate(X):
            if item > 14:
                samples.append(Y[i-1])
                break

        for i, item in enumerate(X):
            if item > 17:
                samples2.append(Y[i-1])
                break
    mean = np.mean(samples)
    var = np.mean([ pow(X - mean, 2) for X in samples])
    mean2 = np.mean(samples2)
    summary = 0
    for i in range(len(samples)): summary += ((samples[i] - mean) * (samples2[i] - mean2))
    cov = summary/(len(samples)-1)
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
