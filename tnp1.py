'''s="Welcome to srit"
print(s[:5])
print(s[2:5])
print(s[::])
print(s[1:3:2])
print(s[-12:-2])
s="Hot"
s1="It is summer"
print(s1[0:6]+s+s1[5:])
a=int(input())
b=int(input())
c=int(input())
if a>b and b>c:
    print("a is greter")
elif b>c:
    print("b is greater")
else:
    print("c")
marks=int(input())
if marks>=90:
    print("A")
elif marks>=80:
    print("B")
elif marks>=70:
    print("C")
elif marks>=60:
    print("D")
elif marks<60:
    print("F")
else:
    print("Invalid")
for i in range(6,10):
    print(i)'
n=int(input())
while(n<=10):
      print(n)
      n=n+1
i=[1,3,7,10,11]
k=10
for j in range(len(i)):
    print(i[j])'''
a=int(input())
while a<6:
    print("hi")
    a=a+1
print("no")
