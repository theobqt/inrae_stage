import numpy
import scipy.integrate
import os.path
import matplotlib.pyplot as plt


def FindZeta():
    for r in range(-60, 80, 20):
        plt.xlabel("Angle incident")
        plt.ylabel("Zeta")
        plt.title("Zeta = f(i)")
        zData = []
        for i in range(20, 330, 10):
            zData.append(Zcalc(i, r))
        plt.plot(numpy.arange(20, 330, 10), zData, label=str(r))
    plt.legend()
    plt.show()


def Zcalc(i, r):  # i angle d'incidence, r angle de reception
    if r < -60 or r > 60 or i < 20 or i > 340:
        print("Wrong angle values")
        return 0

    leafFile = "./Données/2908/feuille/type_txt/leaf"
    refFile = "./Données/2908/reference/type_txt/Ref"
    i2 = int((i / 10) - 1)
    r2 = int(((r + 60) / 20) + 1)
    if i2 >= 10:
        i2 = "a" + str(i2)
    leafFile += str(i2) + str(r2) + ".txt"
    refFile += str(i2) + str(r2) + ".txt"

    if os.path.isfile(leafFile) and os.path.isfile(refFile):
        leafData = numpy.loadtxt(leafFile)
        refData = numpy.loadtxt(refFile)
        lenData = numpy.loadtxt("./Données/2908/feuille/type_txt/Lambda.txt")
    else:
        return 0
    rcData = []
    rcLenData = []
    rsData = []
    rsLenData = []
    for x in range(0, len(lenData)):
        if 655 <= lenData[x] <= 665:
            rc = leafData[x] / refData[x]
            rcData.append(rc)
            rcLenData.append(lenData[x])
        elif 725 <= lenData[x] <= 735:
            rs = leafData[x] / refData[x]
            rsData.append(rs)
            rsLenData.append(lenData[x])
    zeta = Rcalc(rcLenData, rcData) / Rcalc(rsLenData, rsData)
    return zeta


def Rcalc(lenData, rData):
    iR = scipy.integrate.simps(rData, lenData)
    return iR / (lenData[-1] - lenData[0])


def RMeanCalc(rData):
    mR = numpy.mean(rData)
    return mR
