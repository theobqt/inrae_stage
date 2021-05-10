import numpy


def ExtractData():
    leafFile = "./Données/2908/feuille/type_txt/leaf"
    refFile = "./Données/2908/reference/type_txt/Ref"
    lenData = numpy.loadtxt("./Données/2908/feuille/type_txt/Lambda.txt")
    leafData = numpy.zeros((31, 7), numpy.ndarray)
    tmpData = []
    for i in range(1, 32, 1):
        for j in range(1, 8, 1):
            if i < 10:
                tmpData = numpy.loadtxt(leafFile + str(i) + str(j) + ".txt")
            else:
                tmpData = numpy.loadtxt(leafFile + "a" + str(i) + str(j) + ".txt")
                leafData[i-1][j-1] = numpy.interp(numpy.arange(450, 900, 2), lenData, tmpData)
            numpy.savetxt("./Données/2908/feuille/type_txt/normalizedData/nLeaf" + str(i) + str(j) + ".txt", numpy.interp(numpy.arange(450, 900, 2), lenData, tmpData), "%6f")
