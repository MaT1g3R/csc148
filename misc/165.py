import matplotlib.pyplot as plt
from numpy import polyfit, log

def my_sum(lst):
    x = 0
    y = 1
    n = len(lst)
    i = 0
    iters = 0
    while x + y < n:
        iters += 1
        if lst[i] % 2 == 0:
            y += 1
        else:
            x += y
        i += 1
    return iters

if __name__ == '__main__':
    xaxis = []
    yaxis = []
    for i in range(1, 1000):
        xaxis.append(i)
        yaxis.append(my_sum([n for n in range(i)]))
    plt.plot(xaxis, yaxis)
    plt.savefig('myplot.png')

    print(polyfit(log(xaxis), yaxis, 1))