#a Try the following:

import calendar
cal = calendar.TextCalendar()
cal.pryear(2012)

#b Observe that the week starts on Monday. An adventurous CompSci student believes that it is better mental chunking
#  to have his week start on Thursday, because then there are only two working days to the weekend, and every
# week has a break in the middle.
# Read the documentation for TextCalendar, and see how you can help him print a calendar that suits his needs.

import calendar
cal=calendar.TextCalendar(firstweekday=3)
cal.pryear(2012)

#c. Find a function to print just the month in which your birthday occurs this year.

import calendar

cal = calendar.TextCalendar()
print(cal.prmonth(2018, 11))

#d
d = calendar.LocaleTextCalendar(6, "SPANNISH")
d.pryear(2012)

"language that doesn't work"
d = calendar.LocaleTextCalendar(6, "ICELANDIC")
d.pryear(2012)

#e Experiment with calendar.isleap. What does it expect as an argument? What does it return as a result? What kind of a
# function is this?

"""it wants to have a year inputed into it. For example, from calendar import *
>>> isleap(2015)
False
>>> isleap(2004)
True 
it will return whether if the year inputed is a leap year or not through True or False"""

