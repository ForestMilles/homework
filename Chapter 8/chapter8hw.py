import sys


def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


def test_suite():

    print("tests for Problem #7")
    test(reverse("happy") == "yppah")
    test(reverse("Python") == "nohtyP")
    test(reverse("a") == "a")

    print("test for Problem #8)")
    test(mirror("good") == "gooddoog")
    test(mirror("Python") == "PythonnohtyP")
    test(mirror("a") == "aa")
    test(mirror("berry") == ("berryyrreb"))

    print("tests for Problem 9")
    test(remove_letter("a", "apple") == "pple")
    test(remove_letter("a", "banana") == "bnn")
    test(remove_letter("z", "banana") == "banana")
    test(remove_letter("i", "Mississippi") == "Msssspp")
    test(remove_letter("b", "") = "")
    test(remove_letter("b", "c") = "c")

""" Modify:

prefixes = "JKLMNOPQ"
suffix = "ack"

for letter in prefixes:
    print(letter + suffix)


so that Ouack and Quack are spelled correctly.
"""


"""Pick any 5 exercises from numbers 3-13. Save them in a single file - comment each exercise with its number"""


#Problem #2

def prefix():
    prefixes = "JKLMNOPQ"
    suffix = "ack"

    for letter in prefixes:
        if letter == "O" or letter == "Q":
            print(letter + "u" + suffix)
        else:
            print(letter + suffix)


prefix()


#Problem 3


def count_letters(word, letter):
    count = 0
    for char in word:
        if char == letter:
            count += 1
    return count


print(count_letters("soup", "o"))


count_letters("word", "letter")

#Problem 4


def count_letters(string,char):
    result = -1
    count = 0
    while 1:
        result = string.find(char,result+1)
        if result == -1:
            break
        count +=1
    return count


print(count_letters("aacbasbaab","a"))

#Problem 7


def reverse(word):
    reversed = ""
    for i in range(len(word)-1, -1, -1):
        reversed += word[i]
        return reversed

#Problem 8


def mirror(word):
    mirrored = word + reverse(word)
    return mirrored


print (mirror("happybirthday"))

#Problem 9


def remove_letter(char,text):
    charremovedtext = ""
    for letter in text:
        if letter != char:
            charremovedtext += letter
    return charremovedtext
print(remove_letter("a","banana"))


test_suite()