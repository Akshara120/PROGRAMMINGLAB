#1.Program to find the factorial of a number

n = int(input("Enter a number:"))
fact =1
for i in range(1,n+1):
    fact= fact*i
print("Factorial of",n,":",fact)
#using Recurssive functon
'''def factorial(x):
    if x == 1:
        return 1
    else:
        return(x*factorial(x-1))
n = int(input("Enter a number:"))
print("Factorial of",n,":",factorial(n))'''