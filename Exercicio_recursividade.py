def fib(i):
    if i==1: return 0
    elif (i==2): return 1
    else: return fib(i-1)+fib(i-2)
for i in range(1,11):
    print (fib(i))
