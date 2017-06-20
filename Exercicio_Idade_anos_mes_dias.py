n=input("Digite seu nome: ")
print("Olá, "+n)
data=input("Informe a data de seu nascimento (com barras) [dd/mm/aaaa] -->")
print(len(data))
print (data[0:2])
print (data[3:5])
print (data[6:10])

ano=int(data[6:10])

idade=2017-ano
print("Você tem %s anos" %(idade))
