#5.Prompt the user for a list of integers. For all values greater than 100, store ‘over’ instead
n=int(input("enter the number of element:"))
list2=[]
for a in range(n):
    a=int(input("enter the number :"))
    if a>=100:
        list2.append("over")
    else:
        list2.append(a)
print("the output:",list2)
    