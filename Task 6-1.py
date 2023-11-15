# You have been given Python List[10,501,22,37,100,999,87,351] your task is to create two List one which have all the Even Numbers and another List which will have all the ODD numbers in it?
list=[10,501,22,37,100,999,87,351]
evenlist =[]
oddlist  =[]
for no in list:
    if no%2 == 0:
       evenlist.append(no)
    else:
        oddlist.append(no)
print("evenlist: ",evenlist)
print("oddlist: ",oddlist)           

