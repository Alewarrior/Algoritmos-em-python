#2 Vetores/
#com Login e senha/
#Sortear um Login e exibir o Login/
#Um usuário deve digitar a senha correspondente ao login sorteado
#SE acertar exibe a msg "Acesso Liberado"
#O Sistema só pode permitir 3 tentativas
 
 
from random import randint
 
l = ["Alessandro", "Erika", "Fabiano", "Emanuel", "Daniel"]
s = ["Alessandro123", "Erika123", "Fabiano123", "Emanuel123", "Daniel123"]
x=randint(0,4)
cont=0
print(l[x])
while cont<3:
   senha=input("digite a senha:")
   if senha==s[x]:
       print("Acesso Liberado")
       break
   cont=cont+1