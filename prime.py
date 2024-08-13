num=int(input("Number:"))
for i in range(2,num+1):
    isprime=True
    for num in range(2,i):
        if i%num==0:
            isprime=False
            break
    if isprime:
        print(i)
