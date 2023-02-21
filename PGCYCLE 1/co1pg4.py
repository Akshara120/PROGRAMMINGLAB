#4. Count the occurrences of each word in a line of text.
text="the quick brown fox jump over the lazy dog"
words={}
text=text.split(" ")
for word in text:
    if word in words:
        words[word]+=1
    else:
        words[word]=1
print(words)
