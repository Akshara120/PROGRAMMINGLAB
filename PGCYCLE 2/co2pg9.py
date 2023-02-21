'''#Construct following pattern using nested loop
n = int(input("Enter the limit:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print("\n")

for i in range(n-1,0,-1):
    for j in range(i,0,-1):
        print("*",end=" ")
    print("\n")


for i in reversed(range(1,n+1)):
    for j in reversed(range(1,i+1)):
        print("*",end=" ")
    print("\n")'''
    
    #9. Construct following pattern using nested loop
n=int(input("entr a limit:"))
for i in range(0,n+1):
    for j in range(0,i):
        print("*",end="")
    print("\n")
for i in reversed(range(0,n)):
    for j in reversed(range(0,i)):
        print("*",end="")
    print("\n")
    