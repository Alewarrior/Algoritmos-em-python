# Faça um programa onde o usuário informe a km no  momento que o tanque é cheio, no próximo abastecimento o usuário
#  deve informar os km percorridos e a quantidade de combustível necessária para completar o tanque (l). O sistema deve
# informar a o consumo médio (km/l).

## calcular consumo baseado na km do veiculo e litros de combustivel


print("Calcule o consumo de seu percurso")

consumo=0


km=int(input("Informe quantos quilometros foram percorridos"))
litro=int(input("Informe quantos litros foram consumidos"))
consumo=km/litro
print("O consumo médio é ",consumo,"km/l")
