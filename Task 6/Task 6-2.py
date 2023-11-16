# Given a Python List [10,501,22,37,100,999,87,351] your task is to Count all the Prime Numbers and create a new Python List which willcontain all the Prime Numbers in it?
list=[10,501,22,37,100,999,87,351]
primelist=[]
for no in list:
    for m in range(2,(no//2+1)):
        if no%m==0:
            break
    else:
        print('prime no',no)
        primelist.append(no)
        print(primelist)
        
