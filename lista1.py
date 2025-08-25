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
"""
Tome $n^2 + 1000n = g(n)$ e $n^2 = f(n)$, para $N = 100$ temos:

$g(n) \le cf(n)$

$n^2 + 1000n \le c(n)^2$

$100^2 + 1000\times100 \le c(100)^2$

$10.000 + 100.000 \le 10.000c$

$\frac{110.000}{10.000} \le c$

$c = 11$

Ou seja, $n^2 + 1000n = O(n^2)$ com $N = 100$ e $c = 11$

Tomando $c = 2$ e $N = 1000$, temos:

$1000^2 + 1000\times1000 \le 2(1000)^2$

$1.000.000 + 1.000.000 \le 2\times1.000.000$

$2.000.000 \le 2.000.000$

Tomando $c = 101$ e $N = 10$, temos:

$10^2 + 1000\times10 \le 101(10)^2$

$100 + 10.000 \le 101\times100$

$10.100 \le 10.100$

Tomando $c = 1001$ e $N = 1$, temos:

$1^2 + 1000\times1 \le 1001(1)^2$

$1 + 1000 \le 1001\times1$

$1001 \le 1001$
"""
#Questão 4
"""
Por definição: $g$ é $O(f)$ quando existem $N \in \mathbb{N}$ e $c \in R_*^+$ tais que $g(n) \le cf(n)$ para todo $n \ge N$.

Tomando $c = \frac{1}{c}$ e multiplicando ambos os lados por c, temos:

$cg(n) \le \frac{cf(n)}{c}$

$f(n) \ge cg(n)$

Note que essa é a definição de $\Omega(g)$:

$f$ é $\Omega(g)$ quando existem $N \in \mathbb{N}$ e $c \in R_*^+$ tais que $f(n) \ge cg(n)$ para todo $n \ge N$.
"""
#Questão 5
"""
Por definição: $g$ é $\theta(f)$ quando $g$ é $O(f)$ e $g$ é $\Omega(f)$.

Pelo resultado da questão anterior: Se $g$ é $O(f)$ então $f$ é $\Omega(g)$ e se $g$ é $\Omega(f)$ então $f$ é $O(g)$

Note que essa é a definição de $\theta(g)$: $f$ é $\theta(g)$ quando $f$ é $O(g)$ e $f$ é $\Omega(g)$
"""
