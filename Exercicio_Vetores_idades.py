x=int(input("Informe Quantas idades vai digitar? "))
cont=0
Maior=0
menor=1000
i=[]
while (cont<x):
    i.append(int(input("Informe a idade")))
    print (i)
    print (Maior)
    print (menor)
    if(i[cont]>Maior):
        print(i)
        Maior = int(i[cont])
    if(i[cont]<menor):
        menor = int(i[cont])
    cont=cont+1
print(Maior)
print(menor)
