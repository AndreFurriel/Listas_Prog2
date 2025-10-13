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

#Questão5
