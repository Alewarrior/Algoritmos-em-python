# infantil A 5 a 7 - infantil B 8 a 10 - juvenil A 11 a 13 - juvenil B 14 a 17 - adulto 18 ou mais

print ("Pesquisa de categoria de nadadores")

print (" ")

categ1=("Infantil_A")
categ2=("Infantil B")
categ3=("Juvenil A")
categ4=("Juvenil B")
categ5=("Adulto")

data=input("Informe a data de seu nascimento do nadador(com barras) [dd/mm/aaaa] -->")

print (data[0:2])
print (data[3:5])
print (data[6:10])

ano=int(data[6:10])

idade=2017-ano

if idade>7:
    sit=categ2
else:
    categ1

if idade>10:
    sit=categ3
else:
    categ2

if idade>13:
    sit=categ4
else:
    categ3

if idade>17:
    sit=categ5
else:
    categ4

print("O nadador tem %s anos" %(idade))
print ("Então ele se encaixa na categoria %s"%(sit))

