#given string is anagram or not
str1=input("enter the string1")
str2=input("enter the string2")
sort1=sorted(str1)
sort2=sorted(str2)
if len(str1) == len(str2):
    if sort1 == sort2:
        print("given strings are anagram")
    else:
        print("given strings are not anagrams")