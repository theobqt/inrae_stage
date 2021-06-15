import importlib
import matplotlib.pyplot as plt
import numpy
import scipy
from scipy.interpolate import griddata
import DataClass

importlib.reload(DataClass)
numpy.set_printoptions(suppress=True)


def GetData(lam, rep):
    data = numpy.zeros((36, 7), DataClass.Data)

    for i in range(0, 36, 1):
        for j in range(1, 8, 1):
            data[i][j - 1] = DataClass.Data(lam, rep, i=i, r=j)
    return data


def PlotRefl(lam, rep):
    alphaValues = list(range(-80, -10, 10))
    alphaValues.extend(range(20, 90, 10))
    alphas = list(range(-80, 90, 10))
    betas = list(range(60, -80, -20))

    xs = []
    ys = []
    refl = []
    for beta in betas:
        tmpRef = []
        tmpLeaf = []
        for alpha in alphas:
            d = DataClass.Data(lam, rep, alpha=alpha, beta=beta)
            xs.append(d.x)
            ys.append(d.y)
            if -80 <= alpha <= -20 or 20 <= alpha <= 80:
                tmpRef.append(d.refData)
                tmpLeaf.append(d.leafData)
        leaf = numpy.interp(numpy.arange(-80, 90, 10), alphaValues, tmpLeaf)
        ref = numpy.interp(numpy.arange(-80, 90, 10), alphaValues, tmpRef)
        for i in range(0, len(leaf)):
            refl.append(leaf[i] / ref[i])

    # Vo = Variogram(xs, ys, refl)
    # print(Vo)
    DrawPlot(xs, ys, refl)
    DrawDirections()
    plt.title("Feuille " + str(d.nLeaf) + " éclairée à " + str(d.lightAngle) + "° pour " + str(lam) + ' nm')
    plt.show()


def DrawPlot(x, y, data, norm=False):
    xi = numpy.linspace(-1.7, 1.7, 100)
    yi = numpy.linspace(-1.7, 1.7, 100)
    # grid the data.
    zi = griddata((x, y), data, (xi[None, :], yi[:, None]), method='cubic')
    if norm:
        pcm = plt.pcolormesh(xi, yi, zi, vmin=0, vmax=1, shading='auto')
    else:
        pcm = None
    plt.contour(xi, yi, zi, linewidths=0.2, colors='k')
    plt.contourf(xi, yi, zi)
    plt.colorbar(pcm)
    plt.axis('off')


def DrawDirections():
    alphas = list(range(-80, -10, 10))
    alphas.extend(range(20, 90, 10))
    betas = list(range(60, -80, -20))
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
            if -80 <= alpha <= -20:
                plt.plot(x, y, "b.", alpha=0.6)
            elif 20 <= alpha <= 80:
                plt.plot(x, y, "r.", alpha=0.6)
    plt.text(-0.3, -1.8, r'$\alpha_v = -90°$')
    plt.text(-0.3, 1.6, r'$\alpha_v = 90°$')
    plt.text(-1.5, -0.4, r'$\beta_v = 60°$', rotation='vertical')
    plt.text(1.4, -0.4, r'$\beta_v = -60°$', rotation='vertical')


def Variogram(x, y, data):
    n = len(x)
    print(n)
    z = []
    Vo = numpy.zeros((39, 39))
    for i in range(0, n):
        z.append(numpy.complex(x[i], y[i]))
    A = numpy.matmul(numpy.ones((n, n)), numpy.diagflat(z))
    H = numpy.subtract(A, A.T)
    dh = numpy.linspace(0, numpy.max(H) / 2, 5)
    delta = (dh[2] - dh[1]) / 2
    k = []
    c = numpy.ones((5, 1))
    g = numpy.ones((5, 1))
    Nx = []
    Ny = []
    for j in range(0, 5):
        for x in range(n):
            for y in range(n):
                if dh[j] == 0 and H[x][y] <= delta:
                    Nx.append(x)
                    Ny.append(y)
                elif dh[j] - delta < H[x][y] <= dh[j] + delta:
                    Nx.append(x)
                    Ny.append(y)
        if len(Nx) == 0:
            k.append(j)
        else:
            tmpX = []
            tmpY = []
            for a in Nx:
                tmpX.append(data[a])
            for a in Ny:
                tmpY.append(data[a])
            c[j] = numpy.mean((tmpX - numpy.mean(tmpX)) * (tmpY - numpy.mean(tmpY)))
            g[j] = numpy.mean(numpy.power(numpy.subtract(tmpX, tmpY), 2)) / 2
    for a in k:
        dh[a] = []
        c[a] = []
        g[a] = []
    lin = linear(dh, g, 2)
    print(lin)
    print(numpy.shape(lin[0] + lin[1] * H), numpy.shape(-numpy.ones((n, 1))))

    tmp1 = numpy.concatenate((lin[0] + lin[1] * H, -numpy.ones((n, 1))))
    tmp2 = numpy.concatenate((-numpy.ones((1, n)), 0))
    C = numpy.stack(tmp1, tmp2)

    c_x = 1

    for xo in range(-95, 95, 5):
        c_y = 1
        for yo in range(-95, 95, 5):
            zo = numpy.complex(xo, yo)
            Ho = abs(numpy.subtract(z, zo))
            D = [lin[0] + lin[1] * Ho, -1]
            print(C, D)
            wo = numpy.linalg.lstsq(C, D)
            Vo[c_y, c_x] = numpy.sum(wo[1:n] * data)
            c_y = c_y + 1
        c_x = c_x + 1
    print(Vo)
    return Vo


def linear(x, y, i):
    n = len(x)
    y = numpy.reshape(y, len(y))
    sx = numpy.sum(x)
    sy = numpy.sum(y)
    sx2 = numpy.sum(numpy.power(x, 2))
    sy2 = numpy.sum(numpy.power(y, 2))
    sxy = numpy.sum(numpy.multiply(x, y))
    r = (n * sxy - sx * sy) / ((n * sx2 - sx ** 2) * (n * sy2 - sy ** 2)) ** 0.5

    if i == 1:
        b = sxy / sx2
        rmse = numpy.sqrt(sum((y - b * x) ** 2) / (n - 1))
        ans = [0, b, r, rmse]

    else:
        d = n * sx2 - sx ** 2
        a = (sx2 * sy - sx * sxy) / d
        b = (n * sxy - sx * sy) / d
        rmse = numpy.sqrt(sum((y - x) ** 2) / n)
        ans = [a, b, r, rmse]
    return ans



