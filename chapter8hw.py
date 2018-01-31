""" Modify:

prefixes = "JKLMNOPQ"
suffix = "ack"

for letter in prefixes:
    print(letter + suffix)


so that Ouack and Quack are spelled correctly.
"""

def prefix():
    prefixes = "JKLMNOPQ"
    suffix = "ack"

    for letter in prefixes:
        if letter == "O" or letter == "Q":
            print(letter + "u" + suffix)
        else:
            print(letter + suffix)

prefix()
