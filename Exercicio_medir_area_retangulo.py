# Medir area de um retangulo

print("Quantos métros quadrados tem um cômodo?")

n1=int(input("Digite medida de um lado: "))
n2=int(input("Medida do outro lado: "))

mq=n1*n2

if n1==n2:
    print("O cômodo é quadrado, e sua área é: %s m²"%mq)
else:
    print ("A área do cômodo retângulo é: %s m²"%mq)
