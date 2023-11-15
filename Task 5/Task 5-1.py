#WRITE A FUNCTION THAT TAKES A STRING AND RETURNS A NEW STRING WITH ALL THE VOWELS REMOVED?
str= input("enter the string")
vowel='a,e,i,o,u,A,E,I,O,U'

for i in str:
    if i in vowel:
        str=str.replace(i,"")
print(str)      