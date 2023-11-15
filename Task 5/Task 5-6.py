#takes two string and returns longest common substring between them?
str1=input("enter the string1")
str2=input("enter the string2")
list1=[]
list2=[]
common=[]
list1=str1.split(" ")
list2=str2.split(" ")
n=len(list1)
n1=len(list2)
for i in  range(n):
    for j in range(n1):
        if list1[i] == list2[j]:
             common.append(list1[i])
print("the longest common substring is:",common)