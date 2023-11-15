#total count of vowels and individual element
str = 'guvi geeks private limited'
str=str.lower()
vowels=['a','e','i','o','u']
vc=0
for i in str:
    if i in vowels:
        vc=vc+1
print('total vowel count is',vc)
print('vowel count a is ',str.count('a'))
print('vowel count e is',str.count('e'))
print('vowel count i is ',str.count('i'))
print('vowel count a is ',str.count('o'))
print('vowel count a is ',str.count('u'))