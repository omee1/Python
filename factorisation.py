def fact(n):
    fac=1
    for i in range (n):
        fac=fac*(i+1)
    return fac
num=int(input("enter the no \n"))
print(fact(num))

def fact1(n):
    if n==1:
        return 1
    else:
        return n* fact1(n-1)
print(fact1(num))