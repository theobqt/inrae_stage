import importlib

import numpy
import matplotlib.pyplot as plt
import Zeta
importlib.reload(Zeta)
plt.rcParams.update({'figure.max_open_warning': 0})

Zeta.Zcalc(40, 20)

# numpy.loadtxt("/Users/theo/Documents/INRA/Données/Mesures/2908/2908/feuille/type_txt/leaf11.txt", float)
# numpy.loadtxt("/Users/theo/Documents/INRA/Données/Mesures/2908/2908/feuille/type_txt/Lambda.txt")
# ampData = []
# lenData = numpy.loadtxt("/Users/theo/Documents/INRA/Données/Mesures/2908/2908/feuille/type_txt/Lambda.txt")

# for i in range(1, 8):
#     fig = plt.figure()
#     subplot = fig.add_subplot()
#     subplot.set_xlabel("Longueur d'onde")
#     subplot.set_ylabel("Amplitude")
#     subplot.set_title("Angle récepteur : " + str(60 - (i - 1)*20))
#
#     for j in range(1, 32):
#         fileName = "/Users/theo/Documents/INRA/Données/Mesures/2908/2908/feuille/type_txt/leaf"
#         if j >= 10:
#             fileName += "a" + str(j)
#         else:
#             fileName += str(j)
#         ampData = numpy.loadtxt(fileName + str(i) + ".txt")
#         subplot.plot(lenData, ampData)
#     plt.show()
