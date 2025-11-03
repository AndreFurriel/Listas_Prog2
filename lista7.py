#Questão 1
"""
Considere o seguinte cenário: você está encarregado de criar um programa em Python para lidar com medidas
que são expressas em centenas de quilômetros, mas exigem uma precisão de milímetros.
Por exemplo, isso poderia ser aplicado para representar as coordenadas exatas de componentes em uma planta industrial,
como a posição de um parafuso. Discuta como você abordaria esse problema.
Dica: você pode criar a sua própria classe numérica.
"""
class posicao():
    def __init__(self, km:int, m:int, mm:int):
        self.km = km
        self.m = m
        self.mm = mm
parafuso = posicao(123,456,789)
#Questão 2
"""
Estenda o código CodigosExcerciciosProvas/root_finder.py com o método de Newton (newton root)
para encontrar raízes de funções reais. Crie também um código exemplificando o uso do seu código e das funções/código:
• newton root
• bissect
• grid search
• A classe RealFunction
"""
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
        return  np.all(np.logical_and(self.inff <= x, x <= self.supp))

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


def bissect(f: RealFunction, 
            search_space: Interval, 
            erroTol: float = 1e-4, 
            maxItr: int = 1e4, 
            eps: float = 1e-6 ) -> Interval:
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
        a, b, m =  ss.min, ss.max, ss.haf
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


def newton_root(f: RealFunction, 
            search_space: Interval, 
            erroTol: float = 1e-4, 
            maxItr: int = 1e4, 
            eps: float = 1e-6 ) -> Interval:
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
            m =  m - f(m)/f.prime(m)
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
#Questão 3

#Questão 4

#Questão 5
