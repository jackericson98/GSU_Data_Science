import matplotlib.pyplot as plt
import numpy as np

periods = 3
colors = ['r', 'g']

for i in range(periods*2):

    x1data = np.linspace(-5*np.pi/2, -3*np.pi/2, 100) + i*np.pi  # 3 periods for 2sin(x)
    x2data = x1data - np.pi/2  # 3 periods for 2cos(x)

    y1data = 2*np.sin(x1data)  # y data for 2sin(x)
    y2data = 2*np.cos(x2data)  # y data for 2cos(x)

    plt.plot(x1data, y1data, c=colors[i % 2])
    plt.plot(x2data, y2data, linestyle='dashed', c=colors[i % 2])


plt.ylim([-4, 4])
plt.xlabel("X", fontsize=15)
plt.ylabel("Y", fontsize=15)
plt.legend(("2sin(x)", "2cos(x)"))
plt.grid()

plt.show()
