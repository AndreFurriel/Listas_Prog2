#Questão 1
class graph():
    def __init__(self):
        self.vertexes = dict()
        self.edges = dict()
    def adjacent(self, x, y):
        if x in self.edges.keys():
            return y in self.edges[x]
    def neighbors(self, x):
        if x in self.edges.keys():
            return self.edges[x]
    def add_vertex(self, x):
        if x not in self.vertexes.keys():
            self.vertexes[x] = None
            self.edges[x] = []
    def remove_vertex(self, x):
        if x in self.vertexes.keys():
            self.vertexes.pop(x)
            for a in self.edges[x]:
                self.remove_edge(x, a)
            self.edges.pop(x)
    def add_edge(self, x, y):
        if x not in self.vertexes.keys():
            self.add_vertex(x)
        if y not in self.vertexes.keys():
            self.add_vertex(y)
        if y not in self.edges[x]:
            self.edges[x].append(y)
            self.edges[y].append(x)
    def remove_edge(self, x, y):
        if y in self.edges[x]:
            self.edges[x].remove(y)
            self.edges[y].remove(x)
    def get_vertex_value(self, x):
        if x in self.vertexes.keys():
            return self.vertexes[x]
    def set_vertex_value(self, x, v):
        if x in self.vertexes.keys():
            self.vertexes[x] = v
G = graph()
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
print(G.adjacent("B", "A"))
print(G.neighbors("A"))
print(G.neighbors("B"))
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
#Questão 3
import random
class Pilha():
  def __init__(self):
    self.pilha = []
  def __repr__(self):
    return str(self.pilha)
  def __len__(self):
    return len(self.pilha)
  def push(self, item):
    self.pilha.append(item)
  def pop(self):
    if len(self) == 0:
      raise Exception("Pilha vazia")
    else:
      return self.pilha.pop()
def generate_maze(m, n, room = 0, wall = 1, cheese = '.' ):
    # Initialize a (2m + 1) x (2n + 1) matrix with all walls (1)
    maze = [[wall] * (2 * n + 1) for _ in range(2 * m + 1)]
    # Directions: (row_offset, col_offset) for N, S, W, E
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    def dfs(x, y):
        """Recursive DFS to generate the maze."""
        # Mark the current cell as visited by making it a path (room)
        maze[2 * x + 1][2 * y + 1] = room
        # Shuffle the directions to create a random path
        random.shuffle(directions)
        for dx, dy in directions:
            nx, ny = x + dx, y + dy  # New cell coordinates
            if 0 <= nx < m and 0 <= ny < n and maze[2 * nx + 1][2 * ny + 1] == wall:
                # Open the wall between the current cell and the new cell
                maze[2 * x + 1 + dx][2 * y + 1 + dy] = room
                # Recursively visit the new cell
                dfs(nx, ny)
    def idfs(x, y):
        """Iterative DFS to generate the maze."""
        l = []
        # Mark the current cell as visited by making it a path (room)
        maze[2 * x + 1][2 * y + 1] = room
        # Shuffle the directions to create a random path
        random.shuffle(directions)
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and maze[2 * nx + 1][2 * ny + 1] == wall:
                # Open the wall between the current cell and the new cell
                maze[2 * x + 1 + dx][2 * y + 1 + dy] = room
                print_maze(maze)
                # Save the new cell
                p.push([nx, ny])
            print(p)
        while len(p) != 0:
            d = p.pop()
            d[0] = x
            d[1] = y
            # Mark the current cell as visited by making it a path (room)
            maze[2 * x + 1][2 * y + 1] = room
            # Shuffle the directions to create a random path
            random.shuffle(directions)
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and maze[2 * nx + 1][2 * ny + 1] == wall:
                    # Save the new cell
                    p.push([nx, ny])
    # Start DFS from the top-left corner (0, 0) of the logical grid
    idfs(0, 0)
    count = 0
    while True: # placing the chesse
        i = int(random.uniform(0, 2 * m))
        j = int(random.uniform(0, 2 * m))
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
    m, n = 2, 2  # Grid size
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

#Questão 4
