"""
9. Describe the relationship between " ".join(song.split()) and song in the fragment of code below. Are they the same for
all strings assigned to song? When would they be different?

1
song = "The rain in Spain..."


answer: string.join(string.split(song)) uses all the words in the variable song by splitting the words into a list
 with each word as a different element. Furthermore, it takes the ltters in the words of the list and will separate it
 into a single character outside of the list. Both use a string but song only uses a string while string.join will use a
 string in a list. """



"""10. Write a function replace(s, old, new) that replaces all occurrences of old with new in a string s:"""
def replace(Str,old,new):
    strlist=[]
    strlist = Str.split(old)
    newstr=new.join(strlist)
    return(newstr)


print(replace("Mississippi", "i", "I") == "MIssIssIppI")

s = "I love spom! Spom is my favorite food. Spom, spom, yum!"
print(replace(s, "om", "am") ==
    "I love spam! Spam is my favorite food. Spam, spam, yum!")
print(replace(s, "o", "a") ==
    "I lave spam! Spam is my favarite faad. Spam, spam, yum!")