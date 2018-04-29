def fib(n):
    lst=[0,1]
    a=0
    b=1
    for i in range(0,n-1):
        b=a+b
        a=b-a
        lst.append(b)
    return lst

print(fib(100))