

''''''

n=int(input("Digite um número para sequencia de Fibonacci: "))
i=int(input("Digite o valor máximo para o intervalo: "))
def fibonacci(n):

    a, b = 0, n

    while b < i:

         print (b),
         a, b = b, a+b



print(fibonacci(n))
