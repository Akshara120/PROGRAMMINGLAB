'''7. Add ‘ing’ at the end of a given string. If it already ends with ‘ing’, then add ‘ly’ 
s = "Construct following pattern using nested loop"
c = "ing"
r = 'ly'
new=""
for i in s.split(" "):
    if i[-3:] == c:
        new = new+" "+i+r
    else:
        new = new+" "+i+c
        
print(new)


#7. Add ‘ing’ at the end of a given string. If it already ends with ‘ing’, then add ‘ly’
st=input("enter the string")
s = "ing"
for i in range(0,len(st)):
    if st[-3]=='i' and st[-2]=='n' and st[-1]=='g':
        print(st+"ly")
        break
    else:
        print(st+"ing")
        break '''


string = input("enter a string:")
if string.endswith('ing'):
    string += 'ly'
else:
    string += 'ing'
print(string)




"""string = input("enter a string:")
if string.endswith('ing'):
    string += 'ly'
elif len(string) >= 3:
    string += 'ing'
print(string)"""