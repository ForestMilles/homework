def find2(string, ch, start=0, end=None):
    ix = start
    if end is None:
        end = len(string)
    while ix < len(string):
        if string[ix] == ch:
            return ix
        ix += 1
    return -1


print (find2("banana", "a", 3, 4))



def count_letters(text, letter):
    count = 0
    for c in text:
        if c == letter:
            count += 1
    return count


print(count_letters("banana", "n") == 3)
test(count_letters("banana", "b") == 1)