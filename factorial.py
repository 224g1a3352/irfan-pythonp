num=int(input("Enter a number:"))
fact=1
if num<0:
    print("NN")
elif num==0:
    print("Zero")
else:
    for i in range(1,num+1):
        fact=fact*i
    print("factorisl of given number:",fact)
