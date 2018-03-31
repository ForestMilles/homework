"""1. We’ve said nothing in this chapter about whether you can pass tuples as arguments to a function.
Construct a small Python example to test whether this is possible, and write up your findings.
"""

def tuple((x,w),(y,z)):
    if (x*y) + (w*z) > 50:
        return "more than 50"
    else:
        return "less than 50"

print(tuple[(5,6),(30,15)])


""" From running this function we can see that you can't pass tuples as arguments of a function."""

