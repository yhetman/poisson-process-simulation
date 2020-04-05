import numpy as np
import matplotlib.pyplot as plt
 
# Prepare data
N = 20 # step
lambdas = [3, 15, 1]
X_T = [np.random.poisson(lam, size=N) for lam in lambdas]
S = [[np.sum(X[0:i]) for i in range(N)] for X in X_T]
X = np.linspace(0, N, N)
  
# Plot the graph
graphs = [plt.step(X, S[i], label="Lambda = %d"%lambdas[i])[0]
        for i in range(len(lambdas))]
plt.legend(handles=graphs, loc=2)
plt.title("Poisson Process", fontdict={'fontname': 'Times New Roman', 'fontsize': 21}, y=1.03)
plt.ylim(0)
plt.xlim(0)
plt.show()
