
'''def ponp(n):
    if n<2:
        return "NOt prime"
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return "NOt prime"
    return "Prime"
print("Enter valid")
num=int(input("enter a number: "))
print(ponp(num))
def reverse(s):
    print(s[::-1])
String=input("Enter a string:")
print(reverse(String))
def fib(n):2
    a,b=0,1
    temp=1
    for i in range(n):
        print(a)
        a,b=b,a+b
n=int(input("Enter number: "))
fib(n)
def maxi(a):
    print(max(a))
a=list(map(int,input("enter the array elements: ").split()))
print(maxi(a))
n=int(input())
print(str(n)[::-1])
n=input()
j=n[::-1]
if j==n:
    print("palindrome")
else:
    print("not a palindrome")'''
n=list(map(int,input("enter the array elements: ").split()))
print(n)
es=0
os=0
for i in range(len(n)):
    if n[i]%2==0:
        es=es+n[i]
    else:
        os=os+n[i]
print(es,os,end=' ')


