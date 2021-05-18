import numpy
import scipy.special


class Data:
    rep = ""  # dossier contenant les données
    nLeaf = 0  # n feuille
    nLight = 0  # n eclairage
    lightAngle = 0  # angle eclairage
    i = 0  # n incidence
    r = 0  # n reception
    inc = 0  # angle d'incidence alpha en deg
    incRad = 0  # angle d'incidence en rad
    rec = 0  # angle reception beta en deg
    recRad = 0  # angle reception en rad
    azi = 0  # phi = acos(sin(inc) * cotan(rec))
    zen = 0  # theta = acos(cos(inc) * cos(rec))
    lam = 0  # longueur d'onde consideree
    leafData = 0  # données feuille pour conditions
    refData = 0  # données reference pour conditions

    def __init__(self, i, r, lam, rep):
        self.i = i
        self.r = r
        self.lam = lam
        self.rep = rep
        self.CalcNLightNLeaf()
        self.CalcAngle()
        self.FillData()

    def CalcNLightNLeaf(self):
        nameData = ['', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
                    'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                    't', 'u', 'v', 'w', 'x', 'y', 'z', 'aa', 'ab', 'ac',
                    'ad', 'ae', 'af', 'ag', 'ah', 'ai', 'aj', 'ak', 'al', 'am']
        k = nameData.index(self.rep[4:6])
        self.nLeaf = k / 4 + 1
        self.nLight = (k + 1) % 4
        self.lightAngle = (self.nLight - 1) * 20

    def CalcAngle(self):
        self.inc = self.i * 10 - 90
        self.rec = 80 - (self.r * 20)  # correct
        # conversion en radians
        self.incRad = numpy.deg2rad(self.inc)
        self.recRad = numpy.deg2rad(self.rec)
        # calcul azimut et zenith
        self.zen = numpy.arccos(numpy.cos(self.incRad) * numpy.cos(self.recRad))
        self.azi = numpy.arctan(numpy.sin(self.incRad) * scipy.special.cotdg(self.rec))

    def FillData(self):  # recuperation des donnees selon i r et lambda
        if -80 <= self.inc <= -20:
            tmpData = numpy.loadtxt(
                "./Données/" + self.rep + "/reference/type_txt/interpData/interpRef" + str(int(self.inc / 10 + 9)) + str(
                    self.r) + ".txt")
            self.refData = tmpData[int((self.lam - 450))] / 0.92
        elif 20 <= self.inc <= 80:
            tmpData = numpy.loadtxt(
                "./Données/" + self.rep + "/reference/type_txt/interpData/interpRef" + str(int(self.inc / 10 + 6)) + str(
                    self.r) + ".txt")
            self.refData = tmpData[int((self.lam - 450))] / 0.92
        elif 100 <= self.inc <= 160:
            tmpData = numpy.loadtxt(
                "./Données/" + self.rep + "/reference/type_txt/interpData/interpRef" + str(int(24 - self.inc / 10)) + str(
                    self.r) + ".txt")
            self.refData = tmpData[int((self.lam - 450))] / 0.92
        elif 200 <= self.inc <= 260:
            tmpData = numpy.loadtxt(
                "./Données/" + self.rep + "/reference/type_txt/interpData/interpRef" + str(int(27 - self.inc / 10)) + str(
                    self.r) + ".txt")
            self.refData = tmpData[int((self.lam - 450))] / 0.92
        else:
            self.refData = 0

        if -80 <= self.inc <= -20:
            tmpData = numpy.loadtxt(
                "./Données/" + self.rep + "/feuille/type_txt/interpData/interpLeaf" + str(int(self.inc / 10 + 9)) + str(
                    self.r) + ".txt")
            self.leafData = tmpData[int((self.lam - 450))] / 2
        elif 20 <= self.inc <= 80:
            tmpData = numpy.loadtxt(
                "./Données/" + self.rep + "/feuille/type_txt/interpData/interpLeaf" + str(int(self.inc / 10 + 6)) + str(
                    self.r) + ".txt")
            self.leafData = tmpData[int((self.lam - 450))] / 2
        elif 100 <= self.inc <= 260:
            tmpData = numpy.loadtxt(
                "./Données/" + self.rep + "/feuille/type_txt/interpData/interpLeaf" + str(int(self.inc / 10 + 5)) + str(
                    self.r) + ".txt")
            self.leafData = tmpData[int((self.lam - 450))] / 2
        else:
            self.leafData = 0
