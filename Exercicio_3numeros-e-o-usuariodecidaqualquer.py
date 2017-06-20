# faça um algortmo que receba 3 números inteiros e o usuário decida quais das opções o sistema deve retornar:



# soma
n=input("digite seu nome: ")

print("Digite 3 números, "+n)

n1=float(input("Digite N1: "))
n2=float(input("Digite N2: "))
n3=float(input("Digite N3: "))
op=int(input("Selecione uma das opções =  Soma  [1] -  Maior  [2] -  Menor  [3] -  Media  [4]"))
s=(n1+n2+n3)

# exibir maior número digitado

if n1>n2 and n1>n3:
    ma=n1
if n2>n1 and n2>n3:
    ma=n2
if n3>n1 and n3>n2:
    ma=n3



# exibir menor numero digitado
if n1<n2 and n1<n3:
    me=n1
if n2<n1 and n2<n3:
    me=n2
if n3<n1 and n3<n2:
    me=n3


# calcular média

med=(n1+n2+n3)/3


if op==1:
    print ("A soma é: ",s)
if op==2:
    print ("O maior número é: ",ma)
if op==3:
    print ("O menor número é: ",me)
if op==4:
    print(" A média é",med)

