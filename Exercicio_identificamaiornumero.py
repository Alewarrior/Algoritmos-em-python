## identifica maior numero

print("Maior número digitado.")

n=0
m=0
x=0

while (x < 10):
    n=int(input("Entre com um número: "))
    x=x+1
    if (n > m):
        m=n
print ("O maior número é:",m)
