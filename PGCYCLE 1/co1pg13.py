#13. Create a list of colors from comma-separated color names entered by user. Display
# first and last colors.

n=int(input("Limit:"))
a=[]
for i in range(n):
    b=input("Enter the color name:")
    a.append(b)
print(a)
print(a[0],a[-1])