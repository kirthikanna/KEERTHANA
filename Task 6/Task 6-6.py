
#You have been three lists. Your task is to find the duplicates in the three lists. Write a python program for the same. You can use your own python lists?
a=[1,2,3,1,1,1,4,5,6,6,6,7]
b=[3,5,4,6,7,7,7,7,7,8]
c=[9,9,9,10,2,2,5,6,10]
d=b+c+a
nonrep=[]
dup=[]
for i in d:
    if i not in nonrep :
        nonrep.append(i)
    else:
        dup.append(i)
print("THE NON REPEATED ELEMENTS IN THE LIST",nonrep)
print("THE DUPLICATE ELEMENTS IN THE LIST",dup)
