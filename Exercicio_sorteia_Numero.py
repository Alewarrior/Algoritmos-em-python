# adivinhação
print ("Adivinhação")

i=0

n1=int(input(("Oi, amigo 1. Digite um número chave entre 0 e 10 para outra pessoa adivinhar: ")))
# n2=float(input("Adivinhe qual é o número chave:"))
# n3=float(input("Adivinhe qual é o número chave:"))
# n4=float(input("Última chance, adivinhe qual é o número chave:"))

while i<3:
	n=input("Oi amigo 2. Adivinhação. Digite um número de 0 a 10: ")
	i=i+1
print("Suas tentativas foram: %s"%i)

if n == n1:
    print("Parabéns, você acertou. A responsta é %s."%n1)
else:
    print("Infelizmente você errou. A resposta é %s."%n1)

#
