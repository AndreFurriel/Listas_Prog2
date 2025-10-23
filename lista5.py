#Questão1
import csv
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
alunos = []
with open("alunos_notas.csv", newline='', encoding='utf-8') as csvfile:
    leitor = csv.reader(csvfile)
    next(leitor)  # pula o cabeçalho
    for linha in leitor:
        nome = linha[0]
        notas = list(map(float, linha[1:]))
        alunos.append(Aluno(nome, notas))
def media(aluno):
    return f"{aluno.media():.1f}"
def aprovado(aluno):
    return aluno.aprovado()
def soma(soma,aluno2):
    return soma+aluno2.media()
medias = []
for c in alunos:
    medias.append(media(c))
aprovados = []
for d in alunos:
    if aprovado(d):
        aprovados.append(d)
print("Médias:",list(map(media,alunos)))
print("Aprovados:",list(filter(aprovado,alunos)))
print(f"Média da turma: {(reduce(soma,alunos,0))/len(alunos):.1f}")
print("Médias:",medias)
print("Aprovados:",aprovados)
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
    def contar(map, ground = '1'):
        visitadas = set()
        c = 0
        if type(map) is str:
            m=[]
            arquivo=open(map,"r", encoding="utf-8")
            linha=arquivo.readline()
            while linha!="":
                if linha!="":
                    l=[]
                    for d in range(len(linha)-1):
                        l.append(linha[d])
                    m.append(l)
                linha = arquivo.readline()
            arquivo.close()
            map=m
        if type(map) is list:
            for a in range(len(map)):
                for b in range(len(map[0])):
                    if map[a][b] == ground:
                        if (a, b) not in visitadas:
                            explorar(map, a, b, ground, visitadas)
                            c = c + 1
            return c                        
    print(contar(m1, ground = "X"))
    print(contar('test_map.txt'))
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
    def contar(map, ground = '1'):
        visitadas = set()
        c = 0
        tmin = 0
        tmax = 0
        if type(map) is str:
            m=[]
            arquivo=open(map,"r", encoding="utf-8")
            linha=arquivo.readline()
            while linha!="":
                if linha!="":
                    l=[]
                    for d in range(len(linha)-1):
                        l.append(linha[d])
                    m.append(l)
                linha = arquivo.readline()
            arquivo.close()
            map=m
        if type(map) is list:
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
    print(contar('test_map.txt'))
#Questão4
if __name__ == '__main__':
    random.seed(10012)
    m1 = generateMap(50, 10, 0.2, '-', 'X')
    print_map(m1)
    m2 = generateMap(100, 120)
    save_map(m2, 'test_map.txt')
    def explorar(map, a, b, ground, visitadas):
        if -1 < a < len(map) and -1 < b < len(map[0]):
            if map[a][b] != ground:
                if (a, b) not in visitadas:
                    visitadas.add((a, b))
                    explorar(map, a-1, b, ground, visitadas)
                    explorar(map, a, b-1, ground, visitadas)
                    explorar(map, a, b+1, ground, visitadas)
                    explorar(map, a+1, b, ground, visitadas)
    def lago(map, ground = '1'):
        visitadas = set()
        if type(map) is str:
            m=[]
            arquivo=open(map,"r", encoding="utf-8")
            linha=arquivo.readline()
            while linha!="":
                if linha!="":
                    l=[]
                    for d in range(len(linha)-1):
                        l.append(linha[d])
                    m.append(l)
                linha = arquivo.readline()
            arquivo.close()
            map=m
        if type(map) is list:
            for a in range(1, len(map)-1):
                if map[a][0] != ground:
                    if (a, 0) not in visitadas:
                        explorar(map, a, 0, ground, visitadas)
                if map[0][a] != ground:
                    if (0, a) not in visitadas:
                        explorar(map, 0, a, ground, visitadas)
                if map[len(map)-1][a] != ground:
                    if (len(map)-1, a) not in visitadas:
                        explorar(map, len(map)-1, a, ground, visitadas)
                if map[a][len(map[0])-1] != ground:
                    if (a, len(map)-1) not in visitadas:
                        explorar(map, a, len(map)-1, ground, visitadas)
            for a in range(1, len(map)-1):
                for b in range(1, len(map[0])-1):
                    if map[a][b] != ground:
                        if (a, b) not in visitadas:
                            return True
            return False
    print(lago(m1, ground = "X"))
    #print(lago('test_map.txt'))
#Questão5
import numpy
class ToroArray(numpy.ndarray):
    """
    Uma subclasse customizada de numpy.array representando um toro unidimensional.
    
    Isso significa que qualquer valor inteiro pode ser usado como índice,
    e a classe retorna o valor da sua posição depois de calcular o módulo
    do tamanho do array. Isso permite que o array se comporte como um círculo,
    onde os índices negativos ou valores que ultrapassem o tamanho do array são tratados
    de forma apropriada.
      
    Métodos:
        __new__(cls, input_array):
            Cria um novo toro de um array.
        
        __getitem__(self, inputArray):
            Calcula o valor da posição.
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

    def __getitem__(self, key):
        """
        Calcula o valor da posição.

        Parametros:
            key (int): indice

        Retorna:
            valor correspondente
        """
        key = key % self.size
        return super().__getitem__(key)
tr = ToroArray([10, 11, 12, 13, 14])
print(tr[6])
print(tr[-20])
