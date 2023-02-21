#Sort dictionary in ascending and descending order. 
dic={'carl':40,'alan':2,'bob':1,'danny':3} 
print(dic)                                         
s=sorted(dic.items())
print("Ascending order is:",s)
s2=sorted(dic.items(),reverse=True)
print("Descending order is:",s2)