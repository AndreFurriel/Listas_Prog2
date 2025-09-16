#Questão 1
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
class Fila():
  def __init__(self):
    self.pilha1 = Pilha()
    self.pilha2 = Pilha()
  def __repr__(self):
    return str(self.pilha1) + str(self.pilha2)
  def __len__(self):
    return len(self.pilha1) + len(self.pilha2)
  def enqueue(self, item):
    self.pilha1.push(item)
  def dequeue(self):
    if len(self) == 0:
      raise Exception("Pilha vazia")
    else:
      if len(self.pilha2) == 0:
        for a in range(len(self.pilha1)):
          b = self.pilha1.pop()
          self.pilha2.push(b)
        c = self.pilha2.pop()
      else:
        c = self.pilha2.pop() 
    return c
f = Fila()
f.enqueue(1)
f.enqueue(2)
f.enqueue(3)
f.enqueue(4)
print(f, len(f))
print(f.dequeue())
print(f, len(f))
print(f.dequeue())
print(f, len(f))
print(f.dequeue())
print(f, len(f))
print(f.dequeue())
print(f, len(f))
#f.dequeue()

#Questão 2
class TreeNode:
  def __init__(self, val=0):
    self.val = val
    self.left = None
    self.right = None
  def height(self):
    if self.left is None and self.right is None:
      return 0
    else:
      h = 1 + max(self.left.height(), self.right.height())
    return h
def balanceada(tree):
  if tree.left is None and tree.right is None:
    return True
  else:
    l = tree.left.height()
    r = tree.right.height()
    if abs(l-r)>1:
      return False
    else:
      a = balanceada(tree.left) and balanceada(tree.right)
      return a
T = TreeNode()
print(balanceada(T))

#Questão 3
class TreeNode:
  def __init__(self, val=0):
    self.val = val
    self.left = None
    self.right = None
def inOrder(tree, list):
  if tree.left is not None:
    inOrder(tree.left, list)
  list.append(tree.val)
  if tree.right is not None:
    inOrder(tree.right, list)
  return list
def bread(tree, list, queue):
  list.append(tree.val)
  if tree.left is not None:
    queue.enqueue(tree.left)
  if tree.right is not None:
    queue.enqueue(tree.right)
  if len(queue) != 0:
    d = queue.dequeue()
    bread(d, list, queue)
  return list
T = TreeNode()
l = []
b = []
q = Fila()
print(inOrder(T, l))
print(bread(T, b, q))
print("Vantagem:")
print("As árvores podem representar uma estrutura hierárquica muito dificilmente representada em uma lista.")
print("Desvantagem:")
print("As árvores são estruturas complexas que precisam de mais espaço na memória do que listas.")
print()

#Questão 4
print("a)")
print("Partindo da classe TreeNode da questão 2")
print("Eu adicionaria uma propiedade que seria uma lista de nós, para substituir o self.left e o self.right da classe atual")
print("Para saber o número de filhos de cada nó basta saber o len da lista")
print("b)")
print("Para adicionar um novo filho basta dar append na lista")
print("c)")
print("Para percorrer em profundidade podemos usar um algoritmo similar ao pre-order")
print("Primeiramente adicionando a raiz e depois percorrendo recursivamente as árvores de cada filho listado")
print("Para percorrer em largura podemos usar um for para incluir todos os filhos de um nó na fila")
class TreeNode:
  def __init__(self, val=0):
    self.val = val
    self.sons = []
    self.degree = len(self.sons)
  def insert_node(self, val=0):
    self.sons.append(TreeNode(val=val))
def preOrder(tree, list):
  list.append(tree.val)
  for a in range(len(tree.sons)):
    preOrder(tree.sons[a],list)
  return list
def bread(tree, list, queue):
  list.append(tree.val)
  for a in range(len(tree.sons)):
    queue.enqueue(tree.sons[a])
  if len(queue) != 0:
    d = queue.dequeue()
    bread(d, list, queue)
  return list
l = []
b = []
q = Fila()
T = TreeNode(val=2)
T.insert_node(val=1)
T.insert_node(val=3)
T.sons[0].insert_node()
print(len(T.sons))
print(len(T.sons[0].sons))
print(len(T.sons[1].sons))
print(preOrder(T, l))
print(bread(T, b, q))
print()

#Questão 5
class TreeNode:
  def __init__(self, val=0):
    self.val = val
    self.left = None
    self.right = None
def inOrder(tree, list):
  if tree.left is not None:
    inOrder(tree.left, list)
  list.append(tree.val)
  if tree.right is not None:
    inOrder(tree.right, list)
  return list
def aparo(tree, low, high):
  if tree.val < low:
    if tree.right is not None:
      return aparo(tree.right, low, high)
    else:
       return None
  if tree.val > high:
    if tree.left is not None:
      return aparo(tree.left, low, high)
    else:
       return None
  if tree.left is not None:
    tree.left = aparo(tree.left, low, high)
  if tree.right is not None:
    tree.right = aparo(tree.right, low, high)
  return tree
T = TreeNode(val=1)
l = 0
h = 2
v = []
A = aparo(T, l, h)
print(inOrder(A, v))
