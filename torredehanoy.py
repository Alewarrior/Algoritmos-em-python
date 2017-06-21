def hanoi(ndiscos, inicioPeg=1, fimPeg=3):
    if ndiscos:
        hanoi(ndiscos-1, inicioPeg, 6-inicioPeg-fimPeg)
        print ("Mova o disco %d  do pino %d para o pino %d" % (ndiscos, inicioPeg, fimPeg))
        hanoi(ndiscos-1, 6-inicioPeg-fimPeg, fimPeg)

hanoi(ndiscos=3)
