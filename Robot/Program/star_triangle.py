def fib(n):
    a=0
    b=1
    count=0
    if n==0:
        print(a)
    elif n==1:
        print(b)
    while count<n:
        print(a)
        c=a+b
        a=b
        b=c
        count+=1

fib(5)
