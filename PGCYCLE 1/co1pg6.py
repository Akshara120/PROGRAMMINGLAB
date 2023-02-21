#6. Store a list of first names. Count the occurrences of ‘a’ within the list
names=['akshara','akshaya','krishna','chinnamma']
count=0
for name in names:
    count=count+name.count('a')
print("the occurrence of 'a' is:",count)