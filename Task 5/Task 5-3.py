#WRITE A FUNCTION THAT TAKES A STRING AND RETURNS THE NUMBER OF UNIQUE CHARACTERS IN IT?
string=input("enter the string")
unique_characters = []
for i in string:
    if i not in unique_characters:
       unique_characters.append(i.lower())
print("the list of unique_characters is:{}".format("".join(unique_characters)))