f1_obj=open("sample.txt",'r')
r1=f1_obj.readlines()
print("File line by line in list : ")
print(r1)
print("\n\n")
#to remove newline characters
r1=[x.strip() for x in r1]
print("File line by line,post removing newline : ")
print(r1)

