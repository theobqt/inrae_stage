import numpy
import scipy.integrate
from matplotlib import pyplot as plt

import DataClass
import Plotting


def Zeta(sp, alpha=None, beta=None, rep="2908"):
    if alpha is None and beta is None:
        rcSpec = SelectSpec(sp, 655, 665)
        rsSpec = SelectSpec(sp, 725, 735)
    else:
        rcSpec = SpecRefl(SelectSpec(sp, 655, 665), alpha, beta, rep)
        rsSpec = SpecRefl(SelectSpec(sp, 725, 735), alpha, beta, rep)
    rc = SumSp(rcSpec)
    rs = SumSp(rsSpec)
    z = rc / rs
    return z


def RC(sp, alpha=None, beta=None):
    if alpha is None and beta is None:
        rcSpec = SelectSpec(sp, 655, 665)
    else:
        rcSpec = SpecRefl(SelectSpec(sp, 655, 665), alpha, beta, "2908")
    rc = SumSp(rcSpec)
    return rc


def RS(sp, alpha=None, beta=None):
    if alpha is None and beta is None:
        rsSpec = SelectSpec(sp, 725, 735)
    else:
        rsSpec = SpecRefl(SelectSpec(sp, 725, 735), alpha, beta, "2908")
    rs = SumSp(rsSpec)
    return rs


def GraphZeta(sp, rep="2908"):
    alphas = list(range(-80, -10, 10))
    alphas.extend(range(20, 90, 10))
    betas = list(range(60, -80, -20))
    zetas = []
    xs = []
    ys = []
    for alpha in alphas:
        for beta in betas:
            theta = numpy.arccos(numpy.cos(numpy.deg2rad(alpha)) * numpy.cos(numpy.deg2rad(beta)))
            phi = numpy.arctan(numpy.sin(numpy.deg2rad(alpha)) * scipy.special.cotdg(beta))
            x = theta * numpy.cos(phi)
            y = theta * numpy.sin(phi)
            r = numpy.sqrt(x ** 2 + y ** 2)
            t = numpy.arctan2(y, x)
            if (t > 0 and alpha <= -20) or (t < 0 and 20 <= alpha):
                t += numpy.pi
            x = r * numpy.cos(t)
            y = r * numpy.sin(t)
            xs.append(x)
            ys.append(y)
            zetas.append(Zeta(sp, alpha, beta, rep=rep))

    Plotting.DrawPlot(xs, ys, zetas)
    Plotting.DrawDirections()
    plt.title("Zeta en fonction de l'angle de visée")
    plt.show()


def GraphRC(sp):
    alphas = list(range(-80, -10, 10))
    alphas.extend(range(20, 90, 10))
    betas = list(range(60, -80, -20))
    rc = []
    xs = []
    ys = []
    for alpha in alphas:
        for beta in betas:
            theta = numpy.arccos(numpy.cos(numpy.deg2rad(alpha)) * numpy.cos(numpy.deg2rad(beta)))
            phi = numpy.arctan(numpy.sin(numpy.deg2rad(alpha)) * scipy.special.cotdg(beta))
            x = theta * numpy.cos(phi)
            y = theta * numpy.sin(phi)
            r = numpy.sqrt(x ** 2 + y ** 2)
            t = numpy.arctan2(y, x)
            if (t > 0 and alpha <= -20) or (t < 0 and 20 <= alpha):
                t += numpy.pi
            x = r * numpy.cos(t)
            y = r * numpy.sin(t)
            xs.append(x)
            ys.append(y)
            rc.append(RC(sp, alpha, beta))
            if -80 <= alpha <= -20:
                plt.plot(x, y, "b.", alpha=0.6)
            elif 20 <= alpha <= 80:
                plt.plot(x, y, "r.", alpha=0.6)

    Plotting.DrawPlot(xs, ys, rc)
    plt.title("RC en fonction de l'angle de visée")
    plt.show()


def GraphRS(sp):
    alphas = list(range(-80, -10, 10))
    alphas.extend(range(20, 90, 10))
    betas = list(range(60, -80, -20))
    rs = []
    xs = []
    ys = []
    for alpha in alphas:
        for beta in betas:
            theta = numpy.arccos(numpy.cos(numpy.deg2rad(alpha)) * numpy.cos(numpy.deg2rad(beta)))
            phi = numpy.arctan(numpy.sin(numpy.deg2rad(alpha)) * scipy.special.cotdg(beta))
            x = theta * numpy.cos(phi)
            y = theta * numpy.sin(phi)
            r = numpy.sqrt(x ** 2 + y ** 2)
            t = numpy.arctan2(y, x)
            if (t > 0 and alpha <= -20) or (t < 0 and 20 <= alpha):
                t += numpy.pi
            x = r * numpy.cos(t)
            y = r * numpy.sin(t)
            xs.append(x)
            ys.append(y)
            rs.append(RS(sp, alpha, beta))
            if -80 <= alpha <= -20:
                plt.plot(x, y, "b.", alpha=0.6)
            elif 20 <= alpha <= 80:
                plt.plot(x, y, "r.", alpha=0.6)

    Plotting.DrawPlot(xs, ys, rs)
    plt.title("RS en fonction de l'angle de visée")
    plt.show()


# selectionne les donneées ud spectre pour lambda entre a et b inclus
def SelectSpec(sp, a, b):
    data = []
    for x in sp:
        if a <= x[0] <= b:
            data.append(x)
    return data


def SumSp(sp):
    return scipy.integrate.simpson([i[1] for i in sp], [i[0] for i in sp])


def SpecRefl(sp, alpha, beta, rep):
    data = []
    for x in sp:
        d = DataClass.Data(x[0], rep, alpha=alpha, beta=beta)
        if d.GetRefl() == 0:
            data.append([x[0], x[1]])
        else:
            data.append([x[0], x[1] * d.GetRefl()])
    return data
