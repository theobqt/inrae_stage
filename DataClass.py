import numpy
import scipy.special


class Data:
    rep = ""  # dossier contenant les données
    nLeaf = 0  # n feuille
    nLight = 0  # n eclairage
    lightAngle = 0  # angle eclairage
    i = 0  # n incidence
    r = 0  # n reception
    alpha = 0  # angle d'incidence alpha en deg
    alphaRad = 0  # angle d'incidence en rad
    beta = 0  # angle reception beta en deg
    betaRad = 0  # angle reception en rad
    phi = 0  # phi = acos(sin(inc) * cotan(rec))  azimut
    theta = 0  # theta = acos(cos(inc) * cos(rec))  zenithal
    x = 0  # position x en cartesien
    y = 0  # position y en cartesien
    t = 0  # position angulaire en polaire
    rayon = 0  # rayon en polaire
    lam = 0  # longueur d'onde consideree
    leafData = 0  # données feuille pour conditions
    refData = 0  # données reference pour conditions
    bruData = 0  # données bruit pour conditions

    def __init__(self, lam, rep, i=None, r=None, alpha=None, beta=None):
        if i is not None and r is not None:
            self.i = i
            self.r = r
            self.CalcAngle()
        else:
            self.alpha = alpha
            self.beta = beta
            self.CalcAngle2()
        self.CalcPos()
        self.lam = lam
        self.rep = rep
        self.CalcNLightNLeaf()
        self.FillRefData()
        self.FillLeafData()

    def CalcNLightNLeaf(self):
        nameData = ['', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
                    'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                    't', 'u', 'v', 'w', 'x', 'y', 'z', 'aa', 'ab', 'ac',
                    'ad', 'ae', 'af', 'ag', 'ah', 'ai', 'aj', 'ak', 'al', 'am']

        k = nameData.index(self.rep[4:6])
        self.nLeaf = int(numpy.ceil((k + 1) / 4))
        self.nLight = k % 4
        self.lightAngle = self.nLight * 20

    def CalcAngle(self):
        if self.i <= 18:
            self.alpha = self.i * 10
        else:
            self.alpha = self.i * 10 - 360
        self.beta = 80 - (self.r * 20)  # correct
        # conversion en radians
        self.alphaRad = numpy.deg2rad(self.alpha)
        self.betaRad = numpy.deg2rad(self.beta)
        # calcul theta et phi
        self.theta = numpy.arccos(numpy.cos(self.alphaRad) * numpy.cos(self.betaRad))
        self.phi = numpy.arctan(numpy.sin(self.alphaRad) * scipy.special.cotdg(self.beta))
        if numpy.isnan(self.phi):
            self.phi = 0

    def CalcAngle2(self):
        if self.alpha <= 180:
            self.i = self.alpha / 10
        else:
            self.i = (self.alpha - 360) / 10
        self.r = int((80 - self.beta) / 20)  # correct
        # conversion en radians
        self.alphaRad = numpy.deg2rad(self.alpha)
        self.betaRad = numpy.deg2rad(self.beta)
        # calcul theta et phi
        self.theta = numpy.arccos(numpy.cos(self.alphaRad) * numpy.cos(self.betaRad))
        self.phi = numpy.arctan(numpy.sin(self.alphaRad) * scipy.special.cotdg(self.beta))
        if numpy.isnan(self.phi):
            self.phi = 0

    def CalcPos(self):
        self.x = self.theta * numpy.cos(self.phi)
        self.y = self.theta * numpy.sin(self.phi)
        self.rayon = numpy.sqrt(self.x ** 2 + self.y ** 2)
        self.t = numpy.arctan2(self.y, self.x)
        if (self.t > 0 and self.alpha <= -20) or (self.t < 0 and 20 <= self.alpha):
            self.t += numpy.pi
        self.x = self.rayon * numpy.cos(self.t)
        self.y = self.rayon * numpy.sin(self.t)

    def FillRefData(self):  # recuperation des donnees selon i r et lambda
        index = 0
        if 20 <= self.alpha <= 80:
            index = str(int(self.alpha / 10 + 6))
        elif 100 <= self.alpha <= 160:
            index = str(int(24 - self.alpha / 10))
        elif -160 <= self.alpha <= -100:
            index = str(int(- self.alpha / 10 - 9))
        elif -80 <= self.alpha <= -20:
            index = str(int(9 + self.alpha / 10))
        if index == 0:
            self.refData = 0
        else:
            tmpData = numpy.loadtxt(
                "./Données/" + self.rep + "/reference/type_txt/interpData/interpRef" + index + str(self.r) + ".txt")
            bruData = numpy.loadtxt(
                "./Données/" + self.rep + "/reference/type_txt/interpData/interpBru" + index + str(self.r) + ".txt")
            self.bruData = bruData[int((self.lam - 450))]
            self.refData = (tmpData[int((self.lam - 450))] - self.bruData) / 0.92

    def FillLeafData(self):
        index = 0
        if 20 <= self.alpha <= 80:
            index = str(int(self.alpha / 10 - 1))
        elif 100 <= self.alpha <= 180:
            index = str(int(self.alpha / 10 - 2))
        elif -170 <= self.alpha <= -100:
            index = str(int(34 + self.alpha / 10))
        elif -80 <= self.alpha <= -20:
            index = str(int(33 + self.alpha / 10))
        if index == 0:
            self.leafData = 0
        else:
            tmpData = numpy.loadtxt(
                "./Données/" + self.rep + "/feuille/type_txt/interpData/interpLeaf" + index + str(
                    self.r) + ".txt")
            self.leafData = (tmpData[int((self.lam - 450))] - self.bruData) / 2

    def GetRefl(self):
        if self.refData != 0:
            return self.leafData / self.refData
        else:
            return 0
