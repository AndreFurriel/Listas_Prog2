#Questão 1
def hanoi(n,origem,trabalho,destino):
    if n==1:
        print("Mover disco 1 da pilha",origem,"para a pilha",destino)
    else:
        hanoi(n-1,origem,destino,trabalho)
        print("Mover disco",n,"da pilha",origem,"para a pilha",destino)
        hanoi(n-1,trabalho,origem,destino)
#Chamando a função
n=int(input("Número de discos:"))
a=input("Nome da pilha da esquerda:")
b=input("Nome da pilha do centro:")
c=input("Nome da pilha da direita:")
hanoi(n,a,b,c)
#Questão 2
#Fibonacci kk
def escada(n):
    s=0
    if n==1:
        return 1
    elif n==2:
        return 2
    else:
        s=s+escada(n-1)
        s=s+escada(n-2)
        return s
n=int(input("Número de degraus:"))
print(escada(n))
#Questão 3
