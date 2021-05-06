import importlib
import matplotlib.pyplot as plt
import numpy

import Zeta

importlib.reload(Zeta)
plt.rcParams.update({'figure.max_open_warning': 0})

for r in range(-60, 80, 20):
    plt.xlabel("Angle")
    plt.ylabel("Zeta")
    plt.title("Zeta = f(i)")
    zData = []
    for i in range(20, 330, 10):
        zData.append(Zeta.Zcalc(i, r))
    plt.plot(numpy.arange(20, 330, 10), zData, label=str(r))
plt.legend()
plt.show()
