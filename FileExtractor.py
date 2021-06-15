import numpy
import os


# récupération des données de feuilles et interpolation + stockage dans des fichiers
def InterpData(rep, force=False):
    leafPath = "./Données/" + rep + "/feuille/type_txt/leaf"
    lenData = numpy.loadtxt("./Données/" + rep + "/feuille/type_txt/Lambda.txt")

    if not os.path.isdir("./Données/" + rep + "/feuille/type_txt/interpData/"):
        os.mkdir("./Données/" + rep + "/feuille/type_txt/interpData/")
    for i in range(1, 32, 1):
        for j in range(1, 8, 1):
            if not os.path.isfile("./Données/" + rep + "/feuille/type_txt/interpData/interpLeaf" + str(i) + str(
                    j) + ".txt") or force:
                if i < 10:
                    tmpData = numpy.loadtxt(leafPath + str(i) + str(j) + ".txt")
                else:
                    tmpData = numpy.loadtxt(leafPath + "a" + str(i) + str(j) + ".txt")
                tmpData = numpy.resize(tmpData, 1024)
                leaf = numpy.interp(numpy.arange(450, 900), lenData, tmpData)
                numpy.savetxt("./Données/" + rep + "/feuille/type_txt/interpData/interpLeaf" + str(i) + str(j) + ".txt",
                              leaf, "%6f")
            else:
                print("./Données/" + rep + "/feuille/type_txt/interpData/interpLeaf" + str(i) + str(
                    j) + ".txt existe déjà")


# récupération des données de ref et bruit, et interpolation + stockage dans des fichiers
def InterpRef(rep, force=False):
    nameData = ['', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
                'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                't', 'u', 'v', 'w', 'x', 'y', 'z', 'aa', 'ab', 'ac',
                'ad', 'ae', 'af', 'ag', 'ah', 'ai', 'aj', 'ak', 'al', 'am']
    k = nameData.index(rep[4:6])
    if k < 16:
        refPath1 = "./Données/" + rep[0:4] + nameData[k % 4] + "/reference/type_txt/Ref"
        refPath2 = "./Données/" + rep[0:4] + nameData[8 + (k % 4)] + "/reference/type_txt/Ref"
        bruPath = "./Données/Bruit/br" + rep[0:4] + "/type_txt/bru"
    else:
        refPath1 = "./Données/" + rep[0:4] + nameData[16 + (k % 4)] + "/reference/type_txt/Ref"
        refPath2 = "./Données/" + rep[0:4] + nameData[36 + (k % 4)] + "/reference/type_txt/Ref"
        bruPath = "./Données/Bruit/br" + rep[0:4] + "a/type_txt/bru"
    lenData = numpy.loadtxt("./Données/" + rep + "/feuille/type_txt/Lambda.txt")
    if not os.path.isdir("./Données/" + rep + "/reference/"):
        os.mkdir("./Données/" + rep + "/reference/")
        os.mkdir("./Données/" + rep + "/reference/type_txt/")
    if not os.path.isdir("./Données/" + rep + "/reference/type_txt/interpData/"):
        os.mkdir("./Données/" + rep + "/reference/type_txt/interpData/")
    for i in range(1, 15, 1):
        for j in range(1, 8, 1):

            if not os.path.isfile("./Données/" + rep + "/reference/type_txt/interpData/interpRef" + str(i) + str(
                    j) + ".txt") or not os.path.isfile(
                    "./Données/" + rep + "/reference/type_txt/interpData/interpBru" + str(i) + str(
                            j) + ".txt") or force:
                if i < 10:
                    tmpData1 = numpy.loadtxt(refPath1 + str(i) + str(j) + ".txt")
                    tmpData2 = numpy.loadtxt(refPath2 + str(i) + str(j) + ".txt")
                    bruData = numpy.loadtxt(bruPath + str(i) + str(j) + ".txt")
                else:
                    tmpData1 = numpy.loadtxt(refPath1 + "a" + str(i) + str(j) + ".txt")
                    tmpData2 = numpy.loadtxt(refPath2 + "a" + str(i) + str(j) + ".txt")
                    bruData = numpy.loadtxt(bruPath + "a" + str(i) + str(j) + ".txt")
                tmpData1 = numpy.resize(tmpData1, 1024)
                tmpData2 = numpy.resize(tmpData2, 1024)
                bruData = numpy.resize(bruData, 1024)
                data1 = numpy.interp(numpy.arange(450, 900), lenData, tmpData1)
                if i == 1 and j == 1:
                    toto = numpy.interp(numpy.arange(450, 900, 2), lenData, tmpData1)
                    for x in toto:
                        print(x)
                data2 = numpy.interp(numpy.arange(450, 900), lenData, tmpData2)
                bru = numpy.interp(numpy.arange(450, 900), lenData, bruData)
                data = []
                for d in range(0, data1.size):
                    data.append((data1[d] + data2[d]))
                numpy.savetxt(
                    "./Données/" + rep + "/reference/type_txt/interpData/interpRef" + str(i) + str(j) + ".txt",
                    data, "%6f")
                numpy.savetxt(
                    "./Données/" + rep + "/reference/type_txt/interpData/interpBru" + str(i) + str(j) + ".txt",
                    bru, "%6f")
            else:
                print("./Données/" + rep + "/reference/type_txt/interpData/interpBru" + str(i) + str(
                    j) + ".txt existe déjà")
