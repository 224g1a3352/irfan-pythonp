A=[]
print("enter values for matrix - A")
m=int(input('enter how many rows for matrix-A,m='))
n=int(input('enter how many columns for matrix-A,n='))
for i in range(m):
    matrix=[]
    for j in range(n):
        print("enter row:{} column:{}".format(i+1,j+1))
        matrix.append(int(input()))
    A.append(matrix)
B=[]
print("Enter values for matrix - B")
p=int(input('enter how many rows for matrix-B,m='))
q=int(input('enter how many columns for matrix-B,n='))
for i in range(p):
    matrix=[]
    for j in range(q):
        print("enter row:{} column:{}".format(i+1,j+1))
        matrix.append(int(input()))
    B.append(matrix)
print("matrix - A={}".format(A))
print("matrix - B={}".format(B))
if(n==p):
    result=[[0 for i in range(q)]for j in range(m)]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j]+=A[i][k]*B[k][j]
print("Matrix - A * Matrix- B = ",result)
                   
        
