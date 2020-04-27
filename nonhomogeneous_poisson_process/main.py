import graphic
import numpy as np

l_array = np.array([[1, 5],
                    [4, 6],
                    [7, 11],
                    [14, 17],
                    [9, 19],
                    [4, 20],
                    [2, 23]])

def simulate_period(previous_t, lam_t):
    cumsum = previous_t 
    while True:
        new_elmnt = np.random.exponential( 1/lam_t[0] )
        if cumsum[-1] + new_elmnt <= lam_t[1]:  
            cumsum.append(cumsum[-1] + new_elmnt)
        else:
            cumsum.append(lam_t[1])
            return cumsum

def process_simulation():
    t_sum = [0]
    for period in l_array:
        t_sum = simulate_period(t_sum, period)
    return t_sum

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
    return [mean, var, cov]


def main():
    X = process_simulation()
    Y = range(len(X))
    graphic.draw(X, Y)
    properties = calc_properties()
    print('For t = 14: ')
    print('Mean is %.4f' % properties[0])
    print('Variance is %.4f ' % properties[1])
    print('Covariance for N(14) and N(17) is %.4f' % properties[2], '\n')

main()
