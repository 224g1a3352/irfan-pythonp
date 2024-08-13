f=input("Enter file name:")
f1=open(f,'w')
f1.write("Hello")

f1=open(f,"r")

print(f1.read())
f1.close()
f1=open(f,"a+")
f1.write("stay home stay safe")
f1.close()
f1=open(f,"r")
print(f1.read())
f1.close()
