import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import math

Lambdas = [[1, 4], [3, 7], [8, 12], [15, 19], [10, 20], [5, 22], [3, 24]] #Pairs of lambda values and ends of their time periods 


# Simulates homogenous poisson process with certain rate and up to a certain point of time.
# Rate and stop time are set using the lam_t argument which should be a list with 2 elements.
# Argument cumsum passes all the values during previous periods of time.
def simulate_period(previous_t, lam_t):
    cumsum = previous_t 
    while True:
        new_elmnt = np.random.exponential( 1/lam_t[0] )
        if cumsum[-1] + new_elmnt <= lam_t[1]:  # because we will almost certainly never get our exact end of time period value, we just take the closest one that is less or equal to it
            cumsum.append(cumsum[-1] + new_elmnt)
        else:
            cumsum.append(lam_t[1]) # then we add the desired end of time period manually
            return cumsum

def simulate(): # simulates inhomogenous poisson process for lambda and time period given above (Lambdas variable)
    t_sum = [0]
    for period in Lambdas:
        t_sum = simulate_period(t_sum, period)
    return t_sum

def plot_process(process):
    sns.set()
    x = process
    y = np.arange(0, len(process))
    plt.step(x,y, c='crimson')
    plt.xlabel('time')
    plt.ylabel('process')
    plt.suptitle('Nonhomogenous Pоisson Process', fontsize=25)
    plt.show()

def calc_properties(): # calculates mean, var, cov for t = 14
    samples = []
    samples2 = []
    for _ in range(100):
        x = simulate()
        y = np.arange(0, len(x))
    
        for i, item in enumerate(x): #find first element greater than 14 and pass index of previous element to samples
            if item > 14:
                samples.append(y[i-1])
                break

        for i, item in enumerate(x): #find first element greater than 17 and pass index of previous element to samples2
            if item > 17:
                samples2.append(y[i-1])
                break
    # here numpy functions for calculating var and cov should be used, but for the sake of the assignment I do it manually here
    mean = np.mean(samples)

    var = np.mean([ (x - mean)**2 for x in samples])

    mean2 = np.mean(samples2)
    sum = 0
    for i in range(len(samples)):
        sum += ((samples[i] - mean)*(samples2[i] - mean2))
    cov = sum/(len(samples)-1)

    return [mean, var, cov]





if __name__ == "__main__":
    plot_process(simulate())  
    properties = calc_properties()
    print('For t = 14: ')
    print('Mean is ' + str(properties[0]))
    print('Variance is ' + str(properties[1]))
    print('Covariance for N(14) and N(17) is ' + str(properties[2]))
    print('')
