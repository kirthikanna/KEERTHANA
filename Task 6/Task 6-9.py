# You have been given a python list[10,20,30,9] and a value of 59. Write a python program to find the triplet in the list whose sum is equal to the given value?
list=[10,20,30,9]
a=len(list)
value=59
for i in range(a):
    f=list[i]
    for j in range(i+1,a):
        s=list[j]
        for k in range(i+2,a):
            t=list[k]
            sum1=f+s+t
            if sum1 == value:
                print("THE TRIPLET OF THE LIST EQUAL TO THE value IS",[f,s,t])