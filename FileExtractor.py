import numpy
import os


def InterpData(rep):
    leafPath = "./Données/" + rep + "/feuille/type_txt/leaf"
    refPath = "./Données/" + rep + "/reference/type_txt/Ref"
    lenData = numpy.loadtxt("./Données/2908/feuille/type_txt/Lambda.txt")

    if not os.path.isdir("./Données/" + rep + "/reference/type_txt/interpData/"):
        os.mkdir("./Données/" + rep + "/reference/type_txt/interpData/")
    if not os.path.isdir("./Données/" + rep + "/feuille/type_txt/interpData/"):
        os.mkdir("./Données/" + rep + "/feuille/type_txt/interpData/")
    for i in range(1, 32, 1):
        for j in range(1, 8, 1):
            if i < 10:
                tmpData = numpy.loadtxt(leafPath + str(i) + str(j) + ".txt")
            else:
                tmpData = numpy.loadtxt(leafPath + "a" + str(i) + str(j) + ".txt")
            numpy.savetxt("./Données/" + rep + "/feuille/type_txt/interpData/interpLeaf" + str(i) + str(j) + ".txt",
                          numpy.interp(numpy.arange(450, 900), lenData, tmpData), "%6f")
    for i in range(1, 15, 1):
        for j in range(1, 8, 1):
            if i < 10:
                tmpData = numpy.loadtxt(refPath + str(i) + str(j) + ".txt")
            else:
                tmpData = numpy.loadtxt(refPath + "a" + str(i) + str(j) + ".txt")
            numpy.savetxt("./Données/" + rep + "/reference/type_txt/interpData/interpRef" + str(i) + str(j) + ".txt",
                          numpy.interp(numpy.arange(450, 900), lenData, tmpData), "%6f")
