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
print("Questão 1")
a = My_Array([])
a = a.append(1)
a = a.append(2.1)
a = a.append(3.21)
print(a.sig)
print(a)
print()
print("Minha implementação do append trabalha com tipo fixo (float).")
print("Sempre dobra o comprimento do array, enquanto no python esse valor varia.")
print("Retorna um novo array, enquanto o python altera o antigo.")
print()
#Questão2
print("Questão 2")
print('Encontra o ponto "idt" de um array "data", mais próximo do ponto "point"')
print('    Calcula a distância entre os pontos do array "data" e do ponto "point"')
print('        Com subtração de arrays: O(n)')
print('    Cria um array "d" com as normas das diferenças entre os pontos do array "data" e o ponto "point"')
print('        Com linalg.norm: O(n)')
print('    Encontra o índice "idt" do ponto com diferença mínima do array "d"')
print('        Com argmin: O(n)')
print('    Retorna a distância mínima "d[idt]" e o índice "idt": O(1)')
print('ComplexidadeTotal = O(n) + O(n) + O(n) + O(1) = O(3n + 1) = O(n)')
print()
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
print()
print("Questão 3")
print("Para representar cada dígito, temos β - 1 opções, ou seja, precisamos do menor inteiro maior que log(β - 1) bits")
print("Como temos p dígitos precisamos de p * log(β - 1) bits")
print("Para reprentar a base, precisamos do menor inteiro maior do que log(β) bits")
print("Para representar o expoente, precisamos saber qual entre e_min ou e_max tem o maior módulo")
print("Para representar o sinal do número precisamos de 1 bit e para representar o sinal do expoente precisamos de 1 bit")
print("Para representar o 0 precisamos de 1 bit")
print("Precisamos portanto de:")
print("p * ⌈log(β - 1)⌉ + ⌈log(β)⌉ + ⌈max(abs(log(e_min)), abs(log(e_max)))⌉ + 3")
print()
#Questão4
e = 1
s = 2
while s != 1:    
    e = e/2
    s = 1 + e
print("Questão 4")
print(2*e)
print()
#Questão5
e = 1
s = 2 * 10**6
while s != 10**6:    
    e = e/2
    s = 10**6 + e
print("Questão 5")
print(2*e)
print()
print("a)")
print("Episilon de 10**6 é 6 ordens de magnitude maior do que epsilon de 1.")
print("Que é a mesma relação entre 1 e 10**6.")
print("b)")
print("Porque o float tem um número fixo de casas alocadas para os dígitos significativos,")
print("Ou seja, cada casa decimal a mais antes da virgula é uma casa a menos depois da virgula")
print("c)")
print("Em aplicações com números muito grandes ou muito pequenos,")
print("Perdemos tanta precisão que os valores menores não alteram o valores maiores,")
print("Como visto com o epsilon maquina, comparações falsas se tornam verdadeiras.")