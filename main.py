import importlib
import matplotlib.pyplot as plt
import Zeta
import FileExtractor
import Plotting
import DataClass
import numpy

importlib.reload(Zeta)
importlib.reload(FileExtractor)
importlib.reload(Plotting)
importlib.reload(DataClass)
plt.rcParams.update({'figure.max_open_warning': 0})

# nameData = ['', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
#             'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
#             't', 'u', 'v', 'w', 'x', 'y', 'z', 'aa', 'ab', 'ac',
#             'ad', 'ae', 'af', 'ag', 'ah', 'ai', 'aj', 'ak', 'al', 'am']
# for n in nameData:
#     FileExtractor.InterpData("2908" + n)
#     FileExtractor.InterpRef("2908" + n, force=True)

Plotting.PlotRefl(450, "2908")
# Plotting.PlotRefl(550, "2908")
# Plotting.PlotRefl(660, "2908")
# Plotting.PlotRefl(730, "2908")

# sp = numpy.loadtxt("./Données/Soleil1nm.txt")
#
# Zeta.GraphZeta(sp)
