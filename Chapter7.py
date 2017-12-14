import sys
import turtle
wn = turtle.Screen()
s = turtle.Turtle()

mylist=[-3,-5,0,2,3,7,11,12]
wordlist=["How", "many" ,"fish" ,"does" ,"the" ,"little", "child", "kid", "have"]
samlist={"How", "sam", "many", "fish", "does", "the", "little" ,"kid","have?"}


def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)
    
def test_suite():
    """run the suite of tests for code in this module (this file)"""
    print("tests for 5 words")
    
    print("\ncount_odd")
    test(count_odd(mylist)==5)
    
    print("\nsum_even")
    test(sum_even(mylist)==14)
    
    print("\nsum negative")
    test(sum_negative(mylist)==-8)
    
    print("test for number of words that have wordlength 5")
    test(word_length(wordlist) == 1)
    
    print("test for sum of even exept first one (#5)")
    test(sum_element(mylist) == -8)
    
    print("test for sam")
    test(word_sam(samlist) == 1)
    
    print("\nis_prime")
    test(is_prime(11))
    test(not is_prime(35))
    test(is_prime(19911121))
    test(is_prime(19701013))
    
    
"""Write a function to count how many odd numbers are in a list."""

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

def word_length(list):
    words=0
    for i in list:
        if 5 == len(i):
            words += 1
    return words

print(word_length(wordlist))

"""Sum all the elements in a list up to but not including the first even number.
    (Write your unit tests. What if there is no even number?) 
"""

def sum_element(list):
    mysum=0
    for i in list:
        if i%2 == 0:
            break 
        else:
            mysum +=i
    return mysum
print(sum_element(mylist))

"""Count how many words occur in a list up to and including the first occurrence
1of the word “sam”. (Write your unit tests for this case too. What if “sam” does notoccur?)"""

def word_sam(list):
    count =0
    for i in samlist:
        if len(i) == "sam":
            count += 1
            break
        count += 1
    return count

print(word_sam(samlist))

def sqrt(n):
    """Ex 7:Newtons square root function -"""
    approx = n/2.0     # Start with some or other guess at the answer
    while True:
        better = (approx + n/approx)/2.0
        print("better",better)
        if abs(approx - better) < 0.001:
            return better
        approx = better


print("sqrt",sqrt(25.0))

def is_prime(n):
    """Write a function, is_prime, which takes a single integer
    argument and returns True when the argument is a prime number and False otherwise"""
    for i in range(2,n):
        if n % i == 0:
            return False
    return True
    



test_suite()    