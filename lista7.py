#Questão 1
"""
Transformando os valores em inteiros não temos que nos preocupar com a aritmetica de floating point,
a classe int do python armazena inteiros arbitrariamente grande, pois pode alocar mais memória para si, ao ínves de dar overflow.
"""
class posicao():
    def __init__(self, km: float):
        km = str(km).split(".")
        mm = int(km[1]) * 10**(6 - len(km[1]))
        km = int(km[0]) * 10 ** 6 
        self.mm = km + mm
parafuso = posicao(123.456789)
print(parafuso.mm)
print()

#Questão 2

from typing import Any
import numpy as np
import matplotlib.pyplot as plt

class Domain:
    min = None
    max = None

    def __contains__(self, x):
        raise NotImplementedError

    def __repr__(self):
        raise NotImplementedError

    def __str__(self):
        return self.__repr__()

    def copy(self):
        raise NotImplementedError

class Interval(Domain):
    def __init__(self, p1, p2):
        self.inff, self.supp = min(p1, p2), max(p1, p2)

    @property
    def min(self):
        return self.inff

    @property
    def max(self):
        return self.supp

    @property
    def size(self):
        return (self.max - self.min)

    @property
    def haf(self):
        return (self.max + self.min)/2.0

    def __contains__(self, x):
        return np.all(np.logical_and(self.inff <= x, x <= self.supp))

    def __str__(self):
        return f'[{self.inff:2.4f}, {self.supp:2.4f}]'

    def __repr__(self):
        return f'[{self.inf!r:2.4f}, {self.supp!r:2.4f}]'

    def copy(self):
        return Interval(self.inff, self.supp)

class RealFunction:
    f = None
    prime = None
    domain = None

    def eval_safe(self, x):
        if self.domain is None or x in self.domain:
            return self.f(x)
        else:
            raise Exception("The number is out of the domain")

    def prime_safe(self, x):
        if self.domain is None or x in self.domain:
            return self.prime(x)
        else:
            raise Exception("The number is out of the domain")

    def __call__(self, x) -> float:
        return self.eval_safe(x)

    def plot(self):
        fig, ax = plt.subplots()
        X = np.linspace(self.domain.min, self.domain.max, 100)
        Y = self(X)
        ax.plot(X,Y)
        return fig, ax

def bissect(f: RealFunction, search_space: Interval, erroTol: float = 1e-4, maxItr: int = 1e4, eps: float = 1e-6 ) -> Interval:
    count = 0
    ss = search_space.copy()
    err = ss.size/2.0
    fa, fb = f(ss.min), f(ss.max)
    if fa * fb > -eps:
        if abs(fa) < eps:
            return Interval(ss.min, ss.min)
        elif abs(fb) < eps:
            return Interval(ss.max, ss.max)
        else:
            raise Exception("The interval extremes share the same signal;\n employ the grid search method to locate a valid interval.")
    while count <= maxItr and err > erroTol:
        count += 1
        a, b, m = ss.min, ss.max, ss.haf
        fa, fb, fm = f(a), f(b), f(m)
        if abs(fm) < eps:
            return Interval(m, m)
        elif fa * fm < -eps:
            ss = Interval(a, m)
        elif fb * fm < -eps:
            ss = Interval(m, b)
    return ss

def grid_search(f: RealFunction, domain: Interval = None, grid_freq = 8) -> Interval:
    if domain is not None:
        D = domain.copy()
    else:
        D = f.domain.copy()
    L1 = np.linspace(D.min, D.max, grid_freq)
    FL1 = f(L1)
    TI = FL1[:-1]*FL1[1:]
    VI = TI <= 0
    if not np.any(VI):
        return None
    idx = np.argmax(VI)
    return Interval(L1[idx], L1[idx+1])

def newton_root(f: RealFunction, search_space: Interval, erroTol: float = 1e-4, maxItr: int = 1e4, eps: float = 1e-6 ) -> Interval:
    count = 0
    ss = search_space.copy()
    err = ss.size/2.0
    m = ss.haf
    fm = f(m)
    df = f.prime(fm)
    if abs(fm) < eps:
        return m
    while count <= maxItr and err > erroTol:
        count += 1
        if abs(df) < eps:
            raise Exception("Derivada muito próxima de zero em",m,"escolha outro intervalo")
        else:
            m = m - f(m)/f.prime(m)
            fm = f(m)
            df = f.prime(fm)
        if abs(fm) < eps:
            return m
    return m

if __name__ == '__main__':
    import sympy as sp

    d = Interval(-1.0, 2.0)
    print(d)

    nt = np.linspace(d.min-.1, d.max+1, 5)

    for n in nt:
        sts = 'IN' if n in d else 'OUT'
        print(f'{n} is {sts} of {d}')

    class funcTest(RealFunction):
        f = lambda self, x : np.power(x, 2) - 1
        prime = lambda self, x : 2*x
        domain = Interval(-2, 2)

    ft = funcTest()
    ND = grid_search( ft, grid_freq=12)
    print(bissect(ft, search_space=ND))
    print()
    print(newton_root(ft, search_space=ND))
    print()

#Questão 3

import numpy as np
import scipy
import time

class interpolater:

    def evaluate(self, X):
        raise NotImplementedError

    def __call__(self,  X):
        return self.evaluate(X)

class VandermondeMatrix(interpolater):

    def __init__(self, x, y):
        if len(x) != len(y):
            raise RuntimeError(f"Dimensions must be equal len(x) = {len(x)} != len(y) = {len(y)}")
        self.data = [x, y]
        self._degree = len(x) -1
        self._buildMatrix()
        self._poly = np.linalg.solve(self.matrix, self.data[1])

    def _buildMatrix(self):
        self.matrix = np.ones([self._degree+1, self._degree+1])
        for i, x in enumerate(self.data[0]):
            self.matrix[i, 1:] = np.multiply.accumulate(np.repeat(x, self._degree))

    def evaluate(self, X):
        r = 0.0
        for c in self._poly[::-1]:
            r = c+r*X
        return r

class LagrangePolynomial(interpolater):

    def __init__(self, x, y):
        if len(x) != len(y):
            raise RuntimeError(f"Dimensions must be equal len(x) = {len(x)} != len(y) = {len(y)}")
        self.data = [x, y]
        self._degree = len(x) -1
        self._poly = scipy.interpolate.lagrange(x, y)

    def evaluate(self, X):
        return self._poly(X)

def random_sample(intv, N):
    r = np.random.uniform(intv[0], intv[1], N-2)
    r.sort()
    return np.array([intv[0]] + list(r) + [intv[1]])

def error_pol(f, P, intv, n = 1000):
    x = random_sample(intv, n)
    vectError = np.abs(f(x)-P(x))
    return np.sum(vectError)/n, np.max(vectError)

if __name__ == '__main__':
    import matplotlib.pyplot as plt

    DataX = [10.7       , 11.075    , 11.45     , 11.825    , 12.2      , 12.5]
    DataY = [-0.25991903, 0.04625002, 0.16592075, 0.13048074, 0.13902777, 0.2 ]

    Pvm = VandermondeMatrix(DataX, DataY)
    Plp = LagrangePolynomial(DataX, DataY)

    X = np.linspace(min(DataX)-0.2, max(DataX)+0.2, 100)
    Yvm = Pvm(X)

    _, ax1 = plt.subplots(1)
    ax1.plot(X,Yvm)
    ax1.axis('equal')
    ax1.plot(DataX, DataY, 'o')
    plt.show()

    X = np.linspace(min(DataX)-0.2, max(DataX)+0.2, 100)
    Ylp = Plp(X)

    _, ax2 = plt.subplots(1)
    ax2.plot(X,Ylp)
    ax2.axis('equal')
    ax2.plot(DataX, DataY, 'o')
    plt.show()
    
    start = time.time()
    Pvm = VandermondeMatrix(DataX, DataY)
    print("Vandermonde:", time.time() - start, "s")

    start = time.time()
    Plp = LagrangePolynomial(DataX, DataY)
    print("Lagrange (SciPy):", time.time() - start, "s")

#Questão 4
"""
Um avião decolou e registrou a seguinte tabela relacionando a temperatura do ar com a altura:
Altura (m) 200 400 600 800 1000 1200 1400
Temperatura (◦C) 15 9 5 3 -2 -5 -15

Desenvolva um programa em Python que resolva os seguintes problemas utilizando técnicas de interpolação e de busca de raízes:
(a) Estime a altura em que o avião provavelmente se encontrava quando a temperatura foi de 0◦C.
(b) Estime a temperatura do ar quando o avião estava a 700 metros.

Requisitos:
• Teste utilizando pelo menos dois métodos de interpolação diferentes (por exemplo, interpolação linear por partes e polinomial);
• Teste utilizando pelo menos dois métodos numéricos para encontrar raízes (por exemplo, método da bisseção e secante);
• Exibir os resultados obtidos para cada um dos itens acima;
• Discuta as discrepâncias e concordâncias entre os resultados
"""
import sympy

class InterpolacaoLinear():

    def __init__(self, x, y):
        self.x = sympy.symbols("x")
        l = []
        for i in range(1,len(x)):
            reta = (x[i-1], x[i], y[i-1] + (self.x - x[i-1]) * (y[i] - y[i-1]) / (x[i] - x[i-1]))
            l.append(reta)
        self.polinomio = l

    def __call__(self, x):
        for i in self.polinomio:
            if i[0] <= x <= i[1]:
                return i[2].subs(self.x, x)

class DerivadaLinear():

    def __init__(self, polinomio):
        self.x = sympy.symbols("x")
        self.polinomio = polinomio.polinomio
        l = []
        for i in self.polinomio:
            l.append(i[2].diff())
        self.derivada = l

    def __call__(self, x):
        for i in range(len(self.derivada)):
            if self.polinomio[i][0] <= x <= self.polinomio[i][1]:
                return self.derivada[i].subs(self.x, x)

class InterpolacaoPolinomial():

    def __init__(self, x, y):
        self.x = sympy.symbols("x")
        soma = 0
        for j in range(len(x)):
            produto = 1
            for i in range(len(x)):
                if i != j:
                    parcela = (self.x - x[i]) / (x[j] - x[i])
                    produto = produto * parcela
            soma = soma + y[j] * produto
        self.polinomio = sympy.simplify(soma)

    def __call__(self, x):
        return self.polinomio.subs(self.x, x)

class DerivadaPolinomial():

    def __init__(self, polinomio):
        self.x = sympy.symbols("x")
        self.derivada = polinomio.polinomio.diff()

    def __call__(self, x):
        return self.derivada.subs(self.x, x)

def bissecao(polinomio, x, y, toleranciax, maxc, toleranciay):
    for i in range(1, len(x)):
        if y[i-1] * y[i] > -toleranciay:
            if abs(y[i-1]) < toleranciay:
                return x[i-1]
            elif abs(y[i]) < toleranciay:
                return x[i]
        else:
            espaco = (x[i-1], x[i])
            break
    c = 0
    errox = (espaco[1]-espaco[0])/2
    while c <= maxc and errox > toleranciax:
        c += 1
        media = (espaco[0]+espaco[1])/2
        if abs(polinomio(media)) < toleranciay:
            return media
        elif polinomio(espaco[0]) * polinomio(media) < -toleranciay:
            espaco = (espaco[0], media)
        elif polinomio(espaco[1]) * polinomio(media) < -toleranciay:
            espaco = (media, espaco[1])
        errox = (espaco[1]-espaco[0])/2
    return espaco

def newton(polinomio, derivada, x, y, toleranciax, maxc, toleranciay):
    for i in range(1, len(x)):
        if y[i-1] * y[i] > -toleranciay:
            if abs(y[i-1]) < toleranciay:
                return x[i-1]
            elif abs(y[i]) < toleranciay:
                return x[i]
        else:
            espaco = (x[i-1], x[i])
            break
    c = 0
    errox = (espaco[1]-espaco[0])/2
    media = (espaco[0]+espaco[1])/2
    if abs(polinomio(media)) < toleranciay:
        return media
    while c <= maxc and errox > toleranciax:
        c += 1
        if abs(derivada(media)) < toleranciay:
            raise Exception("Método de newton falhou: Derivada muito próxima de zero em",media)
        else:
            media =  media - polinomio(media)/derivada(media)
        if abs(polinomio(media)) < toleranciay:
            return media
        errox = errox/2
    return media

altura = [200, 400, 600, 800, 1000, 1200, 1400]
temperatura = [15, 9, 5, 3, -2, -5, -15]
pl = InterpolacaoLinear(altura, temperatura)
dl = DerivadaLinear(pl)
pp = InterpolacaoPolinomial(altura, temperatura)
dp = DerivadaPolinomial(pp)
print(bissecao(pl, altura, temperatura, 1e-4, 1e5, 1e-4))
print(bissecao(pp, altura, temperatura, 1e-4, 1e5, 1e-4))
print(newton(pl, dl, altura, temperatura, 1e-4, 1e5, 1e-4))
print(newton(pp, dp, altura, temperatura, 1e-4, 1e5, 1e-4))
print()
print(pl(700))
print(pp(700))
"""
Como não conhecemos a função original que relaciona temperatura e altura,
as discrepâncias entre os resultados vêm das diferenças entre as curvas polinomiais,
e mesmo assim os valores estão bem próximos entre si.
"""