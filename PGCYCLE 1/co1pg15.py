#15. Print out all colors from color-list1 not contained in color-list2.
l1=["white", "black", "pink"]
l2=["white", "blue", "red"]
a=[x for x in l1 if x not in l2]
print(a)