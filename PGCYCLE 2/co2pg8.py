#Accept a list of words and return length of longest word
l =['Accept','list','of','words','returning','length','longest','word']
long = 0
for i in l:
    if len(i) > long:
        long= len(i)
print("length of longest word",long)