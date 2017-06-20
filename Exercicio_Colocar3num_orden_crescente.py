# 3 numeros em ordem crescente

print("Coloque 3 números em ordem crescente !")

n1=int(input("Digite o primeiro: "))
n2=int(input("O segundo: "))
n3=int(input("E agora o terceiro: "))

if n1 > n2 and n2 > n3:
        print ("A sequência é %s"%n3,n2,n1)
elif n2 > n3 and n3 > n1:
        print ("A sequência é %s"%n1,n3,n2)
elif n3 > n1 and n1 > n2:
        print ("A sequência é %s"%n2,n1,n3)
elif n2 > n1 and n1 > n3:
        print ("A sequência é %s"%n3,n1,n2)
elif n3 > n1 and n2 > n1:
        print ("A sequência é %s"%n1,n2,n3)
elif n1 > n3 and n3 > n2:
        print ("A sequência é %s"%n2,n3,n1)
