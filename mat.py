m=int(input('enter how many rows for matrix-A,m='))
n=int(input('enter how many columns for matrix-A,n='))
p=int(input('enter how many rows for matrix-B,p='))
q=int(input('enter how many columns for matrix-B,q='))
if m!=p and n!=q:
    print("addition not possible")
else:
    a=[]
    b=[]
    c=[]
    print("enter values for matrix-A")
    for i in range(m):
        row=[]
        for j in range(n):
            x=int(input(f"entry in row:{i+1} columns:{j+1}\n"))
            row.append(x)
        a.append(row)
    print("Enter values for matrix-B")
    for i in range(p):
        row=[]
        for j in range(q):
            x=int(input(f"entry in row:{i+1} columns:{j+1}\n"))
            row.append(x)
        b.append(row)
    for i in range(m):
        row=[]
        for j in range(n):
            row.append(a[i][j]*b[i][j])
        c.append(row)
    print("Matrix a=",a)
    print("Matrix b=",b)
    print("final matrix c=",c)

            
                  

          





