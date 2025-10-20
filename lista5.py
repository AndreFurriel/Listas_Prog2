#Questão1
from functools import reduce
class Aluno():
    def __init__(self,nome,notas):
        self.nome = nome
        self.notas = notas
    def media(self):
        m1 = 0
        m2 = 1
        for a in range(2,len(self.notas)):
            if self.notas[a] < self.notas[m1]:
                if self.notas[m1] < self.notas[m2]:
                    m2 = m1
                    m1 = a
                else:
                    m1 = a
            elif self.notas[a] < self.notas[m2]:
                if self.notas[m2] < self.notas[m1]:
                    m1 = m2
                    m2 = a
                else:
                    m2 = a
        m = 0
        for b in self.notas:
            m = m + b
        m = m - self.notas[m1] - self.notas[m2]
        return m/(len(self.notas)-2)
    def aprovado(self):
        return self.media() >= 6
    def __repr__(self):
        return f"Aluno(nome={self.nome}, media={self.media():.1f}, aprovado={self.aprovado()})"
alunos = [Aluno("Ana", [8, 7, 9, 3, 8, 5]),Aluno("Bruno", [0, 6, 4, 4, 5, 6]),Aluno("Carla", [10, 9, 8, 7, 9, 0])]
def media(aluno):
    return f"{aluno.media():.1f}"
def aprovado(aluno):
    return aluno.aprovado()
def soma(soma,aluno2):
    return soma+aluno2.media()
print("Médias:",list(map(media,alunos)))
print("Aprovados",list(filter(aprovado,alunos)))
print(f"Média da turma: {(reduce(soma,alunos,0))/len(alunos):.1f}")
#Questão2
import random
def generateMap(m: int, n: int, ground_water_ration = .2, water = '0', ground = '1' ):
    r = int(m*n*ground_water_ration+.5)
    newMap = [[water]*m for _ in range(n)]
    coord = [(i, j) for i in range(n) for j in range(m)]
    random.shuffle(coord)
    for i, j in coord[:r]:
        newMap[i][j] = ground
    return newMap
def save_map(map_s, path = 'new_map.txt'):
    with open(path, 'wt') as f:
        for row in map_s:
            f.write("".join(map(str, row)))
            f.write('\n')
def print_map(map_p):
    for row in map_p:
        print("".join(map(str, row)))
if __name__ == '__main__':
    random.seed(10012)
    m1 = generateMap(50, 10, 0.1, '-', 'X')
    print_map(m1)
    m2 = generateMap(100, 120)
    save_map(m2, 'test_map.txt')
    def explorar(map, a, b, ground, visitadas):
        if -1 < a < len(map) and -1 < b < len(map[0]):
            if map[a][b] == ground:
                if (a, b) not in visitadas:
                    visitadas.add((a, b))
                    explorar(map, a-1, b-1, ground, visitadas)
                    explorar(map, a-1, b, ground, visitadas)
                    explorar(map, a-1, b+1, ground, visitadas)
                    explorar(map, a, b-1, ground, visitadas)
                    explorar(map, a, b+1, ground, visitadas)
                    explorar(map, a+1, b-1, ground, visitadas)
                    explorar(map, a+1, b, ground, visitadas)
                    explorar(map, a+1, b+1, ground, visitadas)
    def contar(map, ground = 1):
        visitadas = set()
        c = 0
        for a in range(len(map)):
            for b in range(len(map[0])):
                if map[a][b] == ground:
                    if (a, b) not in visitadas:
                        explorar(map, a, b, ground, visitadas)
                        c = c + 1
        return c                        
    print(contar(m1, ground = "X"))
#Questão3
if __name__ == '__main__':
    random.seed(10012)
    m1 = generateMap(50, 10, 0.1, '-', 'X')
    print_map(m1)
    m2 = generateMap(100, 120)
    save_map(m2, 'test_map.txt')
    def explorar(map, a, b, ground, visitadas, ilha, t):
        if -1 < a < len(map) and -1 < b <len(map[0]):
            if (a, b) not in visitadas:
                visitadas.add((a, b))
                if map[a][b] == ground:
                    t = t + 1
                    ilha.add((a,b))
                    visitadas, ilha, t = explorar(map, a-1, b-1, ground, visitadas, ilha, t)
                    visitadas, ilha, t = explorar(map, a-1, b, ground, visitadas, ilha, t)
                    visitadas, ilha, t = explorar(map, a-1, b+1, ground, visitadas, ilha, t)
                    visitadas, ilha, t = explorar(map, a, b-1, ground, visitadas, ilha, t)
                    visitadas, ilha, t = explorar(map, a, b+1, ground, visitadas, ilha, t)
                    visitadas, ilha, t = explorar(map, a+1, b-1, ground, visitadas, ilha, t)
                    visitadas, ilha, t = explorar(map, a+1, b, ground, visitadas, ilha, t)
                    visitadas, ilha, t = explorar(map, a+1, b+1, ground, visitadas, ilha, t)
        return visitadas, ilha, t
    def contar(map, ground = 1):
        visitadas = set()
        c = 0
        tmin = 0
        tmax = 0
        for a in range(len(map)):
            for b in range(len(map[0])):
                if map[a][b] == ground:
                    if (a, b) not in visitadas:
                        ilha = set()
                        visitadas, ilha, t = explorar(map, a, b, ground, visitadas, ilha, 0)
                        if t > tmax:
                            tmax = t
                            ilhamax = ilha
                        if tmin == 0:
                            tmin = t
                            ilhamin = ilha
                        if t < tmin:
                            tmin = t
                            ilhamin = ilha
                        c = c + 1
        xmin, ymin, xmax, ymax = 0, 0, 0, 0
        for d in ilhamin:
            xmin = xmin + d[0]
            ymin = ymin + d[1]
        for e in ilhamax:
            xmax = xmax + e[0]
            ymax = ymax + e[1]
        cmin = (xmin/tmin,ymin/tmin)
        cmax = (xmax/tmax,ymax/tmax)
        return c, cmin, cmax
    print(contar(m1, ground = "X"))
#Questão4
if __name__ == '__main__':
    random.seed(10012)
    m1 = generateMap(50, 10, 0.2, '-', 'X')
    print_map(m1)
    m2 = generateMap(100, 120)
    save_map(m2, 'test_map.txt')
    def lago(map, ground = 1):
        visitadas = set()
        for a in range(1, len(map)-1):
            for b in range(1, len(map[0])-1):
                if map[a][b] != ground:
                    if (a, b) not in visitadas:
                        visitadas.add((a, b))
                        visitadas.add((a-1, b))
                        visitadas.add((a, b-1))
                        visitadas.add((a, b+1))
                        visitadas.add((a+1, b))
                        if map[a-1][b] == ground and map[a][b-1] == ground and map[a][b+1] == ground and map[a+1][b] == ground:
                            return True
        return False
    print(lago(m1, ground = "X"))
#Questão5
import numpy
#numpy.array(object, dtype=None, *, copy=True, order='K', subok=False, ndmin=0, like=None)
class ToroArray(numpy.array):
    """
    Uma subclasse customizada de numpy.array representa um toro unidimensional.
    
    Isso significa que qualquer valor inteiro pode ser usado como indice,
    e a classe retorna o valor da sua posicao depois de calcular o modulo
    do tamanho do array. Isso permite que o array se comporte como um circulo,
    onde os indices negativos ou valores que ultrapassem o tamanho do array sao tratados
    de forma apropriada.
      
    Metodos:
        __new__(cls, input_array):
            Cria um novo toro de um array.
        
        __init__(self, inputArray):
            Inicializa o objeto calculando e guardando o modulo.
    """

    def __new__(cls, input_array):
        """
        Cria um novo toro de um array.
        
        Parametros:
            input_array (array-like): Array a ser convertido.
        
        Retorna:
            ToroArray: O toro criado pelo array.
        """
        obj = numpy.asarray(input_array).view(cls)  # Convert the input array and create a view as this class
        return obj

    def __init__(self):
        """
        Inicializa o objeto calculando e guardando o modulo.
        
        Parametros:
            input_array (array-like): Array a ser convertido.
        """
        self.mod = numpy.prod(self.shape)  # Calculate and store the product of dimensions of the array

    def getDim(self):
        """
        Retrieves the calculated dimension of the array.
        
        Returns:
            int: The calculated dimension of the array.
        """
        return self.dim

    def __mul__(self, w):
        """
        Overrides the multiplication behavior for CustomArray instances.
        
        If w is a numpy array or CustomArray, this method checks if their shapes match.
        If shapes match, element-wise multiplication is performed. If shapes do not match,
        the input array w is adjusted to match the shape of this CustomArray, and then
        element-wise multiplication is performed. If w is not a numpy array or CustomArray,
        regular multiplication is performed.
        
        Parameters:
            w (array-like): Input array or value to be multiplied with this CustomArray.
        
        Returns:
            array-like: Result of element-wise multiplication or regular multiplication.
        """
        if type(w) in [numpy.ndarray, ToroArray]:  # Check if w is a numpy array or an instance of CustomArray
            if self.shape == w.shape:  # Check if the shapes of the arrays match
                return super().__mul__(w)  # If shapes match, perform element-wise multiplication
            else:
                tw = w.flatten()  # Flatten the input array w
                if len(tw) < self.dim:  # If flattened array length is less than stored dimension
                    ft = numpy.ones(self.dim)  # Create an array of ones with length equal to stored dimension
                    ft[:len(tw)] = tw  # Copy values from flattened array to the front
                    tw = ft
                else:
                    tw = tw[:self.dim]  # If flattened array length is greater, trim it
                tw = tw.reshape(self.shape)  # Reshape tw to match the shape of the CustomArray
                return super().__mul__(tw)  # Perform element-wise multiplication
        return super().__mul__(w)  # If w is not a numpy array or CustomArray, perform regular multiplication
#tr = ToroArray([10, 11, 12, 13, 14])
#print(tr[6])
#print(tr[-20])
#11
#10
# Criando uma instância da classe personalizada
v = ToroArray([[ 1, 2, 4], [2, 3, 4]])
print(v.dim)
print(v.shape)
print(v*numpy.array([[3,2],[10,100]]))
