#write a function that takes a string and returns the number of words in it
str=input("enter the string")
count=1
for i in str:
    if i == ' ' :
        count=count+1
print("THE NUMBER OF WORDS",count)