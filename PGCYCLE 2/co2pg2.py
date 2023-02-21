#2. Generate Fibonacci series of N terms
n = int(input("Enter a number:"))
l = [0,1]
for i in range(n-2):
    s = l[i]+l[i+1]
    l.append(s)
print("Fibonacci:")
print(l)