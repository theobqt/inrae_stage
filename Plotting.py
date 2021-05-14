import matplotlib.pyplot as plt
import numpy
import matplotlib.cm as cm

numpy.set_printoptions(suppress=True)


def PlotGraph(lam, rep):
    data = FindRefl(lam, rep)

    fig, ax = plt.subplots()
    ax.imshow(data, interpolation='bilinear', cmap=cm.plasma, extent=[-60, 60, 20, 330])
    plt.xlabel("Angle reception")
    plt.ylabel("Angle incident")
    plt.title("Reflectance en fonction des angles pour l = " + str(lam))
    plt.show()


def PlotPolarGraph(lam, rep):
    data = FindRefl(lam, rep)
    rad = 2 * numpy.pi / 360
    # ax = plt.subplot(projection='polar')
    # ax.set_rmax(7)
    # ax.set_rticks([1, 2, 3, 4, 5, 6, 7])  # Less radial ticks
    # ax.set_rlabel_position(0)  # Move radial labels away from plotted line
    # ax.grid(True)
    # ax.set_title("A line plot on a polar axis")

    fig, ax = plt.subplots(subplot_kw=dict(projection='polar'))
    ax.contourf(numpy.arange(0 * rad, 370 * rad, 10 * rad), numpy.arange(-60, 80, 20), data)
    plt.title("Reflectance en fonction des angles pour l = " + str(lam))
    plt.show()


def FindRefl(lam, rep):
    refData = numpy.zeros((28, 7), numpy.float)
    data = numpy.zeros((7, 37), numpy.float)
    for j in range(1, 8, 1):
        for i in range(1, 29, 1):
            if i < 15:
                tmpData = numpy.loadtxt(
                    "./Données/" + rep + "/reference/type_txt/interpData/interpRef" + str(i) + str(j) + ".txt")
                refData[i - 1][j - 1] = tmpData[int((lam - 450))] / 0.92
            else:
                tmpData = numpy.loadtxt(
                    "./Données/" + rep + "/reference/type_txt/interpData/interpRef" + str(29 - i) + str(j) + ".txt")
                refData[i - 1][j - 1] = tmpData[int((lam - 450))] / 0.92

    for j in range(1, 8, 1):
        for i in range(0, 37, 1):
            if 2 <= i < 16 and refData[i][j - 1] != 0:
                tmpData = numpy.loadtxt(
                "./Données/" + rep + "/feuille/type_txt/interpData/interpLeaf" + str(i+1) + str(j) + ".txt")
                data[7 - j][i] = tmpData[int((lam - 450))] / (refData[i - 1][j - 1] * 2)
            elif 20 <= i < 34 and refData[i - 6][j - 1] != 0:
                tmpData = numpy.loadtxt(
                "./Données/" + rep + "/feuille/type_txt/interpData/interpLeaf" + str(i-3) + str(j) + ".txt")
                data[7 - j][i] = tmpData[int((lam - 450))] / (refData[i - 6][j - 1] * 2)
            else:
                data[7 - j][i] = 0
    # print(data)
    return data
