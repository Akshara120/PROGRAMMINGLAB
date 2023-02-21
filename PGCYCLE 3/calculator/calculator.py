import myfunctions as f
a=int(input("enter first number:"))
b=int(input("enter second number:"))
option=int(input("Enter your option:1-addition.2-substraction.3-multiplication.4-division\n"))
if option==1:
    print(a,"+",b,"=",f.sum(a,b))
elif option==2:
    print(a,"-",b,"=",f.substract(a,b))
elif option==3:
     print(a,"*",b,"=",f.multiple(a,b))
elif option==4:
    print(a,"/",b,"=",f.division(a,b))
else:
    print("Invalid option")
    