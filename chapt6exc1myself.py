"""The four compass points can be abbreviated by single-letter strings as
“N”, “E”, “S”, and “W”. Write a function turn_clockwise that takes one of
these four compass points as its parameter, and returns the next compass
point in the clockwise direction. Here are some tests that should pass:
test(turn_clockwise("N") == "E")
test(turn_clockwise("W") == "N")"""

def turn_clockwise(d):
    if d == "N":
        return "E"
    elif d == "E":
        return "S"
    elif d == "S":
        return "w"
    elif d == "w":
        return "N"
    else:
        return "None"