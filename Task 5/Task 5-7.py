# takes the string and returns to the most frequenct character in it?
str=input("enter the string")
a=dict()
b=0
for i in str:
    if i in a:
        a[i]=a[i]+1
        print(a[i])
    else:
        a[i]=1
b=max(a,key=a.get)
#print(a)
print("most frequent characters in it:", b)
