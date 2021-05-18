import importlib
import matplotlib.pyplot as plt
import Zeta
import FileExtractor
import Plotting
import DataClass

importlib.reload(Zeta)
importlib.reload(FileExtractor)
importlib.reload(Plotting)
importlib.reload(DataClass)
plt.rcParams.update({'figure.max_open_warning': 0})

# FileExtractor.InterpData("2908a")
# FileExtractor.InterpData("2908b")
# FileExtractor.InterpData("2908c")


# Plotting.PlotGraph(450, "2908")
# Plotting.PlotGraph(550, "2908")
# Plotting.PlotGraph(650, "2908")
# Plotting.PlotGraph(750, "2908")

# Plotting.PlotPolarGraph(450, "2908")
# Plotting.PlotPolarGraph(550, "2908")
# Plotting.PlotPolarGraph(660, "2908")
# Plotting.PlotPolarGraph(730, "2908")

Plotting.PlotRefl(450, "2908")
# Plotting.PlotRefl(550, "2908")
# Plotting.PlotRefl(650, "2908")
# Plotting.PlotRefl(750, "2908")
