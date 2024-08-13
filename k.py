t=input("Enter:")
d=int(t[:-1])
i=t[-1]
if i.upper()=='C':
    r=int(round(d*9)/5+32)
    h='Fahrenhiet'
elif i.upper()=='F':
    r=int(round(d-32)*5/9)
    h='Celsius'
else:
    print("enter valid")
    quit()
print("in",h,"is",r)
