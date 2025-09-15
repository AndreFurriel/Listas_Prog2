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

#Questão 4

#Questão 5
