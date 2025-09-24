#Questão 1
class Graph():
    def __init__(self):
        self.vertexes = dict()
        self.edges = dict()
    def adjacent(self, x, y):
        return y in self.edges.get(x, set())
    def neighbors(self, x):
        return self.edges.get(x, set())
    def add_vertex(self, x):
        if x not in self.vertexes:
            self.vertexes[x] = None
            self.edges[x] = set()
    def remove_vertex(self, x):
        if x in self.vertexes:
            for a in list(self.edges[x]):
                self.remove_edge(x, a)
            self.vertexes.pop(x)
            self.edges.pop(x)
    def add_edge(self, x, y):
        if x not in self.vertexes:
            self.add_vertex(x)
        if y not in self.vertexes:
            self.add_vertex(y)
        if y not in self.edges[x]:
            self.edges[x].add(y)
            self.edges[y].add(x)
    def remove_edge(self, x, y):
        if x in self.vertexes and y in self.edges[x]:
            self.edges[x].remove(y)
            self.edges[y].remove(x)
    def get_vertex_value(self, x):
        if x in self.vertexes:
            return self.vertexes[x]
    def set_vertex_value(self, x, v):
        if x in self.vertexes:
            self.vertexes[x] = v
G = Graph()
G.add_vertex("A")
G.add_edge("A","B")
print(G.adjacent("A", "B"))
print(G.neighbors("A"))
print()
G.remove_edge("B","A")
G.set_vertex_value("B", 0)
print(G.adjacent("A", "B"))
print(G.neighbors("A"))
print(G.get_vertex_value("A"))
print(G.get_vertex_value("B"))
print()
G.add_edge("A","B")
G.remove_vertex("B")
print(G.adjacent("A", "B"))
print(G.neighbors("A"))
print()

#Questão 2
def findjudge(n, trust):
    a = [0]*n
    b = [0]*n
    j = -1
    for c in range(len(trust)):
        a[trust[c][0] - 1] = a[trust[c][0] - 1] + 1
        b[trust[c][1] - 1] = b[trust[c][0] - 1] + 1
    for d in range(n):
        if a[d] == 0:
            if b[d] == n-1:
                if j == -1:
                    j = d + 1
                else:
                    print(-1)
                    break
    print(j)
t = [[1, 2], [1 ,3], [2, 3]]
n = 3
findjudge(n, t)
t = [[ 1, 3], [2 ,3], [3, 1]]
n = 3
findjudge(n, t)
print()

#Questão 3
import random
def generate_maze(m, n, room = 0, wall = 1, cheese = '.' ):
    # Initialize a (2m + 1) x (2n + 1) matrix with all walls (1)
    maze = [[wall] * (2 * n + 1) for _ in range(2 * m + 1)]
    # Directions: (row_offset, col_offset) for N, S, W, E
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    def idfs(x, y):
        """Iterative DFS to generate the maze."""
        visited = set()
        stack = []
        # Mark the current cell as visited by making it a path (room)
        visited.add((x, y))
        maze[2 * x + 1][2 * y + 1] = room
        stack.append([x,y])
        while len(stack)!=0:
            d = stack.pop()
            x = d[0]
            y = d[1]
            # Mark the current cell as visited by making it a path (room)
            maze[2 * x + 1][2 * y + 1] = room
            random.shuffle(directions)
            for dx, dy in directions:
                nx, ny = x + dx, y + dy  # New cell coordinates
                if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    maze[2 * x + 1 + dx][2 * y + 1 + dy] = room  # Open the wall
                    stack.append([nx, ny])
    # Start DFS from the top-left corner (0, 0) of the logical grid
    idfs(0, 0)
    count = 0
    while True: # placing the chesse
        i = int(random.uniform(0, 2 * m))
        j = int(random.uniform(0, 2 * n))
        count += 1
        if maze[i][j] == room:
            maze[i][j] = cheese 
            break
    return maze
def print_maze(maze):
    for row in maze:
        print(" ".join(map(str, row)))
# Example usage:
if __name__ == '__main__':
    m, n = 10, 14  # Grid size
    random.seed(10110)
    maze = generate_maze(m, n)
    print('Maze 1')
    print_maze(maze)
    room = ' '
    wall = 'H'
    cheese = '*'
    maze = generate_maze(m, n, room, wall, cheese)
    print('\nMaze 2')
    print_maze(maze)
    print()

#Questão 4
def path(maze):
    steps = []
    x, y = 1, 1
    going = "down"
    steps.append((x, y, going))
    while maze[x][y]!=cheese:
        if going == "left":
            if maze[x-1][y] == wall:
                if maze[x][y-1] == wall:
                    going = "down"
                else:
                    steps.append((x, y, going))
                    y = y - 1
            else:
                going = "up"
                steps.append((x, y, going))
                x = x - 1
        elif going == "up":
            if maze[x][y+1] == wall:
                if maze[x-1][y] == wall:
                    going = "left"
                else:
                    steps.append((x, y, going))
                    x = x - 1
            else:
                going = "right"
                steps.append((x, y, going))
                y = y + 1          
        elif going == "right":
            if maze[x+1][y] == wall:
                if maze[x][y+1] == wall:
                    going = "up"
                else:
                    steps.append((x, y, going))
                    y = y + 1
            else:
                going = "down"
                steps.append((x, y, going))
                x = x + 1
        elif going == "down":
            if maze[x][y-1] == wall:
                if maze[x+1][y] == wall:
                    going = "right"
                else:
                    steps.append((x, y, going))
                    x = x + 1
            else:
                going = "left"
                steps.append((x, y, going))
                y = y - 1
    for x, y, going in steps:
        if going == "left":
            maze[x][y] = "←"
        if going == "up":
            maze[x][y] = "↑"
        if going == "right":
            maze[x][y] = "→"
        if going == "down":
            maze[x][y] = "↓"
    return maze
print('\nMaze 3')
print_maze(path(maze))
print()
print("Minha solução toma os caminhos em ordem anti-horária")
print("Por isso sempre mantém uma parede do labirinto a direita do sentido em que ela está indo")
print("Ela é uma busca em profundidade, porque ela verifica somente um caminho por vez")
