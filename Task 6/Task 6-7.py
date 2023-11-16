#PROGRAM TO FIND THE FIRST NON REPEATING ELEMENT IN THE LIST
def count(l, n):

   
   a = [False for i in range(n)]


   
   for i in range(n):

     
     if (a[i] == True):
        continue

     
     count = 1
     for j in range(i + 1, n, 1):
        if (l[i] == l[j]):
          a[j] = True
          count += 1
     if count == 1 :
        print(l[i]);
   


l = [1,2,3,3,5,5,7,8,9,4,4]
n = len(l)
count(l, n)