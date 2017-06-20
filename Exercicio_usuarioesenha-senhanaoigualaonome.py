#  criar usuario e senha, senha nao igual ao usuario e confirmacao

n1=input("digite um nome de usuario")
n2=input("digite uma senha")

while n2 == n1:
    print ("senha invalida")
    n2=input("digite uma senha (diferente do nome de usuario)")
n3=input("confirme a senha")
while n3 != n2:
    print ("confirmacao de senha invalida")
    n3=input("confirme a senha")

print ("usuario e senha criados")
