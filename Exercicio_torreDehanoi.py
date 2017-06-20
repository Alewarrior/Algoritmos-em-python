
# torre de hanoi
"Implementação das torres de Hanói"
def hanoi(n, a=1, b=3):

    if n:
        hanoi (n-1, a, 6-a-b)
        print ("Move disco %d de %s para %s" % (n, a, b))
        hanoi (n-1, 6-a-b, b)
hanoi(n=4)
