import numpy


def Zcalc(i, r):  # i angle d'incidence, r angle de reception
    if i < -60 or i > 60 or r < 20 or r > 340:
        print("Wrong angle values")
        return 0

    leafFile = "/Users/theo/Documents/INRA/Données/Mesures/2908/2908/feuille/type_txt/leaf"
    refFile = "/Users/theo/Documents/INRA/Données/Mesures/2908/2908/reference/type_txt/Ref"
    i2 = int((i / 10) - 1)
    r2 = int((r + 60) / 20)
    if i2 >= 10:
        leafFile = "a" + str(i2)
        refFile = "a" + str(i2)
    leafFile += str(i2)
    refFile += str(i2)
    leafData = numpy.loadtxt(leafFile + str(r2) + ".txt")
    refData = numpy.loadtxt(refFile + str(r2) + ".txt")
    lenData = numpy.loadtxt("/Users/theo/Documents/INRA/Données/Mesures/2908/2908/feuille/type_txt/Lambda.txt")

    for x in range(0, len(lenData)):
        if 655 <= lenData[x] <= 665:
            rc = leafData[x] / refData[x]
            print(rc)
        elif 725 <= lenData[x] <= 735:
            rs = leafData[x] / refData[x]
            print(rs)
