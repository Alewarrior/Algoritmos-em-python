def operacao_troco (vp, vc):
    troco=0
    ced = [50, 20, 5, 2, 1]
    troco=vp-vc
    numNotas = []

    ced.sort()
    ced.reverse()
    for i in ced:
        numNotas.append(troco/i)
        troco %= i

    for i in range(len(ced)):
        if numNotas[i]>=1:
            print ("Número de notas: %d - %d"%(numNotas[i], ced[i]))

vc=int(input("Valor da Compra : "))
vp=int(input("Valor pago : "))
print(operacao_troco(vp, vc))