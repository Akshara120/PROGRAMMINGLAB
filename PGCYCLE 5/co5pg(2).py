f1=open("sample.txt",'r')
f2=open("new.txt",'w')
lines=f1.readlines()
for i in range(0,len(lines)):
    if i%2!=0:
        l=f2.write(lines[i])
f1.close()
f2=open("new.txt",'r')
content=f2.read()
print(content)
f2.close()