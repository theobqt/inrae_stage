import importlib
import matplotlib.pyplot as plt
import numpy
import matplotlib.cm as cm
import DataClass

importlib.reload(DataClass)

numpy.set_printoptions(suppress=True)


def PlotGraph(lam, rep):  # graph 2D rectangulaire de la reflectance suivant i et r
    data = GetData(lam, rep)

    fig, ax = plt.subplots()
    ax.imshow(data, interpolation='bilinear', cmap=cm.plasma, extent=[-60, 60, 20, 330])
    plt.xlabel("Angle reception")
    plt.ylabel("Angle incident")
    plt.title("Reflectance en fonction des angles pour l = " + str(lam))
    plt.show()


def PlotPolarGraph(lam, rep):
    data = GetData(lam, rep)
    refl = numpy.zeros((7, 37), numpy.float)
    zen = []
    for i in range(0, 37, 1):
        zen.append(data[i][0].zen)
        for j in range(0, 7, 1):
            if data[i][j].refData != 0:
                refl[j][i] = data[i][j].leafData / data[i][j].refData
            else:
                refl[j][i] = 0

    fig, ax = plt.subplots(subplot_kw=dict(projection='polar'))
    ax.contourf(numpy.arange(numpy.deg2rad(-90), numpy.deg2rad(280), numpy.deg2rad(10)), numpy.arange(-60, 80, 20), refl)
    plt.title("Reflectance en fonction des angles pour l = " + str(lam))
    plt.show()
    print(zen)


def GetData(lam, rep):
    data = numpy.zeros((37, 7), DataClass.Data)

    for i in range(0, 37, 1):
        for j in range(1, 8, 1):
            data[i][j - 1] = DataClass.Data(i, j, lam, rep)
    return data


def PlotRefl(lam, rep):
    data = GetData(lam, rep)
    plt.axes(polar=True)
    for i in range(0, 37, 1):
        for j in range(0, 7, 1):
            if -80 <= data[i][j].inc <= -20:
                x = data[i][j].zen * numpy.cos(data[i][j].azi)
                y = data[i][j].zen * numpy.sin(data[i][j].azi)
                r = numpy.sqrt(x ** 2 + y ** 2)
                t = numpy.arctan2(y, x)
                plt.plot(t, r, "r.", alpha=0.6)
            if 20 <= data[i][j].inc <= 80:
                x = data[i][j].zen * numpy.cos(numpy.pi + data[i][j].azi)
                y = data[i][j].zen * numpy.sin(data[i][j].azi)
                r = numpy.sqrt(x ** 2 + y ** 2)
                t = numpy.arctan2(y, x)
                plt.plot(t, r, "g.", alpha=0.6)
    plt.show()
