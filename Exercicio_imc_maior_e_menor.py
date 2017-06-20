## maior e menor IMC de alunos


quant = int(input("Digite a quantidade de aluno: "))
x = 0
n = []
soma_imc = 0
soma_altura = 0
soma_peso = 0
media_imc = 0
media_altura = 0
media_peso = 0
imc = 0
nome_maior = 0
nome_menor = 0
globalIMC = 0

for x in range(quant):
    nome = str(input('Digite seu nome: '))
    peso = float(input("Digite seu peso: "))
    altura = float(input("Digite sua altura: "))
    imc = peso /(altura*altura)
    print("     Seu imc é: ",imc)

    if x == 0:
        maiorIMC = imc
        menorIMC = imc
        nome_maior = nome
        nome_menor = nome

    if imc > maiorIMC:
       maiorIMC = imc
       nome_maior = nome

    if imc < menorIMC:
        menorIMC = imc
        nome_menor = nome


    soma_imc = soma_imc + imc
    soma_altura = soma_altura + altura
    soma_peso = soma_peso + peso



media_imc = soma_imc / quant
media_altura = soma_altura / quant
media_peso = soma_peso / quant

print('          o(a) aluno(a) com maior IMC é : ',nome_maior)
print('          o(a) aluno(a) com menor IMC é : ',nome_menor)
print('          A média do imc é: ',media_imc)
print('          A média da altura é: ',media_altura)
print('          A média do peso é: ',media_peso)


