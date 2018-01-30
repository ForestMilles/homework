"""Write a function to count how many odd numbers are in a list."""

mylist=[0,2,3,7,11,12]

def count_odd(mylist):
    cant = 0
    for i in mylist:
        if i%2 != 0:
            count += 1
            
    return count

count_odd(mylist)