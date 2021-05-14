import importlib
import matplotlib.pyplot as plt
import Zeta
import FileExtractor
import Plotting

importlib.reload(Zeta)
importlib.reload(FileExtractor)
importlib.reload(Plotting)
plt.rcParams.update({'figure.max_open_warning': 0})

# FileExtractor.InterpData("2908")

# Plotting.PlotGraph(450, "2908")
# Plotting.PlotGraph(550, "2908")
# Plotting.PlotGraph(650, "2908")
# Plotting.PlotGraph(750, "2908")

Plotting.PlotPolarGraph(450, "2908")
Plotting.PlotPolarGraph(550, "2908")
Plotting.PlotPolarGraph(660, "2908")
Plotting.PlotPolarGraph(730, "2908")
