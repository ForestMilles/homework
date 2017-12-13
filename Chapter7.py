"""Write a function to count how many odd numbers are in a list."""

mylist=[-3,-5,0,2,3,7,11,12]

def count_odd(numlist):
    count = 0
    for i in numlist:
        if i%2 != 0:
            count += 1
            
    return count

print(count_odd(mylist))

"""Sum up all the even numbers in a list."""

def sum_even(numlist):
    mysum=0
    for i in numlist:
        if i%2 == 0:
            mysum = mysum +i
            
    return mysum

print(sum_even(mylist))

"""Sum up all the negative numbers in a list."""


def sum_negative(numlist):
    mysum = 0
    for i in numlist:
        if i < 0:
            mysum = mysum + i
    return mysum

print(sum_negative(mylist))

"""Count how many words in a list have length 5"""

wordlist=("How", "many" ,"fish" ,"does" ,"the" ,"little", "kid", "have")

def word_length(wordlist):
    words=0
    for words in wordlist:
        if 5 == len(i):
            words + 1
    return words

print(word_length(wordlist))

"""Sum all the elements in a list up to but not including the first even number.  (Write your unit tests. What if there is no even number?) 
"""

mylist=[-3,-5,0,2,3,7,11,12]

def sum_element(list):
    mysum=0
    for i in list:
        if i%2 != 0:
            mysum = mysum +i
        else:
            break
    return mysum

print(sum_element(list))

"""Count how many words occur in a list up to and including the first occurrence of the word “sam”. (Write your unit tests for this case too. What if “sam” does not occur?)"""
 
wordlistd=["How many fish does the little kid Sam have?"] 

def word_sam(list):
    mysum=0
    for i in list:
        if len(i) == 3:
            mysum = mysum + 1
    return mysum

print(word_sam(wordlistd))
    


