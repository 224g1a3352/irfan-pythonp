#f=input("enter file name:")
f1=open("textfile.txt",'w')

f1.write("irfan is a good boy")
f1.close()
f2=open("textfile.txt",'r')
print("*****Text in a file****")
print(f2.read())
f2.seek(0)
f3=open("textfile2.txt",'w')
char=input("enter a character:")
count=0
rc=-1
while(rc):
    rc=f2.read(1)
    if rc==char:
        count+=1
    else:
        f3.write(rc)
f2.close()
f3.close()
print("total characters:",char,count)
f4=open("textfile2.txt",'r')
print("***text after eliminating*****")
print(f4.read())
f4.close()

      
