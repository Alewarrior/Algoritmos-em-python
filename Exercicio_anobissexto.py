ano=int(input("Digite um ano para saber se e bissexto: "))
if (ano%4 == 0 and ano%100 != 0) or ano%400 == 0:
    print (ano, "e bissexto")
else:
    print (ano, "Nao e bissexto")
