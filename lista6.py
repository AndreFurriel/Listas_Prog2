#Questão1
import numpy
class My_Array(numpy.ndarray):
    """
    Uma subclasse customizada de numpy.array que adiciona o método append
    
    Métodos:
        append (float): Adiciona um item ao final do array
    """
    def __new__(cls, input_array):
        """
        Cria um novo My_Array
        
        Argumentos:
            input_array (array-like): Array a ser convertido.
        
        Retorna:
            My_Array: My_Array criado
        """
        obj = numpy.asarray(input_array).view(cls)
        obj.sig = obj.size
        return obj
    def append(self, item):
        """Adiciona um item ao final do array

        Args:
            item (float): Adiciona um item ao final do array

        Returns:
            My_Array: Novo array com o item no final
        """
        if self.sig == 0:
            aux = My_Array([float(item)])
        elif self.sig == self.size:
            p = 1
            while p <= self.sig:
                p = 2*p
            l = [0.0]*(p)
            aux = My_Array(l)
            for i in range(self.sig):
                aux[i] = self[i]
            aux[self.sig] = item
            aux.sig = self.sig + 1
        elif self.sig < self.size:
            self[self.sig] = item
            self.sig = self.sig + 1
            aux = self
        return aux
    def __str__(self):
        return str(self[:self.sig].tolist())
a = My_Array([])
a = a.append(1)
print(a.sig)
print(a)
a = a.append(2.1)
print(a.sig)
print(a)
a = a.append(3.21)
print(a.sig)
print(a)
"""
Minha implementação do append trabalha com tipo fixo (float),
sempre dobra o comprimento do array, enquanto no python esse valor varia,
e retorna um novo array, enquanto o python altera o antigo.
"""
#Questão2
"""Explique o que a função find_nb faz, e analise qual a sua complexidade."""
"""
Encontra o ponto "idt" de um array "data", mais próximo do ponto "point"
    Calcula a distancia entre os pontos do array "data" e do ponto "point"
        Com subtração de arrays: O(n)
    Cria um array "d" com as normas das diferenças entre os pontos do array "data" e o ponto "point"
        Com linalg.norm: O(n)
    Encontra o indice "idt" do ponto com diferença minima do array "d"
        Com argmin: O(n)
    Retorna a distância minima "d[idt]" e o indice "idt": O(1)
    ComplexidadeTotal = O(n) + O(n) + O(n) + O(1) = O(3n + 1) = O(n)
"""
from matplotlib import pyplot as plt
import scipy as sp
numpy.random.seed(1001)
normaldist1 = sp.stats.gamma(2, 4)
normaldist2 = sp.stats.gamma(4, 1)
X = normaldist1.rvs(200)
Y = normaldist2.rvs(200)
data  = numpy.array([X, Y]).T
def find_nb(data, point):
    Dt = data - point
    d = numpy.linalg.norm(Dt, axis=1)
    idt = numpy.argmin(d)
    return d[idt], idt
point = numpy.array([8.5, 4.5])
dd, idx = find_nb(data, point)
print(f"O ponto mais proximo está a {dd:.2f} de distância, é o ponto ({data[idx,0]:.2f},{data[idx,1]:.2f})  no índice {idx}")
#Questão3

#Questão4

#Questão5
