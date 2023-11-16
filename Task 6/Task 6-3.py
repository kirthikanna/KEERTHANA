# Given a Python List [10,501,22,37,100,999,87,351] Find out how many numbers are there in the given Python List which are Happy numbers?

a=[10,501,22,37,100,999,87,351]
b=len(a)
res=0
rem=0
n=0
for i in range(b):
    n=a[i]
    while n > 0:
        rem=n%10
        res=res+rem*rem
        n=n//10
    if res!=1:
        print("not happynumbers",a[i])
    else:
        print("happynumbers :",a[i])
     
