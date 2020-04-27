import matplotlib.pyplot as plt

def draw(x_ax, y_ax):
    
    fig, ax = plt.subplots()
    fig.set(facecolor = 'pink')
    ax.set(facecolor = 'pink')
    plt.title('Poisson Process',
        fontdict={ 'fontsize': 21},
        y=1.03, color='navy') 
    plt.step(x_ax, y_ax, c='indigo')
    plt.text(15, -2, "Done by YULIIA HETMAN", fontdict={'fontsize': 6})
    plt.show()

