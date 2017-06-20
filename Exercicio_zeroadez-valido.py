# nota entre 0 e 10 e que continue pedindo


n=int(input("Digite um número válido"))

while n > 10 or n < 0:
    print ("invalido")
    n=int(input("Digite um número válido"))

print ("parabens")
