import importlib
import matplotlib.pyplot as plt
import Zeta
import FileExtractor

importlib.reload(Zeta)
importlib.reload(FileExtractor)
plt.rcParams.update({'figure.max_open_warning': 0})

FileExtractor.ExtractData()