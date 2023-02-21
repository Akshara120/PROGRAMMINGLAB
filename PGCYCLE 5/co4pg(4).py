import pandas as p
s=p.read_csv("studentsdetails.csv",usecols=["NAME","CLASS"])
print("Student Name and Address  : ")
print(s)
#speacif coloumn
'''import pandas as p
s=p.read_csv("studentsdetails.csv")
spec_col=s(["NAME","ROLL NO"])
print("Student Name and Roll no : ")
print(spec_col)'''