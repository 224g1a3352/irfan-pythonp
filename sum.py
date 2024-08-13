'''num=int(input("Number:"))
sum=0
while num>0:
    rem=num%10
    sum=sum+rem
    num=num//10
    print(sum)
def add(a,b,max=100):
    print(a)
    print(b)
    print(max)
    C=a+b+max
    print(C)
add(10,20)
def var(*X):
    print(X[2])
    print(X[1])
var(12,145,98,"Python")
def myfun(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}=={value}")
myfun(first="WELCOME",mid='TO',last='SRIT')
def f():
    s='k\n'
    def f2():
        print(s*100)
    f2()
f()
double=lambda x:2*x
print(double(5))'''
big=lambdax,y: x if x>y else y print(big(10,20))
